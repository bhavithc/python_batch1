from openai import OpenAI
from creds import Creds




creds = Creds() # Creds.base_uri= "124", Creds.api_key="12324"
creds.foo() # Creds.foo(creds)

# print(creds)

# print(creds.api_key)
# print(creds.base_url)
# print(creds.model_name)

client = OpenAI(
    base_url=creds.base_url,
    api_key=creds.api_key
)

while True:
    msg = input("> ")
    response = client.responses.create(
        model=creds.model_name,
        input=f"{msg}, Don't respond in Markdown format, also print the question asked")

    print(response.output_text)
