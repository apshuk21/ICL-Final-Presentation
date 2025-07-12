from langgraph.graph import MessagesState # type: ignore
from langgraph.types import Command # type: ignore
from typing import Literal

def matcher_agent(state: MessagesState) -> Command[Literal['supervisor_agent']]:
    print("-------------------Matcher Agent--------------------")
    return Command(
        goto='supervisor_agent',
        update={
            **state
        }
    )