#https://etherscan.io/myapikey
from requests import get
from matplotlib import pyplot as plt
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
API_KEY = os.getenv("BASE_KEY")
