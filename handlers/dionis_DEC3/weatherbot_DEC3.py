'''
import json
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

forecast_api = "0ddd3a2c6e4f80e906a0ad517358d967"

weather_images = {
    'Clear': 'sun.png',
    'Clouds': 'cloud.png',
    'Rain': 'rain.png',
    'Snow': 'snow.png',
}

weather_translations = {
    'Cloudy': 'Облачно',
    'Rain': 'Дождь',
    'Snow': 'Снег',
    'Clear': 'Ясно',
}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Выберите бота')  # предложение выбрать бота из следующих: Busybot, Photobot, Mathix, Gamebot


@dp.message_handler(content_types=['text'])
async def get_weather(message: types.Message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={forecast_api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        pressure_hPa = data['main']['pressure']
        pressure_mmHg = round(pressure_hPa * 0.750062, 2)
        weather_kind = data['weather'][0]['main']

        await message.reply(f"Температура сейчас: {temp}°C.\n"
                            f"Давление: {pressure_mmHg} мм рт ст.\n"
                            f"{weather_translations.get(weather_kind, 'Ясно')}.")  # Clear/Clouds/Rain/Snow

        image = weather_images.get(weather_kind, 'sun.png')
        file = InputFile('weather_pictures/' + image)
        await bot.send_photo(message.chat.id, file)
    else:
        await message.reply("Такого города нет. Введите существующий город, пожалуйста.")
        # ENG The city was not found. Enter the name of an existing city.


@dp.message_handler(lambda message: message.text.lower() == 'about me')
async def about_me(message: types.Message):
    await message.reply("I'm a simple Telegram bot for playing Rock-paper-scissors.\n"
                        "Just choose your move, and I'll let you know the result!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
'''