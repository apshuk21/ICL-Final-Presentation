from langgraph.prebuilt import create_react_agent # type: ignore
from tools.handoff_tool import assign_to_affirmer_agent, assign_to_filter_agent, assign_to_matcher_agent

def supervisor_agent():
    print("-------------------Supervisor Agent--------------------")
    return create_react_agent(
        name='supervisor_agent',
        model="openai:gpt-4.1",
        prompt=(
        "You are a supervisor managing three agents:\n"
        "- a matcher agent. Assign matching-related tasks to this agent\n"
        "- a filter agent. Assign filter-related tasks to this agent\n"
        "- a affirmer agent. Assign affirmation-related tasks to this agent\n"
        "Assign work to one agent at a time, do not call agents in parallel.\n"
        "You should understand the flow and the sequence or the order to call these agents"
        "Example 1: If user asks to match all the trades of last week. You should first go to the filter agent\n"
        "and then go to the matcher agent with the response of the filtered agent. \n"
        "Example 2: If user asks to give all the matched trades of last week. You should understand that user\n"
        "is only asking for the filtered data. User is not asking to perform any actions. You just need to go\n"
        "the filter agent."
        "Do not do any work yourself."
    ),
        tools=[assign_to_matcher_agent, assign_to_filter_agent, assign_to_affirmer_agent]
    )