import requests

token = "1ce8c58c6369dd2f7657a3ea37e6814dbbd29892a16fd732ea1b506abd9a3db06d84af70fb8ab4c62c285"
user_id = "56719936"

album_names = requests.get("https://api.vk.com/method/photos.getAlbums?user_id=" +
                           user_id + '&v=5.8&access_token=' + token).json()

print("User albums:")
for name in album_names["response"]["items"]:
    try:
        album_title = name["title"]
        print(album_title)
    except KeyError:
        pass

print("\nUser friends:")
friends_id = requests.get("https://api.vk.com/method/friends.get?user_id=" +
                          user_id + '&v=5.8&access_token=' + token).json()

for people in friends_id["response"]["items"]:
    people_info = requests.get("https://api.vk.com/method/users.get?user_id="
                               + str(people) +
                               "&v=5.8&access_token=" + token).json()

    try:
        first_name = people_info["response"][0]["first_name"]
        last_name = people_info["response"][0]["last_name"]
        print(first_name + " " + last_name)
    except KeyError:
        pass
