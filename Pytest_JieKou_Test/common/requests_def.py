import requests


def requests_def(method, url, params=None, headers=None, json=None,data=None,files=None):
    try:
        resp = requests.request(method, url, params=params, headers=headers, json=json,data=data,files=files)
        return resp
    except requests.exceptions.ConnectionError as e:
        print(f"ConnectionError: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout: {e}")
        return None
    except requests.exceptions.TooManyRedirects as e:
        print(f"TooManyRedirects: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return None
    except Exception as e:
        print(f"Unknown Exception: {e}")
        return None