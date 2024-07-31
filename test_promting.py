import replicate
import os
from dotenv import load_dotenv 
load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def main():
    for event in replicate.stream(
        "meta/meta-llama-3-70b-instruct",
        input={
            "prompt": "Привет, можешь рассказать о себе?"
        },
    ):
        print(str(event), end="")

if __name__ == "__main__":
    main()