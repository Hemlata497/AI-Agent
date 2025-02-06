from fastapi import FastAPI, HTTPException, Query
import requests
import wikipediaapi
from textblob import TextBlob
import nltk

# Download required NLTK data
nltk.download("punkt", quiet=True)

app = FastAPI()

# API Keys
WEATHER_API_KEY = "c98cd40e48bbc1d413c6fedc4c6fe96b"
CURRENCY_API_KEY = "dd6901498bae08bdda940387"

@app.get("/")
def home():
    return {"message": "AI Multi-Agent API is running!"}

@app.get("/weather/")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") == 200:
        weather = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        return {"city": city, "weather": weather, "temperature": temp}
    raise HTTPException(status_code=404, detail="City not found")

@app.get("/currency/")
def convert_currency(amount: float, from_currency: str, to_currency: str):
    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url).json()
        if "conversion_rates" in response:
            rate = response["conversion_rates"].get(to_currency.upper())
            if rate:
                converted = amount * rate
                return {
                    "amount": amount,
                    "from": from_currency,
                    "to": to_currency,
                    "converted_amount": converted
                }
        raise HTTPException(status_code=400, detail="Invalid currency code")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Currency service unavailable")

@app.get("/wikipedia/")
async def wiki_summary(query: str = Query(..., description="Wikipedia page title to search for")):
    try:
        wiki = wikipediaapi.Wikipedia(
            language="en",
            user_agent="AIMultiAgent/1.0 (your@email.com)"
        )
        page = wiki.page(query)
        
        if page.exists():
            summary = page.summary[:500] + "..."
            return {"query": query, "summary": summary}
        raise HTTPException(status_code=404, detail=f"Page '{query}' not found on Wikipedia")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Wikipedia API error: {str(e)}")

@app.get("/sentiment/")
def analyze_sentiment(text: str):
    if not text or text.strip() == "":
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    
    try:
        sentiment = TextBlob(text).sentiment.polarity
        sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
        return {"text": text, "sentiment": sentiment_label, "score": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing sentiment analysis: {str(e)}")

@app.get("/bitcoin/")
def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url).json()
        
        if "bitcoin" in response:
            return {"bitcoin_price": response["bitcoin"]["usd"]}
        raise HTTPException(status_code=503, detail="Failed to fetch Bitcoin price")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Bitcoin price service unavailable")