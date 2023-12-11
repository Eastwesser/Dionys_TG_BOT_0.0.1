'''
import os
import threading
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image
from rembg import remove

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

forecast_api = "0ddd3a2c6e4f80e906a0ad517358d967"


async def process_image(message: types.Message):
    try:
        file_id = message.photo[-1].file_id
        file_info = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(file_info.file_path)

        with open('input_photo.png', 'wb') as new_file:
            new_file.write(downloaded_file)

        input_photo = 'input_photo.png'
        output_photo = 'output_photo.png'

        input_image = Image.open(input_photo)
        output_image = remove(input_image)
        output_image.save(output_photo)

        with open(output_photo, 'rb') as file:
            await bot.send_photo(message.chat.id, file)

        os.remove('input_photo.png')
        os.remove('output_photo.png')

    except Exception as e:
        print(f"Error processing image: {e}")


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    t = threading.Thread(target=process_image, args=(message,))
    t.start()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

'''