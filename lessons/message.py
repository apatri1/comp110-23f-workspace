"""Class to store a message (operator overloads, default parameters, union types)."""

class Message:

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool):
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag


    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f"{self.content}"
        return output
    

    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg_to_myself: Message = Message("me", "Do your 110 homework!", True)
msg_to_myself * 10
print(msg_to_myself)
