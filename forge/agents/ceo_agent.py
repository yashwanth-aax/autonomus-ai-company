# forge/agents/ceo_agent.py

import json

from agents.base_agent import Agent
from models.prd import PRD


class CEOAgent(Agent):

    def __init__(
        self,
        name,
        memory,
        event_bus,
        state,
        llm
    ):

        super().__init__(
            name,
            memory,
            event_bus,
            state
        )

        self.llm = llm

    def think(self):

        idea = self.state.get("idea")

        print()

        print(
            f"{self.name} is analyzing:"
        )

        print(idea)

    def act(self):

        idea = self.state.get("idea")

        prompt = f"""

You are the CEO of an autonomous AI software company.

Product Idea:

{idea}


Generate a STRICT JSON object with EXACTLY these keys:

{{
    "vision":"...",

    "target_users":"...",

    "features":[...],

    "requirements":[...],

    "user_stories":[...],

    "success_metrics":[...]
}}


Rules:

1. Return ONLY JSON

2. Do NOT explain anything

3. Do NOT use markdown

4. Do NOT use ```json

5. JSON must be parsable by Python json.loads()

"""

        response = self.llm.generate(prompt)

        print()

        print("Raw LLM Output:\n")

        print(response)

        # Remove markdown if Qwen returns it

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

        response = response.strip()

        # Fix missing final brace

        if not response.endswith("}"):

            response += "\n}"

        try:

            data = json.loads(
                response
            )

            prd = PRD(

                title=idea,

                vision=data[
                    "vision"
                ],

                target_users=data[
                    "target_users"
                ],

                features=data[
                    "features"
                ],

                requirements=data[
                    "requirements"
                ],

                user_stories=data[
                    "user_stories"
                ],

                success_metrics=data[
                    "success_metrics"
                ]

            )

            self.state.update(
                "prd",
                prd
            )

            print()

            print(
                "CEO created PRD successfully."
            )

        except Exception as e:

            print()

            print(
                "Failed to parse JSON"
            )

            print()

            print(e)