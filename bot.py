import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from callbacks import pagination
from config_reader import config
from handlers import bot_messages, user_commands, questionaire


async def main():
    session = AiohttpSession(proxy="http://proxy.server:3128/")
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML", session=session)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
