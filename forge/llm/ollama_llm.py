# forge/llm/ollama_llm.py

import ollama

from llm.base_llm import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(self, model="qwen3"):

        self.model = model

    def generate(self, prompt: str):

        response = ollama.chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response["message"]["content"]