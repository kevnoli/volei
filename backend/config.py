from dotenv import load_dotenv
from os import getenv

load_dotenv()

database_url = getenv('DATABASE_URL')
