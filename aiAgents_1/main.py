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

llm_chain.run("What is lablab.ai")

search = DuckDuckGoSearchRun()
# Web Search Tool
search_tool = Tool (
	name = "Web Search",
	func = search.run,
	description = 'A useful tool for searching the Internet to find information on world events, issues etc. Worth using for general topics. Use precise questions.'
	)

class WA:
	"""
	Wolfram | Alpha API
	"""
	def __init__(self, app_id):
		self.url = f"http://api.wolframalpha.com/VI/result?appid={app_id}&i="

	def run(self, query):
		query = query.replace("+","plus").replace("-","minus")
		result = requests.post(f"{self.url}{query}")
		if not result.ok:
			raise Exception ("Cannot call WA API.")
		return result.text
