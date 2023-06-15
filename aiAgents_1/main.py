import requests

from langchain import OpenAI
from langchain.agents import initialize_agent, load_tools, Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import DuckDuckGoSearchRun

OPENAI_API_KEY = "..."

llm = OpenAI (
	openai_api_key = OPENAI_API_KEY,
	temperature=0.8,
	model_name="text-davinci-003"
	)
prompt = PromptTemplate (
	input_variables = ["query"],
	template = "You're New Native Internal Bot. Help users with their important tasks, like a professor in a particular field. Query:{query}"
	)

llm_chain = LLMChain(llm=llm, prompt=prompt)
