from core.graph import create_graph, compile_workflow
from termcolor import colored
from core.helper import Helper, MessageType
from core.state import state

class App():

    def __init__(self, state):
        self.graph = create_graph()
        self.workflow = compile_workflow(self.graph)
        self.state = state #Helper.set_users_persona(state, 4)
        self.initial_message = True
        iteration = 40
        self.thread = {"recursion_limit" : iteration, "configurable": {"thread_id": "4"}}

    def bind_output(self, event):
        Helper.print_log(MessageType.AI_REPLY, event["conversation"][-1]["message"])
    
    def set_users_message(self, message):
        self.state["conversation"].append({"message" : message, "type" : "USER"})

    def run(self):
        while True:

            if self.initial_message:
                self.set_users_message("** INITIAL GREETINGS  **")
                self.initial_message = False
            else:
                # Reset message as empty.
                self.state["agent_message"]["next_agent"] = ""
                self.state["agent_message"]["previous_agent_response"] = ""
                
                user_message = input(colored("Shakti : ", "magenta"))
                if user_message.lower() == "exit":
                    break
                self.set_users_message(user_message)

            events = self.workflow.invoke(self.state, self.thread, stream_mode="updates")
            event = events[-1]
            self.state = event["output"]
            self.bind_output(event["output"])
            
if __name__ == "__main__":
    app = App(state)
    app.run()