import telebot
import config
import time
import vk

array = [None]
bot = telebot.TeleBot(config.token)

def posting():
    try:
        vk_api = vk.API(vk.AuthSession(app_id = 6087806 , user_login = '***', user_password = '***'))
        while True:
            post = vk_api.wall.get(owner_id=-45745333, count=1, offset=1)[1]
            if post['marked_as_ads'] == 0 and post['attachment']['type'] == 'photo' and post['id'] != array[0]:
                array[0] = post['id']
                bot.send_photo('@***', vk_api.wall.get(owner_id=-45745333, count=1, offset=1)[1]['attachment']['photo']['src_big'])
                time.sleep(2)
    except Exception as e:
        posting()
posting()

def main():
    sleep(1)

if __name__ == '__main__':
    main()