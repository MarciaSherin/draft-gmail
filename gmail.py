from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = ""

credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
tools = toolkit.get_tools()

instructions = """You are an assistant."""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)
llm = ChatOpenAI(temperature = 0)
agent = create_openai_functions_agent(llm, toolkit.get_tools(), prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=False,
)
input_data = {
    "input": (
        "Create a Gmail draft for me to edit of a letter from the perspective of a sentient parrot"
        " who is looking to collaborate on some research with her estranged friend, a cat."
        " The draft should include a valid 'To' header with the recipient's email address"
        " (e.g., 'kiran@webtiga.com'). Under no circumstances may you send the message, however."
    )
}
agent_executor.invoke(
    input_data
)