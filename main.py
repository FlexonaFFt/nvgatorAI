import replicate
from dotenv import load_dotenv
import os

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")


class Commands:


    def __init__(self):
        self = self

    @staticmethod
    def simple_promt(promt):
        for event in replicate.stream(
            "meta/meta-llama-3-70b-instruct",
            input={
                "prompt": f"{promt}"
            },
        ):
            print(str(event), end="")

if __name__ == '__main__':
    print("Hello, my name is nvgator!")
    print("How can i help you?")
    promt = input()
    Commands.simple_promt(promt)