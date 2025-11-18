import os
from groq import Groq

class GroqClient:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("❌ GROQ_API_KEY no está definida en .env")

        self.client = Groq(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_completion_tokens=4096,
            top_p=1,
            reasoning_effort="medium",
            stream=True
        )

        final_output = ""

        for chunk in completion:
            piece = chunk.choices[0].delta.content or ""
            print(piece, end="")
            final_output += piece

        print()
        return final_output
