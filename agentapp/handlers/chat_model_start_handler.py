from typing import Any, Dict, List
from uuid import UUID
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from pyboxen import boxen


def print_box(*args, **kwargs):
    print(boxen(*args, **kwargs))

class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        
        print("==================SENDING MESSAGES===============\n\n")

        for message in messages[0]:
            if message.type =="system":
                print_box(message.content, title=message.type, color="yellow")
            
            elif message.type=="human":
                print_box(message.content, title=message.type, color="green")

            elif message.type == "ai" and  "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                print_box(
                    f"Running Tool {call['name']} with args {call['arguments']}",
                    title=message.type,
                    color = "cyan")
            elif message.type=="ai":
                print_box(message.content, title=message.type, color="blue")
            elif message.type=="function":
                print_box(message.content, title=message.type, color="purple")
            else:
                print_box(message.content, title=message.type, color="purple")


            


