from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message

@bot.message_handler(commands=['survey'])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username} введи свое имя')

@bot.message_handler(state=UserInfoState.name)
def get_name(message:Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо, записал. Теперь введи свой возраст')
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Имя может содержать только буквы')
