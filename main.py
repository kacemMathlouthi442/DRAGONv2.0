import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keepalive import keep_alive
from aiogram.types import FSInputFile
from aiogram import Bot
from aiogram.types import ChatMember
from aiogram.enums.chat_member_status import ChatMemberStatus
from time import sleep
import os

keep_alive()

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher()



async def is_user_subscribed(bot: Bot, user_id, channel , vouches):
    try:
        member: ChatMember = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        member1: ChatMember = await bot.get_chat_member(chat_id=vouches, user_id=user_id)
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR] and member1.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]
    except:
        return True

@dp.message(lambda message: message.text and message.text.startswith('/'))
async def unknown_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ]])
    await message.answer("❌ Unknown command. Contact the support for help.",reply_markup=keyboard)
# Fallback handler for unknown text messages
@dp.message()
async def unknown_text(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ]])
    await message.answer("🤖 Sorry I didn't understand that. Please contact the support for any question.",reply_markup=keyboard)
@dp.message(Command("black"))
async def send_local_video(message: Message):
    user_id = message.from_user.id
    if user_id == 7674917466 or user_id == 7575518830:
        args = message.text.split(maxsplit=1)
        with open("blacklist.txt", 'a') as f:
            f.write(f"{args[1]}\n")
        await bot.send_message(chat_id=7674917466,text='user added to black list successfully!')

        for msg_id in range(message.message_id - 100, message.message_id):
            try:
                await bot.delete_message(chat_id=int(args[1]), message_id=msg_id)
            except:
                pass
        try:
            await bot.ban_chat_member(chat_id=-1002420776698, user_id=int(args[1]))
            await bot.send_message(f"User "+args[1]+" has been banned from the channel.")
        except Exception as e:
            await bot.send_message(chat_id=7674917466,text="Failed to ban user: "+{e})
        try:
            await bot.ban_chat_member(chat_id=-1002682344927, user_id=int(args[1]))
            await bot.send_message(chat_id=7674917466,text="User "+args[1]+" has been banned from the vouches.")
        except Exception as e:
            await bot.send_message(chat_id=7674917466,text="Failed to ban user: {e}")
@dp.message(Command("start"))
async def send_local_video(message: Message):
    iduser = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if iduser not in blacklist:
        name = message.from_user.first_name
        if message.from_user.username:
            username = "@"+message.from_user.username
        else:
            username='None'
        with open("users.txt", 'r') as f:
            users = set(line.strip() for line in f.readlines())
        if iduser not in users:
            with open("users.txt", 'a') as f:
                f.write(f"{iduser}\n")
            await bot.send_message(chat_id=7674917466,text='🆕 New user\nUsername: '+username+'\nName: '+name+'\nUser ID: '+iduser+'\nTotal users: '+str(len(users)+1))
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ],
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1"),
            ],
            [
                InlineKeyboardButton(text="⚙️ Commands", callback_data="Commands"),
                InlineKeyboardButton(text="🧠 Features", callback_data="Features")
            ],
            [
                InlineKeyboardButton(text="💳 Purchase", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🎯 Enter Bot", callback_data="enter")
            ]
        ]
        )
        video = FSInputFile("img.jpg")  # Path to your local file
        await message.answer_photo(video, caption="""*The Ultimate Spoofing Experience*
                                
    Hello *"""+name+"""*\, Welcome to *DRAGON OTP v2\.0* 🐲\.                         
    *DRAGON OTP* is the \#1 Telegram\-based OTP spoofing system built for professionals\.

    Powered by advanced *AI*\, global *voice routing*\, and *real\-time control*\, it delivers unmatched OTP grabbing performance\.

    ✅ *Lightning\-fast execution*
    ✅ *Stealth\-grade spoofing*
    ✅ *Full automation tools*
    ✅ *Global reach with 100% uptime*

    Whether you're *testing*\, *analyzing*\, or *automating* — DRAGON OTP gives you the *precision*\, *power*\, and *stealth* you need to *dominate*\.""", reply_markup=keyboard,parse_mode='MarkdownV2')

@dp.message(Command("redeem"))
async def send_local_video(message: Message): #NEED WORK
    user_id = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        args = message.text.split(maxsplit=1)
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        with open("API.txt", 'r') as f:
            APIs = set(line.strip() for line in f.readlines())
        if len(args) < 2:
            await message.answer("❌ Please add your activation key. /redeem [activation key]")
        elif args[1] == 'PTd82e519c42cc97d5066b4423c718c8a132ebaf07dab24d32':
            sleep(1)
            await message.answer("⌛ Please wait.")
            sleep(5)
            with open("API.txt", 'a') as f:
                f.write(f"{user_id}\n")
            await message.answer("✅ API Token redeemed successfuly!")
        elif user_id not in APIs:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ]])
            sleep(1)
            await message.answer("⌛ Please wait.")
            sleep(9)
            await message.answer("❌ ERROR [501]\n\n⚠️ Sorry, we facing a problem in your account, you have to buy an APi token.\n\nContact the support to buy one.",reply_markup=keyboard)
        else:
            if args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa1':
                if user_id not in subscribers:
                    sleep(1)
                    await message.answer("⌛ Please wait.")
                    sleep(5)
                    await message.answer("✅ 1-Day key redeemed successfuly!")
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa2':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ 2-Days key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhCa7':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ 1-Week key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC14':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ 2-Weeks key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC30':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ 1-Month key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-F4awb4Vf1KJp7P4LhC60':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ 2-Months key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP-C4awb4Vf1KJp7P4LhCaN':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ Custum key redeemed successfuly!")
                if user_id not in subscribers:
                    with open("subscribers.txt", 'a') as f:
                        f.write(f"{user_id}\n")
            elif args[1] == 'DRAGONOTP1-C4awb4Vf1KJp7P4LhCaN':
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("✅ Premium access key redeemed successfuly!")
                with open("blacklist.txt", 'a') as f:
                    f.write(f"{user_id}\n")
                for msg_id in range(message.message_id - 100, message.message_id):
                    try:
                        await bot.delete_message(chat_id=int(user_id), message_id=msg_id)
                    except:
                        pass
                try:
                    await bot.ban_chat_member(chat_id=-1002420776698, user_id=int(user_id))
                    await bot.send_message(chat_id=7674917466,text="User "+user_id+" has been banned from the channel.")
                except Exception as e:
                    await bot.send_message(chat_id=7674917466,text="Failed to ban user: "+e)
                try:
                    await bot.ban_chat_member(chat_id=-1002682344927, user_id=int(user_id))
                    await bot.send_message(chat_id=7674917466,text="User "+user_id+" has been banned from the vouches.")
                except Exception as e:
                     await bot.send_message(chat_id=7674917466,text="Failed to ban user: "+e)
            else:
                sleep(1)
                await message.answer("⌛ Please wait.")
                sleep(5)
                await message.answer("❌ Unavailable or expired key.")


@dp.message(Command("Phonelist"))
async def send_local_video(message: Message):
    user_id = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        channel_username = "@dragonotpchannel"
        vouches = "@DragonOtp_Vouches1"
        if await is_user_subscribed(bot, user_id, channel_username,vouches):
            with open("subscribers.txt", 'r') as f:
                subscribers = set(line.strip() for line in f.readlines())
            if user_id in subscribers:
                keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
                ]
            ]
            )
                await message.answer("""🐲 *Spoofing Numbers*

    》 Marcus \| `\+14165550137`
    》 zelle \| `\+12125550143`
    》 Email \| `\+447800667788`
    》 CIBC \| `\+16045550198`
    》 CashApp \| `\+13105550191`
    》 ApplePay \| `\+447480112233`
    》 PayPal \| `\+19055550176 `                                                         
    》 BankofAmerica \| `\+14155550175`
    》 Amazon \| `\+447910333888`
    》 Gmail \| `\+15875550112`
    》 wellsfargo \| `\+16465550168`
    》 Venmo \| `\+447900555999 `                                
    》 citizens \| `\+14385550159`
    》 CapitalOne \| `\+13035550133`
    》 Coinbase \| `\+447700900123`
    》 Afterpay \| `\+17095550101`
    》 Visa \| `\+17025550122`
    》 MasterCard \| `\+447400654321`
    》 Facebook \| `\+12045550183`
    》 WhatsApp \| `\+16175550188`
    》 Instagram \| `\+447911123456`""",parse_mode='MarkdownV2',reply_markup=keyboard)
            else:
                keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
                await message.answer("❌ You have to Subscribe first to use this command!",reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
            ],
            [
                InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
            ]
        ]
        )
            await message.answer("""⚠️ *You are not subscribed to our channels*

    To use the bot, please subscribe to the required channels and group\.

    👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)

@dp.callback_query(F.data.in_(["start"]))
async def send_local_video(callback: CallbackQuery):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        await callback.message.delete()
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
            ],
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1"),
            ],
            [
                InlineKeyboardButton(text="⚙️ Commands", callback_data="Commands"),
                InlineKeyboardButton(text="🧠 Features", callback_data="Features")
            ],
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🎯 Enter Bot", callback_data="enter")
            ]
        ]
        )
        video = FSInputFile("img.jpg")  # Path to your local file
        await callback.message.answer_photo(video, caption="""🐲 *DRAGON OTP v2\.0* \- Ultimate Spoofing Experience

    *DRAGON OTP* is the \#1 Telegram\-based OTP spoofing system built for professionals\.

    It combines cutting\-edge AI, global voice routing, and real\-time control to deliver the most advanced OTP grabbing experience on the market\.

    Whether you're testing, analyzing, or automating — DRAGON OTP gives you the tools to dominate with speed, stealth, and precision\.""", reply_markup=keyboard,parse_mode='MarkdownV2')
    else:
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You didn't subscribe yet*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["Commands"]))
async def handle_vote(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""🐲 DRAGON OTP v2.0  - 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ( INTERNATIONAL CALLS )
  ❓ 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 
    🔑 》/redeem | 𝙍𝙚𝙙𝙚𝙚𝙢 𝙖 𝙠𝙚𝙮
    📲 》/call | 𝘾𝙖𝙥𝙩𝙪𝙧𝙚 𝘼𝙣𝙮 𝙘𝙤𝙙𝙚 
    📱 》/Phonelist | Check List of Latest Spoof Numbers  
                                                 
  📞 Available Services For /call command                 
    》 Marcus | capture Marcus otp
    》 zelle | capture zelle otp
    》 Email | capture email otp
    》 CIBC | capture CIBC otp
    》 CashApp | capture cashapp otp
    》 ApplePay | capture applepay otp
    》 PayPal | capture paypal otp                                                            
    》 BankofAmerica | capture bank of america otp 
    》 Amazon | capture amazon otp
    》 Gmail | capture gmail otp
    》 wellsfargo | capture wellsfargo otp
    》 Venmo | capture venmo otp                                  
    》 citizens | capture citizens otp
    》 CapitalOne | capture capitalone otp
    》 Coinbase | capture coinbase otp
    》 Afterpay | capture afterpay otp
    》 Visa | capture visa otp
    》 MasterCard | capture mastercard otp
    》 Facebook | capture facebook otp
    》 WhatsApp | capture whatsapp otp
    》 Instagram | capture instagram otp""",reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.message(Command("call"))
async def send_local_video(message: Message):
    user_id = str(message.from_user.id)
    with open("blacklist.txt", 'r') as f:
        blacklist = set(line.strip() for line in f.readlines())
    if user_id not in blacklist:
        channel = "@dragonotpchannel"
        vouches = "@DragonOtp_Vouches1"
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        if user_id in subscribers:
            args = message.text.split(maxsplit=3)
            victim=args[1]
            number=args[2]
            if len(args) == 4 and victim[1:].isdecimal() and victim[0]=='+' and number[1:].isdecimal() and number[0]=='+' and args[3].isdecimal():

                keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
                ],
                [
                    InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
                ]
            ]
            )
                sleep(1)
                await message.answer("📞 Call INITIATED")
                sleep(8)
                await message.answer("❌ ERROR[302]\n\n Sorry your country doesen't support the spofing.\n\nYou have to Buy a premium access.\n\n❕ the call from your country it's soo expensive in the premium access you will get a full control of the bot but you have to cost more.\nSorry for your time and thanks for your attention.\nContact the support to buy a premium subscription.",reply_markup=keyboard)
            elif not(args[1].isdecimal()) or not(args[1][0]=='+') or (args[2].isdecimal() ) or (args[2][0]=='+'):
                await message.answer("You have to type a valid phone number start with +")
            elif not(args[3].isdecimal()):
                await message.answer("The digits must be between 4 and 8")
        elif await is_user_subscribed(bot, user_id, channel, vouches):
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await message.answer("❌ You have to Subscribe first to use this command!",reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
                InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
            ],
            [
                InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
            ]
        ]
        )
            await message.answer("""⚠️ *You are not subscribed to our channels*

    To use the bot, please subscribe to the required channels and group\.

    👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)

@dp.callback_query(F.data.in_(["Purchase"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="💲 USDT", callback_data="usdt"),
            InlineKeyboardButton(text="♢ ETH", callback_data="eth")
        ],
        [
            InlineKeyboardButton(text="𝑳 LTC", callback_data="ltc"),
            InlineKeyboardButton(text="◎ SOL", callback_data="sol")
        ],
        [
            InlineKeyboardButton(text="₿ BTC", callback_data="btc")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""🐲 *DRAGON OTP v2\.0* Prices list 💰
━━━━━━━━━━━━━━━━
• 1 Day Plan *\(25$\)*
• 2 Days Plan *\(30$\)*
• 1 Week Plan *\(40$\)*
• 2 Weeks Plan *\(55$\)* 
• 1 Month Plan *\(70$\)*
• 2 Months Plan *\(100$\)*
━━━━━━━━━━━━━━━━
 
📩 After payment\, send a screenshot to SUPPORT to verify your subscription\.
❓ Need help or a different wallet\? Contact SUPPORT\.""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["Features"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        video = FSInputFile("img.jpg")  # Path to your local file
        await callback.message.answer_photo(video, caption="""🐉 *UNIQUE FEATURES*

🚀 Lightning Fast OTP Delivery  
🎭 Custom Caller ID \(Spoofing Mode\)  
🔊 AI Voice Calls with Human Detection  
📞 Call Any Number Worldwide  
📦 Multiple OTP Services Supported  
📁 Live Call Recording \& Logs  
📊 Real\-Time Dashboard \& Analytics  
🔐 Encrypted Access \& Security  
📲 Use Anywhere Anytime""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer() 


@dp.callback_query(F.data.in_(["enter"]))
async def handle_vote1(callback: CallbackQuery, bot: Bot):
    user_id = str(callback.from_user.id)
    channel_username = "@dragonotpchannel"
    vouches = "@DragonOtp_Vouches1"
    if await is_user_subscribed(bot, user_id, channel_username,vouches):
        with open("subscribers.txt", 'r') as f:
            subscribers = set(line.strip() for line in f.readlines())
        if user_id in subscribers:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await callback.message.delete()
            video = FSInputFile("img.jpg")  # Path to your local file
            await callback.message.answer_photo(video, caption="""🐲 *Dragon OTP v2\.0 Bot*
📡 *Status*\: Fully Operational \| ⏱️ *Uptime: 100%*

🚀 *Limited Access*\: Only few spots remaining\!

⚠️ Active License Detected\!""",parse_mode='MarkdownV2',reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💳 Purchase Subscription", callback_data="Purchase")
            ],
            [
                InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
            ]
        ]
        )
            await callback.message.delete()
            video = FSInputFile("img.jpg")  # Path to your local file
            await callback.message.answer_photo(video, caption="""🐲 *Dragon OTP v2\.0 Bot*
📡 *Status*\: Fully Operational \| ⏱️ *Uptime: 100%*

🚀 *Limited Access*\: Only few spots remaining\!

⚠️ No Active License Detected\!

🔐 To activate the bot, you must first purchase a license\.
💸 We recommend getting a [LICENSE BUNDLE](https\://t\.me/dragonotpowner) for exclusive features and the best discounted price\!""",parse_mode='MarkdownV2',reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Community", url="https://t.me/dragonotpchannel"),
            InlineKeyboardButton(text="✅ Vouches", url="https://t.me/DragonOtp_Vouches1")
        ],
        [
            InlineKeyboardButton(text="📍 I've Subscribed", callback_data="start")
        ]
    ]
    )
        await callback.message.delete()
        await callback.message.answer("""⚠️ *You are not subscribed to our channels*

To use the bot, please subscribe to the required channels and group\.

👇 Click the buttons below to reach our channels\:""",parse_mode='MarkdownV2', reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(F.data.in_(["btc"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Bitcoin \(BTC\)*
                                  
• `bc1q98y83fh28y6ysklu9qmla7enuegldmgdcdawvk`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["usdt"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*USDT \(TRC20\)*
                                  
• `TRRVAuPEGJ4EgE33u1pV6gNUXxM1R5v1aY`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["sol"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Solana \(SOL\)*
                                  
• `8Ra9HKVrKNakEeQfqDzrVn1sFoQoFmbR51UHMRweT9hY`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["eth"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Ethereum \(ETH\)*
                                  
• `0xc76acc06684b2e2a2d43b9ba3b5f2618cd7a6307`""",parse_mode='MarkdownV2', reply_markup=keyboard)


@dp.callback_query(F.data.in_(["ltc"]))
async def handle_vote1(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="📞 Support", url="https://t.me/dragonotpowner")
        ],
        [
            InlineKeyboardButton(text="🔙 BACK TO MENU", callback_data="start")
        ]
    ]
    )
    await callback.message.delete()
    await callback.message.answer("""*Litecoin \(LTC\)*
                                  
• `LRJ8n55djedy4jyKP3Kkqi6iEy3BYC1FLt`""",parse_mode='MarkdownV2', reply_markup=keyboard)



# Run bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
