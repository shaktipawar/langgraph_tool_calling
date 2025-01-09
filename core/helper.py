from termcolor import colored
from enum import Enum
from langchain_core.messages import HumanMessage, SystemMessage

class ColorPalette(Enum):
    USER_MESSAGE = "green"
    AI_MESSAGE = "magenta"

class MessageType(Enum):
    AI_REPLY = "AI_REPLY"     

class Helper():

    def print_log(messagetype, message):

        match messagetype.value:
            case MessageType.AI_REPLY.value:
                print(colored(f"Jarvis : {message}", "green"))
                NotImplemented

    def get_prompt(system_prompt, user_prompt):
        if user_prompt:
            return [SystemMessage(content = system_prompt),HumanMessage(content = user_prompt)]
        else:
            return [SystemMessage(content = system_prompt)]