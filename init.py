import json
import telebot
import sys
import requests
from modules import get_os, graphics

advert = "Система удаленного администрирования разработана проектом @akiraproject"


def start():
    try:
        with open('config.json') as json_file:
            data = json.load(json_file)
            token = data['token']
            trusted = data['trusted_id']
    except FileNotFoundError:
        cfg_create = open("config.json", "w")
        cfg_create.write("{\n    \"token\": \"token\",\n    \"trusted_id\": \"Your telegram_id in @getmyid_bot\"\n}")
        graphics.info("config.json: Файл конфигурации был создан. Произведите его настройку!")
        sys.exit()
    try:
        trusted = int(trusted)
    except ValueError:
        graphics.error("config.json: Неверно указан параметр \"trusted_id\". Он должен содержать только цифры!")
        sys.exit()
    try:
        bot = telebot.TeleBot(token)
        system = get_os.system()
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton(text=f"{system} 🟩")
        markup.add(btn1)
        bot.send_message(trusted, f'Устройство {system} появилось в сети.\n\n{advert}', reply_markup=markup)
        return bot, trusted, system
    except (telebot.apihelper.ApiTelegramException, requests.exceptions.ConnectionError):
        graphics.error("Введен неверный токен бота или отсутствует подключение к интернету! Работа Акиры "
                       "приостановлена.")
        sys.exit()
