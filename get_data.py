import json

import lookup_users as user
import lookup_follows as follows
import tools as t

user_ids = []

try:
    user_names = "usernames=elonmusk,Tesla,SpaceX"
    user_fields = "user.fields=description,created_at"

    user_url = user.create_url(user_names, user_fields)
    user_response = user.connect_to_endpoint(user_url)

    with open("json/users.json", "w", encoding="utf-8") as users:
        users.write(json.dumps(user_response, indent=4, sort_keys=True, ensure_ascii=False))
except Exception as e:
    print(f'error in getting user data: {e}')

user_response_data = user_response["data"]
for urd in user_response_data:
    user_ids.append(urd["id"])

if user_ids:
    for user_id in user_ids:
        try:
            followers_field = follows.get_user_fields()
            followers_response = follows.connect_to_endpoint_with_tail(followers_field, "ers", user_id)
            with open(f'json/{user_id}_followers.json', "w", encoding="utf-8") as followers:
                followers.write(json.dumps(followers_response, indent=4, sort_keys=True, ensure_ascii=False))
        except Exception as e:
            print(f'error in getting followers data: {e}')

        try:
            following_field = follows.get_user_fields()
            following_response = follows.connect_to_endpoint_with_tail(following_field, "ing", user_id)
            with open(f'json/{user_id}_following.json', "w", encoding="utf-8") as following:
                following.write(json.dumps(following_response, indent=4, sort_keys=True, ensure_ascii=False))
        except Exception as e:
            print(f'error in getting following data: {e}')

# t.aggrate_nodes([user_response, followers_response, following_response])
# print(t.get_name(44196397))
# print(t.get_user_name(44196397))

