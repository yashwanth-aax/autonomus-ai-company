# forge/agents/base_agent.py

from abc import ABC, abstractmethod

from agents.message import Message


class Agent(ABC):

    def __init__(
        self,
        name,
        memory,
        event_bus,
        state
    ):

        self.name = name

        self.memory = memory

        self.event_bus = event_bus

        self.state = state

        self.inbox = []

        self.tools = []

    def receive_message(
        self,
        message
    ):

        self.inbox.append(message)

    def send_message(
        self,
        receiver,
        content
    ):

        message = Message(

            sender=self.name,

            receiver=receiver,

            content=content

        )

        self.event_bus.publish(message)

    def add_tool(
        self,
        tool
    ):

        self.tools.append(tool)

    def show_inbox(self):

        for msg in self.inbox:

            print(msg)

    @abstractmethod
    def think(self):

        pass

    @abstractmethod
    def act(self):

        pass