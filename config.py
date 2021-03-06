
import telebot
from database import db
import datetime
import threading
import os
import re
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_env = os.getenv("ADMIN")
ADMIN = [int(i) for i in admin_env.split(' ')]
URL = os.getenv("URL")
print(TOKEN, ADMIN, URL)
bot = telebot.TeleBot(TOKEN, threaded=True)
DEBUG = (os.getenv("DEBUG") == 'True')

############################################################ MARKUPS

markup =  telebot.types.InlineKeyboardMarkup()
engagement_button = telebot.types.InlineKeyboardButton(text="Engagement", callback_data="engagement")
warn_button = telebot.types.InlineKeyboardButton(text="Warnungen`", callback_data="warn")
markup.add(engagement_button, warn_button)

register_markup = telebot.types.InlineKeyboardMarkup()
register_button = telebot.types.InlineKeyboardButton(text="Jetzt registrieren✅", callback_data="register_member")
register_markup.add(register_button)


input_markup = telebot.types.InlineKeyboardMarkup()
input_button = telebot.types.InlineKeyboardButton("Username", callback_data="input_user")
input_markup.add(input_button)

force_reply = telebot.types.ForceReply()
##
dashboard_markup = telebot.types.InlineKeyboardMarkup()
dashboard_button = telebot.types.InlineKeyboardButton(text="Dashboard", callback_data="dashboard")
dashboard_markup.add(dashboard_button)

dashboard_markup_en = telebot.types.InlineKeyboardMarkup()
dashboard_button_en = telebot.types.InlineKeyboardButton(text="Dashboard", callback_data="dashboard")
dashboard_markup_en.add(dashboard_button_en)
dashboard_markup = {
    "en": dashboard_markup_en,
    "de": dashboard_markup
}
##

###
dashview_markup_de = telebot.types.InlineKeyboardMarkup()
u_btn = telebot.types.InlineKeyboardButton("Nutzername bearbeiten", callback_data="input_user")
e_btn = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn = telebot.types.InlineKeyboardButton("Warnungen", callback_data="warns")
dashview_markup_de.add(u_btn)
dashview_markup_de.add(e_btn, w_btn)

dashview_markup_en = telebot.types.InlineKeyboardMarkup()
u_btn_en = telebot.types.InlineKeyboardButton("Modify Username", callback_data="input_user")
e_btn_en = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn_en = telebot.types.InlineKeyboardButton("Warns", callback_data="warns")
dashview_markup_en.add(u_btn_en)
dashview_markup_en.add(e_btn_en, w_btn_en)
dashview_markup = {
    "en": dashview_markup_en,
    "de": dashview_markup_de
}


#############################################################     FUNCT     #######################
