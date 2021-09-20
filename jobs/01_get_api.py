import requests
from datetime import datetime

from requests.api import head

def getSomething():
    data = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    print(f'iniciando job API ${data}')
    request = requests.get(
        url= 'https://api.github.com/user/',
        headers={"accept": "application/vnd.github.v3+json"},
        params={"name":"ThiagoBmg"}
    )
    print(f'Usuário localizado com sucesso -> ${request.json()}')
    print(f"concluindo job API {data}")
    pass

getSomething()