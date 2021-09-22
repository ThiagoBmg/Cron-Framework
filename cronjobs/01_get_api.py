import requests
import os
import logging

# log config
current_dir  = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=f"{current_dir}/log/cronjobs.log", 
level=logging.DEBUG, 
format=f'[%(asctime)s] %(levelname)s - [%(filename)s]: %(message)s')


def step01():
    logging.info(f'iniciando job API')
    response = requests.get(url= f'https://api.github.com/users/ThiagoBmg')
    logging.debug(f'api response {response}')
    step02(response)

def step02(data):
    print(data.json())
    logging.info(f'finalizando job API')

step01()