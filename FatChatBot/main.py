import logging
import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import emoji
import random
from keyboards import kb1
from popugai import popugai

#Vkluchaem logirovanie
logging.basicConfig(level=logging.INFO)

#Sozdaem object bota
bot = Bot(token=config.token)

#Dispecher
dp = Dispatcher()

#Handler na comandu
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name=message.chat.first_name
    await message.answer(f'Privet, {name}', reply_markup=kb1)

@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Bye, {name}')

#PodkluchaemService
@dp.message(Command('ShowPicture'))
@dp.message(Command('picture'))
@dp.message(F.text.lower() == 'arbu')
async def show_picture(message: types.Message):
    name = message.chat.first_name
    #imgpop = popugai()
    await message.answer_photo(photo='https://img.freepik.com/free-photo/closeup-shot-of-a-macaw-parrot-with-colorful-feathers-on-a-grey-background_181624-24916.jpg?size=626&ext=jpg&ga=GA1.1.1145443884.1710612999&semt=ais')
    #await bot.send_photo(message.from_user.id, photo=imgpop)

#Handler na soobschenia
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    name = message.chat.first_name
    if 'hi' in msg_user:
        #await message.answer_dice(emoji="😍")
        #await message.answer('\U0001F440')
        await message.answer(':heart:')
    else:
        await message.answer(f'You entered - {msg_user}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())