import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

prompt_one = PromptTemplate(
    input_variables = ["concept"],
    template = "explain the concept of {concept} in one sentence"
)

prompt_two = PromptTemplate(
    input_variables = ["explanation"],
    template = "translate the explanation {explanation} to Japanese"
)

chain_one = prompt_one | llm | StrOutputParser()

chain_two = prompt_two | llm | StrOutputParser()

if __name__ == "__main__":

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        first_result = chain_one.invoke({"concept":user_input})
        print("chain_one_result: ",first_result)

        second_result = chain_two.invoke({"explanation":first_result})
        print("chain_two_result: ",second_result)