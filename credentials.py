import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = {
    'CONSUMER_KEY' : os.environ['CONSUMER_KEY'],
    'CONSUMER_SECRET' : os.environ['CONSUMER_SECRET'],
    'ACCESS_TOKEN' : os.environ['ACCESS_TOKEN'],
    'ACCESS_SECRET' : os.environ['ACCESS_SECRET']
}