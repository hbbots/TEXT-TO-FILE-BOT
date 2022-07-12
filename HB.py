import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
import tgcrypto
import io
from pyrogram.types import Message


HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)   


START_TEXT = """**
HI {}, 
I AM A SIMPLE 
TEXT TO FILE BOT 
JUST SENT YOUR CODE OR TEXT MESSAGE 
THEN I WILL CONVERT IT INTO FILE

MADE BY @TELSABOTS**"""

list_text = """**LIST OF  LANGAUGES

PYTHON➲  /python
JAVA ➲  /java
HTML ➲ /html
CSS ➲ /css
PHP ➲ /php
SASS ➲ /sass
PERL ➲ /perl
SHELL ➲ /shell
MATLAB ➲ /matlab
KIVY ➲ /kivy
KOTLIN ➲ /kotlin
JAVA SCRIPT ➲  /js
SQL ➲  /sql
LESS ➲  /less
SWIFT ➲  /swift
SAS ➲ /sas
XML ➲ /xml
RUBY ➲ /ruby
YAML ➲ /yaml
DOCKER FILE ➲ /docker
C PROGRAMMING ➲ /C
MARK DOWN ➲ /markdown 

MADE BY @TELSABOTS**"""

HELP_TEXT = """**
SENT ANY TEXT MESSAGE.......

THEN REPLY WITH ANY /COMMAND

eg :- /python

PRESS /LIST COMMAND TO KNOW ABOUT
CUREENTLY SUPPORTED EXTENSIONS

MADE BY @TELSABOTS**
"""

ABOUT_TEXT = """
 🤖<b>BOT :TEXT TO FILE </b>
 
 🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT
 
 📢<b>CHANNEL :</b>@TELSABOTS
 
 📝<b>Language :</b>  <a href='https://python.org/'>Python3</a>
 
 🧰<b>Frame Work :</b>  <a href='https://pyrogram.org/'>Pyrogram</a>
 
 🤩<b>SOURCE :</b>  <a href='https://github.com/hbbots/TEXT-TO-FILE-BOT'>CLICK HERE</a>
 
 
"""

SOURCE_TEXT = """<b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑‍💻DEV🧑‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://github.com/hbbots/TEXT-TO-FILE-BOT')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
list_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='list')
        ]]
    )
result_text = """**JOIN @TELSABOTS**"""

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    
@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
@HB.on_message(filters.command(["list"]))
async def LIST(bot, update):
    text = list_text
    reply_markup = list_buttons
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@HB.on_message(filters.command(["Source", "s"]))
async def Source_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

CAPTION = os.environ.get("CAPTION", None)
            
WATERMARK = os.environ.get("WATERMARK", None)
    
result_text = """**JOIN @TELSABOTS"""

if bool(WATERMARK):
                caption = WATERMARK
else:
    caption=result_text

if bool(CAPTION):
                caption = CAPTION
else:
    caption=result_text
                    #EXTENSIONS
@HB.on_message(filters.text & filters.command(["docker"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "DOCKER.dockerfile"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["php"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "Site.php"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
    
@HB.on_message(filters.text & filters.command(["plain"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "MSG.txt"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup,caption=caption)


@HB.on_message(filters.text & filters.command(["YAML"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "HB.yml"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["swift"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "HB.swift"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["python"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "MAIN.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["sql"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "MY.sql"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["C"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "Main.c"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)



@HB.on_message(filters.text & filters.command(["ruby"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "RUBY.rb"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["markdown"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "README.md"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
    
@HB.on_message(filters.text & filters.command(["html"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "index.html"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["java"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "app.java"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["js"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "script.js"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["css"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "style.css"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["sass"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "STYLE.scss"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["perl"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "file.perl"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
            
@HB.on_message(filters.text & filters.command(["xml"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "PROJECT.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
    
@HB.on_message(filters.text & filters.command(["sas"]))
async def echo_document(client: Client, msg: Message):
    reply_markup =result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "SAS .sas"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
    
@HB.on_message(filters.text & filters.command(["shell"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "SHELL.cgi"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["matlab"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "MATLAB.matlab"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["kotlin"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "KOTLIN.kt"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)

@HB.on_message(filters.text & filters.command(["kivy"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "thelab.kv"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)


@HB.on_message(filters.text & filters.command(["php"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "site.php"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)


@HB.on_message(filters.text & filters.command(["less"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text + "\n" +WATERMARK, "utf-8"))
    file_obj.name = "HB.less"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=caption)
            
print("HB")

HB.run()
