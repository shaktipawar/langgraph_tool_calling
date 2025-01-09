from agents.agent import Agent
from prompt_templates import autonomous_template
from core.helper import Helper
from core.model import ModelFactory
from langchain_core.tools import tool

from langchain_core.runnables import RunnableLambda
from langchain_core.messages import ToolMessage

class Autonomous_Agent(Agent):

    @tool
    def get_stock_price(stock_name):
        """
        This method returns stock price.
        Args :
            stock_name : Name of the stock.
        """

        if stock_name == "Apple":
            return f"The {stock_name} price is INR 100"
        else:
            return f"The {stock_name} price is INR 110"

    @tool
    def get_weather(city):
        """
        This method returns weather of the city.
        Args :
            city : Name of the city.
        """
        if city == "Mumbai":
            return f"The weather in {city} is Sunny"
        else :
            return f"The weather in {city} is Breezy"

    def invoke(self):

        question = self.state["conversation"][-1]["message"]
        template = autonomous_template.content
        system_prompt = template.format(PH_tool_response = self.state["agent_message"]["tool_response"])
        self.state["agent_message"]["tool_response"] = "" #reset to empty
        user_prompt = f"** USERS MESSAGE ** <br> {question}"
        prompt = Helper.get_prompt(system_prompt, user_prompt)

        #Invoke Model
        model_with_tools = ModelFactory.get_chat_model(provider = "openai",
                                               model = "gpt-4o-mini",
                                               temperature = 0,
                                               kwargs= {"response_format": {"type": "text"}}
                                               ).bind_tools([self.get_stock_price, self.get_weather])

        response = model_with_tools.invoke(prompt)
        json_object = response
        self.state["agent_message"]["previous_agent_response"] = json_object
        return self.state

    def should_continue(self):
        if self.state["agent_message"]["previous_agent_response"] != "":
            if self.state["agent_message"]["previous_agent_response"].tool_calls:
                self.state["agent_message"]["next_agent"] = "toolbox"
            else :
                self.state["agent_message"]["next_agent"] = "output"

        return self.state["agent_message"]["next_agent"]

    def _invoke_tool(tool_call):
        tools = [Autonomous_Agent.get_stock_price, Autonomous_Agent.get_weather]
        tool = {tool.name: tool for tool in tools}[tool_call["name"]]
        return ToolMessage(tool.invoke(tool_call["args"]), tool_call_id=tool_call["id"])

    def call_tools(self):
        tool_executor = RunnableLambda(Autonomous_Agent._invoke_tool)
        last_message = self.state["agent_message"]["previous_agent_response"]
        if last_message != '':
            val = tool_executor.batch(last_message.tool_calls)
            content = ""
            for item in val:
                content += item.content + "\n"
            self.state["agent_message"]["tool_response"] = content
        return self.state
