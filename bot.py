import asyncio
import json

import requests
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from fake_useragent import UserAgent

from callbacks import pagination
from config_reader import config
from handlers import bot_messages, user_commands, questionaire

'''
ua = UserAgent()


# print(ua.random)

def collect_data(cat_type=2):
    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):  # цикл: в ссылке меняется параметр offset с шагом в 60

            # maxPrice=10000&minPrice=2000 - 2000$ минимальная цена, с этой цифрой можно играться
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type={cat_type}&withStack=true'
            try:
                response = requests.get(
                    url=url,
                    headers={'user-agent': f'{ua.random}'}
                )
                response.raise_for_status()  # Check if the request was successful

                data = response.json()
                if data.get('error') == 2:
                    return 'Data were collected'

                items = data.get('items')

                for i in items: # собираем/парсим только те позиции, которые нам нужны (скидка не менее 10%)
                    if i.get('overprice') is not None and i.get('overprice') < -10:
                        item_full_name = i.get('fullName')
                        item_3d = i.get('3d')
                        item_price = i.get('price')
                        item_over_price = i.get('overprice')

                        result.append( # формируем из собранных данных словарь
                            {
                                'full_name': item_full_name,
                                '3d': item_3d,
                                'overprice': item_over_price,
                                'item_price': item_price
                            }
                        )

                count += 1
                print(f'Page #{count}')
                print(url)

            except requests.exceptions.RequestException as e:
                print(f"Error in request: {e}")

        # if len(items) < 60:
        #    break


    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=True)

    print(len(rezult))
'''

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
