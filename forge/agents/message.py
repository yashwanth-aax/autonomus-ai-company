# forge/agents/message.py

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Message:
    sender: str
    receiver: str
    content: str

    timestamp: datetime = field(
        default_factory=datetime.now
    )

    def __str__(self):

        return (
            f"[{self.timestamp.strftime('%H:%M:%S')}] "
            f"{self.sender} -> "
            f"{self.receiver}: "
            f"{self.content}"
        )