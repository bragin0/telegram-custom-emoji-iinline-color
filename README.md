<h1 align="center">Telegram TG-Emoji & Inline Button Demo</h1>
<h2 align="center">Демо Telegram TG-Emoji и Inline-кнопок</h2>

<hr>

<h2>🇬🇧 English Version</h2>

<h3>Overview</h3>

<p>This repository demonstrates how to properly handle Telegram <code>&lt;tg-emoji&gt;</code> in:</p>

<ul>
  <li>Message text (premium animated emoji)</li>
  <li>Inline buttons (custom emoji icons)</li>
  <li>Colored inline button styles</li>
  <li>JSON-based storage</li>
</ul>

<p>Built with <b>aiogram 3</b>.</p>

<hr>

<h2>🚀 Features</h2>

<h3>✅ Premium Emoji in Messages</h3>

<p>Telegram provides ready-to-use HTML via:</p>

<pre><code>message.html_text</code></pre>

<p>This preserves:</p>

<ul>
  <li><code>&lt;tg-emoji&gt;</code> entities</li>
  <li>Bold / italic formatting</li>
  <li>All valid HTML supported by Telegram</li>
</ul>

<hr>

<h3>✅ Custom Emoji in Inline Buttons</h3>

<p>Inline buttons support <b>only ONE</b> custom emoji via:</p>

<pre><code>icon_custom_emoji_id="..."</code></pre>

<p><b>⚠ Telegram limitation:</b></p>

<p>Only one custom emoji can be used per inline button.</p>

<p>If multiple <code>&lt;tg-emoji&gt;</code> are sent, only the first one can be extracted for the button icon.</p>

<hr>

<h3>✅ Colored Inline Button Styles</h3>

<p>Telegram Bot API supports button styling:</p>

<table>
<tr><th>Style</th><th>Color</th></tr>
<tr><td>primary</td><td>Blue</td></tr>
<tr><td>success</td><td>Green</td></tr>
<tr><td>danger</td><td>Red</td></tr>
<tr><td>default</td><td>Default Telegram style</td></tr>
</table>

<p>Example:</p>

<pre><code>InlineKeyboardButton(
    text="Accept",
    style="success",
    icon_custom_emoji_id="5774022692642492953",
    callback_data="accept"
)</code></pre>

<hr>

<h3>✅ JSON Storage</h3>

<p>Saved text (with HTML preserved) is stored in:</p>

<pre><code>{
  "saved_text": "&lt;tg-emoji emoji-id='...'&gt;🔥&lt;/tg-emoji&gt; Demo"
}</code></pre>

<hr>

<h2>🛠 How It Works</h2>

<h3>1️⃣ Save formatted HTML text</h3>

<pre><code>def convert_to_html(message: Message) -> str:
    return getattr(message, "html_text", message.text or "")</code></pre>

<h3>2️⃣ Extract emoji for inline button</h3>

<pre><code>match = re.search(r'emoji-id="(\d+)"', html_text)
emoji_id = match.group(1) if match else None</code></pre>

<h3>3️⃣ Create inline button</h3>

<pre><code>InlineKeyboardButton(
    text=text,
    icon_custom_emoji_id=emoji_id,
    callback_data="..."
)</code></pre>

<hr>

<h2>📦 Installation</h2>

<pre><code>git clone https://github.com/YOUR_USERNAME/telegram-tg-emoji-inline-demo.git
cd telegram-tg-emoji-inline-demo
pip install -r requirements.txt</code></pre>

<p>Create <code>.env</code> file:</p>

<pre><code>API_TOKEN=your_bot_token_here</code></pre>

<p>Run:</p>

<pre><code>python main.py</code></pre>

<hr>

<h2>⚠ Important Telegram Limitations</h2>

<ul>
  <li>Unlimited <code>&lt;tg-emoji&gt;</code> allowed in messages</li>
  <li>Only ONE <code>icon_custom_emoji_id</code> allowed in inline buttons</li>
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


<h2>🇷🇺 Русская версия</h2>

<h3>Описание</h3>

<p>Этот репозиторий демонстрирует, как правильно работать с Telegram <code>&lt;tg-emoji&gt;</code>:</p>

<ul>
  <li>В тексте сообщений (premium-анимация)</li>
  <li>В inline-кнопках (custom emoji)</li>
  <li>С цветными стилями кнопок</li>
  <li>С использованием JSON-хранилища</li>
</ul>

<p>Проект написан на <b>aiogram 3</b>.</p>

<hr>

<h3>🚀 Возможности</h3>

<h4>✅ Premium-эмодзи в тексте</h4>

<p>Telegram автоматически передаёт HTML через:</p>

<pre><code>message.html_text</code></pre>

<p>Это сохраняет:</p>

<ul>
  <li><code>&lt;tg-emoji&gt;</code></li>
  <li>Жирный / курсив</li>
  <li>Поддерживаемую HTML-разметку</li>
</ul>

<hr>

<h4>✅ Custom Emoji в inline-кнопках</h4>

<p>Inline-кнопка поддерживает <b>только ОДИН</b> custom emoji:</p>

<pre><code>icon_custom_emoji_id="..."</code></pre>

<p><b>⚠ Ограничение Telegram:</b></p>

<p>В inline-кнопке можно использовать только один custom emoji.</p>

<p>Если в тексте несколько <code>&lt;tg-emoji&gt;</code>, для кнопки можно извлечь только первый.</p>

<hr>

<h4>✅ Цветные стили кнопок</h4>

<table>
<tr><th>Стиль</th><th>Цвет</th></tr>
<tr><td>primary</td><td>Синий</td></tr>
<tr><td>success</td><td>Зелёный</td></tr>
<tr><td>danger</td><td>Красный</td></tr>
<tr><td>default</td><td>Стандартный</td></tr>
</table>

<hr>

<h2>⚠ Ограничения Telegram</h2>

<ul>
  <li>В тексте можно использовать неограниченное количество <code>&lt;tg-emoji&gt;</code></li>
  <li>В inline-кнопке — только один <code>icon_custom_emoji_id</code></li>
  <li>Эмодзи в кнопке статичный</li>
  <li>Для custom emoji требуется Telegram Premium</li>
</ul>

<hr>

<h2>📦 Установка</h2>

<pre><code>pip install -r requirements.txt
python main.py</code></pre>

<p>В <code>.env</code>:</p>

<pre><code>API_TOKEN=ваш_токен_бота</code></pre>
