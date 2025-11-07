from dotenv import load_dotenv
import os

def load_ambient_variables():
    load_dotenv()
    return[os.getenv('SECRET_KEY'), os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('BROKER')]
