from langchain.utilities import SerpAPIWrapper
from dotenv import load_dotenv

load_dotenv()
if __name__ == "__main__":
    pass

# Implement your tools here. You can use the template below.

class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            response = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            response = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            response = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            response = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            response = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            response = res["organic_results"][0]["link"]

        else:
            response = "No good search result found"
        return response


def get_google_search(query: str):
    """Searches on Google."""
    search = CustomSerpAPIWrapper()
    res = search.run(f"{query}")
    return res.strip()