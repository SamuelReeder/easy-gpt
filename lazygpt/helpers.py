"""
Helper methods for managing GPT.
"""

def compile_messages(messages: list[list[str, str | str, None]], system: str = None, ) -> list[dict]:
    """
    Compile a list of message dictionaries given a list of lists [user_prompt, gpt_response], and an optional system message.    
    """
    formatted_messages = messages.copy()
    formatted_messages = [] if not system else [{"role": "system", "content": system}]
    for exchange in messages:
        formatted_messages.append({"role": "user", "content": exchange[0]})
        if exchange[1] is not None:
            formatted_messages.append({"role": "assistant", "content": exchange[1]})
    return formatted_messages
    
    