from modules import pc_manage
from init import *

bot, trusted, system = start()


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.id == trusted:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton(text=f"{system} 🟩")
        markup.add(btn1)
        bot.send_message(trusted, 'Добро пожаловать! \n\nВыберите устройство:', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Не-а! Нет доступа 🙃', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "poweroff":
        bot.edit_message_text(f'Устройству {system} был отправлен запрос на завершение работы.\n\n💬 Ответ '
                              f'модуля: {pc_manage.shutdown_system()}', chat_id=trusted,
                              message_id=call.message.message_id)
    elif call.data == "hibernate":
        bot.edit_message_text(f'Устройству {system} был отправлен запрос на отправку системы в режим '
                              f'сна\n\n💬 Ответ модуля: {pc_manage.hibernate_system()}', chat_id=trusted,
                              message_id=call.message.message_id)
    elif call.data == "block_system":
        bot.edit_message_text(f'Устройству {system} был отправлен запрос на блокировку системы\n\n💬 Ответ '
                              f'модуля: {pc_manage.block_system()}', chat_id=trusted,
                              message_id=call.message.message_id)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.from_user.id == trusted:
        if message.text == f"{system} 🟩":
            markup = telebot.types.InlineKeyboardMarkup()
            shutdown = telebot.types.InlineKeyboardButton(text="📴 Завершение работы",
                                                          callback_data="poweroff")
            hibernation = telebot.types.InlineKeyboardButton(text="💤 Режим сна",
                                                             callback_data="hibernate")
            block_user = telebot.types.InlineKeyboardButton(text="🚫 Заблокировать систему",
                                                            callback_data="block_system")
            markup.add(shutdown, hibernation)
            markup.add(block_user)
            bot.send_message(trusted, f"{system}\nСтатус: 🟩", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Не-а! Нет доступа 🙃', reply_markup=telebot.types.ReplyKeyboardRemove())


if __name__ == "__main__":
    while True:
        try:
            bot.polling()
        except requests.exceptions.ReadTimeout:
            graphics.error("Пропало подключение к интернету! Акира была отключена.")
            sys.exit()
