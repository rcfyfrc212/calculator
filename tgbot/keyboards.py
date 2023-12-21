from aiogram.utils.keyboard import InlineKeyboardBuilder

operationIkb = InlineKeyboardBuilder()
operationIkb.button(text='Сложение ➕', callback_data='operation:+')
operationIkb.button(text='Вычитание ➖', callback_data='operation:-')
operationIkb.button(text='Умножение ✖️', callback_data='operation:*')
operationIkb.button(text='Деление ➗', callback_data='operation:/')
operationIkb.button(text='Разработка от Профи ⚡️', url='https://zelenka.guru/threads/5872770/')
operationIkb.adjust(2,2,1)
operationIkb = operationIkb.as_markup()

cancelIkb = InlineKeyboardBuilder()
cancelIkb.button(text='Отмена ❌', callback_data='cancelInput')
cancelIkb = cancelIkb.as_markup()

backToStartIkb = InlineKeyboardBuilder()
backToStartIkb.button(text='Назад 👈🏻', callback_data='menu')
backToStartIkb = backToStartIkb.as_markup()