from langchain_core.tools import tool, InjectedToolCallId # type: ignore
from typing_extensions import Annotated # type: ignore
from langgraph.graph import MessagesState # type: ignore
from langgraph.prebuilt import InjectedState # type: ignore
from langgraph.types import Command # type: ignore

def create_handoff_tool(agent_name: str, description: str | None = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help."

    @tool(name, description=description)
    def handoff_tool(
        state: Annotated[MessagesState, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId]
    ) -> Command:
        # print('##handoff_tool name', name)
        # print('##handoff_tool state', state)
        tool_message = {
            'role': 'tool',
            'content': f'Successfully transferred to {agent_name}',
            'tool_call_id': tool_call_id,
            'name': name 
        }

        return Command(
            goto=agent_name,
            update={
                **state,
                'messages': state['messages'] + [tool_message]
            },
            graph=Command.PARENT
        )
        

    return handoff_tool

## Handoffs
assign_to_filter_agent = create_handoff_tool(
    agent_name='filter_agent',
    description='Assign the task to the filter agent'
)

assign_to_matcher_agent = create_handoff_tool(
    agent_name='matcher_agent',
    description='Assign the task to the matcher agent'
)

assign_to_affirmer_agent = create_handoff_tool(
    agent_name='affirmer_agent',
    description='Assign the task to the matcher agent'
)