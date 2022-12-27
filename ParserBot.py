from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from OneWkBot_credits import bot_token
import requests
from bs4 import BeautifulSoup


def get_weather():
    appid = "d9c55fa87ce5fa0674e1e580a1c17baf"
    city_id = 524901
    print('city_id=', city_id)

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    return data['weather'][0]['description'], data['main']['temp']


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Выберите:',
                              reply_markup=keyboard_main_menu())


def main_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Выберите:',
                            reply_markup=keyboard_main_menu())


def keyboard_main_menu():
    keyboard = [
        [InlineKeyboardButton("Погода", callback_data='1'),
         InlineKeyboardButton("Курс доллара", callback_data='2'), ],
    ]

    return InlineKeyboardMarkup(keyboard)


def weather(update: Update, context: CallbackContext) -> None:
    conditions, temp = get_weather()

    keyboard = [[InlineKeyboardButton("Главное меню", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Погода в Москве: "
                                 f"\n{conditions}, {temp}",
                            reply_markup=reply_markup)


def dollar(update: Update, context: CallbackContext) -> None:
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    keyboard = [[InlineKeyboardButton("Main menu", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Курс ЦБ РФ доллара США: \n"
                                 f"{data['Valute']['USD']['Value']}.",
                            reply_markup=reply_markup)


def main() -> None:
    updater = Updater(bot_token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(weather, pattern='1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dollar, pattern='2'))

    updater.start_polling()
    print('started')


if __name__ == '__main__':
    main()
