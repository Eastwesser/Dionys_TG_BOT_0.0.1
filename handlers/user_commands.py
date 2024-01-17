import random

from aiogram import Router, Bot, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message

# from bot import collect_data
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello, <b>{message.from_user.first_name}</b>. "
                         f"This is AIOgram 3.x",
                         reply_markup=reply.main)


@router.message(Command(commands=["rn", "random-number"]))  # /rn 1-100
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)

    await message.reply(f"Random number: {rnum}")


@router.message(F.text == "play")
async def play_games(message: Message):
    x = await message.answer_dice(DiceEmoji.BOWLING)
    print(x.dice.value)


@router.message(F.text == "dice")
async def play_games1(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)


@router.message(F.text == "casino")
async def play_games1(message: Message):
    x = await message.answer_dice(DiceEmoji.SLOT_MACHINE)
    print(x.dice.value)


@router.message(F.text == "dart")
async def play_games2(message: Message):
    x = await message.answer_dice(DiceEmoji.DART)
    print(x.dice.value)


@router.message(F.text == "basketball")
async def play_games2(message: Message):
    x = await message.answer_dice(DiceEmoji.BASKETBALL)
    print(x.dice.value)


@router.message(F.text == "football")
async def play_games2(message: Message):
    x = await message.answer_dice(DiceEmoji.FOOTBALL)
    print(x.dice.value)


'''
# ======================================================================================================================
# PYTHON PARSING BOT FOR CS GO
# ======================================================================================================================
@router.message(Command(commands='start_cs'))
async def start_cs(message: types.Message):
    start_buttons = ['нож', 'снайпер']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@router.message(F.text == 'нож')
async def get_discount_knives(message: types.Message):
    await message.answer('Please waiting...')

    collect_data(cat_type=2)

    with open('rezult.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}🔥'

        await message.answer(card)


@router.message(F.text == 'снайпер')
async def get_discount_guns(message: types.Message):
    await message.answer('Please waiting...')

    collect_data(cat_type=4)

    with open('rezult.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}🔥'

        await message.answer(card)


# ======================================================================================================================

@router.message(F.text.one_of(["play", "dice", "casino", "dart", "basketball", "football"]))
async def play_games(message: Message):
    game_mapping = {
        "play": DiceEmoji.BOWLING,
        "dice": DiceEmoji.DICE,
        "casino": DiceEmoji.SLOT_MACHINE,
        "dart": DiceEmoji.DART,
        "basketball": DiceEmoji.BASKETBALL,
        "football": DiceEmoji.FOOTBALL
    }
    command = message.text.lower()

    x = await message.answer_dice(game_mapping[command])
    print(x.dice.value)



@router.message(Command(commands=['calculate']))
async def calculate_expression(expression):
    try:
        # Парсим введенное выражение без использования eval
        parsed_expr = ast.parse(expression, mode='eval')

        # Запускаем выполнение выражения в безопасной среде
        result = eval(compile(parsed_expr, filename="<string>", mode='eval'))

        return result
    except Exception as e:
        return f"Ошибка: {str(e)}"


async def calculate(message: types.Message):
    # Получаем введенное пользователем выражение
    expression = message.text.replace('/calculate', '').strip()

    # Выполняем расчет с помощью нашей функции
    result = await calculate_expression(expression)

    # Отправляем результат пользователю
    await message.reply(f"Ваш результат: {result}")
'''


# ======================================================================================================================

@router.message(Command("test"))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "test")
