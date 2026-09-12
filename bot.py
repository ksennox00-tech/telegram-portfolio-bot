from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Вставь сюда токен, полученный от @BotFather
BOT_TOKEN = "8991565111:AAFlpzCeQmNyV8j2xyf63h4KlasstZggplA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)


# Команда /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ℹ️ О боте", callback_data="about")],
            [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        ]
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я демо-бот для портфолио. Умею отвечать на команды и кнопки.\n"
        "Попробуй /help или нажми на кнопку ниже.",
        reply_markup=keyboard,
    )


# Команда /help
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — начать\n"
        "/help — список команд\n"
        "/echo <текст> — бот повторит твой текст\n\n"
        "Можешь просто написать любое сообщение — я его повторю."
    )


# Команда /echo
@router.message(Command("echo"))
async def cmd_echo(message: Message):
    text = message.text.replace("/echo", "", 1).strip()
    if text:
        await message.answer(f"Ты написал: {text}")
    else:
        await message.answer("Напиши текст после команды, например: /echo привет")


# Нажатие на кнопку "О боте"
@router.callback_query(F.data == "about")
async def callback_about(callback):
    await callback.message.answer(
        "Это демонстрационный бот, созданный для портфолио разработчика.\n"
        "Написан на Python с использованием библиотеки aiogram."
    )
    await callback.answer()


# Нажатие на кнопку "Контакты"
@router.callback_query(F.data == "contacts")
async def callback_contacts(callback):
    await callback.message.answer("Связаться со мной: @ksenn0x")
    await callback.answer()


# Эхо на любое остальное текстовое сообщение
@router.message(F.text)
async def echo_message(message: Message):
    await message.answer(f"Ты написал: {message.text}")