from openai import OpenAI
from os import getenv
from Creds import Creds


creds = Creds()

# gets API Key from environment variable OPENROUTER_API_KEY
client = OpenAI(
  base_url = creds.base_url,
  api_key = creds.api_key
)

completion = client.chat.completions.create(
  model=creds.model_name,
  messages=[
    {
      "role": "user",
      "content": "Say this is a test",
    },
  ],
)

print(completion.choices[0].message.content)

