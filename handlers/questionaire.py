from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboards.builders import profile
from keyboards.reply import rmk

router = Router()


@router.message(Command("profile"))
async def fill_profile(message: Message, state: FSMContext): # назвали так, чтобы две функции profile не перебивали или перезаписывали друг друга
    await state.set_state(Form.name)
    await message.answer(
        "Давай начнем, введи своё имя!",
        reply_markup=profile(message.from_user.first_name)
    )

@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text) # мы обновляем данные в нашем state (по сути, словарь)
    await state.set_state(Form.age)
    await message.answer("Отлично, а теперь введи свой возраст", reply_markup=rmk)

@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit(): # метод isdigit() возвращает булевое значение (True/False)
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer(
            "Выберите пол",
            reply_markup=profile(["Парень", "Девушка"])
        )
    else:
        await message.answer("Введи число, ещё раз!") # обязательно заполнить это поле, иначе стэйт не будет работать



@router.message(Form.sex, F.text.casefold().in_(["парень", "девушка"])) # если пользователь ввел эти слова, то дальше обрабатывается эта функция
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Form.about)
    await message.answer("Расскажи о себе", reply_markup=rmk)


@router.message(Form.sex)
async def incorrect_form_sex(message: Message, state: FSMContext):
    await message.answer("Нажми на кнопку")


@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer("Введи что-нибудь поинтереснее")
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.photo)
        await message.answer("Теперь отправь своё фото")

@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id # -1, чтобы убрать последне фото, хорошего качества
    data = await state.get_data() # это последний стейт, с него мы получаем данные
    await state.clear() # завершаем стейт

    formatted_text = [] # выводим текстовую инфу
    [
        formatted_text.append(f"{key}: {value}") # создаем генератор
        for key, value in data.items() # метод айтемс возвращает ключ-значение
    ]

    await message.answer_photo(
        photo_file_id,  # выводим фото
        "\n".join(formatted_text)
    )

@router.message(Form.photo, ~F.photo) # ~ означает неравенство. То есть "форм фото != фото"
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer("Нет, отправь именно фото, а не файл!")
