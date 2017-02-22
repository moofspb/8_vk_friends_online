import getpass
import vk


APP_ID = 5887873


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return getpass.getpass(prompt='Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2
    )
    api = vk.API(session)
    raw_friend_ids = api.friends.getOnline(online_mobile=True)
    friend_ids = raw_friend_ids['online_mobile'] + raw_friend_ids['online']
    friends_online = api.users.get(user_ids=friend_ids)
    return friends_online


def output_friends_to_console(friends_online):
    print('Your friends online:')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
