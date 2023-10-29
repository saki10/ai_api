import openai
openai.api_key = "your_apykey"

response =openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    messages =[
        {"role":"system","content":"あなたは優秀な英語教師です"},
        {"role" :"system","content":"英語が話せるようになりたいを英語で翻訳してください"}
    ]
)

print(response["choices"][0]["message"]["content"])