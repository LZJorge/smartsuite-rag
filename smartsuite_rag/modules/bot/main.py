import colorama
from telebot import TeleBot
from smartsuite_rag.modules.bot.openai import OpenAI
from smartsuite_rag.logger import logger
from smartsuite_rag.modules.bot.history import ChatHistory

colorama.init()

chat_histories = {}

class Bot:
    def __init__(self, token, repository):
        self.token = token
        self.repository = repository
        self.bot = TeleBot(self.token)
        self.openai = OpenAI()

    def load_commands(self):
        """
        This function loads the commands for the bot
        """
        @self.bot.message_handler(commands=['start', 'hello'])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?")

        @self.bot.message_handler(func=lambda msg: True)
        def ai_response(message):
            chat_id = message.chat.id

            if chat_id not in chat_histories:
                chat_histories[chat_id] = ChatHistory()

            chat = chat_histories[chat_id]
            chat.add("human", message.text)

            nearest_docs = self.repository.get_nearest(text=message.text, limit=4)

            response = self.openai.ask(chat.get_with_context(nearest_docs))
            chat.add("system", response.content)

            self.bot.send_message(chat_id, response.content)

    def start(self):
        self.load_commands()

        logger.info(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[+] " + colorama.Style.RESET_ALL + "Bot is running")
        self.bot.infinity_polling(timeout=15, long_polling_timeout=8)
