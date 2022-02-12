import requests

from config import BEARER_TOKEN
import json


def create_url(usernames, userfields):
    user_names = usernames  # up to 100 comma-separated usernames.

    """
    user.fields is adjustable, options include:
    created_at, description, entities, id, location, name,
    pinned_tweet_id, profile_image_url, protected,
    public_metrics, url, username, verified, and withheld
    """
    user_fields = userfields

    url = f'https://api.twitter.com/2/users/by?{user_names}&{user_fields}'

    return url


def create_auth(req):
    req.headers["Authorization"] = f'Bearer {BEARER_TOKEN}'
    req.headers["User-Agent"] = "v2UserLookupPython"

    return req


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=create_auth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            f'Request returned an error: {response.status_code} {response.text}'
        )
    return response.json()


if __name__ == "__main__":
    url = create_url("usernames=TwitterDev,TwitterAPI", "user.fields=description,created_at")
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
