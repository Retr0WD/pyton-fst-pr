import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

pass_file = open('pass', 'r')
token = pass_file.readline().strip()
# password = pass_file.readline().strip()

def captcha_handler(captcha):
    """
    Обрабатываем каптчу
    :param captcha:
    :return:
    """
    key = input('Enter captcha code {0}: '.format(captcha.get_url()).strip())

    return captcha.try_again(key)

def main():
    """
    Получение сообщения из вк

    """
    vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('New msge: ')
            print(event.text)


main()
