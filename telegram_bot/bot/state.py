from aiogram.filters.state import State, StatesGroup


class UserPhoneNumberForm(StatesGroup):
    phone_number = State()


class ReplaceUserPhoneNumberForm(StatesGroup):
    replace_phone_number = State()
