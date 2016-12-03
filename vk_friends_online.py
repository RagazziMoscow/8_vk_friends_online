import getpass
import vk


APP_ID = 5740470


def get_user_login():
    return(input("Введите логин:\n"))


def get_user_password():
    return(getpass.getpass("Введите пароль:\n"))


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline(order='hints')
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("{first_name} {last_name}".format(first_name=friend["first_name"],
                                                last_name=friend["last_name"]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("\n\nДрузья онлайн:\n")
    output_friends_to_console(friends_online)
