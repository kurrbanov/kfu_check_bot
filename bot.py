import telebot
from config import BOT_TOKEN
from telebot import types

from bs4 import BeautifulSoup
import requests

bot = telebot.AsyncTeleBot(BOT_TOKEN, parse_mode="HTML")

link = ''
user_id = ''


@bot.message_handler(commands=['start'])
def hello(message):
    global user_id
    user_id = message.from_user.id
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('ВШ ИТИС', 'ИВМиИТ', 'МатМех', 'Хим.инст.')
    markup.row('Инст.физики', 'ИМО', 'ЮрФак', 'Инст.псих.и обр.')
    markup.row('ИУЭФ', 'Инженер.инст.', 'Инст.геолог.и нефт.')
    markup.row('ИСФНиМК', 'Инст.фил.и МК', 'Инст.фунд.мед.и биол.')
    bot.send_message(message.from_user.id, "Выбери институт 👇", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def btn_res(message):

    markup_inline = types.InlineKeyboardMarkup()
    if message.text == 'ИВМиИТ':
        fuck1 = types.InlineKeyboardButton(text='Бизнес-Информатика', callback_data ='BI')
        fuck2 = types.InlineKeyboardButton(text='Инфобез', callback_data='IB')
        fuck3 = types.InlineKeyboardButton(text='ИСиТ', callback_data='ISiT')
        fuck4 = types.InlineKeyboardButton(text='ПИ', callback_data='PI')
        fuck5 = types.InlineKeyboardButton(text='ПМИ', callback_data='PMI')
        fuck6 = types.InlineKeyboardButton(text='ПМ', callback_data='PMIT')
        fuck7 = types.InlineKeyboardButton(text='ФИИТ', callback_data='FIIT')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6, fuck7)
    elif message.text == 'МатМех':
        fuck1 = types.InlineKeyboardButton(text='МКН', callback_data='MKN')
        fuck2 = types.InlineKeyboardButton(text='ПМ', callback_data='PM')
        fuck3 = types.InlineKeyboardButton(text='МММ', callback_data='MMM')
        fuck4 = types.InlineKeyboardButton(text='Математ.', callback_data='Math')
        fuck5 = types.InlineKeyboardButton(text='Педагог.обр.', callback_data='PedEMath')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5)
    elif message.text == 'ИМО':
        fuck1 = types.InlineKeyboardButton(text='Антроп. и этнология', callback_data='AE')
        fuck2 = types.InlineKeyboardButton(text='Восток. и африк.', callback_data='VA')
        fuck3 = types.InlineKeyboardButton(text='История', callback_data='Hist')
        fuck4 = types.InlineKeyboardButton(text='Международные отношения', callback_data='MO')
        fuck5 = types.InlineKeyboardButton(text='Лингвистика', callback_data='Ling')
        fuck6 = types.InlineKeyboardButton(text='История(имо)', callback_data='HistIMO')
        fuck7 = types.InlineKeyboardButton(text='Культурология', callback_data='Cult')
        fuck8 = types.InlineKeyboardButton(text='Педагог.обр.', callback_data='POIMO')
        fuck9 = types.InlineKeyboardButton(text='Регионовед', callback_data='Reigion')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6, fuck7, fuck8, fuck9)
    elif message.text == 'Инст.физики':
        fuck1 = types.InlineKeyboardButton(text='Астрономия', callback_data='Astr')
        fuck2 = types.InlineKeyboardButton(text='Инноватика', callback_data='Inno')
        fuck3 = types.InlineKeyboardButton(text='БСиТ', callback_data='BSiT')
        fuck4 = types.InlineKeyboardButton(text='Инфобез', callback_data='IBPh')
        fuck5 = types.InlineKeyboardButton(text='Инфобез АС', callback_data='IBPhAB')
        fuck6 = types.InlineKeyboardButton(text='Физика', callback_data='Phis')
        fuck7 = types.InlineKeyboardButton(text='Радиофиз.', callback_data='Radio')
        fuck8 = types.InlineKeyboardButton(text='Педагог.обр.', callback_data='PedEPhis')
        fuck9 = types.InlineKeyboardButton(text='Нанотех.и МС', callback_data='Nano')
        fuck10 = types.InlineKeyboardButton(text='Геодез. и ДЗЗ', callback_data='Geodez')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6, fuck7, fuck8, fuck9, fuck10)
    elif message.text == 'ВШ ИТИС':
        fuck1 = types.InlineKeyboardButton(text='Программная инженерия', callback_data='SE')

        markup_inline.add(fuck1)
    elif message.text == 'ЮрФак':
        fuck1 = types.InlineKeyboardButton(text='Юриспруденция', callback_data='law')

        markup_inline.add(fuck1)
    elif message.text == 'ИУЭФ':
        fuck2 = types.InlineKeyboardButton(text="Гос.и муницип. упр.", callback_data='GMU')
        fuck3 = types.InlineKeyboardButton(text="Карт. и геоинф.", callback_data='KG')
        fuck4 = types.InlineKeyboardButton(text="Менеджмент", callback_data='Men')
        fuck5 = types.InlineKeyboardButton(text="Туризм", callback_data='Tur')
        fuck7 = types.InlineKeyboardButton(text="Экономика", callback_data="Econom")
        fuck9 = types.InlineKeyboardButton(text="Географ", callback_data='Geog')

        markup_inline.add(fuck2, fuck3, fuck4, fuck5, fuck7, fuck9)
    elif message.text == 'Инженер.инст.':
        fuck1 = types.InlineKeyboardButton(text='Тех.физика', callback_data='TPhi')
        fuck2 = types.InlineKeyboardButton(text='Упр.качест.', callback_data='MQ')
        fuck3 = types.InlineKeyboardButton(text='Упр.качест.(УРПС)', callback_data='MQ1')

        markup_inline.add(fuck1, fuck2, fuck3)
    elif message.text == 'Инст.геолог.и нефт.':
        fuck1 = types.InlineKeyboardButton(text='Геология', callback_data='Geog')
        fuck2 = types.InlineKeyboardButton(text='Геолог(геохим.)', callback_data='GeogHim')
        fuck3 = types.InlineKeyboardButton(text='Геолог(геофиз.)', callback_data='GeogPhi')
        fuck4 = types.InlineKeyboardButton(text='Нефтегаз. дело', callback_data='ND')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4)
    elif message.text == 'ИСФНиМК':
        fuck1 = types.InlineKeyboardButton(text='Конфликт.', callback_data='Konf')
        fuck2 = types.InlineKeyboardButton(text='Полит.', callback_data='Polit')
        fuck3 = types.InlineKeyboardButton(text='Религиовед.', callback_data='Relig')
        fuck4 = types.InlineKeyboardButton(text='Социолог.', callback_data='Soc')
        fuck5 = types.InlineKeyboardButton(text='Телогия', callback_data='Teo')
        fuck6 = types.InlineKeyboardButton(text='Философ.', callback_data='Filos')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6)
    elif message.text == 'Инст.фил.и МК':
        fuck1 = types.InlineKeyboardButton(text='Дизайн', callback_data='Des')
        fuck2 = types.InlineKeyboardButton(text='Пед.обр.(франц.)', callback_data='PedObr')
        fuck3 = types.InlineKeyboardButton(text='Пед.обр.(ин.яз)', callback_data='PedObrFL')
        fuck4 = types.InlineKeyboardButton(text='Пед.обр.(русс.и лит.)', callback_data='PedObrRL')
        fuck5 = types.InlineKeyboardButton(text='Пед.обр.(русс.и ин.)', callback_data='PedObrRI')
        fuck6 = types.InlineKeyboardButton(text='Проф.обуч.(дизайн)', callback_data='POD')
        fuck7 = types.InlineKeyboardButton(text='Филол.(заруб.)', callback_data='filz')
        fuck8 = types.InlineKeyboardButton(text='Филол.(прикл.фил.)', callback_data='PF')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6, fuck7, fuck8)
    elif message.text == 'Инст.фунд.мед.и биол.':
        fuck1 = types.InlineKeyboardButton(text='Биолог.', callback_data='biol')
        fuck2 = types.InlineKeyboardButton(text='Лечеб.дело', callback_data='lechdel')
        fuck3 = types.InlineKeyboardButton(text='Мед.биофиз.', callback_data='medbiophi')
        fuck4 = types.InlineKeyboardButton(text='Мед.биохим.', callback_data='medbiohim')
        fuck5 = types.InlineKeyboardButton(text='Мед.кибер.', callback_data='medcyber')
        fuck6 = types.InlineKeyboardButton(text='Стомат.', callback_data='stoma')
        fuck7 = types.InlineKeyboardButton(text='Пед.обр.', callback_data='PedObrMed')

        markup_inline.add(fuck1, fuck2, fuck3, fuck4, fuck5, fuck6, fuck7)
    elif message.text == 'Хим.инст.':
        fuck1 = types.InlineKeyboardButton(text='Химия', callback_data='chim')
        fuck2 = types.InlineKeyboardButton(text='Фунд.и прикл.хим.', callback_data='fchim')
        fuck3 = types.InlineKeyboardButton(text='Педагог.образ.', callback_data='PedChim')

        markup_inline.add(fuck1, fuck2, fuck3)
    elif message.text == 'Инст.псих.и обр.':
        fuck1 = types.InlineKeyboardButton(text='Клинич.психол.', callback_data='ClinPsih')
        fuck2 = types.InlineKeyboardButton(text='Психология', callback_data='psih')
        fuck3 = types.InlineKeyboardButton(text='Логопедия', callback_data='logoped')

        markup_inline.add(fuck1, fuck2, fuck3)

    bot.send_message(message.from_user.id, 'Выбери факультет 👇', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    count = 0
    score = 1000
    if call.data == 'BI':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=203&p_inst=0&p_typeofstudy=1'
        places = int(5 * 0.8)
    elif call.data == 'biol':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=373&p_inst=0&p_typeofstudy=1'
        places = int(143 * 0.8)
    elif call.data == 'PedObrMed':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=1254&p_inst=0&p_typeofstudy=1'
        places = int(18 * 0.8)
    elif call.data == 'logoped':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=17&p_speciality=396&p_inst=0&p_typeofstudy=1'
        places = int(23 * 0.8)
    elif call.data == 'psih':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=17&p_speciality=840&p_inst=0&p_typeofstudy=1'
        places = int(6 * 0.8)
    elif call.data == 'ClinPsih':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=17&p_speciality=841&p_inst=0&p_typeofstudy=1'
        places = int(16 * 0.8)
    elif call.data == 'fchim':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=7&p_speciality=165&p_inst=0&p_typeofstudy=1'
        places = int(57 * 0.8)
    elif call.data == 'PedChim':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=7&p_speciality=362&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'stoma':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=555&p_inst=0&p_typeofstudy=1'
        places = int(8 * 0.8)
    elif call.data == 'medcyber':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=552&p_inst=0&p_typeofstudy=1'
        places = int(8 * 0.8)
    elif call.data == 'chim':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=7&p_speciality=164&p_inst=0&p_typeofstudy=1'
        places = int(54 * 0.8)
    elif call.data == 'lechdel':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=550&p_inst=0&p_typeofstudy=1'
        places = int(29 * 0.8)
    elif call.data == 'medbiohim':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=551&p_inst=0&p_typeofstudy=1'
        places = int(9 * 0.8)
    elif call.data == 'medbiophi':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=1&p_speciality=554&p_inst=0&p_typeofstudy=1'
        places = int(9 * 0.8)
    elif call.data == 'PedEPhis':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=878&p_inst=0&p_typeofstudy=1'
        places = int(19 * 0.8)
    elif call.data == 'Des':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=422&p_inst=0&p_typeofstudy=1'
        places = int(4 * 0.8)
    elif call.data == 'POD':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=454&p_inst=0&p_typeofstudy=1'
        places = int(14 * 0.8)
    elif call.data == 'PF':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=413&p_inst=0&p_typeofstudy=1'
        places = int(14 * 0.8)
    elif call.data == 'filz':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=1394&p_inst=0&p_typeofstudy=1'
        places = int(4 * 0.8)
    elif call.data == 'PedObr':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=1413&p_inst=0&p_typeofstudy=1'
        places = int(7 * 0.8)
    elif call.data == 'PedObrFL':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=451&p_inst=0&p_typeofstudy=1'
        places = int(8 * 0.8)
    elif call.data == 'PedObrRL':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=1342&p_inst=0&p_typeofstudy=1'
        places = int(10 * 0.8)
    elif call.data == 'PedObrRI':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=50&p_speciality=410&p_inst=0&p_typeofstudy=1'
        places = int(11 * 0.8)
    elif call.data == 'IB':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=369&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'ISiT':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=370&p_inst=0&p_typeofstudy=1'
        places = int(32 * 0.8)
    elif call.data == 'PI':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=1084&p_inst=0&p_typeofstudy=1'
        places = int(34 * 0.8)
    elif call.data == 'PMI':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=166&p_inst=0&p_typeofstudy=1'
        places = int(48 * 0.8)
    elif call.data == 'MKN':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=5&p_speciality=358&p_inst=0&p_typeofstudy=1'
        places = int(36 * 0.8)
    elif call.data == 'MMM':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=5&p_speciality=19&p_inst=0&p_typeofstudy=1'
        places = int(30 * 0.8)
    elif call.data == 'PM':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=5&p_speciality=1032&p_inst=0&p_typeofstudy=1'
        places = int(18 * 0.8)
    elif call.data == 'AE':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=353&p_inst=0&p_typeofstudy=1'
        places = int(18 * 0.8)
    elif call.data == 'VA':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=1117&p_inst=0&p_typeofstudy=1'
        places = int(28 * 0.8)
    elif call.data == 'Hist':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=1385&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'Astr':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=162&p_inst=0&p_typeofstudy=1'
        places = int(25 * 0.8)
    elif call.data == 'BSiT':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=771&p_inst=0&p_typeofstudy=1'
        places = int(20 * 0.8)
    elif call.data == 'Inno':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=360&p_inst=0&p_typeofstudy=1'
        places = int(19 * 0.8)
    elif call.data == 'IBPhAB':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=941&p_inst=0&p_typeofstudy=1'
        places = int(17 * 0.8)
    elif call.data == 'IBPh':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=658&p_inst=0&p_typeofstudy=1'
        places = int(23 * 0.8)
    elif call.data == 'SE':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=47&p_speciality=1416&p_inst=0&p_typeofstudy=1'
        places = int(93 * 0.8)
    elif call.data == 'law':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=8&p_speciality=25&p_inst=0&p_typeofstudy=1'
        places = int(23 * 0.8)
    elif call.data == 'MO':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=543&p_inst=0&p_typeofstudy=1'
        places = int(7 * 0.8)
    elif call.data == 'GMU':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=1401&p_inst=0&p_typeofstudy=1'
        places = int(17 * 0.8)
    elif call.data == 'KG':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=117&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'Men':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=1400&p_inst=0&p_typeofstudy=1'
        places = int(17 * 0.8)
    elif call.data == 'Tur':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=1403&p_inst=0&p_typeofstudy=1'
        places = int(10 * 0.8)
    elif call.data == 'Econom':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=1399&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'Geog':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=72&p_speciality=6&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)
    elif call.data == 'Ling':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=367&p_inst=0&p_typeofstudy=1'
        places = int(8 * 0.8)
    elif call.data == 'HistIMO':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=1386&p_inst=0&p_typeofstudy=1'
        places = int(3 * 0.8)
    elif call.data == 'Cult':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=356&p_inst=0&p_typeofstudy=1'
        places = int(14 * 0.8)
    elif call.data == 'POIMO':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=1112&p_inst=0&p_typeofstudy=1'
        places = int(13 * 0.8)
    elif call.data == 'Reigion':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=1169&p_inst=0&p_typeofstudy=1'
        places = int(5 * 0.8)
    elif call.data == 'TPhi':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=82&p_speciality=1089&p_inst=0&p_typeofstudy=1'
        places = int(27 * 0.8)
    elif call.data == 'MQ':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=82&p_speciality=762&p_inst=0&p_typeofstudy=1'
        places = int(13 * 0.8)
    elif call.data == 'MQ1':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=82&p_speciality=1033&p_inst=0&p_typeofstudy=1'
        places = int(11 * 0.8)
    elif call.data == 'PMIT':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=559&p_inst=0&p_typeofstudy=1'
        places = int(38 * 0.8)
    elif call.data == 'FIIT':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=9&p_speciality=167&p_inst=0&p_typeofstudy=1'
        places = int(20 * 0.8)
    elif call.data == 'Geog':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=3&p_speciality=1030&p_inst=0&p_typeofstudy=1'
        places = int(20 * 0.8)
    elif call.data == 'GeogHim':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=3&p_speciality=866&p_inst=0&p_typeofstudy=1'
        places = int(20 * 0.8)
    elif call.data == 'GeogPhi':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=3&p_speciality=9&p_inst=0&p_typeofstudy=1'
        places = int(21 * 0.8)
    elif call.data == 'ND':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=3&p_speciality=364&p_inst=0&p_typeofstudy=1'
        places = int(23 * 0.8)
    elif call.data == 'Math':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=5&p_speciality=63&p_inst=0&p_typeofstudy=1'
        places = int(29 * 0.8)
    elif call.data == 'PedEMath':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=5&p_speciality=1388&p_inst=0&p_typeofstudy=1'
        places = int(19 * 0.8)
    elif call.data == 'Konf':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=191&p_inst=0&p_typeofstudy=1'
        places = int(3 * 0.8)
    elif call.data == 'Polit':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=192&p_inst=0&p_typeofstudy=1'
        places = int(10 * 0.8)
    elif call.data == 'Relig':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=193&p_inst=0&p_typeofstudy=1'
        places = int(15 * 0.8)
    elif call.data == 'Soc':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=181&p_inst=0&p_typeofstudy=1'
        places = int(24 * 0.8)
    elif call.data == 'Teo':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=877&p_inst=0&p_typeofstudy=1'
        places = int(24 * 0.8)
    elif call.data == 'Filos':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=13&p_speciality=189&p_inst=0&p_typeofstudy=1'
        places = int(16 * 0.8)
    elif call.data == 'Phis':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=68&p_inst=0&p_typeofstudy=1'
        places = int(58 * 0.8)
    elif call.data == 'Radio':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=83&p_inst=0&p_typeofstudy=1'
        places = int(39 * 0.8)
    elif call.data == 'Nano':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=342&p_inst=0&p_typeofstudy=1'
        places = int(25 * 0.8)
    elif call.data == 'Geodez':
        link = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=6&p_speciality=163&p_inst=0&p_typeofstudy=1'
        places = int(22 * 0.8)

    html = gethtml(link)
    ans = get_list(html.text, count, score, places)
    count = ans[0]
    score = ans[1]

    bot.send_message(call.message.chat.id, 'Количество бюджетных мест💰: ' + '<b>' + str(places) + '</b>' + ' по первой волне' + '\n' + '\n' + 'Подано согласий✅: ' + '<b> '+ str(count) + '</b>' + '\n' + '\n' + 'Проходной по согласиям‼️: ' + '<b>' + str(score) + '</b>' + ' <b>балла(-ов)</b>', parse_mode="HTML")


def gethtml(url):
    r = requests.get(url)
    return r


def get_list(html, count, score, place):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id="t_common")
    table_rows = table.find_all('tr')

    lol = 0
    limit = place
    lnRow = 0

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]

        lol += 1
        if lol == 1:
            continue

        lnRow = max(len(row), lnRow)

        if row[lnRow - 3] == '\nда\n':
            count += 1
            if count <= limit:
                if row[lnRow - 6] == '':
                    continue
                score = min(score, int(row[lnRow - 6]))

    if count <= 0:
        score = 0

    return [count, score]


bot.polling()