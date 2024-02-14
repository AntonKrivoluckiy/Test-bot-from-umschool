import datetime
import math
import random

import requests
import telebot

from init_bot import bot


@bot.message_handler(commands=['start'])
def hello(message: telebot.types.Message):
    button = telebot.util.quick_markup(
        {
            "-1 к мск": {'callback_data': 'Timer-1'},
            "+0 к мск": {'callback_data': 'Timer0'},
            "+1 к мск": {'callback_data': 'Timer+1'},
            "+2 к мск": {'callback_data': 'Timer+2'},
            "+3 к мск": {'callback_data': 'Timer+3'},
            "+4 к мск": {'callback_data': 'Timer+4'},
            "+5 к мск": {'callback_data': 'Timer+5'},
            "+6 к мск": {'callback_data': 'Timer+6'},
            "+7 к мск": {'callback_data': 'Timer+7'},
            "+8 к мск": {'callback_data': 'Timer+8'},
            "+9 к мск": {'callback_data': 'Timer+9'},
        }
    )
    bot.reply_to(message,text='Привет! Для коректной работы некоторых моих функций укажи, пожалуйста, свой часовой пояс относительно Москвы', reply_markup=button)

time_ = 0

@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer-1')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = -1
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer0')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 0
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+1')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 1
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+2')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 2
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+3')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 3
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+4')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 4
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+5')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 5
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+6')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 6
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+7')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 7
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+8')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 8
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')
@bot.callback_query_handler(func=lambda callback: callback.data == 'Timer+9')
def timep(callback: telebot.types.CallbackQuery):
    global time_
    time_ = 9
    bot.send_message(callback.from_user.id, 'Спасибо, теберь бот полностью настроен и готов к работе, для начала работы используйте команду:\n/go')

def timer() -> str:
    global time_
    _time = datetime.datetime.now()
    local_time = _time + datetime.timedelta(hours=time_)
    if 0 <= local_time.hour <= 4:
        return 'Доброй ночи!'
    if 4 <= local_time.hour <= 12:
        return 'Доброе утро!'
    if 12 <= local_time.hour <= 16:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'

@bot.message_handler(commands=['go'])
def start_bot(message: telebot.types.Message):
    text = (f'{timer()} Я тестовый бот, задачей которого является развлечение пользователя и выдача ему некоторой информации, давай я раскажу тебе немного о моем функционале:'
            '\n    1. Я могу написать тебе один из небольшого количества стишков, которые я нахожу в своих файлах, для этого тебе нужно нажать на кнопку "Раскажи стишок";'
            '\n    2. Я так же могу работать в режиме эхо-бота (это ознает, что я буду повторять любые ваши сообщения), для этого вам требуется нажать на кнопку "Режим эхо-бота";'
            '\n    3. У меня также есть функция, в которой я могу показать точное время в столице и в вашем регионе, или погоду в любои городе мира (желательно указывать ближайший крупный населенный пункт), для этого вам необходимо нажать на кнопки: "Время" и "Погода" соответственно;'
            '\n    4. И последнее, чем меня одарил разработчик - небольшая, но всем известная игра - "Камень, Ножницы, Бумага", для активации этого режима вам нужно нажать на одноименную кнопку.'
            '\nЧто бы перезапустить бота используйте команду: /start'
            )
    bot.send_message(message.chat.id, text)
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Камень, ножницы, бумага'))
    button.add(telebot.types.KeyboardButton('Режим эхо-бота'))
    button.add(
        telebot.types.KeyboardButton('Время'),
        telebot.types.KeyboardButton('Раскажи стишок'),
        telebot.types.KeyboardButton('Погода')
    )
    bot.reply_to(message, text='Клавиатура включена', reply_markup=button)

eho = False
@bot.message_handler(func=lambda message: message.text == 'Режим эхо-бота')
def eho_bot(message):
    global eho
    eho = not eho
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Выход из режима эхо-бота'))
    bot.reply_to(message,  text='Режим эхо-бота включен\nЧтобы выйти из режима эхо-бота, нажмите на кнопку "Выход из режима эхо-бота"', reply_markup=button)
@bot.message_handler(func=lambda message: message.text == 'Выход из режима эхо-бота')
def not_eho(message: telebot.types.Message):
    global eho
    eho = not eho
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Камень, ножницы, бумага'))
    button.add(telebot.types.KeyboardButton('Режим эхо-бота'))
    button.add(
        telebot.types.KeyboardButton('Время'),
        telebot.types.KeyboardButton('Раскажи стишок'),
        telebot.types.KeyboardButton('Погода')
    )
    bot.reply_to(message, text='Режим эхо-бота выключен', reply_markup=button)
@bot.message_handler(func=lambda message: eho)
def echo(message):
    bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: message.text == 'Время')
def time(message: telebot.types.Message):
    global time_
    time = datetime.datetime.now()
    if time_ == datetime.datetime.now():
        text = f'Местное время: {time.hour}:{time.minute}:{time.second}'
        bot.send_message(message.chat.id, text)
    else:
        local_time = time + datetime.timedelta(hours=time_)
        text = f'Местное время: {local_time.hour}:{local_time.minute}:{local_time.second}\nМосковское время: {time.hour}:{time.minute}:{time.second}'
        bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == 'Раскажи стишок')
def Poem(message: telebot.types.Message):
    with open('Poems/Poems.txt', 'r', encoding='utf-8') as file:
        poems = file.read().split('\n\n\n')
        poem_ = random.choice(poems)
    bot.send_message(message.chat.id, text=f'Вот стих, который я нашел:\n\n {poem_}')

weather_ = False
@bot.message_handler(func=lambda message: message.text == 'Погода')
def weather(message: telebot.types.Message):
    global weather_
    weather_ = True
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Выход'))
    bot.send_message(message.chat.id,'Введите, пожалуйста, названия города в котором хотите посмотреть погоду. Если захотите выйти из режима погоды, нажмите на кнопку "Выход"', reply_markup=button)

@bot.message_handler(func=lambda message: message.text == 'Выход')
def not_weather(message: telebot.types.Message):
    global weather_
    weather_ = False
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Камень, ножницы, бумага'))
    button.add(telebot.types.KeyboardButton('Режим эхо-бота'))
    button.add(
        telebot.types.KeyboardButton('Время'),
        telebot.types.KeyboardButton('Раскажи стишок'),
        telebot.types.KeyboardButton('Погода')
    )
    bot.reply_to(message, text='Режим погоды выключен', reply_markup=button)

@bot.message_handler(func=lambda message: weather_)
def get_weather(message: telebot.types.Message):
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&units=metric&appid=0e15548c924a0be1bdb15ca016ba29ec")
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]

        weather_description = data["weather"][0]["main"]
        weather_now = {
            "Clear": "Ясно",
            "Clouds": "Облачно",
            "Rain": "Дождь",
            "Drizzle": "Дождь",
            "Thunderstorm": "Гроза",
            "Snow": "Снег",
            "Mist": "Туман"
        }

        weather_now_ = weather_now[weather_description]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        bot.send_message(message.chat.id,f"\n Погода в городе: {city}:"
            f"\n    Погода: {weather_now_}"
            f"\n    Температура: {cur_temp}°C"
            f"\n    Влажность в городе: {humidity},"
            f"\n    Давление: {math.ceil(pressure/1.333)} мм.рт.ст,"
            f"\n    Ветер: {wind} м/с"
            f"\n    Восход солнца: {sunrise_timestamp}, Закат солнца: {sunset_timestamp}"
            f"\n    Продолжительность дня: {length_of_the_day}"
                        )
    except:
        bot.send_message(message.chat.id,'Произошла небольшая ошибка. Пожалуйста проверьте название города!')

wins_player = 0
wins_bot = 0
global_wins_player = 0
global_wins_bot = 0
game = False

@bot.message_handler(func=lambda message: message.text == 'Камень, ножницы, бумага')
def Game(message: telebot.types.Message):
    global game
    game = True
    buttons = telebot.types.ReplyKeyboardMarkup()
    buttons.add(telebot.types.KeyboardButton('Выход из режима игры'))
    buttons.add(telebot.types.KeyboardButton('Общее количество побед'))
    buttons.add(
    telebot.types.KeyboardButton('Камень'),
    telebot.types.KeyboardButton('Ножницы'),
    telebot.types.KeyboardButton('Бумага'),
               )
    bot.reply_to(message, 'Режим игры включен', reply_markup=buttons)

@bot.message_handler(func=lambda message: message.text == 'Выход из режима игры')
def not_game(message: telebot.types.Message):
    global game
    game = False
    button = telebot.types.ReplyKeyboardMarkup()
    button.add(telebot.types.KeyboardButton('Камень, ножницы, бумага'))
    button.add(telebot.types.KeyboardButton('Режим эхо-бота'))
    button.add(
        telebot.types.KeyboardButton('Время'),
        telebot.types.KeyboardButton('Раскажи стишок'),
        telebot.types.KeyboardButton('Погода')
    )
    bot.reply_to(message, text='Режим игры выключен', reply_markup=button)

@bot.message_handler(func=lambda message: game)
def game_(message: telebot.types.Message):
    otvets = ['Камень', 'Ножницы', 'Бумага']
    otvet = random.choice(otvets)
    bot.send_message(message.chat.id, f'Бот выбрал: {otvet}')
    global wins_player, wins_bot, global_wins_player, global_wins_bot
    if message.text == otvet:
        bot.send_message(message.chat.id, f'Ничья, общий счет: {wins_player}/{wins_bot}')
    if message.text == 'Камень':
        if otvet == 'Бумага':
            wins_bot += 1
            bot.send_message(message.chat.id, f'Поражение, общий счет: {wins_player}/{wins_bot}')
        if otvet == 'Ножницы':
            wins_player += 1
            bot.send_message(message.chat.id, f'Победа, общий счет: {wins_player}/{wins_bot}')
        if wins_player == 3:
            bot.send_message(message.chat.id, f'Вы победили со счетом: {wins_player}/{wins_bot}. Так держать!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_player += 1
        if wins_bot == 3:
            bot.send_message(message.chat.id, f'Вы проиграли со счетом: {wins_player}/{wins_bot}. Не растраивайтесь и попробуйте снова, у вас точно получится!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_bot += 1
    if message.text == 'Ножницы':
        if otvet == 'Камень':
            wins_bot += 1
            bot.send_message(message.chat.id, f'Поражение, общий счет: {wins_player}/{wins_bot}')
        if otvet == 'Бумага':
            wins_player += 1
            bot.send_message(message.chat.id, f'Победа, общий счет: {wins_player}/{wins_bot}')
        if wins_player == 3:
            bot.send_message(message.chat.id, f'Вы победили со счетом: {wins_player}/{wins_bot}. Так держать!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_player += 1
        if wins_bot == 3:
            bot.send_message(message.chat.id, f'Вы проиграли со счетом: {wins_player}/{wins_bot}. Не растраивайтесь и попробуйте снова, у вас точно получится!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_bot += 1
    if message.text == 'Бумага':
        if otvet == 'Ножницы':
            wins_bot += 1
            bot.send_message(message.chat.id, f'Поражение, общий счет: {wins_player}/{wins_bot}')
        if otvet == 'Камень':
            wins_player += 1
            bot.send_message(message.chat.id, f'Победа, общий счет: {wins_player}/{wins_bot}')
        if wins_player == 3:
            bot.send_message(message.chat.id, f'Вы победили со счетом: {wins_player}/{wins_bot}. Так держать!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_player += 1
        if wins_bot == 3:
            bot.send_message(message.chat.id,f'Вы проиграли со счетом: {wins_player}/{wins_bot}. Не растраивайтесь и попробуйте снова, у вас точно получится!!!')
            wins_player = 0
            wins_bot = 0
            global_wins_bot += 1
    if message.text == 'Общее количество побед':
        bot.send_message(message.chat.id, f'Вы победили {global_wins_player} раз\nВы проиграли {global_wins_bot} раз')

