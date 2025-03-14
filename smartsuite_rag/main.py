from modules.bot.main import Bot
from modules.rag.repository import Repository
from modules.rag.rag import load_rag
from modules.shared.configs import Configs


def main():
    try:
        token = Configs.get("BOT_TOKEN")

        repository = Repository()
        bot = Bot(token, repository)

        load_rag()
        bot.start()
    except Exception as e:
        print("[-] Error during bot execution -> ", e)


if __name__ == "__main__":
    main()