# forge/state/project_state.py

class ProjectState:

    def __init__(self):

        self.state = {

            "idea": None,

            "prd": None,

            "tasks": [],
            
            "architecture": None,

            "backend_files": {},

            "frontend_files": {},

            "tests": {},

            "deployment": None
        }

    def update(self, key, value):

        self.state[key] = value

    def get(self, key):

        return self.state.get(key)

    def show(self):

        return self.state