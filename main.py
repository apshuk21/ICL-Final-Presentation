from helpers import agentic_chatbot, is_valid_json, json_to_dataframe

if (__name__ == '__main__'):
    result = agentic_chatbot("Give me all the matched trades for last 30 days.")
    print(result)

    print('##is_Valid', is_valid_json(result))

    df = json_to_dataframe(result)

    print('##df', df)

    # for output in app.stream({
    #     'messages': [{'role': 'user', 'content': 'Give me all the matched trades for last week.'}]
    # }):
    #     print('##output', output)
    #     print("***************************"*4)