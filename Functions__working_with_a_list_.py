messages = ['Просто здравствуй', 'Просто как дела', '=3']
send_mess = []

def show_messages(message):
    for mess in message:
        print(mess)


def send_messages(send_mess):
    while messages:
        send = messages.pop()
        send_mess.append(send)
        print(send)

       

show_messages(messages)
send_messages(send_mess)