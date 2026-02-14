<h1 align="center">Telegram TG-Emoji & Inline Button Demo</h1>
<h2 align="center">Демо Telegram TG-Emoji и Inline-кнопок</h2>

<hr>

<h2>🇬🇧 English Version</h2>

<h3>📌 Overview</h3>

<p>This repository demonstrates how to properly handle Telegram <code>&lt;tg-emoji&gt;</code> in:</p>

<ul>
  <li>Message text (Premium animated emoji)</li>
  <li>Inline buttons (custom emoji icons)</li>
  <li>Colored inline button styles</li>
  <li>JSON-based storage</li>
</ul>

<p>Built with <b>aiogram 3.x</b>.</p>

<hr>

<h2>🚀 Features</h2>

<h3>✅ Premium Emoji in Messages</h3>

<p>Telegram automatically provides formatted HTML via:</p>

<pre><code>message.html_text</code></pre>

<p>This preserves:</p>

<ul>
  <li><code>&lt;tg-emoji&gt;</code> entities</li>
  <li>Bold / italic formatting</li>
  <li>All supported Telegram HTML tags</li>
</ul>

<p>Example stored JSON:</p>

<pre><code>{
  "saved_text": "&lt;tg-emoji emoji-id='5368324170671202286'&gt;🔥&lt;/tg-emoji&gt; Demo"
}</code></pre>

<hr>

<h3>✅ Custom Emoji in Inline Buttons</h3>

<p>Inline buttons support <b>only ONE</b> custom emoji using:</p>

<pre><code>icon_custom_emoji_id="..."</code></pre>

<p><b>⚠ Telegram limitation:</b></p>

<ul>
  <li>Only one custom emoji can be used per inline button</li>
  <li>If multiple <code>&lt;tg-emoji&gt;</code> are present, only the first one can be extracted</li>
</ul>

<p>Example:</p>

<pre><code>InlineKeyboardButton(
    text="Accept",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)</code></pre>

<hr>

<h3>🎨 Colored Inline Button Styles</h3>

<p>Telegram Bot API supports button styling:</p>

<table>
<tr><th>Style</th><th>Color</th></tr>
<tr><td>primary</td><td>Blue</td></tr>
<tr><td>success</td><td>Green</td></tr>
<tr><td>danger</td><td>Red</td></tr>
<tr><td>default</td><td>Default Telegram style</td></tr>
</table>

<hr>

<h2>🛠 How It Works</h2>

<h3>1️⃣ Save formatted HTML text</h3>

<pre><code>def convert_to_html(message: Message) -&gt; str:
    return getattr(message, "html_text", message.text or "")</code></pre>

<h3>2️⃣ Extract emoji for inline button</h3>

<pre><code>import re

match = re.search(r'emoji-id="(\d+)"', html_text)
emoji_id = match.group(1) if match else None</code></pre>

<h3>3️⃣ Create inline button</h3>

<pre><code>InlineKeyboardButton(
    text=text,
    icon_custom_emoji_id=emoji_id,
    callback_data="..."
)</code></pre>

<hr>

<h3>⚙ Environment</h3>

<pre><code>API_TOKEN=your_bot_token_here</code></pre>

<p>Run:</p>

<pre><code>python main.py</code></pre>

<hr>

<h3>⚠ Important Telegram Limitations</h3>

<ul>
  <li>Unlimited <code>&lt;tg-emoji&gt;</code> allowed in messages</li>
  <li>Only ONE <code>icon_custom_emoji_id</code> allowed per inline button</li>
  <li>Button emoji is static (not animated)</li>
  <li>Bot owner must have Telegram Premium to use custom emoji</li>
</ul>

<hr>

<h2>🧰 Tech Stack</h2>

<ul>
  <li>Python 3.10+</li>
  <li>aiogram 3.x</li>
  <li>Telegram Bot API</li>
  <li>JSON storage</li>
</ul>

<hr>
<hr>

<h2>🇷🇺 Русская версия</h2>

<h3>📌 Обзор</h3>

<p>Этот репозиторий демонстрирует правильную работу с Telegram <code>&lt;tg-emoji&gt;</code> в:</p>

<ul>
  <li>Тексте сообщений (Premium анимированные эмодзи)</li>
  <li>Inline-кнопках (кастомные emoji-иконки)</li>
  <li>Цветных стилях inline-кнопок</li>
  <li>Хранении данных в формате JSON</li>
</ul>

<p>Проект реализован на <b>aiogram 3.x</b>.</p>

<hr>

<h2>🚀 Возможности</h2>

<h3>✅ Premium Emoji в сообщениях</h3>

<p>Telegram автоматически предоставляет форматированный HTML через:</p>

<pre><code>message.html_text</code></pre>

<p>Это сохраняет:</p>

<ul>
  <li><code>&lt;tg-emoji&gt;</code> сущности</li>
  <li>Жирный / курсивный текст</li>
  <li>Все поддерживаемые Telegram HTML-теги</li>
</ul>

<hr>

<h3>✅ Кастомные emoji в inline-кнопках</h3>

<p>Inline-кнопки поддерживают <b>только ОДНУ</b> кастомную emoji через:</p>

<pre><code>icon_custom_emoji_id="..."</code></pre>

<p><b>⚠ Ограничение Telegram:</b></p>

<ul>
  <li>Можно использовать только одну кастомную emoji на кнопку</li>
  <li>Если передано несколько <code>&lt;tg-emoji&gt;</code>, будет извлечена только первая</li>
</ul>

<hr>

<h3>🎨 Цветные стили inline-кнопок</h3>

<table>
<tr><th>Стиль</th><th>Цвет</th></tr>
<tr><td>primary</td><td>Синий</td></tr>
<tr><td>success</td><td>Зелёный</td></tr>
<tr><td>danger</td><td>Красный</td></tr>
<tr><td>default</td><td>Стандартный стиль Telegram</td></tr>
</table>

<hr>

<h3>⚠ Важные ограничения Telegram</h3>

<ul>
  <li>В сообщениях можно использовать неограниченное количество <code>&lt;tg-emoji&gt;</code></li>
  <li>В inline-кнопке — только один <code>icon_custom_emoji_id</code></li>
  <li>Emoji в кнопке статичная (без анимации)</li>
  <li>Владелец бота должен иметь Telegram Premium для использования кастомных emoji</li>
</ul>

<hr>

<h3>🧰 Стек технологий</h3>

<ul>
  <li>Python 3.10+</li>
  <li>aiogram 3.x</li>
  <li>Telegram Bot API</li>
  <li>JSON-хранение</li>
</ul>
