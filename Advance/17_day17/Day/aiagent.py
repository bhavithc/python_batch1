from dotenv import load_dotenv
import os

load_dotenv() # set the env variables by reading from .env file

print(os.getenv("API_KEY"))
print(os.getenv("BASE_URL"))
print(os.getenv("MODEL_NAME"))
