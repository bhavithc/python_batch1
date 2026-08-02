from openai import OpenAI

from Creds import Creds

creds = Creds()

client = OpenAI(
  base_url = creds.base_url,
  api_key = creds.api_key,
)

response = client.responses.create(
    model= creds.model_name,
    input="what is 100 + 200")

print(response.output_text)