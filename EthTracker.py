#https://etherscan.io/myapikey
from requests import get
from matplotlib import pyplot as plt
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
#Getting everything from .dotenv file
API_KEY = os.getenv("BASE_KEY")
address = os.getenv("BASE_ADDRESS")
BASE_URL = 'https://api.etherscan.io/api'
MODIFIED_address = ''
MODIFIED_address = input('If specific address needed, enter address: ')
if MODIFIED_address != '':
    address = MODIFIED_address

#Only have one address, so no need for address to be a paramater :)
#Can change this later on
def api_URL(module,action,**kwargs):
    url = BASE_URL + f'?module={module}&action={action}&address={address}&apikey={API_KEY}'
    
    for key,value in kwargs.items():
        url += f'&{key}={value}'
        
    result = get_request(url)
    return result

#put the url from api_URL into this to get a result
def get_request(url):  
    response = get(url)
    data = response.json()  
    return data

#convert the idk thing to actual ether value
def convert_to_ether(result):
    value = int(result['result']) / 10 ** 18
    return value
    
def get_account_balance():
    result = api_URL('account','balance', tag = 'latest')
    return convert_to_ether(result)

def get_transaction_history():
    return api_URL('account','txlist',startblock=0,endblock=9999999,page=1,offset=10000,sort='asc')
    
print(get_transaction_history())

#waiting for api services to come back