# SmartSuite RAG

SmartSuite RAG is a sophisticated Retrieval-Augmented Generation (RAG) system designed to power a Telegram bot with AI capabilities. The primary objective of this project is to assist users with university-related queries or provide various information through an intelligent chatbot.

## Features

- **AI-Powered Telegram Bot**: The bot leverages advanced AI to provide accurate and relevant responses to user queries.
- **Retrieval-Augmented Generation (RAG)**: The system retrieves relevant documents and generates responses based on the retrieved information.
- **User Assistance**: Designed to help users with university-related information and other queries.

## Future Improvements

- **CRUD Interface for PDF Files**: Develop an interface to perform CRUD operations on PDF files containing information to be loaded into the RAG system.
- **CRUD Operations via Telegram Bot Commands**: Enable CRUD operations through commands sent to the Telegram bot.
- **User Management**: Implement user management features to handle different user accounts and permissions.
- **File Category Management**: Add functionality to manage categories of files for better organization and retrieval.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Telegram Bot API token

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/LZJorge/smartsuite-rag.git
   cd smartsuite-rag
   ```

2. Install dependencies using Poetry
   ```sh
   poetry install
   ```

3. Set up environment variables:
   ```sh
   BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key

   CHROMADB_HOST=localhost
   CHROMADB_PORT=8000
   ```

### Usage

1. Run the main script:
   ```sh
   poetry run python smartsuite_rag/main.py
   ```

2. Interact with the bot on Telegram using the provided bot token.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any inquiries or support, please contact us at dev.jorge2003@hotmail.com.

### Contributing
We welcome contributions to enhance the functionality of SmartSuite RAG. Please follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.