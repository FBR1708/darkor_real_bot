from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

services_type_uz = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton(text='Ish Topish'), KeyboardButton(text='Ishchi Topish')],
                                           [KeyboardButton(text='E\'lon joylash'), KeyboardButton(text='⬅Ortga')]])

services_type_uz1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[[KeyboardButton(text='Ochiq ishchilar bazasini ko\'rish')],
                                                  [KeyboardButton(text='HR xizmatidan foydalanish')],
                                                  [KeyboardButton(text='🔚Ortga')]])

phone_num = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Tugma orqali', request_contact=True),
                                     ]], row_width=1
                                )

yes_no_but = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton(text='Bor'), KeyboardButton(text='Yo\'q')
                                      ]], row_width=1
                                 )

confirmation_admin = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text='Tasdiqlash', callback_data='confirm')],
    [InlineKeyboardButton(text='Bekor qilish', callback_data='cancel')],
])

approval_but = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1,
                                   keyboard=[[KeyboardButton(text='Tasdiqlash')],
                                             [KeyboardButton(text='O\'zgartirish')], [KeyboardButton(text='🔚Ortga')]])

advertisement_but = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[[KeyboardButton(text='Ish beruvchi')],
                                                  [KeyboardButton(text='Ishchi')], [KeyboardButton(text='🔚Ortga')]])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Saytga o'tish",
                                           url='https://www.darkor22.uz/uz/all-c'
                                               'andidates?keyword=&address=&p'
                                               'osition=&typeOfWork=&experience=&page=1')]])

inline_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Havola",
                                           url='https://www.darkor22.uz/uz/all-vacancies?keyword=&address=&position=&typeOfWork=&experience=&page=1')]])

user_info_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[[KeyboardButton(text='PhD'), KeyboardButton(text='Magistr')],
                                                 [KeyboardButton(text='Bakalavr'), KeyboardButton(text='Talaba')],
                                                 [KeyboardButton(text='O\'rta maxsus')]])

language_level_button = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Rus tili'), KeyboardButton(text='Ingliz tili')],
    [KeyboardButton(text='Koreys tili'), KeyboardButton(text='Xitoy tili')],
    [KeyboardButton(text='Nemis tili'), KeyboardButton(text='Fransuz tili')], [KeyboardButton(text='Keyingi')]])

rus_know_level_but = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Bilmayman'), KeyboardButton(text='Qoniqarli')],
    [KeyboardButton(text='Yaxshi'), KeyboardButton(text='A\'lo')]])

english_know_level_but = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='A1'), KeyboardButton(text='A2')],
    [KeyboardButton(text='B1'), KeyboardButton(text='B2')],
    [KeyboardButton(text='C1'), KeyboardButton(text='C2')]])

korea_know_level_but = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Topik1'), KeyboardButton(text='Topik2')],
    [KeyboardButton(text='Topik3'), KeyboardButton(text='Topik4')],
    [KeyboardButton(text='Topik5'), KeyboardButton(text='Topik6')]])

japan_know_level_but = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='JLPT N5'), KeyboardButton(text='JLPT N4')],
    [KeyboardButton(text='JLPT N3'), KeyboardButton(text='JLPT N2')],
    [KeyboardButton(text='JLPT N1')]])

china_know_level_but = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='HSK 1'), KeyboardButton(text='HSK 2')],
    [KeyboardButton(text='HSK 3'), KeyboardButton(text='HSK 4')],
    [KeyboardButton(text='HSK 5'), KeyboardButton(text='HSK 6')]])
