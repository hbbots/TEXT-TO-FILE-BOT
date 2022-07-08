import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


HB = Client(
    "Echo-bot", 
    api_id = 2152187,
    api_hash = "1a0208e94456f4799a5f5269f1198d62",
    bot_token = "5313152157:AAEd9AqIAavwJme5bRwXfFSO4f0id7naO5o"
    
)     
Username = "THOR_online"



START_TEXT = """HI {}, 
I CAN PROVIDE MOVIES 
MADE BY @TELSABOTS
"""
HELP_TEXT = """
JIUST SENT ANY MOVIE NAME 
❌DONT SENT YEAR 
❌ DONT SENT LANGAUGES 
✅ONLY SENT MOVIE NAME 
eg:- KGF2 

MADE BY @TELSABOTS
"""
ABOUT_TEXT = """
 🤖<b>BOT:DISCUSS UNPIN🤖</b>
 
📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

 
🤩<b>SOURCE :</b> 🤩 <a href='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'>CLICK HERE❤️</a>

"""
feedback_text ="""**😍DUDE YOU CAN REQUEST \n MOVIE THROUGH HERE \n\n😉JUST SENT MOVIE NAME\n\neg:-/feedback kgf2**"""
SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
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
        InlineKeyboardButton('🤩SOURCE🤩', url='https://youtu.be/sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
FEEDBACK_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡FEEDBACK🏡', callback_data='feedback'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
close_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )




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
    elif update.data == "feedback":
        await update.message.edit_text(
            text=feedback_text,
            disable_web_page_preview=True,
            reply_markup =close_buttons
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
GROUP = "filimsmovie"
WELCONE_MSG = "<b>HELLO {},\n\n WELCOME TO HB GROUP\n JOIN OUR CHANNELS</b>"

WELCOME_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton('📢CHANNEL📢', url="https://t.me/+UZzc1ZqHvYXaLeNf"),
        InlineKeyboardButton('📢NEW MOVIES📢', url="https://t.me/+b31QfnWFdmcwYzVl")
        ],[
            InlineKeyboardButton('🧑‍💻DEV🧑‍💻', url="https://t.me/alluaddict"),
            InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]
]

@HB.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, update):
    text=WELCONE_MSG.format(update.from_user.mention)
    reply_markup = InlineKeyboardMarkup(WELCOME_MESSAGE_BUTTONS)
    update.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@HB.on_message(filters.command(["feedback"]))
async def my_handler(client, message):
    await message.forward(Username)

 
#evde buttons add cheyyanam
morbius_button = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩JOIN🤩', url='https://t.me/+b31QfnWFdmcwYzVl'),
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/c/1511271527/83')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

puzhu_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/574'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
aviyal_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩JOIN🤩', url='https://t.me/+b31QfnWFdmcwYzVl'),
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/c/1511271527/53')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
acharya_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩JOIN🤩', url='https://t.me/+b31QfnWFdmcwYzVl'),
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/c/1511271527/42')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
Antakshari_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/530')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
    ]]
    
)
thman_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩JOIN🤩', url='https://t.me/+b31QfnWFdmcwYzVl'),
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/c/1511271527/34')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

rrr_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩JOIN🤩', url='https://t.me/+b31QfnWFdmcwYzVl'),
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/c/1511271527/57')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
KGF2_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/626')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
beast_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/555')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
pandey_button = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/767')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
oruthee_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/589')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
heropanti_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/722')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
eightythree_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/746')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
jalsa_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/780')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
batman_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/515')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
maaran_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/823')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
varthamanam_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/756')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
FREEDOM_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/812')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
    
RADHE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/786')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

proposal_button = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/756')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
ATTACK_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/795')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
ATTACK_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/795')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
RUNAWAY_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/795')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    ) 
RUNAWAY_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩MOVIE🤩', url='https://t.me/malik_minalmurali_money_heist/829')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    ) 

    #movies
selfie="""
🎬 Title: Selfie
🎭 Genres: Crime,  Thriller, 
📆 Year: 2022
🔊 Languages : #Tamil
💿QUALITY : HDRIP"""
RADHE="""
🍿 TITILE : Radhe shyam
📆  YEAR  : 2022
💽  QUALITY : HDRIP
🎭  GENRE : Romantic
📍  LANGUAGE : #Malayalam"""
RUNAWAY="""
🎬 Title :  Runway 34\n🗓 Year : 2022\n🔊 Language : #Hindi\n💿 Quality : HDRip"""
ATTACK="""🍿 TITILE : Attack Part 1\n📆  YEAR  : 2022\n💽  QUALITY : HDRIP\n🎭  GENRE : Romantic\n📍  LANGUAGE : #Hindi"""
freedom="""🍿 TITILE : Freedom Fight\n📆  YEAR  : 2022\n💽  QUALITY : HDRIP\n🎭  GENRE : Drama\n📍  LANGUAGE : Malayalam\n❤️JOIN @FILIMSMOVIE"""
jalsa ="""🎬 ᴛɪᴛʟᴇ » JALSA\n🎭 ɢᴇɴʀᴇs » Drama,  Thriller, \n📆 ʏᴇᴀʀ » 2022\n🔊 ʟᴀɴɢᴜᴀɢᴇs » #Hindi\n📀 QUALITY » HDRIP"""
maaran="""🎬Title: Maaran\n📆 Year :2022\n🎭Genre: #Action #Thriller\n🔊 Languages : #Tamil\n📀QUALITY : HDRIP"""
proposal="""🍿 TITILE : THE PROPOSAL \n📆  YEAR  : 2022 \n💽  QUALITY : HDRIP \n🎭  GENRE :  #Comedy #Romanc\n📍  LANGUAGE : #Malayalam\n⚜️ UPLOADED :@FILIMSMOVIE"""
pandey ="""🎬ᴛɪᴛʟᴇ » Bachchhan Paandey \n🎭 ɢᴇɴʀᴇs » Action,  Comedy,  Crime, \n📆 ʏᴇᴀʀ » 2022\n🔊 ʟᴀɴɢᴜᴀɢᴇs » Hindi\n💿QUALITY :HDRIP"""
morbius = """🎬 Title :  MORBIUS\n🗓\nYear : 2022\n🔊\nLanguage : ENGLISH\n💿 Quality : HDRIP\n📥\nUploaded :\nhttps://t.me/+b31QfnWFdmcwYzVl"""
varthamanam="""🎬 Title : VARTHAMANAM \n🗓 Year : 2022\n🔊 Language : #Malayalam\n💿 Quality :  HDRIP\nJOIN @FILIMSMOVIE"""
eightythree83="""🍿 TITILE : 83 \n📆  YEAR  : 2022\n💽  QUALITY : HDRIP\n🎭  GENRE : Drama \n📍  LANGUAGE : Multi"""
heropanti="""🎥Title: Heropanti 2\n📅YEAR :  2022\n🔆Genre: #Action #Romance\n🔊Language: HINDI\n📀QUALITY : HDRIP"""
batman="""🍿 TITILE : The Batman\n📆  YEAR  : 2022\n💽  QUALITY : HDRIP\n🎭  GENRE : Action Superhero\n📍  LANGUAGE : Multi"""
thman="""🎬 Title : 12th Man\n🗓 Year : 2022\n🔊 Language : Malayalam\n💿 Quality :  HDRip\nJOIN @FILIMSMOVIE"""
Antakshari="""🍿 TITILE : Antakshari\n📆 YEAR  : 2022\n💽 QUALITY : HDRIP\n🎭 GENRE : THRILLER DRAMA\n📍 LANGUAGE : MALAYALM"""
oruthee="""🎬 Title : Oruthee\n🗓 Year : 2022\n🔊 Language : #Malayalam\n💿 Quality :  PreDVDRip"""
aviyal = """🎬 Title :  Aviyal \n🗓 Year : 2022\n🔊 Language : Malayalam\n💿 Quality :  HDRip\n📥 Uploaded\n\nhttps://t.me/+b31QfnWFdmcwYzVl"""
puzhu ="""🎬 Title :  Puzhu\n🗓 Year : 2022\n🔊 Language : Malayalam\n💿 Quality : HDRip\n📥 Uploaded;- https://t.me/+UZzc1ZqHvYXaLeNf"""
acharya="""🎬 Title : Acharya\n🗓 Year : 2022\n🔊 Language : Tamil ,Malayalam\n💿 Quality : HDRip\n📥 Uploaded : https://t.me/+b31QfnWFdmcwYzVl"""
rrr="""🍿 TITILE : RRR\n📆  YEAR  : 2022\n💽  QUALITY : HDRIP\n🎭 GENRE : Action Thriller\n📍 LANGUAGE : Tamil, Malayalam, Telugu"""
kgf2="""🎬 Title :  KGF 2\n🗓 Year : 2022\n🔊 Language : Tamil, Malayalam, Hindi \n💿 Quality : HDRip"""
beast="""🍿 TITILE : Beast\n 📆 YEAR  : 2022\n💽 QUALITY : HDRIP\n 🎭GENRE : Action Thriller\n📍LANGUAGE : Tamil,Hindi,Telugu,Malayalam,Kannada"""
@HB.on_message(filters.text & filters.private & ~filters.group)
async def files(HB, message): 
    if message.text.lower() == 'aviyal':
        await message.reply_photo( photo="https://telegra.ph/file/218570d8e6f51114f33a3.jpg", caption=aviyal, reply_markup=aviyal_BUTTONS)
    elif message.text.lower() == 'acharya':
        await message.reply_photo( photo="https://telegra.ph/file/420e4b12f246cad78dcc4.jpg", caption=acharya, reply_markup=acharya_BUTTONS)
    elif message.text.lower() == 'puzhu':
        await message.reply_photo( photo="https://telegra.ph/file/f1af41712163fdb845c08.jpg", caption=puzhu, reply_markup=puzhu_BUTTONS)
    elif message.text.lower() == 'rrr':
        await message.reply_photo( photo="https://telegra.ph/file/da59a9e4f3ebf601da54f.jpg", caption=rrr, reply_markup=rrr_BUTTONS)
    elif message.text.lower() == 'kgf2':
        await message.reply_photo( photo="https://i.ytimg.com/vi/0NZKW9M7xb8/maxresdefault.jpg", caption=kgf2, reply_markup=KGF2_BUTTONS)
    elif message.text.lower() == 'kgf 2':
        await message.reply_photo( photo="https://i.ytimg.com/vi/0NZKW9M7xb8/maxresdefault.jpg", caption=kgf2, reply_markup=KGF2_BUTTONS)
    elif message.text.lower() == 'kgf':
        await message.reply_photo( photo="https://i.ytimg.com/vi/0NZKW9M7xb8/maxresdefault.jpg", caption=kgf2, reply_markup=KGF2_BUTTONS)
    elif message.text.lower() == 'beast':
        await message.reply_photo( photo="https://telegra.ph/file/283ab00d357f7e16235ec.jpg", caption=beast, reply_markup=beast_BUTTONS)
    elif message.text.lower() == 'antakshari':
        await message.reply_photo( photo="https://telegra.ph/file/5d134a5cd45e6429c9448.jpg", caption=Antakshari, reply_markup=Antakshari_buttons)
    elif message.text.lower() == 'anthakshari':
        await message.reply_photo( photo="https://telegra.ph/file/5d134a5cd45e6429c9448.jpg", caption=Antakshari, reply_markup=Antakshari_buttons)
    elif message.text.lower() == 'anthakshary':
        await message.reply_photo( photo="https://telegra.ph/file/5d134a5cd45e6429c9448.jpg", caption=Antakshari, reply_markup=Antakshari_buttons)
    elif message.text.lower() == 'oruthe':
        await message.reply_photo( photo="https://telegra.ph/file/97a878d0fa0f4557b7b08.jpg", caption=oruthee, reply_markup=oruthee_BUTTONS)
    elif message.text.lower() == 'oruthee':
        await message.reply_photo( photo="https://telegra.ph/file/97a878d0fa0f4557b7b08.jpg", caption=oruthee, reply_markup=oruthee_BUTTONS)
    elif message.text.lower() == 'oruthi':
        await message.reply_photo( photo="https://telegra.ph/file/97a878d0fa0f4557b7b08.jpg", caption=oruthee, reply_markup=oruthee_BUTTONS)
    elif message.text.lower() == 'oruthy':
        await message.reply_photo( photo="https://telegra.ph/file/97a878d0fa0f4557b7b08.jpg", caption=oruthee, reply_markup=oruthee_BUTTONS)
    elif message.text.lower() == '12th':
        await message.reply_photo( photo="https://telegra.ph/file/14665959f0e9d515710b5.jpg", caption=thman, reply_markup=thman_BUTTONS)
    elif message.text.lower() == '12':
        await message.reply_photo( photo="https://telegra.ph/file/14665959f0e9d515710b5.jpg", caption=thman, reply_markup=thman_BUTTONS)
    elif message.text.lower() == 'man':
        await message.reply_photo( photo="https://telegra.ph/file/14665959f0e9d515710b5.jpg", caption=thman, reply_markup=thman_BUTTONS)
    elif message.text.lower() == '12th man':
        await message.reply_photo( photo="https://telegra.ph/file/14665959f0e9d515710b5.jpg", caption=thman, reply_markup=thman_BUTTONS)
    elif message.text.lower() == '12thman':
        await message.reply_photo( photo="https://telegra.ph/file/14665959f0e9d515710b5.jpg", caption=thman, reply_markup=thman_BUTTONS)
    elif message.text.lower() == 'batman':
        await message.reply_photo( photo="https://telegra.ph/file/edb75e89cba665367ac2f.jpg", caption=batman, reply_markup=batman_BUTTONS)
    elif message.text.lower() == 'bat':
        await message.reply_photo( photo="https://telegra.ph/file/edb75e89cba665367ac2f.jpg", caption=batman, reply_markup=batman_BUTTONS)
    elif message.text.lower() == 'hero panti':
        await message.reply_photo( photo="https://telegra.ph/file/e88410665757b63dadca4.jpg", caption=heropanti, reply_markup=heropanti_BUTTONS)
    elif message.text.lower() == 'hero':
        await message.reply_photo( photo="https://telegra.ph/file/e88410665757b63dadca4.jpg", caption=heropanti, reply_markup=heropanti_BUTTONS)
    elif message.text.lower() == 'panti':
        await message.reply_photo( photo="https://telegra.ph/file/e88410665757b63dadca4.jpg", caption=heropanti, reply_markup=heropanti_BUTTONS)
    elif message.text.lower() == '83':
        await message.reply_photo( photo="https://telegra.ph/file/0f8f483f6b57280430126.jpg", caption=eightythree83, reply_markup=eightythree_buttons)
    elif message.text.lower() == 'varthamanam':
        await message.reply_photo( photo="https://telegra.ph/file/a8d9509e3d76a3110b648.jpg", caption=varthamanam, reply_markup=varthamanam_BUTTONS)
    elif message.text.lower() == 'varthamannam':
        await message.reply_photo( photo="https://telegra.ph/file/a8d9509e3d76a3110b648.jpg", caption=varthamanam, reply_markup=varthamanam_BUTTONS)
    elif message.text.lower() == 'varthamanim':
        await message.reply_photo( photo="https://telegra.ph/file/a8d9509e3d76a3110b648.jpg", caption=varthamanam, reply_markup=varthamanam_BUTTONS)
    elif message.text.lower() == 'morbius':
        await message.reply_photo(photo="https://telegra.ph/file/7131cd8a2f95bfa1decb0.jpg", caption=morbius, reply_markup=morbius_button)
    elif message.text.lower() == 'moribus':
        await message.reply_photo(photo="https://telegra.ph/file/7131cd8a2f95bfa1decb0.jpg", caption=morbius, reply_markup=morbius_button)
    elif message.text.lower() == 'Paandey':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'Pandey':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'Pantey':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'Bachan':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'Bachchan':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'Bachchhan':
        await message.reply_photo(photo="https://telegra.ph/file/059a117af16af8e719ced.jpg", caption=pandey, reply_markup=pandey_button)
    elif message.text.lower() == 'proposal':
        await message.reply_photo(photo="https://telegra.ph/file/c8c1e9f72bc2959e94cc6.jpg", caption=proposal, reply_markup=proposal_button)
    elif message.text.lower() == 'propsal':
        await message.reply_photo(photo="https://telegra.ph/file/c8c1e9f72bc2959e94cc6.jpg", caption=proposal, reply_markup=proposal_button)
    elif message.text.lower() == 'maran':
        await message.reply_photo(photo="https://telegra.ph/file/4353751922561ade3a526.jpg", caption=maaran, reply_markup=proposal_button)
    elif message.text.lower() == 'maaran':
        await message.reply_photo(photo="https://telegra.ph/file/4353751922561ade3a526.jpg", caption=maaran, reply_markup=proposal_button)
    elif message.text.lower() == 'maaraan':
        await message.reply_photo(photo="https://telegra.ph/file/4353751922561ade3a526.jpg", caption=maaran, reply_markup=proposal_button)
    elif message.text.lower() == 'jalsa':
        await message.reply_photo(photo="https://telegra.ph/file/0bfeffd593d5d7593ab58.jpg", caption=jalsa, reply_markup=jalsa_buttons)
    elif message.text.lower() == 'jala':
        await message.reply_photo(photo="https://telegra.ph/file/0bfeffd593d5d7593ab58.jpg", caption=jalsa, reply_markup=jalsa_buttons)
    elif message.text.lower() == 'freedom':
        await message.reply_photo(photo="https://telegra.ph/file/bb98551c391c06784fea8.jpg", caption=freedom, reply_markup=FREEDOM_BUTTONS)
    elif message.text.lower() == 'fredom':
        await message.reply_photo(photo="https://telegra.ph/file/bb98551c391c06784fea8.jpg", caption=freedom, reply_markup=FREEDOM_BUTTONS)
    elif message.text.lower() == 'fight':
        await message.reply_photo(photo="https://telegra.ph/file/bb98551c391c06784fea8.jpg", caption=freedom, reply_markup=FREEDOM_BUTTONS)
    elif message.text.lower() == 'fredom fight':
        await message.reply_photo(photo="https://telegra.ph/file/bb98551c391c06784fea8.jpg", caption=freedom, reply_markup=FREEDOM_BUTTONS)
    elif message.text.lower() == 'freedom fight':
        await message.reply_photo(photo="https://telegra.ph/file/bb98551c391c06784fea8.jpg", caption=freedom, reply_markup=FREEDOM_BUTTONS)
    elif message.text.lower() == 'attack':
        await message.reply_photo(photo="https://telegra.ph/file/7fd694a8ab0594bb34eb6.jpg", caption=ATTACK, reply_markup=ATTACK_BUTTON)
    elif message.text.lower() == 'atack':
        await message.reply_photo(photo="https://telegra.ph/file/7fd694a8ab0594bb34eb6.jpg", caption=ATTACK, reply_markup=ATTACK_BUTTON)
    elif message.text.lower() == 'runaway':
        await message.reply_photo(photo="https://telegra.ph/file/1a41768ae852cfb49a41f.jpg", caption=RUNAWAY, reply_markup=RUNAWAY_BUTTON)
    elif message.text.lower() == 'runaway 34':
        await message.reply_photo(photo="https://telegra.ph/file/1a41768ae852cfb49a41f.jpg", caption=RUNAWAY, reply_markup=RUNAWAY_BUTTON)
    elif message.text.lower() == 'run away':
        await message.reply_photo(photo="https://telegra.ph/file/1a41768ae852cfb49a41f.jpg", caption=RUNAWAY, reply_markup=RUNAWAY_BUTTON)
    elif message.text.lower() == 'run away 34':
        await message.reply_photo(photo="https://telegra.ph/file/1a41768ae852cfb49a41f.jpg", caption=RUNAWAY, reply_markup=RUNAWAY_BUTTON)
    elif message.text.lower() == 'radhe shyam':
        await message.reply_photo(photo="https://telegra.ph/file/b4c0c09c851eca025fee4.jpg", caption=RADHE, reply_markup=RADHE_BUTTON)
    elif message.text.lower() == 'radhe':
        await message.reply_photo(photo="https://telegra.ph/file/b4c0c09c851eca025fee4.jpg", caption=RADHE, reply_markup=RADHE_BUTTON)
    elif message.text.lower() == 'syam':
        await message.reply_photo(photo="https://telegra.ph/file/b4c0c09c851eca025fee4.jpg", caption=RADHE, reply_markup=RADHE_BUTTON)
    elif message.text.lower() == 'radhe syaam':
        await message.reply_photo(photo="https://telegra.ph/file/b4c0c09c851eca025fee4.jpg", caption=RADHE, reply_markup=RADHE_BUTTON)
    elif message.text.lower() == 'sham':
        await message.reply_photo(photo="https://telegra.ph/file/b4c0c09c851eca025fee4.jpg", caption=RADHE, reply_markup=RADHE_BUTTON)
    
    else:
        await message.reply_text("**😕SORRY BRO\nNOTHING FOUND\n\n👇PRESS FEEDBACK BUTTON \n😇TO REQUEST MOVIES", reply_markup=FEEDBACK_BUTTONS)



print("hb")
HB.run()




