import requests
import json

clientID = ""
clientSecret = ""

autUri = "https://classic.warcraftlogs.com/oauth/authorize"
tokenUri = "https://classic.warcraftlogs.com/oauth/token"
apiUri = "https://classic.warcraftlogs.com/api/v2/client"

auth = (clientID, clientSecret)

data = {"grant_type": "client_credentials"}


def get_token() -> None:
    with requests.Session() as session:
        response = session.post(tokenUri, data=data, auth=auth)

    if response.status_code == 200:
        store_token(response)


def store_token(response) -> None:
    try:
        with open(".creds.json", mode="w+", encoding="utf-8") as f:
            json.dump(response.json(), f)
    except OSError as e:
        print(e)
        return None


def read_token() -> None:
    try:
        with open(".creds.json", mode="r+", encoding="utf-8") as f:
            access_token = json.load(f)
        return access_token.get("access_token")
    except OSError as e:
        print(e)
        return None


def retrieve_header() -> dict[str, str]:
    return {"Authorization": f"Bearer {read_token()}"}


# graphQL-Query https://classic.warcraftlogs.com/v2-api-docs/warcraft/
def get_data(query: str, **kwargs) -> None:
    """Fetch Data"""
    data = {"query": query, "variables": kwargs}

    with requests.Session() as session:
        session.headers = retrieve_header()
        response = session.get(apiUri, json=data)
        print(str(response.status_code) + ": " + response.reason)
        return response.json()
