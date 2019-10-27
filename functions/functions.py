from dialog_bot_sdk.bot import DialogBot
from config.config import bot
import db.db as core_db


def add_topic(peer: str, command: str):
    try:
        str1, str2 = command.split(" ", 1)
    except:
        str1 = command
        str2 = None
    core_db.add_topic(str1, str2)
    send_message(
        peer,
        'added topic'
    )


def show_all_topic(peer: str, command: str):
    res = core_db.show_all_topic()
    send_message(
        peer,
        res
    )


def show_topic(peer: str, command: str):
    res = core_db.show_topic(command)
    send_message(
        peer,
        res
    )


command_list = {
    'add_topic': add_topic,
    'show_all_topics': show_all_topic,
    'show_topic': show_topic,
}


def send_message(peer, msg: str) -> None:
    bot.messaging.send_message(
        peer,
        msg
    )


def get(string: str):
    str2 = None
    try:
        str1, str2 = string.split(" ", 1)
    except:
        str1 = string
    return str1, str2


def check(peer, command: str) -> bool:
    command, params = get(command)
    if command not in command_list:
        send_message(
            peer,
            'Invalid command'
        )

        return False
    command_list[command](peer, params)
    return True
