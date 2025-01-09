from core.state import AgentGraphState 

class Agent:

    def __init__(self, state : AgentGraphState):
        self.state = state
        self.model = "gpt-4o-mini"
        self.server = "openai"
        self.temperature = 0
        # self.agentflow = ""
        # self.messages = []

    

    
