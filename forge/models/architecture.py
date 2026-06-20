# forge/models/architecture.py

from dataclasses import dataclass, field

from datetime import datetime

from typing import List


@dataclass
class Architecture:

    frontend: str

    backend: str

    database: str

    authentication: str

    cache: str

    modules: List[str]

    deployment: str

    created_at: datetime = field(
        default_factory=datetime.now
    )

    def show(self):

        print()

        print("=" * 50)

        print("SYSTEM ARCHITECTURE")

        print("=" * 50)


        print("\nFrontend:")

        print(self.frontend)


        print("\nBackend:")

        print(self.backend)


        print("\nDatabase:")

        print(self.database)


        print("\nAuthentication:")

        print(self.authentication)


        print("\nCache:")

        print(self.cache)


        print("\nModules:")

        for module in self.modules:

            print(f"- {module}")


        print("\nDeployment:")

        print(self.deployment)