import random

from aiogram import Router, Bot, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message

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


@router.message(Command("test"))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "test")
