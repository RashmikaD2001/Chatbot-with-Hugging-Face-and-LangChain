# Chatbot with Hugging Face and LangChain

This is a simple chatbot project using Hugging Face models and LangChain to generate responses. The chatbot is implemented with Chainlit for an interactive chat interface.

## Features
- Uses a Hugging Face model (`gpt2-medium`) to generate responses.
- Implements conversation memory with `ConversationBufferMemory`.
- Utilizes `LLMChain` from LangChain to process user queries.
- Runs in a Chainlit environment.

### Installation

  Clone the repository:
   ```sh
   git clone https://github.com/yourusername/huggingface-langchain-chatbot.git
   cd huggingface-langchain-chatbot
   ```
  Set up environment variables:
   Create a `.env` file in the root directory and add:
   ```sh
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
   ```

## Running the Chatbot
To start the chatbot, run:
```sh
python -m chainlit run chatbot.py -w --port 8080
```
The chatbot will be accessible at `http://localhost:8080`.

## Project Notes
- This is a side project to explore Hugging Face models and LangChain.
- Contributions and suggestions are welcome!

