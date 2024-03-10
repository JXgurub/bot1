import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import button
from api import create_user
from states import gmailState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
API_TOKEN = 'bot Tokinnni kiriting'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum yaxshimisiz\n sizga qanday yordam bera olaman")
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_id))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)