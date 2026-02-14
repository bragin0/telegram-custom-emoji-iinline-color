🎨 Telegram Custom Emoji & Inline Button Styles Demo
🎨 Демо Telegram Custom Emoji и цветных Inline-кнопок
<p align="center"> <b>Working example of <code>&lt;tg-emoji&gt;</code> in messages and inline buttons</b><br> aiogram 3 • Colored Styles • JSON Storage </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue.svg"> <img src="https://img.shields.io/badge/aiogram-3.x-blue"> <img src="https://img.shields.io/badge/Telegram-Bot%20API-26A5E4"> <img src="https://img.shields.io/badge/License-MIT-green"> </p>
🇬🇧 English
🚀 Overview

This repository demonstrates how to properly work with:

✨ Premium animated emoji in messages

🔘 Custom emoji in inline buttons

🎨 Colored inline button styles (primary, success, danger)

💾 JSON-based storage

Built using aiogram 3.

🔥 Features
Feature	Supported
<tg-emoji> in messages	✅
Custom emoji in inline buttons	✅ (1 per button)
Colored inline buttons	✅
HTML formatting preserved	✅
JSON storage	✅
🔘 Inline Button Styles

Telegram supports colored inline button styles:

Style	Color
primary	🔵 Blue
success	🟢 Green
danger	🔴 Red
default	⚪ Default

Example:

InlineKeyboardButton(
    text="Accept",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)

⚠ Telegram Limitations

Unlimited <tg-emoji> in messages

Only ONE icon_custom_emoji_id per inline button

Button emoji is static (not animated)

Custom emoji requires Telegram Premium

📦 Installation
git clone https://github.com/YOUR_USERNAME/telegram-custom-emoji-inline-color.git
cd telegram-custom-emoji-inline-color
pip install -r requirements.txt


Create .env file:

API_TOKEN=your_bot_token_here


Run:

python main.py

🇷🇺 Русский
🚀 Описание

Этот репозиторий демонстрирует, как правильно работать с:

✨ Premium-анимированными эмодзи в сообщениях

🔘 Custom emoji во встроенных кнопках

🎨 Цветными стилями inline-кнопок (primary, success, danger)

💾 JSON-хранилищем

Проект написан на aiogram 3.

🔥 Возможности
Возможность	Поддержка
<tg-emoji> в тексте	✅
Custom emoji в inline-кнопках	✅ (1 на кнопку)
Цветные кнопки	✅
Сохранение HTML	✅
JSON-хранилище	✅
🔘 Цветные стили кнопок

Telegram поддерживает стили:

Стиль	Цвет
primary	🔵 Синий
success	🟢 Зелёный
danger	🔴 Красный
default	⚪ Стандартный

Пример:

InlineKeyboardButton(
    text="Принять",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)

⚠ Ограничения Telegram

В тексте можно использовать неограниченное количество <tg-emoji>

В inline-кнопке можно использовать только один icon_custom_emoji_id

Эмодзи в кнопке статичный

Для custom emoji требуется Telegram Premium

🧰 Стек технологий

Python 3.10+

aiogram 3.x

Telegram Bot API

JSON

📄 Лицензия

MIT
