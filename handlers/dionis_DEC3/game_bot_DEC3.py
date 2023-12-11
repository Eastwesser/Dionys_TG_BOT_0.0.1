'''
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from aiogram import executor

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Initialize user_data dictionary
user_data = {}

# Define the choices for the game
choices = ["rock", "paper", "scissors"]

class UserLanguage(I18nMiddleware):
    async def get_user_locale(self, action: str, args=None):
        user = types.User.get_current()
        language = user_data.get(user.id, {}).get('language', 'en')
        return language

i18n = UserLanguage()
dp.middleware.setup(i18n)

async def send_welcome_message(chat_id, language):
    if language == 'en':
        message_text = "Welcome to Rock-paper-scissors! Please choose your move:"
    else:
        message_text = "Добро пожаловать в КАМЕНЬ-НОЖНИЦЫ-БУМАГА! Пожалуйста, выберите свой ход:"

    # Create a custom keyboard for game choices
    choice_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for choice in choices:
        choice_markup.add(types.KeyboardButton(choice.capitalize()))

    await bot.send_message(chat_id, message_text, reply_markup=choice_markup)

@dp.message_handler(Command('start'))
async def handle_start(message: types.Message):
    user_id = message.from_user.id
    language = user_data.get(user_id, {}).get('language', 'en')

    # Initialize user game data
    user_data[user_id] = {'language': language, 'choice': None}

    await send_welcome_message(message.chat.id, language)

@dp.message_handler(lambda message: message.text.lower() in choices)
async def handle_choice(message: types.Message):
    user_id = message.from_user.id
    choice = message.text.lower()
    user_data[user_id]['choice'] = choice

    # Get a random choice for the bot
    bot_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(choice, bot_choice, user_data[user_id]['language'])

    # Send the result message
    await message.reply(result)

    # Reset the user's choice
    user_data[user_id]['choice'] = None

def determine_winner(user_choice, bot_choice, language):
    if user_choice == bot_choice:
        if language == 'en':
            return "It's a draw!"
        else:
            return "Ничья!"
    elif (
            (user_choice == "rock" and bot_choice == "scissors") or
            (user_choice == "scissors" and bot_choice == "paper") or
            (user_choice == "paper" and bot_choice == "rock")
    ):
        if language == 'en':
            return "You win!"
        else:
            return "Вы победили!"
    else:
        if language == 'en':
            return "Bot wins!"
        else:
            return "Бот победил!"

@dp.message_handler(Command('about'))
async def about_me(message: types.Message):
    await message.reply("I'm a simple Telegram bot for playing Rock-paper-scissors.\n"
                        "Just choose your move, and I'll let you know the result!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
'''