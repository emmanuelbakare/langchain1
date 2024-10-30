from langchain.callbacks.base import BaseCallbackHandler
from  pyboxen import  boxen


def print_boxen(*args, **kwargs):
    print(boxen(*args, **kwargs))


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        for message in messages[0]:
            if message.type=="system":
                print_boxen(message.content, title=message.type, color="yellow")

            elif message.type=="human":
                print_boxen(message.content, title=message.type, color="green")

            elif message.type=="ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                print_boxen(
                    f"Running Tool {call['name']} with arguments {call['arguments']}",
                    title = message.type,
                    color="cyan"
                )
            elif message.type == "ai":
                print_boxen(message.content, title=message.type, color="blue")
            elif message.type == "function":
                print_boxen(message.content, title=message.type, color="purple")
            else:
                print_boxen(message.content, title=message.type)
