from llm.base_llm import BaseLLM


class MockLLM(BaseLLM):

    def generate(

        self,

        prompt: str

    ):

        print()

        print("LLM received prompt:")

        print(prompt)

        print()


        return {

            "vision":

            "A platform for book lovers.",


            "target_users":

            "Students and Readers",


            "features":[

                "Authentication",

                "Book Search",

                "Recommendations",

                "Reviews"

            ],


            "requirements":[

                "Fast API",

                "Responsive UI"

            ],


            "user_stories":[

                "User can login",

                "User can search books"

            ],


            "success_metrics":[

                "1000 users",

                "99% uptime"

            ]

        }