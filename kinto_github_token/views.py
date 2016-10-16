import requests
from kinto.core import Service, logger

search = Service(name="search",
                 path='/github/token',
                 description="Github Access Token")

@search.post()
def get_search(request):
    authorization_code = request.POST['authorization_code']

    try:
        payload = {
            'client_id': 'bc6a0e70dc379a6313ae',
            'client_secret': '99ca1391ae9b8bc0c0a71628629e43ab32c17def',
            'code': authorization_code
        }
        headers = {"Accept": "application/json"}
        resp = requests.post('https://github.com/login/oauth/access_token', data=payload, headers=headers)
        resp.raise_for_status()
        respjson = resp.json()
        return respjson
    except Exception as e:
        logger.exception(e)
        return None

