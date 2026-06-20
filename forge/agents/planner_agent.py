# forge/agents/planner_agent.py
import json

from agents.base_agent import Agent

from models.task import Task


class PlannerAgent(Agent):

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

            f"{self.name} is planning tasks..."

        )


    def act(self):

        architecture = self.state.get(

            "architecture"

        )


        prompt = f"""

You are an Engineering Manager.


Architecture Modules:

{architecture.modules}


Generate STRICT JSON.

Example:

{{

"tasks":[

{{

"title":"Create Auth Module",

"description":"Implement login and signup APIs."

}},


{{

"title":"Create Books Module",

"description":"Implement books CRUD APIs."

}}

]

}}


Rules:

1. Return ONLY JSON

2. No markdown

3. Valid JSON

"""


        response = self.llm.generate(

            prompt

        )


        print()

        print(

            "Raw Planner Output:\n"

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


            tasks = []


            for idx, task_data in enumerate(

                data["tasks"],

                start=1

            ):


                task = Task(

                    id=idx,

                    title=task_data["title"],

                    description=task_data["description"]

                )


                tasks.append(task)


            self.state.update(

                "tasks",

                tasks

            )


            print()

            print(

                f"Planner created "

                f"{len(tasks)} tasks."

            )


        except Exception as e:


            print()

            print(

                "Failed to parse tasks."

            )


            print(e)