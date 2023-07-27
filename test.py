import openai
import os
from dotenv import load_dotenv # python-dotenv

load_dotenv()
openai.api_key = os.getenv('KeyNoteAPI')
openai.api_base = "https://chimeragpt.adventblocks.cc/v1"
def printurl():
    # response = openai.Image.create(
    #     prompt="a cute anime girl doing",
    #     n=1,
    #     size="256x256"
    # )
    print()
printurl()