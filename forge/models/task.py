# forge/models/task.py

from dataclasses import dataclass


@dataclass
class Task:

    id: int

    title: str

    description: str

    status: str = "Pending"

    assigned_to: str = "None"

    def show(self):

        print()

        print(f"Task #{self.id}")

        print(f"Title: {self.title}")

        print(f"Description: {self.description}")

        print(f"Status: {self.status}")

        print(f"Assigned To: {self.assigned_to}")