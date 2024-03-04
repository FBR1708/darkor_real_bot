from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_type_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton(text='Find a job'), KeyboardButton(text='Find a stuff')],
                                            [KeyboardButton(text='Post an ad'), KeyboardButton(text='⬅Back')]])

services_type_eng1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                         keyboard=[[KeyboardButton(text='View the list of open workers')],
                                                   [KeyboardButton(text='Use of HR service')],
                                                   [KeyboardButton(text='🔚Back')]])

phone_num_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton(text='By button', request_contact=True),
                                         ]], row_width=1
                                    )

yes_no_but_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [KeyboardButton(text='Yes'), KeyboardButton(text='No')
                                          ]], row_width=1
                                     )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_admin_eng = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text='Tasdiqlash', callback_data='confirm_eng')],
    [InlineKeyboardButton(text='Bekor qilish', callback_data='cancel_eng')],
])

approval_but_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[[KeyboardButton(text='Confirmation')],
                                                 [KeyboardButton(text='Cancellation')], [KeyboardButton(text='🔚Back')]])

advertisement_but_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=[[KeyboardButton(text='Employer')],
                                                      [KeyboardButton(text='Employee')],
                                                      [KeyboardButton(text='🔚Back')]])

inline_keyboard_eng = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Go to the site",
                                           url='https://www.darkor22.uz/uz/all-c'
                                               'andidates?keyword=&address=&p'
                                               'osition=&typeOfWork=&experience=&page=1')]])

user_info_button_eng = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[[KeyboardButton(text='PhD'), KeyboardButton(text='Magistr')],
                                                     [KeyboardButton(text='Bachelor'), KeyboardButton(text='Student')],
                                                     [KeyboardButton(text='Medium special')]])

language_level_button_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Russia language'), KeyboardButton(text='English language')],
    [KeyboardButton(text='Korea language'), KeyboardButton(text='China language')],
    [KeyboardButton(text='German language'), KeyboardButton(text='French language')],
    [KeyboardButton(text='Uzbek language'), KeyboardButton(text='Next')]])

rus_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='I don\'t know'), KeyboardButton(text='Satisfactory')],
    [KeyboardButton(text='Good'), KeyboardButton(text='Excellent')]])

uzb_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='I don\'t know'), KeyboardButton(text='Satisfactory')],
    [KeyboardButton(text='Good'), KeyboardButton(text='Excellent')]])

english_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='A1'), KeyboardButton(text='A2')],
    [KeyboardButton(text='B1'), KeyboardButton(text='B2')],
    [KeyboardButton(text='C1'), KeyboardButton(text='C2')]])

korea_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Topik1'), KeyboardButton(text='Topik2')],
    [KeyboardButton(text='Topik3'), KeyboardButton(text='Topik4')],
    [KeyboardButton(text='Topik5'), KeyboardButton(text='Topik6')]])

japan_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='JLPT N5'), KeyboardButton(text='JLPT N4')],
    [KeyboardButton(text='JLPT N3'), KeyboardButton(text='JLPT N2')],
    [KeyboardButton(text='JLPT N1')]])

china_know_level_but_eng = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='HSK 1'), KeyboardButton(text='HSK 2')],
    [KeyboardButton(text='HSK 3'), KeyboardButton(text='HSK 4')],
    [KeyboardButton(text='HSK 5'), KeyboardButton(text='HSK 6')]])
