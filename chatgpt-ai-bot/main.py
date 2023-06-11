from gptbot import GPTBot

bot = GPTBot()
while True:
    user_input = input("Enter your question (Type 'exit' to exit): ")
    response = bot.makeChatRequest(user_input)
    print(response['choices'][0]['message']['content'])
    if user_input == 'exit':
        break
