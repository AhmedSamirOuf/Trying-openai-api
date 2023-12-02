from openai import OpenAI
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
openai_api_key = env_vars.get('OPENAI_API_KEY')

if not openai_api_key:
    print("OpenAI API Key not found. Check your .env file.")

client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)