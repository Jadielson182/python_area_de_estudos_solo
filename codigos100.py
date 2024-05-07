from dotenv import load_dotenv
import os

load_dotenv()

# print(os.environ)
print(os.getenv('BD_USER'))