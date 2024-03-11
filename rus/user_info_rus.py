import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from Token import bot
from rus.keyboard_rus import services_type_rus1, services_type_rus, phone_num_rus, user_info_button_rus, \
    uzb_know_level_but_rus, yes_no_but_rus, approval_but_rus, advertisement_but_rus, language_level_button_rus, \
    confirmation_admin_rus, rus_know_level_but_rus
from total_keyboard import language
from uzb.keyboard_uz import english_know_level_but, \
    korea_know_level_but, china_know_level_but


def validate_phone_number(phone_number):
    phone_regex_with_spaces = re.compile(r'^\+998 \d{2} \d{3} \d{2} \d{2}$')
    phone_regex_without_spaces = re.compile(r'^\+998\d{9}$')
    if phone_regex_with_spaces.match(phone_number) or phone_regex_without_spaces.match(phone_number):
        return True
    else:
        return False


async def services_start_rus(message: types.Message):
    await message.answer('Выберите тип услуги', reply_markup=services_type_rus1)


async def back_func_rus(message: types.Message):
    if message.text == '⬅Назад':
        await message.answer(text='Tilni tanlang', reply_markup=language)
    elif message.text == '🔚Назад':
        await message.answer(text='Выбирать', reply_markup=services_type_rus)
    elif message.text == 'Отмена':
        await message.answer(text='Выбирать', reply_markup=services_type_rus)


# '==============================================================================================================================='

''' Ish topish func'''


class UserInfoRus(StatesGroup):
    name = State()
    user_year = State()
    phone_number = State()
    specialty = State()
    info = State()
    experience = State()
    know_language_list = State()
    know_language = State()
    language_level = State()
    certificate_yes_no = State()
    certificate_image = State()
    address = State()
    comment = State()
    image = State()


service_type = None


async def user_info_start_rus(message: types.Message):
    global service_type
    service_type = message.text
    new_text = 'Фамилия Имя:'
    await message.answer(text=new_text)
    await UserInfoRus.name.set()


async def user_name_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await UserInfoRus.next()
    await message.answer(text='Год рождения:')


async def user_year_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_year'] = message.text
    await UserInfoRus.next()
    await message.answer(
        "Введите свой номер телефона, используя кнопку ниже. Или введите через шаблон:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num_rus)


async def user_phone_number_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await UserInfoRus.next()
    await message.answer(text='Специальность:')


async def user_phone_number1_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, войдите еще раз.")
            return
    await UserInfoRus.next()
    await message.answer('Специальность:')


async def user_specialty_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['specialty'] = message.text
    await UserInfoRus.next()
    await message.answer(text='Информация, используя кнопку ниже:', reply_markup=user_info_button_rus)


async def user_info_rus(message: types.Message, state: FSMContext):
    user_level = ['PhD', 'Магистр', 'Холостяк', 'Студент', 'Средний специальный']
    if message.text in user_level:
        async with state.proxy() as data:
            data['info'] = message.text
        await UserInfoRus.next()
        await message.answer(text='Опыт работы:')
    else:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже')


async def user_experience_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text
    await UserInfoRus.next()
    await message.answer(text='Языковые навыки, используя кнопку ниже', reply_markup=language_level_button_rus)


selected_languages_keyboard = None


async def user_lang_list_rus(message: types.Message, state: FSMContext):
    language_buttons = {'Русский язык': rus_know_level_but_rus, 'Английский язык': english_know_level_but,
                        'Корейский язык': korea_know_level_but, 'Китайский язык': china_know_level_but,
                        'Немецкий язык': english_know_level_but, 'Французский язык': english_know_level_but,
                        'Узбекский язык': uzb_know_level_but_rus}

    async with state.proxy() as data:
        if 'know_language_list' not in data:
            data['know_language_list'] = []

        if message.text in language_buttons and message.text not in data['know_language_list']:
            data['know_language_list'].append(message.text)
            await message.answer(text=f'{message.text} вы выбрали свой язык. Выберите оставшийся язык:',
                                 reply_markup=get_language_keyboard_rus(language_buttons))
        elif message.text == 'Следующий':
            if not data['know_language_list']:
                await message.answer(text='Ошибка. Выберите язык, который вы знаете.')
                return
            global selected_languages_keyboard
            selected_languages_keyboard = get_selected_languages_keyboard_rus(data['know_language_list'])
            await UserInfoRus.next()
            await message.answer(text='Языки по вашему выбору:',
                                 reply_markup=selected_languages_keyboard)
        elif message.text in language_buttons and message.text in data['know_language_list']:
            await message.answer(text='Вы выбрали этот язык', reply_markup=language_level_button_rus)
        else:
            await message.answer(text="Ошибка. Войдите, используя кнопку ниже")


def get_language_keyboard_rus(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Следующий')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard_rus(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='Следующий шаг')
    keyboard1.insert(next_button)
    return keyboard1


async def user_lang_know_rus(message: types.Message, state: FSMContext):
    language_buttons = {'Русский язык': rus_know_level_but_rus, 'Английский язык': english_know_level_but,
                        'Корейский язык': korea_know_level_but, 'Китайский язык': china_know_level_but,
                        'Немецкий язык': english_know_level_but, 'Французский язык': english_know_level_but,
                        'Узбекский язык': uzb_know_level_but_rus}

    async with state.proxy() as data:
        if 'language_know' not in data:
            data['language_know'] = []

    if message.text in language_buttons and message.text not in data['language_know']:
        async with state.proxy() as data:
            data['language_know'].append(message.text)
        await UserInfoRus.next()
        await message.answer(text='Выберите свой уровень', reply_markup=language_buttons[message.text])
    elif message.text == 'Следующий шаг':
        if not data['language_know']:
            await message.answer(text='Ошибка. Выберите уровень языка.')
        elif len(data['language_level']) == len(data['know_language_list']):
            await state.set_state(UserInfoRus.address)
            await message.answer(text='Район, в котором вы ищете работу')
        elif len(data['language_level']) != len(data['know_language_list']):
            await message.answer(text='Выберите свой уровень на выбранных вами языках.')
    elif message.text not in language_buttons:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже.')
    elif message.text in data['language_know']:
        await message.answer(text='Вы выбрали степень на этом языке')


async def user_lang_level_rus(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'Я не знаю', 'Удовлетворительно', 'Хороший', 'Отличный']
    async with state.proxy() as data:
        if 'language_level' not in data:
            data['language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['language_level'].append(message.text)
        await UserInfoRus.next()
        await message.answer(text='У вас есть сертификат?', reply_markup=yes_no_but_rus)
    else:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже')


yes_no = None
p = None


async def user_certificate_rus(message: types.Message, state: FSMContext):
    global p
    p = message.text.lower()
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        if message.photo:
            await certificate_image_rus(message, state)
        else:
            await UserInfoRus.next()
            await message.answer(text='Введите изображение сертификата')
    elif message.text.lower() == 'нет':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        await message.answer(text='Языки по вашему выбору:',
                             reply_markup=selected_languages_keyboard)
        await state.set_state(UserInfoRus.know_language)
    else:
        await message.answer(text='Неверный ответ. Ответьте «Да» или «Нет».')


async def certificate_image_rus(message: types.Message, state: FSMContext):
    global photo_id_certificate, downloaded_file_certificate
    async with state.proxy() as data:
        certificate_yes_no = data.get('certificate_yes_no')
        if certificate_yes_no and certificate_yes_no.lower() == 'да':
            if 'certificate_image' not in data:
                data['certificate_image'] = []
            photo_id_certificate = message.photo[-1].file_id
            data['certificate_image'].append(photo_id_certificate)
            file = await bot.get_file(photo_id_certificate)
            downloaded_file_certificate = await bot.download_file(file.file_path)

            await message.answer(text='Языки по вашему выбору:',
                                 reply_markup=selected_languages_keyboard)
            await state.set_state(UserInfoRus.know_language)
        else:
            await message.answer(text='Вы забыли загрузить картинку. Пожалуйста, загрузите изображение.')


async def user_address_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await UserInfoRus.next()
    await message.answer(text='Дополнительная информация')


async def user_comment_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
    await UserInfoRus.next()
    await message.answer(text='Введите свою картина. Картина должно быть на белом фоне.')


employee_full_information = None
pictures_list = []

async def user_image_rus(message: types.Message, state: FSMContext):
    global photo_id, user_full_information, downloaded_file, pictures_list
    photo_id = message.photo[-1].file_id
    async with state.proxy() as data:
        data['image'] = photo_id
    file = await bot.get_file(photo_id)
    downloaded_file = await bot.download_file(file.file_path)
    global employee_full_information

    employee_full_information = (
        f"Xodim : {data['name']}\nTug'ilgan yili : {data['user_year']}\nTelefon raqam : {data['phone_number']}"
        f"\nMutaxassisligi : {data['specialty']}"
        f"\nMalu'mot: {data['info']}\nIsh tajribasi : {data['experience']}")

    if data['language_know'] is not None and data['language_level'] is not None:
        for language_know, language_level in zip(data['language_know'], data['language_level']):
            employee_full_information += f"\nTil bilishi : {language_know} - {language_level}"

    employee_full_information += (
        f"\nIsh qidirayotgan hududi : {data['address']}"
        f"\nQo'shimcha malumotlar : {data['comment']}")

    await bot.send_photo(chat_id=message.chat.id, photo=downloaded_file, caption=employee_full_information)
    certificate_yes_no = data.get('certificate_yes_no')
    certificate_picture = data.get('certificate_image')
    if certificate_yes_no.lower() == 'да' or certificate_yes_no.lower() == 'нет':
        if certificate_picture:
            # pictures_list = []
            for i in data['certificate_image']:
                pictures_list.append(i)
                await bot.send_photo(chat_id=message.chat.id, photo=i)
            await bot.send_message(chat_id=message.chat.id,
                                   text='Проверьте свои данные и подтвердите их, нажав кнопку ниже..',
                                   reply_markup=approval_but_rus)
        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text='Проверьте свои данные и подтвердите их, нажав кнопку ниже..',
                                   reply_markup=approval_but_rus)

    else:
        return
    await state.finish()


async def send_admin_employee_rus():
    group_chat_id = -1002075927837
    file = await bot.get_file(photo_id)
    downloaded_file = await bot.download_file(file.file_path)
    photo_content = downloaded_file.read()
    await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                         caption=employee_full_information)
    if pictures_list:
        for j in pictures_list:
            await bot.send_message(chat_id=group_chat_id, text='Изображение сертификата')
            await bot.send_photo(chat_id=group_chat_id, photo=j)
    else:
        pass


# '============================================================================================================================'

'''HR xizmatidan foydalanish func'''


class Employer_Info_State_Rus(StatesGroup):
    company_name = State()
    responsible_person_name = State()
    phone_number = State()
    employer_direct = State()
    employer_number = State()
    employer_duty = State()
    work_time = State()
    employer_experience = State()
    employer_salary = State()
    working_vocation = State()


async def employer_info_start_func_rus(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Полное название и вид деятельности компании.')
    await Employer_Info_State_Rus.company_name.set()


async def employer_company_name_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Имя и фамилия ответственного сотрудника')


async def responsible_user_name_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['responsible_person_name'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(
        "Введите свой номер телефона, используя кнопку ниже. Или введите через шаблон:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num_rus)


async def employer_phone_number_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await Employer_Info_State_Rus.next()
    await message.answer(text='Требуемый сотрудник(а)')


async def employer_phone_number1_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, войдите еще раз.")
            return
    await Employer_Info_State_Rus.next()
    await message.answer('Требуемый сотрудник(а)')


async def employer_direct_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_direct'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Требуемое количество сотрудников')


async def employer_number_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_number'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Обязанность работника')


async def employer_duty_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_duty'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Рабочее время')


async def work_time_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_time'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Требуемый опыт работы')


async def employer_experience_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_experience'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Определяется размер заработной платы и период выплаты')


async def employer_salary_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_salary'] = message.text
    await Employer_Info_State_Rus.next()
    await message.answer(text='Адрес рабочего места')


employer_full_information = None


async def employer_vocation_func_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['working_vocation'] = message.text
    global employer_full_information
    employer_full_information = (
        f"🏢Kompaniya ismi  va faoliyati : {data['company_name']}\n🤵Ma\'sul xodim ism-familiyasi: {data['responsible_person_name']}"
        f"\n☎Telefon raqam : {data['phone_number']}"
        f"\n🤵Kerakli xodim : {data['employer_direct']}\n🤵Kerakli  xodimlar soni : {data['employer_number']}"
        f"\n🤵Xodimning vazifasi : {data['employer_duty']}\n🕰Ish vaqti : {data['work_time']}"
        f"\n🤵Talab qilinadigan ish tajriba : {data['employer_experience']}"
        f"\n💲Belgilangan maosh miqdori va to'lash muddati : {data['employer_salary']}"
        f"\n🏢Ish joyi manzili : {data['working_vocation']}")

    await bot.send_message(chat_id=message.chat.id, text=employer_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Проверьте свои данные и подтвердите их, нажав кнопку ниже.',
                           reply_markup=approval_but_rus)
    await state.finish()


async def send_admin_HR_employer_rus():
    group_chat_id = -1002075927837
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=employer_full_information)


# '========================================================================================================================================='

'''Elon joylash qismining Ish beruvchi func'''


class Advertisement_Emloyer_Info_State_Rus(StatesGroup):
    staff_direct = State()
    staff_count = State()
    company_name = State()
    salary = State()
    work_vocation = State()
    employer_suggestion = State()
    employer_request = State()
    employer_phone_number = State()
    employer_comment = State()


async def advertisement_start_rus(message: types.Message):
    await message.answer(text='Выбирать', reply_markup=advertisement_but_rus)


async def advertisement_employer_start_rus(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Хороший сотрудник:')
    await Advertisement_Emloyer_Info_State_Rus.staff_direct.set()


async def advertisement_employer_staff_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_direct'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Количество работников:')


async def advertisement_employer_staff_count_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_count'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Организация:')


async def advertisement_employer_company_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Зарплата:')


async def advertisement_employer_salary_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['salary'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Адрес:')


async def advertisement_employer_vocation_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_vocation'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Предложения:')


async def advertisement_employer_suggestion_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_suggestion'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Требования')


async def advertisement_employer_request_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_request'] = message.text
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(
        "Введите свой номер телефона, используя кнопку ниже. Или введите через шаблон:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num_rus)


async def advertisement_employer_phone_number_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer(text='Объяснение')


async def advertisement_employer_phone_number1_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employer_phone_number'] = phone_number
        else:
            await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, войдите еще раз.")
            return
    await Advertisement_Emloyer_Info_State_Rus.next()
    await message.answer('Объяснение')


advertisement_employer_full_information = None


async def advertisement_employer_comment_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_comment'] = message.text
    global advertisement_employer_full_information
    advertisement_employer_full_information = (
        f"Kerakli xodim: {data['staff_direct']}\nTashkilot: {data['company_name']}"
        f"\nMaosh: {data['salary']}"
        f"\nManzil: {data['work_vocation']}\nTakliflar: {data['employer_suggestion']}"
        f"\nTalablar: {data['employer_request']}\nBog'lanish uchun: {data['employer_phone_number']}"
        f"\nIzoh: {data['employer_comment']}")

    await bot.send_message(chat_id=message.chat.id, text=advertisement_employer_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Проверьте свои данные и подтвердите их, нажав кнопку ниже.',
                           reply_markup=approval_but_rus)
    await state.finish()


async def send_admin_advertisement_employer_rus():
    group_chat_id = [-1002075927837]
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        for i in group_chat_id:
            await bot.send_photo(chat_id=i, photo=photo_content,
                                 caption=advertisement_employer_full_information,
                                 reply_markup=confirmation_admin_rus)


async def send_channel_advertisement_employer_rus():
    # group_chat_id = -1002101580581
    group_chat_id = -1001572125885
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employer_full_information)


# '========================================================================================================================================='

'''Elon joylash qismining Ishchi func'''


class Advertisement_Emloyee_Info_State_Rus(StatesGroup):
    employee_specialty = State()
    employee_experience = State()
    employee_language_list = State()
    employee_language_know = State()
    employee_language_level = State()
    employee_info = State()
    employee_request = State()
    employee_work_vocation = State()
    employee_phone_number = State()
    employee_comment = State()


async def advertisement_employee_start_rus(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Специальность')
    await Advertisement_Emloyee_Info_State_Rus.employee_specialty.set()


async def advertisement_employee_specialty_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_specialty'] = message.text
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer(text='Опыт')


async def advertisement_employee_experience_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_experience'] = message.text
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer(text='Владение языком', reply_markup=language_level_button_rus)


async def advertisement_employee_lang_list_rus(message: types.Message, state: FSMContext):
    language_buttons = {'Русский язык': rus_know_level_but_rus, 'Английский язык': english_know_level_but,
                        'Корейский язык': korea_know_level_but, 'Китайский язык': china_know_level_but,
                        'Немецкий язык': english_know_level_but, 'Французский язык': english_know_level_but,
                        'Узбекский язык': uzb_know_level_but_rus}

    async with state.proxy() as data:
        if 'employee_language_list' not in data:
            data['employee_language_list'] = []

        if message.text in language_buttons and message.text not in data['employee_language_list']:
            data['employee_language_list'].append(message.text)
            await message.answer(
                text=f'{message.text} вы выбрали свой язык.Выберите другой язык, который вы знаете:',
                reply_markup=get_language_keyboard_rus1(language_buttons))
        elif message.text == 'Следующий':
            if not data['employee_language_list']:
                await message.answer(text='Ошибка. Выберите ваш язык.')
                return
            global selected_languages_keyboard1
            selected_languages_keyboard1 = get_selected_languages_keyboard_rus(data['employee_language_list'])
            await Advertisement_Emloyee_Info_State_Rus.next()
            await message.answer(text='Языки по вашему выбору:',
                                 reply_markup=selected_languages_keyboard1)
        elif message.text in language_buttons and message.text in data['employee_language_list']:
            await message.answer(text='Вы выбрали этот язык', reply_markup=language_level_button_rus)
        else:
            await message.answer('Ошибка. Войдите, используя кнопку ниже')


def get_language_keyboard_rus1(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Следующий')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard_rus1(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='Следующий шаг')
    keyboard1.insert(next_button)
    return keyboard1


async def advertisement_employee_lang_know_rus(message: types.Message, state: FSMContext):
    language_buttons = {'Русский язык': rus_know_level_but_rus, 'Английский язык': english_know_level_but,
                        'Корейский язык': korea_know_level_but, 'Китайский язык': china_know_level_but,
                        'Немецкий язык': english_know_level_but, 'Французский язык': english_know_level_but,
                        'Узбекский язык': uzb_know_level_but_rus}

    async with state.proxy() as data:
        if 'employee_language_know' not in data:
            data['employee_language_know'] = []

    if message.text in language_buttons and message.text not in data['employee_language_know']:
        async with state.proxy() as data:
            data['employee_language_know'].append(message.text)
        await Advertisement_Emloyee_Info_State_Rus.next()
        await message.answer(text='Выберите уровень языка', reply_markup=language_buttons[message.text])
    elif message.text == 'Следующий шаг':
        if not data['employee_language_know']:
            await message.answer(text='Ошибка. Выберите уровень языка.')
        elif len(data['employee_language_level']) == len(data['employee_language_list']):
            await state.set_state(Advertisement_Emloyee_Info_State_Rus.employee_info)
            await message.answer(text='Информация', reply_markup=user_info_button_rus)
        elif len(data['employee_language_level']) != len(data['employee_language_list']):
            await message.answer(text='Также выберите свой уровень на других языках.')
    elif message.text not in language_buttons:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже')
    elif message.text in data['employee_language_know']:
        await message.answer(text='Вы выбрали степень на этом языке')


async def advertisement_employee_lang_level_rus(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'Я не знаю', 'Удовлетворительно', 'Хороший', 'Отличный']
    async with state.proxy() as data:
        if 'employee_language_level' not in data:
            data['employee_language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['employee_language_level'].append(message.text)
            await message.answer(text='Языки по вашему выбору:',
                                 reply_markup=selected_languages_keyboard1)
            await state.set_state(Advertisement_Emloyee_Info_State_Rus.employee_language_know)
    else:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже')


async def advertisement_employee_info_rus(message: types.Message, state: FSMContext):
    user_level = ['PhD', 'Магистр', 'Холостяк', 'Студент', 'Средний специальный']
    if message.text in user_level:
        async with state.proxy() as data:
            data['employee_info'] = message.text
        await Advertisement_Emloyee_Info_State_Rus.next()
        await message.answer(text='Тип работы: онлайн оффлайн и т.д....')
    else:
        await message.answer(text='Ошибка. Войдите, используя кнопку ниже')


async def advertisement_employee_request_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_request'] = message.text
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer(text='Адрес')


async def advertisement_employee_vocation_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_work_vocation'] = message.text
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer(
        "Введите свой номер телефона, используя кнопку ниже. Или введите через шаблон.\nНапример:  +998 XX XXX XX XX",
        reply_markup=phone_num_rus)


async def advertisement_employee_phone_number_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer(text='Примечание:')


async def advertisement_employee_phone_number1_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employee_phone_number'] = phone_number
        else:
            await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, войдите еще раз.")
            return
    await Advertisement_Emloyee_Info_State_Rus.next()
    await message.answer('Примечание:')


advertisement_employee_full_information = None


async def advertisement_employee_comment_rus(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_comment'] = message.text
    global advertisement_employee_full_information
    advertisement_employee_full_information = (
        f"Mutaxassisligi: {data['employee_specialty']}\nTajriba: {data['employee_experience']}")

    if data['employee_language_know'] is not None and data['employee_language_level'] is not None:
        for language_know, language_level in zip(data['employee_language_know'], data['employee_language_level']):
            advertisement_employee_full_information += f"\nTil bilishi : {language_know} - {language_level}"

    advertisement_employee_full_information += (
        f"\nMa\'lumoti: {data['employee_info']}\nIsh turi: {data['employee_request']}"
        f"\nManzil: {data['employee_work_vocation']}\nBog'lanish uchun: {data['employee_phone_number']}"
        f"\nIzoh: {data['employee_comment']}")
    await bot.send_message(chat_id=message.chat.id, text=advertisement_employee_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Проверьте свои данные и подтвердите их, нажав кнопку ниже.',
                           reply_markup=approval_but_rus)

    await state.finish()


async def send_admin_advertisement_employee_rus():
    group_chat_id = [-1002075927837]
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        for i in group_chat_id:
            photo_content = photo.read()
            await bot.send_photo(chat_id=i, photo=photo_content,
                                 caption=advertisement_employee_full_information,
                                 reply_markup=confirmation_admin_rus)


async def send_channel_advertisement_employee_rus():
    # group_chat_id = -1002101580581
    group_chat_id = -1001572125885
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employee_full_information)

# '=========================================================================================================='
