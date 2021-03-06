import telebot
import emoji
from requests import get
from telebot import types
bot = telebot.TeleBot('1522095402:AAEW-0hltyEka9AfC-MBVscRM0wXjWPd3Jo')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3 = types.InlineKeyboardMarkup(row_width=1)
nextboard = types.InlineKeyboardMarkup(row_width=1)
nextbut = types.InlineKeyboardButton(emoji.emojize("Следующий стикер!"), callback_data='nextbut_1')
nextboard.add(nextbut)
nextboard1 = types.InlineKeyboardMarkup(row_width=1)
nextbut1 = types.InlineKeyboardButton(emoji.emojize("Следующий стикер!"), callback_data='nextbut_2')
nextboard1.add(nextbut1)
item5 = types.InlineKeyboardButton(emoji.emojize(":cat: Круглый Котик :cat:"), callback_data='animal_1')
item6 = types.InlineKeyboardButton(emoji.emojize(":rabbit: Кролик Супчик :rabbit:"), callback_data='animal_2')
item8 = types.InlineKeyboardButton(emoji.emojize(":dog: Ветерок :dog:"), callback_data='animal_3')
keyboard5 = types.InlineKeyboardMarkup(row_width=1)
keyboard4 = types.InlineKeyboardMarkup(row_width=1)
sup1 = types.InlineKeyboardButton(emoji.emojize(":bear: Животные :bear:"), callback_data='sup_1')
sup2 = types.InlineKeyboardButton(emoji.emojize(":alien: Супергерои :alien:"), callback_data='sup_2')
sup3 = types.InlineKeyboardButton(emoji.emojize(":eyes: Мемы :eyes:"), callback_data='sup_3')
keyboard5.add(sup1,sup2,sup3)
category1 = types.InlineKeyboardButton(emoji.emojize(":bear: Животные :bear:"), callback_data='cat_1')
category2 = types.InlineKeyboardButton(emoji.emojize(":alien: Супергерои :alien:"), callback_data='cat2')
category3 = types.InlineKeyboardButton(emoji.emojize(":clown_face: Мемы :clown_face:"), callback_data='cat3')
keyboard4.add(category1,category2,category3)
keyboard3.add(item5,item6,item8)
keyboard2 = types.InlineKeyboardMarkup(row_width=1)
item3 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Илон Маск :large_blue_diamond:"), callback_data='test1')
item4 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Мастер Йода! :large_blue_diamond:") , callback_data='test2')
item7 = types.InlineKeyboardButton(emoji.emojize(":large_blue_diamond: Чертёнок Лютик :large_blue_diamond:"), callback_data='test5')
keyboard2.add(item3,item4,item7)
item1 = types.KeyboardButton(emoji.emojize(":large_blue_diamond: Обычные стикеры"))
item2 = types.KeyboardButton(emoji.emojize(":large_orange_diamond: Анимированные стикеры"))
keyboard1.add(item1,item2)
memeboard = types.InlineKeyboardMarkup(row_width=1)
memebut1 = types.InlineKeyboardButton(emoji.emojize(":skull: Троллфейс :skull:"), callback_data='meme_1')
memebut2 = types.InlineKeyboardButton(emoji.emojize(":frog: Пепе :frog:"), callback_data='meme_2')
memebut3 = types.InlineKeyboardButton(emoji.emojize(":frog: Пепе-Клоун :frog:"), callback_data='meme_3')
memeboard.add(memebut1,memebut2,memebut3)
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
            bot.send_photo(call.message.chat.id, 'https://imbt.ga/1BWggio5Rv', caption='Илон Маск!')
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/StarmanMusk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5WpgMBbDuvZYd8j0qRgSSOVrA7I2EgACjwgAAnlc4gnodoxFNb6Zvx4E', reply_markup=nextboard1)
        if call.data == 'nextbut_1':
            bot.send_photo(call.message.chat.id, 'https://imbt.ga/cBEk1VbIso', caption='Чертёнок Лютик!')
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/lutik_vk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB9XlgQ1z8fyS3PpxK5L9D4oA_IGwpagACty0AAulVBRhfcRJ-DsDdMx4E')
        if call.data == 'nextbut_2':
            bot.send_photo(call.message.chat.id, 'https://imbt.ga/REv4VuwQ40', caption='Мастер Йода!')
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/yoda_ny_vk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5WxgMBc3xqnXoCaWAcrYMcwxfV3A1wACijIAAulVBRipuIgSwhikOR4E', reply_markup=nextboard)
        if call.data == 'test2':
            bot.send_photo(call.message.chat.id, 'https://imbt.ga/REv4VuwQ40', caption='Мастер Йода!')
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/yoda_ny_vk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5WxgMBc3xqnXoCaWAcrYMcwxfV3A1wACijIAAulVBRipuIgSwhikOR4E', reply_markup=nextboard)
        if call.data == 'test5':
            bot.send_photo(call.message.chat.id, 'https://imbt.ga/cBEk1VbIso', caption='Чертёнок Лютик!')
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/lutik_vk')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB9XlgQ1z8fyS3PpxK5L9D4oA_IGwpagACty0AAulVBRhfcRJ-DsDdMx4E')
        if call.data == 'animal_1':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/Animated_Round_Pretty_Cat')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB7b1gOiKttKvHv9JM4GwJ0R-OmxDzVAACfBIAAujW4hJj7B-YkKSgqx4E')
        if call.data == 'animal_2':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/suppy_anim')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB7b9gOiNZ9idcyFexA1W7CFfP5rvXYAACByMAAulVBRj8wpsP_DYPnR4E')
        if call.data == 'animal_3':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/veter_anim')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB7clgOiU3kRYs78g1Mj97KqaLjlF_9wACASUAAulVBRiLUp-pp22ZQR4E')
        if call.data == 'test4':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/f_weyjrjak_896383854_by_fStikBot')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5XBgMBhJbQhOGWw6x5IO-oLtI90UyQACGwADbrttNSiap30tt3brHgQ')
        if call.data == 'test6':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/aniketanimated')
            bot.send_sticker(call.message.chat.id, 'CAACAgUAAxkBAAEB5fRgMO5ZYF2lcHcIhdMRHhZfe9Gx6gAC3wADpvbGETp5AU4j032MHgQ')
        if call.data == 'cat_1':
            bot.send_message(call.message.chat.id, 'Сейчас выдам доступные смайлики на тему "Животные"', reply_markup=keyboard3)
        if call.data == 'cat2':
            bot.send_message(call.message.chat.id, 'К сожалению, тут ничего нет! \nВозвращаю обратно к категориям', reply_markup=keyboard4)
        if call.data == 'cat3':
            bot.send_message(call.message.chat.id, 'Сейчас выдам доступные смайлики на тему "Мемы"', reply_markup=memeboard)
        if call.data == 'meme_1':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/Troll_animated_by_cocopry')
            bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAEB7jpgOnXqAAFCqYFL0u0aps6zKjEq6JQAAtoAA0tp7hBdnkswEYL7oR4E')
        if call.data == 'meme_2':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/Peepo_Pepe')
            bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAEB7jxgOngUrLy53xS5JLgiipWYKl8EWAACQwEAAqghIQZgSyUtPd-rIB4E')
        if call.data == 'meme_3':
            bot.send_message(call.message.chat.id, 'https://t.me/addstickers/honka_animated')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB7j5gOnmWJBhG5MoYnEhGNcK8JbtviQACpgADq1fEC6lAX0hqfPJfHgQ')
bot.polling()
    
