import telebot
import emoji
from telebot import types
bot = telebot.TeleBot('1522095402:AAEW-0hltyEka9AfC-MBVscRM0wXjWPd3Jo')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3 = types.InlineKeyboardMarkup(row_width=1)
item5 = types.InlineKeyboardButton(emoji.emojize(":large_orange_diamond: что-то анимешное :large_orange_diamond:"), callback_data='test3')
item6 = types.InlineKeyboardButton(emoji.emojize(":large_orange_diamond: Живые смайлики каво :large_orange_diamond:"), callback_data='test4')
item8 = types.InlineKeyboardButton(emoji.emojize(":large_orange_diamond: Микс-стикерпак :large_orange_diamond:"), callback_data='test6')
keyboard4 = types.InlineKeyboardMarkup(row_width=1)
category1 = types.InlineKeyboardButton(emoji.emojize(":bear: Животные :bear:"), callback_data='cat1')
category2 = types.InlineKeyboardButton(emoji.emojize(":alien: Супергерои :alien:"), callback_data='cat2')
category3 = types.InlineKeyboardButton(emoji.emojize(":eyes: Мемы :eyes:"), callback_data='cat3')
keyboard4.add(category1,category2,category3)
keyboard3.add(item5,item6,item8)
keyboard2 = types.InlineKeyboardMarkup(row_width=1)
item3 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Elon Musk :large_blue_diamond:"), callback_data='test1')
item4 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Мастер Йода! :large_blue_diamond:") , callback_data='test2')
item7 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Мастер Йода! :large_blue_diamond:"), callback_data='test5')
keyboard2.add(item3,item4,item7)
item1 = types.KeyboardButton(emoji.emojize(":large_blue_diamond: Обычные стикеры"))
item2 = types.KeyboardButton(emoji.emojize(":large_orange_diamond: Анимированные стикеры"))
keyboard1.add(item1,item2)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, emoji.emojize('Привет. Я могу посоветовать тебе огромное количество стикеров на любой вкус и цвет!  :green_heart: '))
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEB5VxgMAQa0dKAx47DmQWEyUevRUvsKAACCwADO2AkFMPPOZh4z_kHHgQ', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == emoji.emojize(':large_blue_diamond: Обычные стикеры'):
        bot.send_message(message.chat.id, 'Сейчас выдам доступные варианты!', reply_markup=keyboard2)
    if message.text == emoji.emojize(':large_orange_diamond: Анимированные стикеры'):
        bot.send_message(message.chat.id, 'Сейчас выдам доступные категории!', reply_markup=keyboard4)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'test1':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/StarmanMusk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5WpgMBbDuvZYd8j0qRgSSOVrA7I2EgACjwgAAnlc4gnodoxFNb6Zvx4E')
        if call.data == 'test2':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/yoda_ny_vk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5WxgMBc3xqnXoCaWAcrYMcwxfV3A1wACijIAAulVBRipuIgSwhikOR4E')
        if call.data == 'test3':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/Mafumafu_cat_by_cocopry')
            bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAEB5W5gMBg3jATgOCpeNapgyNbQz6GIxwACmAADS2nuEPGZmZgskmj3HgQ')
        if call.data == 'test4':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/f_weyjrjak_896383854_by_fStikBot')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5XBgMBhJbQhOGWw6x5IO-oLtI90UyQACGwADbrttNSiap30tt3brHgQ')
        if call.data == 'test6':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/aniketanimated')
            bot.send_sticker(call.message.chat.id, 'CAACAgUAAxkBAAEB5fRgMO5ZYF2lcHcIhdMRHhZfe9Gx6gAC3wADpvbGETp5AU4j032MHgQ')
        if call.data == 'cat1':
            bot.send_message(call.message.chat.id, 'Сейчас выдам доступные смайлики на тему "Животные"', reply_markup=keyboard3)

bot.polling()
    