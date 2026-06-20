# forge/agents/developer_agent.py
import json

from agents.base_agent import Agent

from models.file import File

from tools.code_generator_tool import CodeGeneratorTool

from tools.file_writer_tool import FileWriterTool


class DeveloperAgent(Agent):

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

        self.codegen = CodeGeneratorTool(

            llm

        )

        self.writer = FileWriterTool()


    def think(self):

        print()

        print(

            f"{self.name} is generating backend..."

        )


    def sanitize_folder_name(

        self,

        name

    ):

        return (

            name

            .lower()

            .replace("&","and")

            .replace("-","_")

            .replace(" ","_")

        )


    def act(self):

        architecture = self.state.get(

            "architecture"

        )


        backend_files = {}


        for module in architecture.modules:


            print()

            print(

                f"Generating module: "

                f"{module.name}"

            )


            folder = self.sanitize_folder_name(

                module.name

            )


            prompt = f"""

You are a Senior Backend Engineer.


Backend Framework:

{architecture.backend}


Module:

{module.name}


Description:

{module.description}


Generate STRICT JSON.


Format:

{{

"router.py":"...",

"service.py":"...",

"model.py":"..."

}}


Rules:

1. Return ONLY JSON

2. No markdown

3. No explanations

4. Values must contain valid Python code

"""


            response = self.codegen.generate(

                prompt

            )


            try:

                data = json.loads(

                    response

                )


                for filename,content in data.items():


                    path = (

                        f"backend/"

                        f"{folder}/"

                        f"{filename}"

                    )


                    file = File(

                        path=path,

                        content=content

                    )


                    backend_files[

                        path

                    ] = file


            except Exception as e:


                print()

                print(

                    f"Failed to parse "

                    f"{module.name}"

                )


                print(e)


        self.writer.write_many(

            backend_files

        )


        self.state.update(

            "backend_files",

            backend_files

        )


        self.send_message(

            "Frontend",

            "Backend generated."

        )


        print()

        print(

            f"Developer generated "

            f"{len(backend_files)} "

            f"files."

        )