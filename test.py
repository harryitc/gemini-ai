import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # Load biến từ file .env

API_KEY = os.getenv("GEMINI_API_KEY")

print(API_KEY)  # Kiểm tra giá trị

client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="1 + 1 = ?"
)
print(response.text)