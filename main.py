import asyncio
import json
import os
import re
from pathlib import Path
from typing import Tuple, Optional

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise ValueError("API_TOKEN not found")

bot = Bot(API_TOKEN)
dp = Dispatcher()

DB_FILE = "data.json"

def init_db():
    if not Path(DB_FILE).exists():
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump({"saved_text": ""}, f, indent=2)

def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

init_db()

def convert_to_html(message: Message) -> str:
    """
    Telegram already provides proper HTML via message.html_text.
    This preserves <tg-emoji> and formatting.
    """
    return getattr(message, "html_text", message.text or "")


def extract_button_data(html_text: str) -> Tuple[str, Optional[str]]:
    """
    Extract the FIRST custom emoji (Telegram supports only one in a button).
    Remove HTML tags for button text.
    """
    if not html_text:
        return "", None

    match = re.search(r'emoji-id="(\d+)"', html_text)
    emoji_id = match.group(1) if match else None

    clean_text = re.sub(r'<tg-emoji[^>]*>.*?</tg-emoji>', '', html_text)
    clean_text = re.sub(r'<[^>]+>', '', clean_text)

    return clean_text.strip(), emoji_id


def smart_button(html_text: str, callback: str):
    """
    Create inline button.
    Important: Telegram supports ONLY ONE custom emoji in inline buttons.
    """
    text, emoji_id = extract_button_data(html_text)

    return InlineKeyboardButton(
        text=text or " ",
        callback_data=callback,
        icon_custom_emoji_id=emoji_id
    )

async def safe_edit(callback: CallbackQuery, text: str, markup=None):
    try:
        await callback.message.edit_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup
        )
    except TelegramBadRequest as e:
        if "message is not modified" not in str(e):
            raise
    await callback.answer()

def main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 Save Text", callback_data="save"))
    builder.row(InlineKeyboardButton(text="📤 Show Saved Text", callback_data="show"))
    builder.row(InlineKeyboardButton(text="🔘 Inline Button Demo", callback_data="button_demo"))
    builder.row(InlineKeyboardButton(text="Info", callback_data=" ", style='primary', icon_custom_emoji_id='6028435952299413210'))
    builder.row(InlineKeyboardButton(text="Accept", callback_data=" ", style='success', icon_custom_emoji_id='5774022692642492953'))
    builder.row(InlineKeyboardButton(text="Reject", callback_data=" ", style='danger', icon_custom_emoji_id='5774077015388852135'))
    builder.row(InlineKeyboardButton(text="Settings", callback_data=" ", style='default', icon_custom_emoji_id='5771449289972650710'))
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Emoji Demo Bot\n\n"
        "This bot demonstrates:\n"
        "• How HTML with <tg-emoji> is saved\n"
        "• How premium emoji render in text\n"
        "• How custom emoji work in inline buttons\n\n"
        "⚠ Important: only ONE custom emoji can be used in an inline button.",
        reply_markup=main_keyboard()
    )


@dp.callback_query(F.data == "save")
async def ask_for_text(callback: CallbackQuery):
    await callback.message.answer(
        "Send any formatted text.\n"
        "You can include premium emoji."
    )
    await callback.answer()


@dp.message()
async def save_text(message: Message):
    html_text = convert_to_html(message)

    data = load_db()
    data["saved_text"] = html_text
    save_db(data)

    await message.answer(
        "Text saved with HTML preserved.",
        parse_mode=ParseMode.HTML
    )


@dp.callback_query(F.data == "show")
async def show_text(callback: CallbackQuery):
    data = load_db()
    saved = data.get("saved_text", "")

    if not saved:
        await callback.answer("No text saved.")
        return

    await safe_edit(
        callback,
        saved,
        main_keyboard()
    )


@dp.callback_query(F.data == "button_demo")
async def button_demo(callback: CallbackQuery):
    data = load_db()
    saved = data.get("saved_text", "")

    if not saved:
        await callback.answer("Save text first.")
        return

    builder = InlineKeyboardBuilder()
    builder.row(smart_button(saved, "noop"))
    builder.row(InlineKeyboardButton(text="⬅ Back", callback_data="back"))

    await safe_edit(
        callback,
        "Inline Button Demo\n\n"
        "Notice:\n"
        "• Emoji in message = animated (if premium)\n"
        "• Emoji in button = static icon\n"
        "• Telegram supports only ONE custom emoji in inline buttons",
        builder.as_markup()
    )


@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await safe_edit(callback, "Main Menu", main_keyboard())


@dp.callback_query(F.data == "noop")
async def noop(callback: CallbackQuery):
    await callback.answer()

async def main():
    print("Emoji demo bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
