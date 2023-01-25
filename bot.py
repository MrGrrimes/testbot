import os
import telebot
import locale
from datetime import date
from datetime import datetime
from telebot import types
import json

locale.setlocale(locale.LC_ALL, 'it_IT.utf8')

file_name = 'perks.json'
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)

BOT_TOKEN = '5953425221:AAGmTg2hxBY-uyx0RVt1W5EBVmH1DCVLgRY'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help'])
def sign_handler(message):
    text = "/code\n/archives\n/prime\n/devupdate\n/test"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

### CODES ###
# CODE NAME
@bot.message_handler(commands=['code'])
def code_formatter(message):
    # Emojis
    gift = u"\U0001F381"
    # Generate Header
    header = gift + " *NUOVO CODICE* " + gift
    # Generate Body
    body_reward = "\n\n• Codice `[codice]` per riscattare *[ricompensa]*."
    body_post = "\n• [Post con tutti i Codici attivi](https://t.me/DbD_NEWS/2375)"
    # Generate Final Message
    final_message = header + body_reward + body_post
    bot.send_message(message.chat.id, final_message, parse_mode="Markdown")

### ARCHIVES ###
# TOME NUMBER
@bot.message_handler(commands=['archives'])
def archives_formatter(message):
    # Emojis
    book = u"\U0001F4D6"
    # Generate Header
    header = book + " *NUOVE SFIDE* " + book
    # Generate Body
    body_challenges = "\n\n• Sono disponibili le nuove Sfide del *Livello [numero]*, *Volume [numero]* degli Archivi."
    body_rift = "\n• La Spaccatura si chiude il *5 Aprile 2023*."
    # Generate Final Message
    final_message = header + body_challenges + body_rift
    bot.send_message(message.chat.id, final_message, parse_mode="Markdown")

### PRIME GAMING ###
# PRIME REWARD
@bot.message_handler(commands=['prime'])
def primegaming_formatter(message):
    # Emojis
    star = u"\u2B50\uFE0F"
    # Generate Header
    header = star + " *RICOMPENSA PRIME GAMING* " + star
    # Generate Body
    body_text = "\n\n• Per gli Utenti iscritti a Prime Gaming è disponibile la nuova Ricompensa del mese: *[ricompensa]*.\n"
    body_link = "• Link: gaming.amazon.com/loot/deadbydaylight\n"
    body_footer = "• Riscattabile fino al *[dataFine]*. 1 Codice per Giocatore."
    # Generate Final Message
    final_message = header + body_text + body_link + body_footer
    bot.send_message(message.chat.id, final_message, parse_mode="Markdown")

### DEVELOPER UPDATE ###
# SUMMARY
@bot.message_handler(commands=['devupdate'])
def devupdate_formatter(message):
    # Emojis
    books = u"\U0001F4DA"
    italy = u"\U000FE4E9"
    uk = u"\U000FE4EA"
    # Get Current Month
    current_month = datetime.now().strftime("%B")
    # Generate Header
    header = books + " *DEVELOPER UPDATE | " + current_month.capitalize() + " 2023* " + books
    # Generate Body - Changes list
    changes_list = "\n\nNovità principali:\n" + "• [testo]\n• [testo]\n• [testo]"
    # Generate Body - Articles
    articles = "\n" + italy + " Articolo in Italiano: [link]\n" + uk + " Articolo in Inglese: [link]"
    # Generate Final Message
    final_message = header + changes_list + articles
    bot.send_photo(message.chat.id, 'https://i.imgur.com/yLVAH70.png', caption=final_message, parse_mode="Markdown")

### SHRINE ###
@bot.message_handler(commands=['shrine'])
def sign_handler(message):
    text = "Send Shrine text"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, shrine_handler, text)

def shrine_handler(message, sign):
    final_message = shrine_parser(message, sign)
    bot.send_photo(message.chat.id, message, caption=final_message, parse_mode="Markdown")

def shrine_parser(message, sign):
    # Emojis
    new = u"\U0001F195"
    # Links
    wiki = "https://deadbydaylight.fandom.com/it/wiki/"

    # This week's shrine is: Object of Obsession, Appraisal, Coulrophobia and Dead Man's Switch.
    sign = sign.replace("This week's shrine is: ", "")
    # Object of Obsession, Appraisal, Coulrophobia and Dead Man's Switch.
    sign = sign.replace(" and", ",")
    # Object of Obsession, Appraisal, Coulrophobia, Dead Man's Switch.
    sign = sign.replace(".", "")
    # Object of Obsession, Appraisal, Coulrophobia, Dead Man's Switch
    perks = sign.split(",")
    # ["Object of Obsession", "Appraisal", "Coulrophobia", "Dead Man's Switch"]
    perks[0] = perks[0].strip()
    perks[1] = perks[1].strip()
    perks[2] = perks[2].strip()
    perks[3] = perks[3].strip()

    for element in data['perks']:
        if element['perk_name'] == perks[0].strip():
            it_perk = element['it_name']
            perks[0] = "[" + it_perk + "](" + wiki + it_perk + ")" + " (" + element['name'] + ")"

    for element in data['perks']:
        if element['perk_name'] == perks[1].strip():
            it_perk = element['it_name']
            perks[1] = "[" + it_perk + "](" + wiki + it_perk + ")" + " (" + element['name'] + ")"

    for element in data['perks']:
        if element['perk_name'] == perks[2].strip():
            it_perk = element['it_name']
            perks[2] = "[" + it_perk + "](" + wiki + it_perk + ")" + " (" + element['name'] + ")"
 
    for element in data['perks']:
        if element['perk_name'] == perks[3].strip():
            it_perk = element['it_name']
            perks[3] = "[" + it_perk + "](" + wiki + it_perk + ")" + " (" + element['name'] + ")"

    # Header
    header = new + " *RELIQUARIO DELLA SETTIMANA* " + new
    body = "\n\n• " + perks[0] + "\n• " + perks[1] + "\n• " + perks[2] + "\n• " + perks[3]
    final_string = header + body
    return final_string 

@bot.message_handler(commands=['shrine2'])
def shrine2_handler(message):
    text = "Send Shrine image"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, shrine2_formatter, text)

@bot.message_handler(func=lambda message: True, content_types=['photo'])
def shrine2_formatter(message, sign):
    bot.send_photo(message.chat.id, sign, parse_mode="Markdown")

bot.infinity_polling()