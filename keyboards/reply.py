from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смайлики"),
            KeyboardButton(text="Ссылки")
        ],
        [
            KeyboardButton(text="Калькулятор"),
            KeyboardButton(text="Спец. кнопки")
        ],
        [
            KeyboardButton(text="Дионис"),
            KeyboardButton(text="play")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить гео", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Создать викторину", request_poll=KeyboardButtonPollType(type="quiz"))
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

dionys = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Business Bot"),
            KeyboardButton(text="Photo Bot")
        ],
        [
            KeyboardButton(text="Mathix"),
            KeyboardButton(text="Game Bot")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

rmk = ReplyKeyboardRemove()