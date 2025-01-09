from typing import TypedDict, List

class Agent_Message:
    next_agent : str # This will hold name of the next Agent (based on Graph design)
    previous_agent_response : str # This will hold latest response from Previous Agent.
    tool_response : str

class Conversation: # This should be updated at output node only.
    message : str
    type : str

class AgentGraphState(TypedDict):
    conversation : List[Conversation]
    agent_message: Agent_Message # This holds, all data which gets communicated between agents.

state = {
    # This node holds information about all communications that happen between ai agents.
    "conversation" : [],
    "agent_message" : {
        "next_agent" : "", # Holds the next_agent name. It helps only when nodes are connected via conditional edge.
        "previous_agent_response" : "", # Hold response from just previous agent. It helps when next agent want to fetch information which was derieved from previous agent.
        "tool_response" : "", # Holds the response from tool agent. It helps to understand the response from tool agent.
    }
}


