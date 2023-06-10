import openai


KEY_PATH = 'key.txt'


class GPTBot:
    @staticmethod
    def __init():
        # For security, I didn't write my API KEY here
        # You can simply replace this with: openai.api_key = 'YOUR_KEY'
        with open(KEY_PATH) as f:
            openai.api_key = f.read()

    def __init__(self, sys_instruct=''):
        GPTBot.__init()
        self.__msgs = [{'role': 'system', 'content': sys_instruct}]

    def __updateMsgs(self, msg, role='user'):
        # exception handle or give an error?
        if role not in ('assistant', 'user'):
            return
        self.__msgs.append({"role": f"{role}", "content": msg})

    def makeChatRequest(self, msg, temperature=1):
        self.__updateMsgs(msg)
        # exception handle
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=temperature,
            max_tokens=100,
            messages=self.__msgs
        )
