from langgraph.graph import MessagesState # type: ignore
from langgraph.types import Command # type: ignore
from langgraph.prebuilt import create_react_agent # type: ignore
from tools.filter_trades import filter_trades
from langchain.chat_models import init_chat_model # type: ignore

from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

model = init_chat_model(model='gpt-4.1', model_provider="openai")

prompt = f"""
You are a filter agent.
Please find the start and end date from the query. The date should be in YYYY-MM-DD format.
Assume today’s date is {today}. When interpreting any relative date ranges like 'last week' or 'last month', use this as the reference point.
Your job is to call the right tool to filter the trades.
"""

filter_agent = create_react_agent(
    name='filter_agent',
    model=model,
    prompt=prompt,
    tools=[filter_trades]
)