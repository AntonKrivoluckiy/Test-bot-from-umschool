import telebot

from init_bot import bot
from Commands.Commands import Game, not_game, game_, weather, Poem, time, eho_bot, echo, not_eho, start_bot, timep, get_weather


@bot.message_handler(func=lambda message: [echo, Game, weather, Poem, time, timep, echo, eho_bot, not_eho, start_bot, not_game, game_, get_weather])
def uncnown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неизвестная команда, пожалуйста, используйте встроенную в бота клавиатуру')