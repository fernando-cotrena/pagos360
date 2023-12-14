from os import getenv

from dotenv import load_dotenv

load_dotenv()

# declaration of constants of the loaded variables
URL_BASE = getenv("URL_BASE")
AUTH = getenv("AUTH")
