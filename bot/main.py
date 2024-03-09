import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import button
from api import create_user,create_gmail
from states import gmailState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
API_TOKEN = '5823103610:AAGxGKk10qVvwRCyCXJucJ_EyBMSL4g6rm0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum baqqata \n ishlar jollimi",reply_markup=button )
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_id))


@dp.message_handler(Text(startswith="emailinggizni tekshiring"))
async def gmail_1(message: types.Message):
    await message.answer("xabar matini yuboring")
    await gmailState.gmail.set()
    
    
@dp.message_handler(state=gmailState.gmail)
async def gmail_2(message:types.Message,state:FSMContext):
    await message.answer(create_gmail(message.from_user.id, message.text , message.text))
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)