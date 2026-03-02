from groq import Groq
import os

class UltimateAI:
    def __init__(self):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )

    def respond(self, message: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "Tu es une IA intelligente, claire, pédagogique et naturelle. Tu expliques comme ChatGPT."
                    },
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
                model="llama3-70b-8192",
            )

            return chat_completion.choices[0].message.content

        except Exception as e:
            return f"Erreur IA : {str(e)}"
