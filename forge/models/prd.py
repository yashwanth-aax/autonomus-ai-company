# forge/models/prd.py

from dataclasses import dataclass, field

from datetime import datetime

from typing import List


@dataclass

class PRD:

    title: str

    vision: str

    target_users: str

    features: List[str]

    requirements: List[str]

    user_stories: List[str]

    success_metrics: List[str]

    created_at: datetime = field(

        default_factory=datetime.now

    )


    def show(self):

        print()

        print("="*50)

        print(

            "PRODUCT REQUIREMENTS DOCUMENT"

        )

        print("="*50)


        print(

            f"\nTitle:\n"

            f"{self.title}"

        )


        print(

            f"\nVision:\n"

            f"{self.vision}"

        )


        print(

            f"\nTarget Users:\n"

            f"{self.target_users}"

        )


        print("\nFeatures:")

        for x in self.features:

            print(f"- {x}")


        print("\nRequirements:")

        for x in self.requirements:

            print(f"- {x}")


        print("\nUser Stories:")

        for x in self.user_stories:

            print(f"- {x}")


        print("\nSuccess Metrics:")

        for x in self.success_metrics:

            print(f"- {x}")