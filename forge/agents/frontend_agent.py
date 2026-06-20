# forge/agents/frontend_agent.py

from agents.base_agent import Agent

from models.file import File

from tools.code_generator_tool import CodeGeneratorTool

from tools.file_writer_tool import FileWriterTool


class FrontendAgent(Agent):

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

            f"{self.name} is generating frontend..."

        )


    def page_name(

        self,

        backend_path

    ):

        folder = (

            backend_path

            .split("/")

            [-2]

        )


        return (

            folder

            .replace("_"," ")

            .title()

            .replace(" ","")

        )


    def act(self):

        architecture = self.state.get(

            "architecture"

        )


        backend_files = self.state.get(

            "backend_files"

        )


        frontend_files = {}


        print()

        print(

            "Generating common frontend files..."

        )


        common_files = {

            "frontend/App.jsx":

            """

Create React App.jsx.

Requirements:

1. Use React Router.

2. Import Navbar.

3. Render routes.

4. Minimal clean code.

Return ONLY code.

""",



            "frontend/components/Navbar.jsx":

            """

Create reusable Navbar.

Requirements:

1. Functional component

2. Navigation links

3. Minimal styling

Return ONLY code.

""",



            "frontend/services/api.js":

            f"""

Backend Files:

{list(backend_files.keys())}


Create axios wrapper.


Requirements:

1. Export api object

2. Export GET, POST, PUT, DELETE helpers

3. Minimal code

Return ONLY code.

"""

        }


        for path,prompt in common_files.items():

            code = self.codegen.generate(

                prompt

            )


            frontend_files[

                path

            ] = File(

                path=path,

                content=code

            )



        print()

        print(

            "Generating pages..."

        )


        for path,file in backend_files.items():


            if not path.endswith(

                "router.py"

            ):

                continue


            page = self.page_name(

                path

            )


            frontend_path = (

                f"frontend/pages/"

                f"{page}.jsx"

            )


            print(

                f"Generating "

                f"{page}.jsx"

            )


            prompt = f"""

You are a Senior React Developer.


Frontend Framework:

{architecture.frontend}


Backend Router:

{file.content}


Create React page.


Requirements:

1. Functional component

2. Use hooks

3. Use api.js

4. If GET exists:

    show list/table

5. If POST exists:

    show form

6. If DELETE exists:

    show delete button

7. Minimal styling

8. Return ONLY code.

"""


            code = self.codegen.generate(

                prompt

            )


            frontend_files[

                frontend_path

            ] = File(

                path=frontend_path,

                content=code

            )



        self.writer.write_many(

            frontend_files

        )


        self.state.update(

            "frontend_files",

            frontend_files

        )


        self.send_message(

            "CEO",

            f"Generated "

            f"{len(frontend_files)} "

            f"frontend files."

        )


        print()

        print(

            f"Frontend generated "

            f"{len(frontend_files)} "

            f"files."

        )