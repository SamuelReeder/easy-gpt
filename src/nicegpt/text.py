import nicegpt

nicegpt.config("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")

gpt_instance = nicegpt.GPT(model=nicegpt.Model.GPT4)  

response = gpt_instance.response("What is the capital of France?")

print(response)  