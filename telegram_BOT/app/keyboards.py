from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог'),
                                     KeyboardButton(text='Карзина')],
                                     [KeyboardButton(text='Контакты'),
                                     KeyboardButton(text='О нас')]],
                                     resize_keyboard=False,
                                     input_field_placeholder='Выберите пункт меню...')

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='куртка', callback_data='kovta')],
                                                [InlineKeyboardButton(text='штаны', callback_data='sharf')],
                                                [InlineKeyboardButton(text='обувь', callback_data='ris')]])

pomosh = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помощь'),
                                     KeyboardButton(text='Не работает бот')],
                                     [KeyboardButton(text ='Вернуться назад')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Выберите пункт меню...')
