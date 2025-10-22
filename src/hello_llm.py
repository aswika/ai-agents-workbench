import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

msg = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}]
)
print(msg.choices[0].message.content)
