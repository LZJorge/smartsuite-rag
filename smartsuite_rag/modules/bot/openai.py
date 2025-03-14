from langchain_openai import ChatOpenAI

class OpenAI():
    def __init__(self):
        self.chat = ChatOpenAI(model="gpt-4o-mini")

    def ask(self, history):
        return self.chat.invoke(history)