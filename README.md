It is a AI AGENT FOR MULTITASKING (Like cheaking current weather , price of bitcoin , currency converter , sentiment and wikipedia ). It created by using python . The official source code is in the https://github.com/Hemlata497/AI-Agent.git repository.

**BUILDING**

Install the following Python libraries:
fastapi , HTTPException, Query, requests ,wikipediaapi ,TextBlob, nltk ,uvicorn , streamlit

**Code implementation**
backend code is divided into 4 parts 

1./weather/
  it is used to check current weather and i have used free weather API to run it . 

2. /currency/
   it is used to covert the currency and i have used free currency converter API to run it .

3. /wikipedia/
   it is used for checking details of any query you want . I used python wikipedia library to run it . by using python wikipedia library it helps me to get informatin directly from the wikipedia

4./sentiment/
   it is used for checking the sentiment that how the customer feeling it gives out in three ways positive , negative and nutral . i have use textBlob and nltk libraries . textBlob is used for sentiment anylasis (positive , negative and neutral) 
   and NLTK(natural language tool kit ) is used for working with human language data .
   
**RUNING**

1.First put the  API keys on WEATHER_API_KEY = "my weather api key" and  CURRENCY_API_KEY = "my currency converter api key"

2.Run the python terminal execute this "uvicorn backend:app"

3.Run the python terminal execute this "streamlit run wikipedia.py"

4.Browser will automatically open .

5. now you can check the weather , convert currency , any summary on wikipidea etc.

**Thank you**
