import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🌍 AI Multi-Agent System")

# User input
user_input = st.text_input("Enter your query")

if st.button("Submit") and user_input:
    user_input = user_input.lower()  # Convert to lowercase for easy detection
    
    try:
        if "weather" in user_input:
            city = user_input.replace("weather in", "").strip()
            response = requests.get(f"{API_URL}/weather/", params={"city": city}).json()
            
        elif "convert" in user_input and "to" in user_input:
            parts = user_input.split()
            amount = float(parts[1])
            from_currency = parts[2].upper()
            to_currency = parts[4].upper()
            response = requests.get(
                f"{API_URL}/currency/",
                params={
                    "amount": amount,
                    "from_currency": from_currency,
                    "to_currency": to_currency
                }
            ).json()
            
        elif "wikipedia" in user_input:
            query = user_input.replace("wikipedia", "").strip()
            response = requests.get(f"{API_URL}/wikipedia/", params={"query": query}).json()
            
        elif "bitcoin" in user_input:
            response = requests.get(f"{API_URL}/bitcoin/").json()
            
        elif "sentiment" in user_input:
            text = user_input.replace("sentiment", "").strip()
            if text:
                response = requests.get(f"{API_URL}/sentiment/", params={"text": text}).json()
            else:
                response = {"error": "Please enter a valid sentence for sentiment analysis."}
        else:
            response = {"error": "Unknown command. Try: weather in [city], convert [amount] [currency] to [currency], wikipedia [query], bitcoin, or sentiment [text]"}
            
        # Display results
        if "error" in response:
            st.error(response["error"])
        else:
            st.success("Request successful!")
            st.json(response)
            
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")