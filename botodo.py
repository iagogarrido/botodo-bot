#!/usr/bin/env python3

import configparser
import logging
import telepot
from telepot.loop import MessageLoop
import time


def read_config(config_file):
    config = configparser.ConfigParser()
    readed = config.read(config_file)

    if len(readed) == 0:
        raise Exception('error reading config file')

    return config


def get_logger(log_level):
    ll = logging.WARNING

    if log_level == 'DEBUG':
        ll = logging.DEBUG
    elif log_level == 'INFO':
        ll = logging.INFO
    elif log_level == 'ERROR':
        ll = logging.ERROR
    elif log_level == 'CRITICAL':
        ll = logging.CRITICAL

    logging.basicConfig(level=ll)
    
    return logging.getLogger(__name__)


def process_command(chat_id, msg_text):
    parsed_msg = msg_text.split(' ')

    logger.debug('command {}'.format(parsed_msg[0]))

    if parsed_msg[0] == '/listtasks':
        bot.sendMessage(chat_id, 'listoooo')
    elif parsed_msg[0] == '/addtask':
        bot.sendMessage(chat_id, 'añadoooo')
    else:
        bot.sendMessage(chat_id, 'ke dise lokooo!!')


def on_chat_message(msg):
    logger.debug(msg)

    content_type, chat_type, chat_id = telepot.glance(msg)
    logger.info('content_type={},chat_type={},chat_id={}'.format(content_type, chat_type, chat_id))

    msg_text = msg['text']

    if msg_text.startswith('/'):
        process_command(chat_id, msg_text)


config = read_config('botodo.conf')
logger = get_logger(config.get(config.default_section, 'LOG_LEVEL'))

logger.info('creating bot')
bot = telepot.Bot(config.get(config.default_section, 'BOT_TOKEN'))

logger.info('initiating message loop')
MessageLoop(bot, {'chat': on_chat_message,}).run_as_thread()

while 1:
    time.sleep(10)

