from agents.get_agents import agent_template
from dotenv import load_dotenv
from utils.callbacks import LLMInstrumentationHandler
import os

load_dotenv()
if __name__ == "__main__":
    pass

verbose = True
temp = 0

query = "What other movie has done the Director of Dune (2021)?"

# Define your agent's flow here. From agent_start, call your other agents orchestating the desired flow. You can use the template below
def agent_start(query: str, temperature=temp):
    print(f"Welcome to the ReAct! We are going to do an example of a simple search in Google\n\n LET'S GO!")
    agent = agent_template(temperature)
    return agent.run(query)