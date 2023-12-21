from aiogram import F
from aiogram.types import CallbackQuery, Message, TelegramObject
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from .loader import dp
from .keyboards import cancelIkb, backToStartIkb
from .misc import start, calculateMessage
from .states import NumberInput

@dp.callback_query(F.data == 'menu')
@dp.message(CommandStart())
async def startCommand(tgobj: TelegramObject):
    if type(tgobj) == Message:
        await start(tgobj)

    elif type(tgobj) == CallbackQuery:
        await start(tgobj.message)

@dp.callback_query(F.data.startswith('operation:'))
async def operation(callback: CallbackQuery, state: FSMContext):
    operator = callback.data.split(':')[1]

    await state.set_state(NumberInput.number1)
    await state.update_data(operator = operator)

    await callback.message.answer('<b>1)</b> Введите первое число:', reply_markup=cancelIkb)

@dp.message(NumberInput.number1)
async def number1Handler(message: Message, state: FSMContext):
    try:
        number = float(message.text)

        await state.update_data(number1 = number)
        await state.set_state(NumberInput.number2)

        await message.answer('<b>2)</b> Введите второе число:', reply_markup=cancelIkb)

    except ValueError:
        await message.answer('Введите число❗️')

@dp.message(NumberInput.number2)
async def number2Handler(message: Message, state: FSMContext):
    try:
        number2 = float(message.text)

        data = await state.get_data()
    
    except ValueError:
        await message.answer('Введите число❗️')
    
    try:
        result = eval(f'{data["number1"]} {data["operator"]} {number2}')
        
        await calculateMessage(message)
        await message.answer(f'<b>Результат:</b> {result}', reply_markup=backToStartIkb)

    except ZeroDivisionError:
        await message.answer('На ноль делить нельзя, ты в школе учился⁉️', reply_markup=backToStartIkb)
    
    except Exception:
        await message.answer('Ошибка❗️', reply_markup=backToStartIkb)
    
    finally:
        await state.clear()


@dp.callback_query(F.data == 'cancelInput')
async def cancelInput(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()

