# Template for React Agents Demo with Vertex AI (Google Cloud)

Note: This repo is not inteded for production use. It is meant to be used to demo the ReAct pattern with customers and find use cases with them. 

[ReAct](https://react-lm.github.io/) is an intiutive pattern to perform actions using natural language. This demo allows us to showcase a use case of a Recruiter Agent and a HR Agent interacting between each other to send and offer to a candidate.

The demo template is based in the awesome work by [Eden Marco](https://github.com/g-emarco) in [this repo](https://github.com/g-emarco/llm-agnets).

We use the awesome tool Langchain in this demo. If you don't know about it, you can find a nice video [here](https://www.youtube.com/watch?v=kYRB-vJFy38)

1. Generate a `.env` file based on the `.env_template` file.
    Some (or most) of the tools require registration. Here you can find information about the tools:
    - Find more information about Serpapi [here](https://serpapi.com/)
2. Install dependencies in the `requirements.txt`file using the following command:
    `pip install -r requirements.txt`

## Execution
To run from the graphical interface run the following command:

    streamlit run web/app.py


### Recommendations:

More information about lanchain and react [here](https://python.langchain.com/docs/modules/agents/agent_types/react)
