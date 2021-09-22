import requests
import os
import logging

current_dir  = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=f"{current_dir}/log/cronjobs.log", 
level=logging.DEBUG, 
format=f'[%(asctime)s] %(levelname)s - [%(filename)s]: %(message)s')

def getSomething():
    logging.info(f'iniciando job API')
    request = requests.get(
        url= 'https://api.github.com/user/',
        headers={"accept": "application/vnd.github.v3+json"},
        params={"name":"ThiagoBmg"}
    )
    logging.debug(f'api response {request.json()}')
    logging.info(f"concluindo job API")
    pass


getSomething()

   