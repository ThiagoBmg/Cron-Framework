import requests
import os
import logging

# log config
current_dir  = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=f"{current_dir}/log/cronjobs.log", 
level=logging.DEBUG, 
format=f'[%(asctime)s] %(levelname)s - [%(filename)s]: %(message)s')

#https://aviationstack.com/dashboard
#https://aviationstack.com/documentation
API_KEY = '44029ca0634b1f7d532133ad687d4554'
BASE_URL = 'http://api.aviationstack.com/v1'

def step01():
    logging.info(f'iniciando job API')
    request = requests.get(
        url= f'{BASE_URL}/flights',
        params={"access_key": API_KEY}
    )
    logging.debug(f'api response {request.json()}')
    logging.info(f"concluindo job API")
    pass


step01()

   