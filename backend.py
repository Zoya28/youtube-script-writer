from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import time
load_dotenv()


# function to generate script
def generate(topic, video_length, creativity):
    time.sleep(2)  # Add delay between requests

    # template for generating title
    title_template = PromptTemplate(
        input_variables=["topic"],
        template="Generate a creative title video on topic {topic}.",
    )

    # template for generating script
    script_template = PromptTemplate(
        input_variables=["topic", "video_length", "DuckDuckGo_search"],
        template="Generate a script for a {video_length}-minute video on topic {topic} using this data {DuckDuckGo_search}.",
    )

    # set up the llm
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=creativity,
        max_tokens=1000,
    )

    # Creating chains for title and script generation
    title_chain = LLMChain(llm=llm, prompt = title_template, verbose=True)
    script_chain = LLMChain(llm=llm, prompt = script_template, verbose=True)

    # Creating DuckDuckGo search tool
    search = DuckDuckGoSearchRun()

    title = title_chain.invoke({"topic": topic})
    title_result = title["text"]

    # DuckDuckGo search
    try:
        search_result = search.run(topic)
    except Exception as e:
        search_result = "Search failed due to rate limit or other issue."
        print(f"Search error: {e}")

    script = script_chain.run(
        {
            "topic": topic,
            "video_length": video_length,
            "DuckDuckGo_search": search_result,
        }
    )
    return search_result, title, script
