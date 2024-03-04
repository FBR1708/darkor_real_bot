import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from Token import bot
from english.keyboard_eng import rus_know_level_but_eng, korea_know_level_but_eng
from total_keyboard import language
from uzb.keyboard_uz import services_type_uz1, phone_num, advertisement_but, services_type_uz, \
    confirmation_admin, language_level_button, rus_know_level_but, english_know_level_but, \
    korea_know_level_but, china_know_level_but, user_info_button, yes_no_but, approval_but


def validate_phone_number(phone_number):
    phone_regex_with_spaces = re.compile(r'^\+998 \d{2} \d{3} \d{2} \d{2}$')
    phone_regex_without_spaces = re.compile(r'^\+998\d{9}$')
    if phone_regex_with_spaces.match(phone_number) or phone_regex_without_spaces.match(phone_number):
        return True
    else:
        return False


async def services_start(message: types.Message):
    await message.answer('Xizmat turini tanlang', reply_markup=services_type_uz1)


async def back_func(message: types.Message):
    if message.text == '⬅Ortga':
        await message.answer(text='Tilni tanlang', reply_markup=language)
    elif message.text == '🔚Ortga':
        await message.answer(text='Tanlang', reply_markup=services_type_uz)
    elif message.text == 'O\'zgartirish':
        await message.answer(text='Tanlang', reply_markup=services_type_uz)


# '==============================================================================================================================='

''' Ish topish func'''


class UserInfoUzb(StatesGroup):
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


async def user_info_start(message: types.Message):
    global service_type
    service_type = message.text
    new_text = 'Familiya Ism Sharif kiriting:\n M-n: Abdurahmonov Sanjar Elyorbek o\'g\'li'
    await message.answer(text=new_text)
    await UserInfoUzb.name.set()


async def user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await UserInfoUzb.next()
    await message.answer(text='Tug\'ilgan yilingizni  kiriting')


async def user_year(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_year'] = message.text
    await UserInfoUzb.next()
    await message.answer(
        "Telefon raqamingizni pastdagi tugma orqali kiriting. Yoki shablon orqali  kiriting:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num)


async def user_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await UserInfoUzb.next()
    await message.answer(text='Mutaxassislik')


async def user_phone_number1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("Noto'g'ri formatdagi telefon raqamini kiritdingiz. Iltimos, qaytadan kiriting.")
            return
    await UserInfoUzb.next()
    await message.answer('Mutaxassislik')


async def user_specialty(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['specialty'] = message.text
    await UserInfoUzb.next()
    await message.answer(text='Ma\'lumotingizni pastdagi tugma orqali kiriting', reply_markup=user_info_button)


async def user_info(message: types.Message, state: FSMContext):
    user_level = ['PhD', 'Magistr', 'Bakalavr', 'Talaba', 'O\'rta maxsus']
    if message.text in user_level:
        async with state.proxy() as data:
            data['info'] = message.text
        await UserInfoUzb.next()
        await message.answer(text='Ish tajribasi')
    else:
        await message.answer(text='Xatolik. Pastdagi tugma orqali kiriting')


async def user_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text
    await UserInfoUzb.next()
    await message.answer(text='Til bilish pastdagi tugma orqali kiriting', reply_markup=language_level_button)


selected_languages_keyboard = None


async def user_lang_list(message: types.Message, state: FSMContext):
    language_buttons = {'Rus tili': rus_know_level_but, 'Ingliz tili': english_know_level_but,
                        'Koreys tili': korea_know_level_but, 'Xitoy tili': china_know_level_but,
                        'Nemis tili': english_know_level_but, 'Fransuz tili': english_know_level_but}

    async with state.proxy() as data:
        if 'know_language_list' not in data:
            data['know_language_list'] = []

        if message.text in language_buttons and message.text not in data['know_language_list']:
            data['know_language_list'].append(message.text)
            await message.answer(text=f'{message.text} tilini tanladingiz. Qolgan tilni tanlang:',
                                 reply_markup=get_language_keyboard(language_buttons))
        elif message.text == 'Keyingi':
            if not data['know_language_list']:
                await message.answer(text='Xatolik. Tilingizni tanlang.')
                return
            global selected_languages_keyboard
            selected_languages_keyboard = get_selected_languages_keyboard(data['know_language_list'])
            await UserInfoUzb.next()
            await message.answer(text='Siz tanlagan tillar:',
                                 reply_markup=selected_languages_keyboard)
        elif message.text in language_buttons and message.text in data['know_language_list']:
            await message.answer(text='Siz ushbu tilni tanlagansiz. Iltimos boshqa biladigan tilingizni tanlang.',
                                 reply_markup=language_level_button)
        else:
            await message.answer('Xatolik.Pastdagi tugma orqali kiriting')


def get_language_keyboard(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Keyingi')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='Keyingi qadam')
    keyboard1.insert(next_button)
    return keyboard1


async def user_lang_know(message: types.Message, state: FSMContext):
    language_buttons = {'Rus tili': rus_know_level_but, 'Ingliz tili': english_know_level_but,
                        'Koreys tili': korea_know_level_but, 'Xitoy tili': china_know_level_but,
                        'Nemis tili': english_know_level_but, 'Fransuz tili': english_know_level_but}

    async with state.proxy() as data:
        if 'language_know' not in data:
            data['language_know'] = []

    if message.text in language_buttons and message.text not in data['language_know']:
        async with state.proxy() as data:
            data['language_know'].append(message.text)
        await UserInfoUzb.next()
        await message.answer(text='Darajangizni tanlang', reply_markup=language_buttons[message.text])
    elif message.text == 'Keyingi qadam':
        if not data['language_know']:
            await message.answer(text='Til bilish darajangizni tanlang')
        elif len(data['language_level']) == len(data['know_language_list']):
            await state.set_state(UserInfoUzb.address)
            await message.answer(text='Ish izlayotgan hududingiz')
        elif len(data['language_level']) != len(data['know_language_list']):
            await message.answer(text='Qolgan tillardagi darajangizni ham tanlang.')
    elif message.text not in language_buttons:
        await message.answer(text='Xatolik.Pastdagi tugma orqali kiriting')
    elif message.text in data['language_know']:
        await message.answer(text='Siz bu tilda darajangizni tanlagansiz')


async def user_lang_level(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'Bilmayman', 'Qoniqarli', 'Yaxshi', 'A\'lo']
    async with state.proxy() as data:
        if 'language_level' not in data:
            data['language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['language_level'].append(message.text)
        await UserInfoUzb.next()
        await message.answer(text='Sertikatingiz bormi?', reply_markup=yes_no_but)
    else:
        await message.answer(text='Xatolik. Pastdagi tugma orqali kiriting')


yes_no = None
p = None


async def user_certificate(message: types.Message, state: FSMContext):
    global p
    p = message.text.lower()
    if message.text.lower() == 'bor':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        if message.photo:
            await certificate_image(message, state)
        else:
            await UserInfoUzb.next()
            await message.answer(text='Sertifikat rasmini kiriting')
    elif message.text.lower() == 'yo\'q':
        async with state.proxy() as data:
            data['certificate_yes_no'] = message.text
        await message.answer(text='Siz tanlagan tillar:',
                             reply_markup=selected_languages_keyboard)
        await state.set_state(UserInfoUzb.know_language)
    else:
        await message.answer(text='Noto\'g\'ri javob. "Bor" yoki "Yo\'q" deb javob bering.')


photo_id_certificate = None
downloaded_file_certificate = None


async def certificate_image(message: types.Message, state: FSMContext):
    global photo_id_certificate, downloaded_file_certificate
    async with state.proxy() as data:
        certificate_yes_no = data.get('certificate_yes_no')
        if certificate_yes_no and certificate_yes_no.lower() == 'bor':
            if 'certificate_image' not in data:
                data['certificate_image'] = []
            photo_id_certificate = message.photo[-1].file_id
            data['certificate_image'].append(photo_id_certificate)
            file = await bot.get_file(photo_id_certificate)
            downloaded_file_certificate = await bot.download_file(file.file_path)

            await message.answer(text='Siz tanlagan tillar:',
                                 reply_markup=selected_languages_keyboard)
            await state.set_state(UserInfoUzb.know_language)

        else:
            await message.answer(text='Rasmni yuklashni unutdingiz. Iltimos, rasmni yuklang.')


async def user_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await UserInfoUzb.next()
    await message.answer(text='Izoh')


async def user_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
    await UserInfoUzb.next()
    await message.answer(text='Rasmingizni kiriting. Rasm oq fonda bo\'lishi kerak')


employee_full_information = None
photo_id = None
user_full_information = None


async def user_image(message: types.Message, state: FSMContext):
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
    if certificate_yes_no.lower() == 'bor' or certificate_yes_no.lower() == 'yo\'q':
        if certificate_picture:
            images_list = []
            for i in data['certificate_image']:
                images_list.append(i)
                await bot.send_photo(chat_id=message.chat.id, photo=i)
            await bot.send_message(chat_id=message.chat.id,
                                   text='Ma\'lumotlaringizni tekshiring va pastdagi tugma orqali tasdiqlang.',
                                   reply_markup=approval_but)
        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text='Ma\'lumotlaringizni tekshiring va pastdagi tugma orqali tasdiqlang.',
                                   reply_markup=approval_but)

    else:
        return
    await state.finish()


async def send_admin_employee():
    group_chat_id = -1002075927837
    file = await bot.get_file(photo_id)
    downloaded_file = await bot.download_file(file.file_path)
    photo_content = downloaded_file.read()
    await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                         caption=employee_full_information)
    if images_list:
        for j in images_list:
            await bot.send_message(chat_id=group_chat_id, text='Sertifikat rasmi')
            await bot.send_photo(chat_id=group_chat_id, photo=j)
    else:
        pass
    # '============================================================================================================================'


'''HR xizmatidan foydalanish func'''


class Employer_Info_State(StatesGroup):
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


async def employer_info_start_func(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Kompaniya to\'liq ismi  va faoliyatini kiriting.')
    await Employer_Info_State.company_name.set()


async def employer_company_name_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Ma\'sul xodimning ism-famailiyasini kiriting')


async def responsible_user_name_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['responsible_person_name'] = message.text
    await Employer_Info_State.next()
    await message.answer(
        "Telefon raqamingizni pastdagi tugma orqali kiriting. Yoki shablon orqali  kiriting:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num)


async def employer_phone_number_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await Employer_Info_State.next()
    await message.answer(text='Kerakli xodim')


async def employer_phone_number1_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['phone_number'] = phone_number
        else:
            await message.answer("Noto'g'ri formatdagi telefon raqamini kiritdingiz. Iltimos, qaytadan kiriting.")
            return
    await Employer_Info_State.next()
    await message.answer('Kerakli xodim')


async def employer_direct_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_direct'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Kerakli xodimlar sonini kiriting')


async def employer_number_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_number'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Xodimning vazifalarini kiriting')


async def employer_duty_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_duty'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Ish vaqtini kiriting')


async def work_time_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_time'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Talab qilinadigan ish tajribani kiriting')


async def employer_experience_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_experience'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Belgilangan maosh miqdori va to\'lash muddati')


async def employer_salary_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_salary'] = message.text
    await Employer_Info_State.next()
    await message.answer(text='Ish joyi manzilini kiriting')


employer_full_information = None


async def employer_vocation_func(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['working_vocation'] = message.text
    global employer_full_information
    employer_full_information = (
        f"🏢Kompaniya ismi  va faoliyati : {data['company_name']}"
        f"\n🤵Ma\'sul xodim ism-familiyasi: {data['responsible_person_name']}"
        f"\n☎Telefon raqam : {data['phone_number']}"
        f"\n🤵Kerakli xodim : {data['employer_direct']}\n🤵Kerakli  xodimlar soni : {data['employer_number']}"
        f"\n🤵Xodimning vazifasi : {data['employer_duty']}\nIsh vaqti : {data['work_time']}"
        f"\n🤵Talab qilinadigan ish tajriba : {data['employer_experience']}"
        f"\n💲Belgilangan maosh miqdori va to'lash muddati : {data['employer_salary']}"
        f"\n🏢Ish joyi manzili : {data['working_vocation']}")

    await bot.send_message(chat_id=message.chat.id, text=employer_full_information)
    await bot.send_message(chat_id=message.chat.id,
                           text='Ma\'lumotlaringizni tekshiring va pastdagi tugma orqali tasdiqlang.',
                           reply_markup=approval_but)
    await state.finish()


async def send_admin_HR_employer():
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


class Advertisement_Emloyer_Info_State(StatesGroup):
    staff_direct = State()
    staff_count = State()
    company_name = State()
    salary = State()
    work_vocation = State()
    employer_suggestion = State()
    employer_request = State()
    employer_phone_number = State()
    employer_comment = State()


async def advertisement_start(message: types.Message):
    await message.answer(text='Tanlang', reply_markup=advertisement_but)


async def advertisement_employer_start(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Kerakli xodim')
    await Advertisement_Emloyer_Info_State.staff_direct.set()


async def advertisement_employer_staff(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_direct'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Xodimlar sonini kiriting')


async def advertisement_employer_staff_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['staff_count'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Tashkilot nomi kiriting')


async def advertisement_employer_company(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Maoshni kiriting')


async def advertisement_employer_salary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['salary'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Manzilini kiriting')


async def advertisement_employer_vocation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work_vocation'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Taklif kiriting')


async def advertisement_employer_suggestion(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_suggestion'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Talablar kiriting')


async def advertisement_employer_request(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_request'] = message.text
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(
        "Telefon raqamingizni pastdagi tugma orqali kiriting. Yoki shablon orqali  kiriting:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num)


async def advertisement_employer_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employer_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyer_Info_State.next()
    await message.answer(text='Izoh kiriting')


async def advertisement_employer_phone_number1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employer_phone_number'] = phone_number
        else:
            await message.answer("Noto'g'ri formatdagi telefon raqamini kiritdingiz. Iltimos, qaytadan kiriting.")
            return
    await Advertisement_Emloyer_Info_State.next()
    await message.answer('Izoh kiriting')


advertisement_employer_full_information = None


async def advertisement_employer_comment(message: types.Message, state: FSMContext):
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
                           reply_markup=approval_but)
    await state.finish()


async def send_admin_advertisement_employer():
    group_chat_id = [-1002075927837]
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        for i in group_chat_id:
            await bot.send_photo(chat_id=i, photo=photo_content,
                                 caption=advertisement_employer_full_information,
                                 reply_markup=confirmation_admin)


async def send_channel_advertisement_employer():
    group_chat_id = -1002101580581
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employer_full_information)


# '========================================================================================================================================='

'''Elon joylash qismining Ishchi func'''


class Advertisement_Emloyee_Info_State(StatesGroup):
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


async def advertisement_employee_start(message: types.Message):
    global service_type
    service_type = message.text
    await message.answer(text='Mutaxassisligingizni kiriting')
    await Advertisement_Emloyee_Info_State.employee_specialty.set()


async def advertisement_employee_specialty(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_specialty'] = message.text
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(text='Tajribangizni kiriting')


async def advertisement_employee_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_experience'] = message.text
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(text='Til bilish darajangizni kiriting', reply_markup=language_level_button)


async def user_lang_list1(message: types.Message, state: FSMContext):
    language_buttons = {'Rus tili': rus_know_level_but_eng, 'Ingliz tili': english_know_level_but,
                        'Koreys tili': korea_know_level_but_eng, 'Xitoy tili': china_know_level_but,
                        'Nemis tili': english_know_level_but, 'Fransuz tili': english_know_level_but}

    async with state.proxy() as data:
        if 'employee_language_list' not in data:
            data['employee_language_list'] = []

        if message.text in language_buttons and message.text not in data['employee_language_list']:
            data['employee_language_list'].append(message.text)
            await message.answer(
                text=f'{message.text} siz oʻz tilingizni tanladingiz. Oʻzingiz bilgan boshqa tilni tanlang:',
                reply_markup=get_language_keyboard1(language_buttons))
        elif message.text == 'Keyingi':
            if not data['employee_language_list']:
                await message.answer(text='Xatolik. Til tanlanmagan')
                return
            global selected_languages_keyboard1
            selected_languages_keyboard1 = get_selected_languages_keyboard(data['employee_language_list'])
            await Advertisement_Emloyee_Info_State.next()
            await message.answer(text='Siz tanlagan tillar',
                                 reply_markup=selected_languages_keyboard1)

        elif message.text in language_buttons and message.text in data['employee_language_list']:
            await message.answer(text='Siz ushbu tilni tanlagansiz. Iltimos boshqa biladigan tilingizni tanlang.',
                                 reply_markup=language_level_button)
        else:
            await message.answer('Xatolik pastdagi tugma orqali kiriting')


def get_language_keyboard1(language_buttons):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language, button_callback in language_buttons.items():
        button = KeyboardButton(text=language)
        keyboard.insert(button)

    next_button = KeyboardButton(text='Keyingi')
    keyboard.insert(next_button)

    return keyboard


def get_selected_languages_keyboard1(selected_languages):
    keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for language in selected_languages:
        button = KeyboardButton(text=language)
        keyboard1.insert(button)

    next_button = KeyboardButton(text='Keyingi qadam')
    keyboard1.insert(next_button)
    return keyboard1


async def user_lang_know1(message: types.Message, state: FSMContext):
    language_buttons = {'Rus tili': rus_know_level_but, 'Ingliz tili': english_know_level_but,
                        'Koreys tili': korea_know_level_but, 'Xitoy tili': china_know_level_but,
                        'Nemis tili': english_know_level_but, 'Fransuz tili': english_know_level_but}

    async with state.proxy() as data:
        if 'employee_language_know' not in data:
            data['employee_language_know'] = []

    if message.text in language_buttons and message.text not in data['employee_language_know']:
        async with state.proxy() as data:
            data['employee_language_know'].append(message.text)
        await Advertisement_Emloyee_Info_State.next()
        await message.answer(text='Darajangizni tanlang', reply_markup=language_buttons[message.text])
    elif message.text == 'Keyingi qadam':
        if not data['employee_language_know']:
            await message.answer(text='Xatolik darajangizni tanlang')
        elif len(data['employee_language_level']) == len(data['employee_language_list']):
            await state.set_state(Advertisement_Emloyee_Info_State.employee_info)
            await message.answer(text='Ish qidirayotgan hudud')
        elif len(data['employee_language_level']) != len(data['employee_language_list']):
            await message.answer(text='Boshqa tillarda ham darajangizni tanlang.')
    elif message.text not in language_buttons:
        await message.answer(text='Xatolik. Pastdagi tugma orqali kiriting')
    elif message.text in data['employee_language_know']:
        await message.answer(text='Siz ushbu tilda o\'z darajangizni tanladingiz')


async def advertisement_employee_lang_level(message: types.Message, state: FSMContext):
    lang_levels = ['Topik1', 'Topik2', 'Topik3', 'Topik4', 'Topik5', 'Topik6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2',
                   'JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1', 'HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5',
                   'HSK 6', 'Bilmayman', 'Qoniqarli', 'Yaxshi', 'A\'lo']
    async with state.proxy() as data:
        if 'employee_language_level' not in data:
            data['employee_language_level'] = []

    if message.text in lang_levels:
        async with state.proxy() as data:
            data['employee_language_level'].append(message.text)
            await message.answer(text='Siz tanlagan tillar:',
                                 reply_markup=selected_languages_keyboard1)
            await state.set_state(Advertisement_Emloyee_Info_State.employee_language_know)
    else:
        await message.answer(text='Xatolik. Pastdagi tugma orqali kiriting')


async def advertisement_employee_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_info'] = message.text
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(text='Ish turi\nM-n : online / offline')


async def advertisement_employee_request(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_request'] = message.text
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(text='Manzil kiriting')


async def advertisement_employee_vocation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_work_vocation'] = message.text
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(
        "Telefon raqamingizni pastdagi tugma orqali kiriting. Yoki shablon orqali  kiriting:\n M-n:  +998 XX XXX XX XX",
        reply_markup=phone_num)


async def advertisement_employee_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employee_phone_number'] = message.contact.phone_number
    await Advertisement_Emloyee_Info_State.next()
    await message.answer(text='Izoh kiriting')


async def advertisement_employee_phone_number1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_number = message.text
        if validate_phone_number(phone_number):
            data['employee_phone_number'] = phone_number
        else:
            await message.answer("Noto'g'ri formatdagi telefon raqamini kiritdingiz. Iltimos, qaytadan kiriting.")
            return
    await Advertisement_Emloyee_Info_State.next()
    await message.answer('Izoh kiriting')


advertisement_employee_full_information = None


async def advertisement_employee_comment(message: types.Message, state: FSMContext):
    global images_list_employee
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
                           reply_markup=approval_but)

    await state.finish()


async def send_admin_advertisement_employee():
    group_chat_id = -1002075927837
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employee_full_information,
                             reply_markup=confirmation_admin)


async def send_channel_advertisement_employee():
    group_chat_id = -1002101580581
    image = 'images/darkor.png'
    with open(image, 'rb') as photo:
        photo_content = photo.read()
        await bot.send_photo(chat_id=group_chat_id, photo=photo_content,
                             caption=advertisement_employee_full_information)

# '=========================================================================================================='
