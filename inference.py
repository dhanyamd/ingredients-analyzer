from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools 
from utils import GOOGLE_API_KEY, TAVILY_API_KEY
from constants import SYSTEM_PROMPT, INSTRUCTIONS
import os 


os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY 
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

agent = Agent(
    model = Gemini(id="gemini-2.0-flash"),
   tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
    markdown=True,
    system_message=SYSTEM_PROMPT,
    instructions=INSTRUCTIONS
)

agent.print_response(
    "Analyze the product image",
    images=[{"url": "https://m.media-amazon.com/images/I/61evZVkAb0L._AC_UF350,350_QL80_.jpg"}],
    stream=True
)