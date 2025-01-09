from langgraph.graph import StateGraph
from agents.autonomous_agent import Autonomous_Agent
from agents.output_agent import Output_Agent
from core.state import AgentGraphState

def create_graph():

    graph = StateGraph(AgentGraphState)

    # Define nodes.

    graph.add_node(
        "autonomous_agent",
        lambda state: Autonomous_Agent(state = state).invoke()
    )

    graph.add_node(
        "toolbox",
        lambda state: Autonomous_Agent(state = state).call_tools() # this calls the tools requested by the model.
    )

    graph.add_node(
        "output",
        lambda state: Output_Agent(state = state).invoke()
    )



    # Define edges

    graph.set_entry_point("autonomous_agent")

    graph.add_conditional_edges(
        "autonomous_agent",
        lambda state : Autonomous_Agent(state = state).should_continue() # toolbox / output
    )

    graph.add_edge("toolbox", "autonomous_agent")

    graph.set_finish_point("output")

    return graph

def compile_workflow(graph):
    workflow = graph.compile()
    return workflow
