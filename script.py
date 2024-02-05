import os
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY')
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def startConversation():
    user_msg = input("Prompt : ")
    if user_msg == "0":
        return 
    chat = model.start_chat(history=[])
    response = chat.send_message(user_msg)
    return response.text

while True:
    print("Enter 0 to exit")
    result = startConversation()
    if not result :
        break 
    else:
        print("\n",result,"\n")

