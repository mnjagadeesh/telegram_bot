#!/usr/bin/env python
import requests

BOT_TOKEN_URL = 'https://api.telegram.org/bot<access-token>'
IDS = []


def telegram_bot_sendtext(bot_message, bot_chatID):
    send_text = ''.join(BOT_TOKEN_URL,
                        '/sendMessage?chat_id=',
                        bot_chatID,
                        '&parse_mode=Markdown&text=',
                        bot_message)

    resp = requests.get(send_text)
    return resp.json()


def sendMessages():
    global IDS
    updatesUrl = BOT_TOKEN_URL + '/getUpdates'
    response = requests.get(updatesUrl)
    # import pdb; pdb.set_trace()
    if response.json().get('result'):
        for i in response.json().get('result'):
            if not i['message']['from']['is_bot']:
                id = i['message']['from']['id']
                if id not in IDS:
                    IDS.append(id)
                    test = telegram_bot_sendtext("test message", str(id))
                    print(test)


if __name__ == '__main__':
    sendMessages()
