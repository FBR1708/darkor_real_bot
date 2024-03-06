import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from Token import bot
from english.keyboard_eng import services_type_eng, services_type_eng1, phone_num_eng, user_info_button_eng, \
    language_level_button_eng, rus_know_level_but_eng, korea_know_level_but_eng, english_know_level_but_eng, \
    china_know_level_but_eng, yes_no_but_eng, advertisement_but_eng, confirmation_admin_eng, \
    uzb_know_level_but_eng, approval_but_eng
from total_keyboard import language


def validate_phone_number(phone_number):
    phone_regex_with_spaces = re.compile(r'^\+998 \d{2} \d{3} \d{2} \d{2}$')
    phone_regex_without_spaces = re.compile(r'^\+998\d{9}$')
    if phone_regex_with_spaces.match(phone_number) or phone_regex_without_spaces.match(phone_number):
        return True
    else:
        return False


async def services_start_eng(message: types.Message):
    await message.answer('Choose a services type', reply_markup=services_type_eng1)


async def back_func_eng(message: types.Message):
    if message.text == '⬅Back':
        await message.answer(text='Tilni tanlang', reply_markup=language)
    elif message.text == '🔚Back':
        await message.answer(text='Choose', reply_markup=services_type_eng)
    elif message.text == 'Cancellation':
        await message.answer(text='Choose', reply_markup=services_type_eng)


# '==============================================================================================================================='

''' Find a job func'''


class UserInfoEng(StatesGroup):
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


async def user_info_start_eng(message: types.Message):
    global service_type
    service_type = message.text
    new_text = 'Enter Full name:\n Example: Abdurahmonov Sanjar Elyorbek o\'g\'li'
    await message.answer(text=new_text)
    await UserInfoEng.name.set()


async def user_name_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await UserInfoEng.next()
    await message.answer(text='Enter Date of birth')


async def user_year_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_year'] = message.text
    await UserInfoEng.next()
    await message.answer(
        "Enter your phone number using the button below. Or enter through a template:\n Example:  +998 XX XXX XX XX",
        reply_markup=phone_num_eng)


async def user_phone_number_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await UserInfoEng.next()
    await message.answer(text='Specialty')


async def user_phone_number1_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("You have entered a phone number in the wrong format. Please re-enter.")
            return
    await UserInfoEng.next()
    await message.answer('Specialty')


async def user_specialty_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['specialty'] = message.text
    await UserInfoEng.next()
    await message.answer(text='Enter your level education using the button below', reply_markup=user_info_button_eng)


async def user_info_eng(message: types.Message, state: FSMContext):
    user_level = ['PhD', 'Magistr', 'Bachelor', 'Medium special', 'Student']
    if message.text in user_level:
        async with state.proxy() as data:
            data['info'] = message.text
        await UserInfoEng.next()
        await message.answer(text='Work experience')
    else:
        await message.answer(text='Error. Enter using the button below')


async def user_experience_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text
    await UserInfoEng.next()
    await message.answer(text='Enter the language skills using the button below',
                         reply_markup=language_level_button_eng)


selected_languages_keyboard = None


async def user_lang_list_eng(message: types.Message, state: FSMContext):
    language_buttons = {'Russia language': rus_know_level_but_eng, 'English language': english_know_level_but_eng,
                        'Korea language': korea_know_level_but_eng, 'China language': china_know_level_but_eng,
                        'German language': english_know_level_but_eng, 'French language': english_know_level_but_eng,
                        'Uzbek language': uzb_know_level_but_eng}

    async with state.proxy() as data:
        if 'know_language_list' not in data:
            data['know_language_list'] = []

        if message.text in language_buttons and message.text not in data['know_language_list']:
            data['know_language_list'].append(message.text)
            await message.answer(
                text=f'{message.text} you have selected your language.Choose another language you know:',
                reply_markup=get_language_keyboard_eng(language_buttons))
        elif message.text == 'Next':
            if not data['know_language_list']:
                await message.answer(text='Error. Choose your language.')
                return
            global selected_languages_keyboard
            selected_languages_keyboard = get_selected_languages_keyboard_eng(data['know_language_list'])
            await UserInfoEng.next()
            await message.answer(text='Languages of your choice:',
                                 reply_markup=selected_languages_keyboard)
        elif message.text in language_buttons and message.text in data['know_language_list']:
            await message.answer(text='You have selected this language', reply_markup=language_level_button_eng)
        else:
            await message.answer('Error. Enter using the button below')


def get_language_keyboard_eng(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Next')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard_eng(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='The next step')
    keyboard1.insert(next_button)
    return keyboard1


async def user_lang_know_eng(message: types.Message, state: FSMContext):
    language_buttons = {'Russia language': rus_know_level_but_eng, 'English language': english_know_level_but_eng,
                        'Korea language': korea_know_level_but_eng, 'China language': china_know_level_but_eng,
                        'German language': english_know_level_but_eng, 'French language': english_know_level_but_eng,
                        'Uzbek language': uzb_know_level_but_eng}

    async with state.proxy() as data:
        if 'language_know' not in data:
            data['language_know'] = []

    if message.text in language_buttons and message.text not in data['language_know']:
        async with state.proxy() as data:
            data['language_know'].append(message.text)
        await UserInfoEng.next()
        await message.answer(text='Choose a language level', reply_markup=language_buttons[message.text])
    elif message.text == 'The next step':
        if not data['language_know']:
            await message.answer(text='Error.Select your language level')
        elif len(data['language_level']) == len(data['know_language_list']):
            await state.set_state(UserInfoEng.address)
            await message.answer(text='The area you are looking for work')
        elif len(data['language_level']) != len(data['know_language_list']):
            await message.answer(text='Choose your level in other languages as well.')
    elif message.text not in language_buttons:
        await message.answer(text='Error. Enter using the button below')
    elif message.text in data['language_know']:
        await message.answer(text='You have chosen your degree in this language')


async def user_lang_level_eng(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'I don\'t know', 'Satisfactory', 'Good', 'Excellent']
    async with state.proxy() as data:
        if 'language_level' not in data:
            data['language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['language_level'].append(message.text)
        await UserInfoEng.next()
        await message.answer(text='Do you have a certificate?', reply_markup=yes_no_but_eng)
    else:
        await message.answer(text='Error. Enter using the button below')


yes_no = None
p = None


async def user_certificate_eng(message: types.Message, state: FSMContext):
    global p
    p = message.text.lower()
    if message.text.lower() == 'yes':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        if message.photo:
            await certificate_image_eng(message, state)
        else:
            await UserInfoEng.next()
            await message.answer(text='Enter the certificate image')
    elif message.text.lower() == 'no':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        await message.answer(text='Languages of your choice:',
                             reply_markup=selected_languages_keyboard)
        await state.set_state(UserInfoEng.know_language)
    else:
        await message.answer(text='Wrong answer. Answer "Yes" or "No".')


async def certificate_image_eng(message: types.Message, state: FSMContext):
    global photo_id_certificate, downloaded_file_certificate
    async with state.proxy() as data:
        certificate_yes_no = data.get('certificate_yes_no')
        if certificate_yes_no and certificate_yes_no.lower() == 'yes':
            if 'certificate_image' not in data:
                data['certificate_image'] = []
            photo_id_certificate = message.photo[-1].file_id
            data['certificate_image'].append(photo_id_certificate)
            file = await bot.get_file(photo_id_certificate)
            downloaded_file_certificate = await bot.download_file(file.file_path)

            await message.answer(text='Languages of your choice:',
                                 reply_markup=selected_languages_keyboard)
            await state.set_state(UserInfoEng.know_language)
        else:
            await message.answer(text='You forgot to upload a picture. Please upload a picture.')


async def user_address_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await UserInfoEng.next()
    await message.answer(text='Comment')


async def user_comment_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
    await UserInfoEng.next()
    await message.answer(text='Enter your picture. The picture should be on a white background')


employee_full_information = None


async def user_image_eng(message: types.Message, state: FSMContext):
    global photo_id, user_full_information, downloaded_file, images_list
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
    if certificate_yes_no.lower() == 'yes' or certificate_yes_no.lower() == 'no':
        if certificate_picture:
            images_list = []
            for i in data['certificate_image']:
                images_list.append(i)
                await bot.send_photo(chat_id=message.chat.id, photo=i)
            await bot.send_message(chat_id=message.chat.id,
                                   text='Check your information and confirm with the button below.',
                                   reply_markup=approval_but_eng)
        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text='Check your information and confirm with the button below.',
                                   reply_markup=approval_but_eng)

    else:
        return
    await state.finish()


async def send_admin_employee_eng():
    group_chat_id = -1002075927837
    file = await bot.get_file(photo_id)
    downloaded_file = await bot.download_file(file.file_path)
    photo_content = downloaded_file.read()
    await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                         caption=employee_full_information)
    if images_list:
        for j in images_list:
            await bot.send_message(chat_id=group_chat_id, text='Certificate image')
            await bot.send_photo(chat_id=group_chat_id, photo=j)
    else:
        pass


# '============================================================================================================================'

'''Use of HR service func'''


class Employer_Info_State_Eng(StatesGroup):
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


async def employer_info_start_func_eng(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Enter the full name and activity of the company.')
    await Employer_Info_State_Eng.company_name.set()


async def employer_company_name_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Enter Full name of employer')


async def responsible_user_name_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['responsible_person_name'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(
        "Enter your phone number using the button below. Or enter through a template:\n Example:  +998 XX XXX XX XX",
        reply_markup=phone_num_eng)


async def employer_phone_number_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await Employer_Info_State_Eng.next()
    await message.answer(text='The right specialist')


async def employer_phone_number1_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("You have entered a phone number in the wrong format. Please re-enter.")
            return
    await Employer_Info_State_Eng.next()
    await message.answer('Necessary employee')


async def employer_direct_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_direct'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Enter the required number of employees')


async def employer_number_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_number'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Enter the duties of the employee')


async def employer_duty_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_duty'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Time working days')


async def work_time_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_time'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Enter required work experience')


async def employer_experience_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_experience'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Determined salary amount and payment period')


async def employer_salary_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_salary'] = message.text
    await Employer_Info_State_Eng.next()
    await message.answer(text='Enter your work address')


employer_full_information = None


async def employer_vocation_func_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['working_vocation'] = message.text
    global employer_full_information
    employer_full_information = (
        f"🏢Kompaniya ismi  va faoliyati : {data['company_name']}\n🤵Ma\'sul xodim ism-familiyasi: {data['responsible_person_name']}"
        f"\n☎Telefon raqam : {data['phone_number']}"
        f"\n🤵Kerakli xodim : {data['employer_direct']}\n🤵Kerakli  xodimlar soni : {data['employer_number']}"
        f"\n🤵Xodimning vazifasi : {data['employer_duty']}\nIsh vaqti : {data['work_time']}"
        f"\n🤵Talab qilinadigan ish tajriba : {data['employer_experience']}"
        f"\n💲Belgilangan maosh miqdori va to'lash muddati : {data['employer_salary']}"
        f"\n🏢Ish joyi manzili : {data['working_vocation']}")

    await bot.send_message(chat_id=message.chat.id, text=employer_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Check your information and confirm with the button below.',
                           reply_markup=approval_but_eng)
    await state.finish()


async def send_admin_HR_employer_eng():
    group_chat_id = [-1002075927837]
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        for i in group_chat_id:
            await bot.send_photo(chat_id=i, photo=photo_content,
                                 caption=employer_full_information)


#
# async def send_channel_HR_employer():
#     group_chat_id = -1002101580581
#     image = 'images/darkor.png'
#     with open(image, 'rb') as photo:
#         await bot.send_photo(chat_id=group_chat_id, photo=photo, text=employer_full_information)

# '========================================================================================================================================='

'''Elon joylash qismining Ish beruvchi func'''


class Advertisement_Emloyer_Info_State_Eng(StatesGroup):
    staff_direct = State()
    staff_count = State()
    company_name = State()
    salary = State()
    work_vocation = State()
    employer_suggestion = State()
    employer_request = State()
    employer_phone_number = State()
    employer_comment = State()


async def advertisement_start_eng(message: types.Message):
    await message.answer(text='Choose', reply_markup=advertisement_but_eng)


async def advertisement_employer_start_eng(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Necessary employee')
    await Advertisement_Emloyer_Info_State_Eng.staff_direct.set()


async def advertisement_employer_staff_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_direct'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter employee count')


async def advertisement_employer_staff_count_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_count'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the name of the organization')


async def advertisement_employer_company_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the salary')


async def advertisement_employer_salary_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['salary'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the address')


async def advertisement_employer_vocation_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_vocation'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the offers')


async def advertisement_employer_suggestion_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_suggestion'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the request')


async def advertisement_employer_request_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_request'] = message.text
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(
        "Enter your phone number using the button below. Or enter through a template:\n Example:  +998 XX XXX XX XX",
        reply_markup=phone_num_eng)


async def advertisement_employer_phone_number_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer(text='Enter the comments')


async def advertisement_employer_phone_number1_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employer_phone_number'] = phone_number
        else:
            await message.answer("You have entered a phone number in the wrong format. Please re-enter.")
            return
    await Advertisement_Emloyer_Info_State_Eng.next()
    await message.answer('Enter the comments')


advertisement_employer_full_information = None


async def advertisement_employer_comment_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_comment'] = message.text
    global advertisement_employer_full_information
    advertisement_employer_full_information = (
        f"Kerakli xodim: {data['staff_direct']}\nXodimlar soni: {data['staff_count']}"
        f"\nTashkilot: {data['company_name']}"
        f"\nMaosh: {data['salary']}"
        f"\nManzil: {data['work_vocation']}\nTakliflar: {data['employer_suggestion']}"
        f"\nTalablar: {data['employer_request']}\nBog'lanish uchun: {data['employer_phone_number']}"
        f"\nIzoh: {data['employer_comment']}")

    await bot.send_message(chat_id=message.chat.id, text=advertisement_employer_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Ma\'lumotlaringizni tekshiring va pastdagi tugma orqali tasdiqlang.',
                           reply_markup=approval_but_eng)
    await state.finish()


async def send_admin_advertisement_employer_eng():
    group_chat_id = [-1002075927837]
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        for i in group_chat_id:
            await bot.send_photo(chat_id=i, photo=photo_content,
                                 caption=advertisement_employer_full_information,
                                 reply_markup=confirmation_admin_eng)


async def send_channel_advertisement_employer_eng():
    group_chat_id = -1002101580581
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employer_full_information)


# '========================================================================================================================================='

'''Worker of the Elon placement section func'''


class Advertisement_Emloyee_Info_State_Eng(StatesGroup):
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


async def advertisement_employee_start_eng(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Enter your specialty')
    await Advertisement_Emloyee_Info_State_Eng.employee_specialty.set()


async def advertisement_employee_specialty_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_specialty'] = message.text
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer(text='Enter your experience')


async def advertisement_employee_experience_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_experience'] = message.text
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer(text='Enter the language you know', reply_markup=language_level_button_eng)


async def employee_lang_list_eng1(message: types.Message, state: FSMContext):
    language_buttons = {'Russia language': rus_know_level_but_eng, 'English language': english_know_level_but_eng,
                        'Korea language': korea_know_level_but_eng, 'China language': china_know_level_but_eng,
                        'German language': english_know_level_but_eng, 'French language': english_know_level_but_eng,
                        'Uzbek language': uzb_know_level_but_eng}

    async with state.proxy() as data:
        if 'employee_language_list' not in data:
            data['employee_language_list'] = []

        if message.text in language_buttons:
            data['employee_language_list'].append(message.text)
            await message.answer(
                text=f'{message.text} you have selected your language.Choose another language you know:',
                reply_markup=get_language_keyboard_eng1(language_buttons))
        elif message.text == 'Next':
            if not data['employee_language_list']:
                await message.answer(text='Error. Choose your language.')
                return
            global selected_languages_keyboard1
            selected_languages_keyboard1 = get_selected_languages_keyboard_eng1(data['employee_language_list'])
            await Advertisement_Emloyee_Info_State_Eng.next()
            await message.answer(text='Languages of your choice:',
                                 reply_markup=selected_languages_keyboard1)
        else:
            await message.answer('Error. Enter using the button below')


def get_language_keyboard_eng1(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Next')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard_eng1(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='The next step')
    keyboard1.insert(next_button)
    return keyboard1


async def employee_lang_know_eng1(message: types.Message, state: FSMContext):
    language_buttons = {'Russia language': rus_know_level_but_eng, 'English language': english_know_level_but_eng,
                        'Korea language': korea_know_level_but_eng, 'China language': china_know_level_but_eng,
                        'German language': english_know_level_but_eng, 'French language': english_know_level_but_eng,
                        'Uzbek language': uzb_know_level_but_eng}

    async with state.proxy() as data:
        if 'employee_language_know' not in data:
            data['employee_language_know'] = []

    if message.text in language_buttons and message.text not in data['employee_language_know']:
        async with state.proxy() as data:
            data['employee_language_know'].append(message.text)
        await Advertisement_Emloyee_Info_State_Eng.next()
        await message.answer(text='Choose a language level', reply_markup=language_buttons[message.text])
    elif message.text == 'The next step':
        if not data['employee_language_know']:
            await message.answer(text='Error.Select your language level')
        elif len(data['employee_language_level']) == len(data['employee_language_list']):
            await state.set_state(Advertisement_Emloyee_Info_State_Eng.employee_info)
            await message.answer(text='Enter your level education using the button below',
                                 reply_markup=user_info_button_eng)
        elif len(data['employee_language_level']) != len(data['employee_language_list']):
            await message.answer(text='Choose your level in other languages as well.')
    elif message.text not in language_buttons:
        await message.answer(text='Error. Enter using the button below')
    elif message.text in data['employee_language_know']:
        await message.answer(text='You have chosen your degree in this language')


async def employee_lang_level_eng1(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'I don\'t know', 'Satisfactory', 'Good', 'Excellent']
    async with state.proxy() as data:
        if 'employee_language_level' not in data:
            data['employee_language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['employee_language_level'].append(message.text)
            await message.answer(text='Languages of your choice:',
                                 reply_markup=selected_languages_keyboard1)
            await state.set_state(Advertisement_Emloyee_Info_State_Eng.employee_language_know)
    else:
        await message.answer(text='Error. Enter using the button below')


async def advertisement_employee_info_eng(message: types.Message, state: FSMContext):
    user_level = ['PhD', 'Magistr', 'Bachelor', 'Medium special', 'Student']
    if message.text in user_level:
        async with state.proxy() as data:
            data['employee_info'] = message.text
        await Advertisement_Emloyee_Info_State_Eng.next()
        await message.answer(text='Type of work\nExample : online / offline')
    else:
        await message.answer(text='Error. Enter using the button below')


async def advertisement_employee_request_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_request'] = message.text
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer(text='Enter an address')


async def advertisement_employee_vocation_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_work_vocation'] = message.text
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer(
        "Enter your phone number using the button below. Or enter through the template:\n Example: +998 XX XXX XX XX",
        reply_markup=phone_num_eng)


async def advertisement_employee_phone_number_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer(text='Enter the comments')


async def advertisement_employee_phone_number1_eng(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employee_phone_number'] = phone_number
        else:
            await message.answer("You have entered a phone number in the wrong format. Please re-enter.")
            return
    await Advertisement_Emloyee_Info_State_Eng.next()
    await message.answer('Enter the  comments')


advertisement_employee_full_information = None


async def advertisement_employee_comment_eng(message: types.Message, state: FSMContext):
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
                           text='Ma\'lumotlaringizni tekshiring va pastdagi tugma orqali tasdiqlang.',
                           reply_markup=approval_but_eng)

    await state.finish()


async def send_admin_advertisement_employee_eng():
    group_chat_id = -1002075927837
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employee_full_information,
                             reply_markup=confirmation_admin_eng)


async def send_channel_advertisement_employee_eng():
    group_chat_id = -1002101580581
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employee_full_information)

# '=========================================================================================================='
