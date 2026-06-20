# forge/agents/architect_agent.py

import json

from agents.base_agent import Agent

from models.architecture import Architecture


class ArchitectAgent(Agent):

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

        print()

        print(

            f"{self.name} is reading PRD..."

        )


    def act(self):

        prd = self.state.get(

            "prd"

        )


        prompt = f"""

You are a Senior Software Architect.


Product:

{prd.title}


Features:

{prd.features}


Design the system.


Return STRICT JSON with EXACTLY:

{{

"frontend":"",

"backend":"",

"database":"",

"authentication":"",

"cache":"",

"modules":[],

"deployment":""

}}


Rules:

1. Return ONLY JSON

2. No markdown

3. No explanation

4. JSON must be valid

"""


        response = self.llm.generate(

            prompt

        )


        print()

        print(

            "Raw Architect Output:\n"

        )

        print(response)


        response = response.replace(

            "```json",

            ""

        )

        response = response.replace(

            "```",

            ""

        )

        response = response.strip()


        if not response.endswith("}"):

            response += "\n}"


        try:

            data = json.loads(

                response

            )


            architecture = Architecture(

                frontend=data[

                    "frontend"

                ],

                backend=data[

                    "backend"

                ],

                database=data[

                    "database"

                ],

                authentication=data[

                    "authentication"

                ],

                cache=data[

                    "cache"

                ],

                modules=data[

                    "modules"

                ],

                deployment=data[

                    "deployment"

                ]

            )


            self.state.update(

                "architecture",

                architecture

            )


            print()

            print(

                "Architect created architecture successfully."

            )


        except Exception as e:


            print()

            print(

                "Failed to parse architecture."

            )

            print(e)