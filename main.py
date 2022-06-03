"""
This is a echo bot.
It echoes any incoming text messages.
"""

from cgitb import text
from email import message
import logging
from tkinter import Menubutton

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import MenuButtonWebApp, WebAppInfo, WebAppData, MenuButton

from config import TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['loc'])
async def cmd_locate_me(message: types.Message):
    reply = "Click on the the button below to share your location"
    #await message.answer(reply, reply_markup=get_keyboard())
    #56.11652974585433, 47.2738052239553
    #print(message.chat.id)
    await bot.send_location(chat_id=message.chat.id,latitude=56.11652974585433, longitude = 47.2738052239553, live_period=900)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)