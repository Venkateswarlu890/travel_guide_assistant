# Write your code here
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()
api_Key = os.getenv("GEMINI_API_KEY")
system_msg = SystemMessage("You are a travel guide who gives brief recommendations for tourist destinations.")
human_msg = HumanMessage("Suggest top 3 places to visit in Japan.")
messages = [system_msg, human_msg]

model = init_chat_model(
  "google_genai:gemini-3.5-flash-lite",
  api_key=api_Key,
)

response = model.invoke(messages)
print(response.text)