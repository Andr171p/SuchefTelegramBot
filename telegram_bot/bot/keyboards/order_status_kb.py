from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_bot.bot.keyboards.buttons import OrderStatusButtons, PayLinkButton


async def order_status_keyboard():
    keyboard_list = [
        [KeyboardButton(text=OrderStatusButtons.get_status_button)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Узнать статус заказа"
    )
    return keyboard


async def pay_link_keyboard(pay_link):
    keyboard_list = [
        [InlineKeyboardButton(
            text=PayLinkButton.pay_link_button,
            url=pay_link
        )]
    ]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=keyboard_list
    )

    return keyboard
