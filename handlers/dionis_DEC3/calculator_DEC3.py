'''
import math
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

class CalculatorState:
    def __init__(self, operation=None, numbers=None):
        self.operation = operation
        self.numbers = numbers or []

calculator_state = CalculatorState()

@router.message(Command("start"))
async def start(message: types.Message):
    calculator_state.numbers = []
    calculator_state.operation = None
    await message.reply("Welcome to the Calculator Bot!\n"
                        "You can perform basic calculations. "
                        "Use commands like /add, /subtract, /multiply, /divide, /sin, /cos, /asin, /acos.")

@router.message(commands=['add', 'subtract', 'multiply', 'divide', 'sin', 'cos', 'asin', 'acos'])
async def handle_operations(message: types.Message):
    calculator_state.operation = message.text[1:]
    calculator_state.numbers = []
    await message.reply(f"Enter numbers for {calculator_state.operation} operation, separated by space.")

@router.message(lambda message: calculator_state.operation is not None)
async def process_numbers(message: types.Message):
    try:
        numbers = [float(x) for x in message.text.split()]
        result = perform_operation(calculator_state.operation, *numbers)
        await message.reply(f"Result of {calculator_state.operation} operation: {result}")
        calculator_state.operation = None
    except ValueError:
        await message.reply("Invalid input. Please enter valid numbers.")

def perform_operation(operation, *args):
    if operation == 'add':
        return sum(args)
    elif operation == 'subtract':
        return args[0] - sum(args[1:])
    elif operation == 'multiply':
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == 'divide':
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    elif operation == 'sin':
        return math.sin(math.radians(args[0]))
    elif operation == 'cos':
        return math.cos(math.radians(args[0]))
    elif operation == 'asin':
        return math.degrees(math.asin(args[0]))
    elif operation == 'acos':
        return math.degrees(math.acos(args[0]))

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(router, skip_updates=True)
'''