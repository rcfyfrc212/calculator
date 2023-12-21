from aiogram.fsm.state import State, StatesGroup

class NumberInput(StatesGroup):
    operator = State()
    number1 = State()
    number2 = State()
