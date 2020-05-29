import requests

token = "2e53bfc4bd56daf857708a8324b35a0692b02aa171c5ecf7138445ab5a32b637485204b5d0837e747a3e7"
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
