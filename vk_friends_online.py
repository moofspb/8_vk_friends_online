import vk


APP_ID = 5887873
# чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Enter user login: ')


def get_user_password():
    return input('Enter user password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2
    )
    api = vk.API(session)
    friends = api.friends.getOnline()
    return friends


def output_friends_to_console(friends_online):
    # [print(get_name) for id in friends]
    pass

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
