import openai


KEY_PATH = 'key.txt'
MAX_WORDS = 300  # Limits the words of parent conversion
MAX_TOKENS = 100
ROLE_SYSTEM = 'system'
ROLE_USER = 'user'
ROLE_ASSISTANT = 'assistant'


def init():
    # For security, I didn't write my API KEY here
    # You can simply replace this with: openai.api_key = 'YOUR_KEY'
    with open(KEY_PATH) as f:
        openai.api_key = f.read()


class GPTBot:
    def __init__(self, sys_instruct=''):
        init()
        self.__msgs = [{'role': ROLE_SYSTEM, 'content': sys_instruct}]

    def __updateMsgs(self, msg, role=ROLE_USER):
        # exception handle or give an error?
        if role not in (ROLE_ASSISTANT, ROLE_USER):
            return
        num = self.__calculateWords()
        if num >= MAX_WORDS:
            self.__resetMsgs()
        self.__msgs.append({"role": f"{role}", "content": msg})

    def __calculateWords(self):
        num_of_words = 0
        for msg in self.__msgs:
            num_of_words += len(msg['content'])
        return num_of_words

    def __resetMsgs(self):
        if len(self.__msgs) > 1:
            self.__msgs[1:len(self.__msgs)] = []

    def makeChatRequest(self, msg, temperature=1):
        self.__updateMsgs(msg)
        # exception handle
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=temperature,
            max_tokens=MAX_TOKENS,
            messages=self.__msgs
        )
        self.__updateMsgs(response['choices'][0]['message']['content'], ROLE_ASSISTANT)
        return response


