import os
import chainlit as cl
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory


# Load environment variables
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

# Initialize the model
conv_model = HuggingFaceHub(
    repo_id="gpt2-medium",
    model_kwargs={"temperature": 0.8, "max_new_tokens": 200}
)

# Initialize memory
memory = ConversationBufferMemory()

# Create the prompt template
template = "You are a helpful AI assistant that makes stories by completing the query provided by the user: {query}"

@cl.on_chat_start
async def main():
    # Initialize the prompt template correctly
    prompt = PromptTemplate(
        template=template,
        input_variables=["query"]  # Note: input_variables is plural, not input_variable
    )
    
    # Create the LLM chain
    conv_chain = LLMChain(
        llm=conv_model,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
    
    # Store in user session
    cl.user_session.set('llm_chain', conv_chain)

@cl.on_message
async def on_message(message: str):
    # Get the LLM chain from the session
    llm_chain = cl.user_session.get('llm_chain')
    
    # Make sure llm_chain is not None before using it
    if llm_chain is None:
        await cl.Message(content="Session expired or LLM chain not initialized. Please refresh the page.").send()
        return
    
    # Call the chain with the message content
    res = await llm_chain.acall({"query": message.content}, callbacks=[cl.AsyncLangchainCallbackHandler()])
    
    # Send the response
    await cl.Message(content=res["text"]).send()

# python -m chainlit run chatbot.py -w --port 8080