from langgraph.prebuilt import create_react_agent # type: ignore
from tools.handoff_tool import assign_to_affirmer_agent, assign_to_filter_agent, assign_to_matcher_agent
from data.trades_schema import TradesResponse
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import PydanticOutputParser # type: ignore
from langchain.chat_models import init_chat_model # type: ignore

response_format = PydanticOutputParser(pydantic_object=TradesResponse).get_format_instructions()

model = init_chat_model(model='gpt-4.1', model_provider="openai")

prompt_template = PromptTemplate.from_template("""
You are a supervisor agent responsible for managing three specialized agents:

- a matcher agent: handles matching-related tasks
- a filter agent: handles trade filtering
- an affirmer agent: handles affirmation-related actions

Your job is to **assign tasks to one agent at a time**. Do not invoke multiple agents in parallel.

Understand the correct flow for multi-step tasks:
Example 1: If the user asks to match all trades from last week, you must first delegate to the filter agent, then pass the filtered response to the matcher agent.
Example 2: If the user asks for matched trades, they likely want the filtered data — only delegate to the filter agent.

You do not perform any work yourself.

When a supervisee agent returns a result, you **must respond with a structured JSON object** that matches the `TradesResponse` schema.

Do not summarize, explain, or format results as natural language.
Just return the structured JSON output in the following format:
{response_format}
""")

final_prompt = prompt_template.format(response_format=response_format)

supervisor_agent = create_react_agent(
        name='supervisor_agent',
        model=model,
        prompt=final_prompt,
        tools=[assign_to_matcher_agent, assign_to_filter_agent, assign_to_affirmer_agent],
        response_format=TradesResponse
    )