from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_type_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton(text='Найти работу'),
                                             KeyboardButton(text='Найти сотрудника')],
                                            [KeyboardButton(text='Разместить рекламу'),
                                             KeyboardButton(text='⬅Назад')]])

services_type_rus1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                         keyboard=[[KeyboardButton(text='Просмотрите открытую базу данных работников')],
                                                   [KeyboardButton(text='Использование кадровой службы')],
                                                   [KeyboardButton(text='🔚Назад')]])

phone_num_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton(text='По кнопке', request_contact=True),
                                         ]], row_width=1
                                    )

yes_no_but_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [KeyboardButton(text='Да'), KeyboardButton(text='Нет')
                                          ]], row_width=1
                                     )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_admin_rus = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text='Tasdiqlash', callback_data='confirm_rus')],
    [InlineKeyboardButton(text='Bekor qilish', callback_data='cancel_rus')],
])

approval_but_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[[KeyboardButton(text='Подтверждение')],
                                                 [KeyboardButton(text='Отмена')], [KeyboardButton(text='🔚Назад')]])

advertisement_but_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=[[KeyboardButton(text='Работодатель')],
                                                      [KeyboardButton(text='Pабочий')],
                                                      [KeyboardButton(text='🔚Назад')]])

inline_keyboard_rus = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Перейти на сайт",
                                           url='https://www.darkor22.uz/uz/all-c'
                                               'andidates?keyword=&address=&p'
                                               'osition=&typeOfWork=&experience=&page=1')]])

inline_keyboard1_rus = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Ссылкa",
                                           url='https://www.darkor22.uz/uz/all-vacancies?keyword=&address=&position=&typeOfWork=&experience=&page=1')]])

user_info_button_rus = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[[KeyboardButton(text='PhD'), KeyboardButton(text='Магистр')],
                                                     [KeyboardButton(text='Холостяк'), KeyboardButton(text='Студент')],
                                                     [KeyboardButton(text='Средний специальный')]])

language_level_button_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Русский язык'), KeyboardButton(text='Английский язык')],
    [KeyboardButton(text='Корейский язык'), KeyboardButton(text='Китайский язык')],
    [KeyboardButton(text='Немецкий язык'), KeyboardButton(text='Французский язык')],
    [KeyboardButton(text='Узбекский язык'), KeyboardButton(text='Следующий')]])

rus_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Я не знаю'), KeyboardButton(text='Удовлетворительно')],
    [KeyboardButton(text='Хороший'), KeyboardButton(text='Отличный')]])

uzb_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Я не знаю'), KeyboardButton(text='Удовлетворительно')],
    [KeyboardButton(text='Хороший'), KeyboardButton(text='Отличный')]])

english_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='A1'), KeyboardButton(text='A2')],
    [KeyboardButton(text='B1'), KeyboardButton(text='B2')],
    [KeyboardButton(text='C1'), KeyboardButton(text='C2')]])

korea_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Topik1'), KeyboardButton(text='Topik2')],
    [KeyboardButton(text='Topik3'), KeyboardButton(text='Topik4')],
    [KeyboardButton(text='Topik5'), KeyboardButton(text='Topik6')]])

japan_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='JLPT N5'), KeyboardButton(text='JLPT N4')],
    [KeyboardButton(text='JLPT N3'), KeyboardButton(text='JLPT N2')],
    [KeyboardButton(text='JLPT N1')]])

china_know_level_but_rus = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='HSK 1'), KeyboardButton(text='HSK 2')],
    [KeyboardButton(text='HSK 3'), KeyboardButton(text='HSK 4')],
    [KeyboardButton(text='HSK 5'), KeyboardButton(text='HSK 6')]])
