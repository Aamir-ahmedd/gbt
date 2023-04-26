import json
import requests
import streamlit as st
import openai
API_KEY = "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"

def basic_generation(user_prompt):
    data = {
        "prompt": user_prompt,
        "model": "text-davinci-002",
        "max_tokens": 1024,
        "n": 1,
        "temperature": 0.5,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers)
    message = response.json()["choices"][0]["text"]
    return message

st.title('Crypto Analyzer with ChatGPT')
st.subheader('Subscribe to my channel!')

coins = ['BTC', 'ETH', 'DOGE', 'BNB']
coin = st.selectbox('Select a coin to analyze', coins)

tasks = ['Price Overview', 'Relative Strength Index (RSI)', 'Advice and Suggestion']
task = st.selectbox('Select a task', tasks)

def get_crypto_prices(coin):
   import requests

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "64477702e2msh430667f78f1ebe3p17465fjsn02f14488cecf",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

if st.button('Analyze'):
    with st.spinner(f'Getting {coin} prices...'):
        crypto_prices = get_crypto_prices(coin.lower())
        st.success('Done!')
    with st.spinner(f'Analyzing {coin} prices for {task}...'):
        chat_gpt_prompt = f"""You are an expert crypto trader with more than 10 years of experience, 
                    I will provide you with a list of {coin} prices for the last 7 days
                    Can you provide me with a {task} analysis
                    of {coin} based on these prices. Here is what I want: 
                    {task},
                    Please be as detailed as much as you can, and explain in a way any beginner can understand. and make sure to use headings
                    Here is the price list: {crypto_prices}"""
    
        analysis = basic_generation(chat_gpt_prompt)
        st.text_area("Analysis", analysis, height=500)
        st.success('Done!')
