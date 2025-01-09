from agents.agent import Agent
class Output_Agent(Agent):

    def invoke(self):
        self.state["conversation"].append({"message" : self.state["agent_message"]["previous_agent_response"].content, "type" : "AI"}) 
        return self.state