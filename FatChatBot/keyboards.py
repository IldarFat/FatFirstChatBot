from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='Stop')
button3 = types.KeyboardButton(text='Info')
button4 = types.KeyboardButton(text='ShowPicture')
button5 = types.KeyboardButton(text='Close')

keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1,resize_keyboard=True)