import json
import pandas as pd # type: ignore
from app import app

def is_valid_json(json_string: str) -> bool:
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
    

def json_to_dataframe(json_string: str) -> pd.DataFrame:
    data = json.loads(json_string)
    # Expecting the structure to be like {"result": [...]}
    if isinstance(data, dict) and "result" in data:
        return pd.DataFrame(data["result"])
    else:
        return pd.DataFrame()  # Empty if unexpected structure
    
    
def agentic_chatbot(user_query: str) -> str:
    input_state = {
        "messages": [{"role": "user", "content": user_query}]
    }

    final_content = ""

    for output in app.stream(input_state):
        for agent_payload in output.values():
            if isinstance(agent_payload, dict) and "messages" in agent_payload:
                messages = agent_payload["messages"]
                for msg in messages:
                    if hasattr(msg, "content") and msg.content:
                        final_content = msg.content  # Keep overwriting
                        
    return final_content or "No trades found."
