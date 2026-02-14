# telegram-custom-emoji-iinline-color
Complete working example of handling Telegram &lt;tg-emoji> in messages and inline buttons, including colored inline button styles (primary, success, danger) using aiogram 3 and JSON storage.

Telegram TG-Emoji & Inline Button Demo
Демо Telegram TG-Emoji и Inline-кнопок
🇬🇧 English Version
Overview

This repository demonstrates how to properly handle Telegram <tg-emoji> in:

Message text (premium animated emoji)

Inline buttons (custom emoji icons)

Colored inline button styles

JSON-based storage

Built with aiogram 3.

🚀 Features
✅ Premium Emoji in Messages

Telegram provides ready-to-use HTML via:

message.html_text


This preserves:

<tg-emoji> entities

Bold / italic formatting

All valid HTML supported by Telegram

✅ Custom Emoji in Inline Buttons

Inline buttons support only ONE custom emoji via:

icon_custom_emoji_id="..."


⚠ Telegram limitation:

Only one custom emoji can be used per inline button.

If multiple <tg-emoji> are sent, only the first one can be extracted for the button icon.

✅ Colored Inline Button Styles

Telegram Bot API supports button styling:

Style	Color
primary	Blue
success	Green
danger	Red
default	Default Telegram style

Example:

InlineKeyboardButton(
    text="Accept",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)

✅ JSON Storage

Saved text (with HTML preserved) is stored in:

{
  "saved_text": "<tg-emoji emoji-id='...'>🔥</tg-emoji> Demo"
}

🛠 How It Works
1️⃣ Save formatted HTML text
def convert_to_html(message: Message) -> str:
    return getattr(message, "html_text", message.text or "")

2️⃣ Extract emoji for inline button
match = re.search(r'emoji-id="(\d+)"', html_text)
emoji_id = match.group(1) if match else None

3️⃣ Create inline button
InlineKeyboardButton(
    text=text,
    icon_custom_emoji_id=emoji_id,
    callback_data="..."
)

📦 Installation
git clone https://github.com/YOUR_USERNAME/telegram-tg-emoji-inline-demo.git
cd telegram-tg-emoji-inline-demo
pip install -r requirements.txt


Create .env file:

API_TOKEN=your_bot_token_here


Run:

python main.py

⚠ Important Telegram Limitations

Unlimited <tg-emoji> allowed in messages

Only ONE icon_custom_emoji_id allowed in inline buttons

Button emoji is static (not animated)

Bot owner must have Telegram Premium to use custom emoji

🧰 Tech Stack

Python 3.10+

aiogram 3.x

Telegram Bot API

JSON storage

📄 License

MIT

🇷🇺 Русская версия
Описание

Этот репозиторий демонстрирует, как правильно работать с Telegram <tg-emoji>:

В тексте сообщений (premium-анимация)

В inline-кнопках (custom emoji)

С цветными стилями кнопок

С использованием JSON-хранилища

Проект написан на aiogram 3.

🚀 Возможности
✅ Premium-эмодзи в тексте

Telegram автоматически передаёт HTML через:

message.html_text


Это сохраняет:

<tg-emoji>

Жирный / курсив

Поддерживаемую HTML-разметку

✅ Custom Emoji в inline-кнопках

Inline-кнопка поддерживает только ОДИН custom emoji:

icon_custom_emoji_id="..."


⚠ Ограничение Telegram:

В inline-кнопке можно использовать только один custom emoji.

Если в тексте несколько <tg-emoji>, для кнопки можно извлечь только первый.

✅ Цветные стили кнопок

Telegram Bot API поддерживает стили:

Стиль	Цвет
primary	Синий
success	Зелёный
danger	Красный
default	Стандартный

Пример:

InlineKeyboardButton(
    text="Принять",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)

✅ JSON-хранилище

Сохранённый текст хранится так:

{
  "saved_text": "<tg-emoji emoji-id='...'>🔥</tg-emoji> Demo"
}

⚠ Ограничения Telegram

В тексте можно использовать неограниченное количество <tg-emoji>

В inline-кнопке — только один icon_custom_emoji_id

Эмодзи в кнопке статичный

Для custom emoji требуется Telegram Premium у владельца бота

📦 Установка
pip install -r requirements.txt
python main.py


В .env:

API_TOKEN=ваш_токен_бота

🧰 Стек технологий

Python 3.10+

aiogram 3.x

Telegram Bot API

JSON
