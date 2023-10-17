from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# menu = [
#     [
#         InlineKeyboardButton(text="Кнопка 1", callback_data="generate_text"),
#         InlineKeyboardMarkup(text='Кнопка 2', callback_data="123"),
#         InlineKeyboardMarkup(text='Кнопка 3', callback_data='321')
#     ]
#
# ]
# menu = InlineKeyboardMarkup(inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
#
# builder = InlineKeyboardBuilder()
# for i in range(15):
#     builder.button(text=f"Кнопка {i}”, callback_data=f”button_{i}")
# builder.adjust(2)


# builder = InlineKeyboardBuilder()
#
# for index in range(1, 11):
#     builder.button(text=f"Set {index}", callback_data=f"set:{index}")
#
# builder.adjust(3, 2)

kb = [
    [
        KeyboardButton(text="Кнопка 1"),
        KeyboardButton(text="Кнопка 2"),
        KeyboardButton(text="Кнопка 3")
    ],
]

keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
)
