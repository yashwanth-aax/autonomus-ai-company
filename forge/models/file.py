# forge/models/file.py


from dataclasses import dataclass


@dataclass

class File:


    path: str

    content: str


    def show(self):

        print()

        print("="*50)

        print(self.path)

        print("="*50)

        print()

        print(self.content)