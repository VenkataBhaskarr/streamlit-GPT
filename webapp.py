import streamlit as st
import openai
import requests
import json

url = "https://api.quotable.io/random"

st.title("Understand everything like a 5 years old kid 😌")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI's AI model.
       Enter a **keyword** in the **text box** and **press enter** to receive 
       a **response**, the response is given in such a way that it can be understood by a **5year old**
       '''
    )

# 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

model_engine = "text-davinci-003"
openai.api_key = "" 

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter keyword here, to exit enter :q", "competetive programming")
    
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        user_query = "Explain " + user_query + " it to 5 year old kid"
        response = ChatGPT(user_query)
        return st.write(response)

def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response

main() 




response = requests.request("GET", url)
answer = json.loads(response.text)

st.markdown(" ## Quote of the day  ")
st.write(answer['content'])
