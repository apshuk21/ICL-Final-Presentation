from langgraph.graph import MessagesState # type: ignore
from langgraph.types import Command # type: ignore
from langgraph.prebuilt import create_react_agent # type: ignore
from tools.filter_trades import filter_trades
from langchain.chat_models import init_chat_model # type: ignore
from data.trades_schema import TradesResponse
from langchain_core.output_parsers import PydanticOutputParser # type: ignore
from langchain_core.prompts import PromptTemplate # type: ignore

from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")
response_format = PydanticOutputParser(pydantic_object=TradesResponse).get_format_instructions()

model = init_chat_model(model='gpt-4.1', model_provider="openai")

# Create the prompt template
prompt_template = PromptTemplate.from_template("""
You are a filter agent.

Your job is to identify and extract relevant date ranges from the user's query.
These dates must be in YYYY-MM-DD format.

Assume today’s date is {today}. When interpreting relative date phrases like "last week" or "last month", use this date as the reference point.

Once you determine the correct date range, call the appropriate tool to filter trades using:
- start date
- end date
- matching status (if specified)

After the tool has executed, respond with a structured JSON object matching the `TradesResponse` schema.
Do not summarize, explain, or format results as natural language.

Your response must strictly follow this format:
{response_format}

Do not perform filtering yourself. Your role is to orchestrate the tool and emit valid structured output only.
""")

# Format the final prompt
formatted_prompt = prompt_template.format(today=today, response_format=response_format)

filter_agent = create_react_agent(
    name='filter_agent',
    model=model,
    prompt=formatted_prompt,
    tools=[filter_trades],
    response_format=TradesResponse
)