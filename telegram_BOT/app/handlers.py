from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message, ):
    await message.answer('Здравствуйте!', reply_markup=kb.main)
    await message.answer('Если нужна помощь напиши "/help")')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи', reply_markup=kb.pomosh)

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара (еще не работает)', reply_markup=kb.catalog)

@router.message(F.text == 'Вернуться назад')
async def cmd_start(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.main)

@router.message(F.text == 'Карзина')
async def cmd_start(message: Message):
    await message.answer('Сдесь пусто)')

@router.message(F.text == 'Контакты')
async def cmd_start(message: Message):
    await message.answer('8-989-230-**-**')

@router.message(F.text == 'О нас')
async def cmd_start(message: Message):
    await message.answer('Пусто')

@router.message(F.text == 'Помощь')
async def cmd_start(message: Message):
    await message.answer('чем помочь?')

@router.message(F.text == 'Не работает бот')
async def cmd_start(message: Message):
    await message.answer('Если он не работает, то как ты сюда попал?)')