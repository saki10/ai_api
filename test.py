import openai

openai.api_key ='your_apikey'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":"あなたは優秀なアシステントAIです"},
    {"role": "user", "content": "あなたはどんなことができますか？"}
  ]
)

print(completion['choices'][0]['message']['content'])

