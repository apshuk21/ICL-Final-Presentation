from dotenv import load_dotenv # type: ignore
from langgraph.types import Command # type: ignore
from langgraph.graph import MessagesState, StateGraph, START, END # type: ignore
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

from agents.supervisor_agent import supervisor_agent
from agents.filter_agent import filter_agent
from agents.matcher_agent import matcher_agent
from agents.affirmer_agent import affirmer_agent

## Create workflow
graph_builder = StateGraph(MessagesState)

## Add nodes in the workflow
graph_builder.add_node(supervisor_agent, destinations=['filter_agent', 'matcher_agent', 'affirmer_agent', END])
graph_builder.add_node('filter_agent', filter_agent)
graph_builder.add_node('matcher_agent', matcher_agent)
graph_builder.add_node('affirmer_agent', affirmer_agent)

## Add edges
graph_builder.add_edge(START, 'supervisor_agent')
graph_builder.add_edge('filter_agent', 'supervisor_agent')
graph_builder.add_edge('matcher_agent', 'supervisor_agent')
graph_builder.add_edge('affirmer_agent', 'supervisor_agent')
graph_builder.add_edge('supervisor_agent', END)

## Create the graph
app = graph_builder.compile()
