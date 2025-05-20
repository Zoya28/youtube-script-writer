from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun
import time


# function to generate script
def generate(api_key, topic, video_length, creativity):
    time.sleep(2)

    title_template = PromptTemplate(
        input_variables=["topic"],
        template="Generate a creative title video on topic {topic}.",
    )

    script_template = PromptTemplate(
        input_variables=["topic", "video_length", "DuckDuckGo_search"],
        template="Generate a script for a {video_length}-minute video on topic {topic} using this data {DuckDuckGo_search}.",
    )
    try:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=creativity,
            max_tokens=1000,
            api_key=api_key,
        )

        title_chain = LLMChain(llm=llm, prompt = title_template, verbose=True)
        script_chain = LLMChain(llm=llm, prompt = script_template, verbose=True)

        # Creating DuckDuckGo search tool
        search = DuckDuckGoSearchRun()
        title = title_chain.invoke({"topic": topic})
        search_result = search.run(topic)    

        script = script_chain.run(
            {
                "topic": topic,
                "video_length": video_length,
                "DuckDuckGo_search": search_result,
            }
        )
        return search_result, title, script

    except Exception as e:
        return f"Enter correct Groq API key! Error: {e}",None,None
