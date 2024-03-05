from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from aiogram.utils.exceptions import MessageToDeleteNotFound

from Token import db, bot
from english.keyboard_eng import services_type_eng, inline_keyboard_eng
from english.user_info_eng import services_start_eng, advertisement_start_eng, send_admin_advertisement_employee_eng, \
    send_admin_advertisement_employer_eng, send_admin_employee_eng, send_admin_HR_employer_eng, \
    send_channel_advertisement_employee_eng, send_channel_advertisement_employer_eng, back_func_eng, \
    user_info_start_eng, UserInfoEng, user_name_eng, user_year_eng, user_phone_number_eng, user_phone_number1_eng, \
    user_specialty_eng, user_info_eng, user_experience_eng, user_lang_list_eng, user_lang_know_eng, \
    user_certificate_eng, user_lang_level_eng, \
    certificate_image_eng, user_address_eng, user_image_eng, user_comment_eng, employer_info_start_func_eng, \
    Employer_Info_State_Eng, employer_company_name_func_eng, responsible_user_name_func_eng, \
    employer_phone_number_func_eng, employer_phone_number1_func_eng, employer_direct_func_eng, employer_duty_func_eng, \
    work_time_func_eng, employer_experience_func_eng, employer_salary_func_eng, employer_vocation_func_eng, \
    advertisement_employer_start_eng, Advertisement_Emloyer_Info_State_Eng, advertisement_employer_staff_eng, \
    advertisement_employer_company_eng, advertisement_employer_salary_eng, advertisement_employer_vocation_eng, \
    advertisement_employer_suggestion_eng, advertisement_employer_request_eng, advertisement_employer_phone_number_eng, \
    advertisement_employer_phone_number1_eng, advertisement_employer_comment_eng, advertisement_employee_start_eng, \
    Advertisement_Emloyee_Info_State_Eng, advertisement_employee_specialty_eng, advertisement_employee_experience_eng, \
    advertisement_employee_phone_number1_eng, advertisement_employee_info_eng, \
    advertisement_employee_request_eng, advertisement_employee_vocation_eng, advertisement_employee_phone_number_eng, \
    advertisement_employee_comment_eng, \
    employer_number_func_eng, employee_lang_level_eng1, employee_lang_list_eng1, employee_lang_know_eng1, \
    advertisement_employer_staff_count_eng
from rus.keyboard_rus import services_type_rus, inline_keyboard_rus
from rus.user_info_rus import send_admin_advertisement_employee_rus, send_admin_advertisement_employer_rus, \
    send_admin_employee_rus, send_admin_HR_employer_rus, back_func_rus, services_start_rus, user_info_start_rus, \
    UserInfoRus, user_name_rus, user_year_rus, user_phone_number_rus, user_phone_number1_rus, user_specialty_rus, \
    user_info_rus, user_experience_rus, user_lang_list_rus, user_lang_know_rus, user_lang_level_rus, \
    user_certificate_rus, certificate_image_rus, user_address_rus, user_image_rus, user_comment_rus, \
    employer_info_start_func_rus, Employer_Info_State_Rus, employer_company_name_func_rus, \
    responsible_user_name_func_rus, employer_phone_number_func_rus, employer_phone_number1_func_rus, \
    employer_direct_func_rus, employer_number_func_rus, employer_duty_func_rus, work_time_func_rus, \
    employer_experience_func_rus, employer_salary_func_rus, employer_vocation_func_rus, \
    advertisement_employer_start_rus, Advertisement_Emloyer_Info_State_Rus, advertisement_employer_staff_rus, \
    advertisement_employer_company_rus, advertisement_employer_salary_rus, advertisement_employer_vocation_rus, \
    advertisement_employer_suggestion_rus, advertisement_employer_request_rus, advertisement_employer_phone_number_rus, \
    advertisement_employer_phone_number1_rus, advertisement_employer_comment_rus, advertisement_employee_start_rus, \
    Advertisement_Emloyee_Info_State_Rus, advertisement_employee_specialty_rus, advertisement_employee_experience_rus, \
    advertisement_employee_lang_list_rus, advertisement_employee_lang_know_rus, \
    advertisement_employee_info_rus, \
    advertisement_employee_request_rus, advertisement_employee_vocation_rus, advertisement_employee_phone_number_rus, \
    advertisement_employee_phone_number1_rus, advertisement_employee_comment_rus, advertisement_start_rus, \
    send_channel_advertisement_employee_rus, send_channel_advertisement_employer_rus, \
    advertisement_employee_lang_level_rus, advertisement_employer_staff_count_rus
from total_keyboard import language
from uzb.keyboard_uz import services_type_uz, inline_keyboard
from uzb.user_info_uzb import send_admin_employee, send_admin_HR_employer, send_channel_advertisement_employer, \
    user_lang_know, user_certificate, certificate_image, user_lang_list, UserInfoUzb, user_lang_list1, \
    user_lang_know1, advertisement_employee_lang_level, advertisement_employer_staff_count
from uzb.user_info_uzb import services_start, user_info_start, user_name, user_year, user_phone_number, \
    user_phone_number1, user_specialty, user_info, user_experience, user_lang_level, user_address, \
    user_comment, user_image, employer_info_start_func, Employer_Info_State, employer_company_name_func, \
    responsible_user_name_func, employer_number_func, employer_phone_number_func, employer_phone_number1_func, \
    employer_direct_func, employer_duty_func, work_time_func, employer_experience_func, employer_salary_func, \
    employer_vocation_func, advertisement_start, Advertisement_Emloyer_Info_State, advertisement_employer_staff, \
    advertisement_employer_company, advertisement_employer_salary, advertisement_employer_vocation, \
    advertisement_employer_suggestion, advertisement_employer_request, advertisement_employer_phone_number, \
    advertisement_employer_phone_number1, advertisement_employer_comment, advertisement_employer_start, \
    advertisement_employee_start, Advertisement_Emloyee_Info_State, advertisement_employee_specialty, \
    advertisement_employee_experience, advertisement_employee_info, \
    advertisement_employee_request, advertisement_employee_vocation, advertisement_employee_phone_number, \
    advertisement_employee_phone_number1, advertisement_employee_comment, back_func, \
    send_channel_advertisement_employee, send_admin_advertisement_employer, send_admin_advertisement_employee


@db.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Tilni tanlang', reply_markup=language)


@db.message_handler(lambda message: message.text in ['🇺🇿Uzbek'])
async def uzb_start(message: types.Message):
    await message.answer(text='Xizmat turini tanlang', reply_markup=services_type_uz)


@db.message_handler(lambda message: message.text == 'Ishchi Topish')
async def handle_message(message: types.Message):
    await services_start(message)


@db.message_handler(lambda message: message.text == 'Ochiq ishchilar bazasini ko\'rish')
async def handle_message(message: types.Message):
    await message.answer(text='Saytga o\'tish', reply_markup=inline_keyboard)


@db.message_handler(lambda message: message.text == 'E\'lon joylash')
async def handle_message(message: types.Message):
    await advertisement_start(message)


@db.message_handler(lambda message: message.text == 'Tasdiqlash')
async def handle_message(message: types.Message, state: FSMContext):
    if services == 'Ishchi':
        await send_admin_advertisement_employee()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ma\'lumotlaringiz qabul qilindi.')
    elif services == 'Ish beruvchi':
        await send_admin_advertisement_employer()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ma\'lumotlaringiz qabul qilindi.')
    elif services == 'Ish Topish':
        await send_admin_employee()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ma\'lumotlaringiz qabul qilindi.')
    elif services == 'HR xizmatidan foydalanish':
        await send_admin_HR_employer()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ma\'lumotlaringiz qabul qilindi.')


@db.callback_query_handler(lambda query: query.data in ['confirm', 'cancel'])
async def process_confirmation_callback(query: types.CallbackQuery):
    chat_id_group = -1002075927837
    user_choice = query.data
    try:
        if user_choice == 'confirm':
            if services == 'Ishchi':
                await send_channel_advertisement_employee()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Ma'lumotlar kanalga jo'natildi."
                await bot.send_message(chat_id_group, text=confirmation_text)
            elif services == 'Ish beruvchi':
                await send_channel_advertisement_employer()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Ma'lumotlar kanalga jo'natildi."
                await bot.send_message(chat_id_group, text=confirmation_text)
        elif user_choice == 'cancel':
            await bot.delete_message(chat_id_group, query.message.message_id)
            user_id = query.from_user.id
            cancel_confirmation_text = "Sizning arizangiz qabul qilinmadi, iltimos qayta urinib ko'ring"
            await bot.send_message(user_id, text=cancel_confirmation_text)
    except MessageToDeleteNotFound:
        pass


# Delete


@db.message_handler(lambda message: message.text in ['🔚Ortga', '⬅Ortga', 'O\'zgartirish'])
async def handle_message(message: types.Message):
    await back_func(message)


# '============================================================================================================='

''' Ish Topish qismi'''

services = None


@db.message_handler(lambda message: message.text == 'Ish Topish')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await user_info_start(message)


@db.message_handler(state=UserInfoUzb.name)
async def handle_message(message: types.Message, state: FSMContext):
    await user_name(message, state)


@db.message_handler(state=UserInfoUzb.user_year)
async def handle_message(message: types.Message, state: FSMContext):
    await user_year(message, state)


@db.message_handler(state=UserInfoUzb.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number(message, state)


@db.message_handler(state=UserInfoUzb.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number1(message, state)


@db.message_handler(state=UserInfoUzb.specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await user_specialty(message, state)


@db.message_handler(state=UserInfoUzb.info)
async def handle_message(message: types.Message, state: FSMContext):
    await user_info(message, state)


@db.message_handler(state=UserInfoUzb.experience)
async def handle_message(message: types.Message, state: FSMContext):
    await user_experience(message, state)


@db.message_handler(state=UserInfoUzb.know_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_list(message, state)


@db.message_handler(state=UserInfoUzb.know_language)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_know(message, state)


@db.message_handler(state=UserInfoUzb.language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_level(message, state)


@db.message_handler(state=UserInfoUzb.certificate_yes_no)
async def handle_message(message: types.Message, state: FSMContext):
    await user_certificate(message, state)


@db.message_handler(state=UserInfoUzb.certificate_image, content_types=types.ContentTypes.PHOTO)
async def handle_certificate_image(message: types.Message, state: FSMContext):
    if message.photo:
        await certificate_image(message, state)
    else:
        await message.answer("Please provide a photo. You didn't attach a picture.")


@db.message_handler(state=UserInfoUzb.address)
async def handle_message(message: types.Message, state: FSMContext):
    await user_address(message, state)


@db.message_handler(content_types=types.ContentTypes.PHOTO, state=UserInfoUzb.image)
async def handle_message(message: types.Message, state: FSMContext):
    if message.photo:
        await user_image(message, state)
    else:
        await message.answer(text='Xatolik.Rasm kiritng')


@db.message_handler(state=UserInfoUzb.comment)
async def handle_message(message: types.Message, state: FSMContext):
    await user_comment(message, state)


# '==========================================================================================================='


''' HR  xizmatidan  foydalanish qismi '''


@db.message_handler(lambda message: message.text == 'HR xizmatidan foydalanish')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await employer_info_start_func(message)


@db.message_handler(state=Employer_Info_State.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_company_name_func(message, state)


@db.message_handler(state=Employer_Info_State.responsible_person_name)
async def handle_message(message: types.Message, state: FSMContext):
    await responsible_user_name_func(message, state)


@db.message_handler(state=Employer_Info_State.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number_func(message, state)


@db.message_handler(state=Employer_Info_State.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number1_func(message, state)


@db.message_handler(state=Employer_Info_State.employer_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_direct_func(message, state)


@db.message_handler(state=Employer_Info_State.employer_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_number_func(message, state)


@db.message_handler(state=Employer_Info_State.employer_duty)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_duty_func(message, state)


@db.message_handler(state=Employer_Info_State.work_time)
async def handle_message(message: types.Message, state: FSMContext):
    await work_time_func(message, state)


@db.message_handler(state=Employer_Info_State.employer_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_experience_func(message, state)


@db.message_handler(state=Employer_Info_State.employer_salary)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_salary_func(message, state)


@db.message_handler(state=Employer_Info_State.working_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_vocation_func(message, state)


# '==================================================================================================================================='

''' Elon joylash qismining Ish beruvchi to'ldiradigan qismi '''


@db.message_handler(lambda message: message.text == 'Ish beruvchi')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employer_start(message)


@db.message_handler(state=Advertisement_Emloyer_Info_State.staff_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.staff_count)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff_count(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_company(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.salary)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_salary(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_vocation(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.employer_suggestion)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_suggestion(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.employer_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_request(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.employer_phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.employer_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number1(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State.employer_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_comment(message, state)


# '==================================================================================================================================='


''' Elon joylash qismining Ishchi to'ldiradigan qismi '''


@db.message_handler(lambda message: message.text == 'Ishchi')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employee_start(message)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_specialty(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_experience(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_lang_level(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_list1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_language_know)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_know1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_info)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_info(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_request(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_vocation(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State.employee_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_comment(message, state)


# '==============================================================================================================================='


'''English part'''


@db.message_handler(lambda message: message.text in ['🇺🇸English'])
async def uzb_start(message: types.Message):
    await message.answer(text='Choose the services type', reply_markup=services_type_eng)


@db.message_handler(lambda message: message.text == 'Find a stuff')
async def handle_message(message: types.Message):
    await services_start_eng(message)


@db.message_handler(lambda message: message.text == 'View the list of open workers')
async def handle_message(message: types.Message):
    await message.answer(text='Go to the site', reply_markup=inline_keyboard_eng)


@db.message_handler(lambda message: message.text == 'Post an ad')
async def handle_message(message: types.Message):
    await advertisement_start_eng(message)


@db.message_handler(lambda message: message.text == 'Confirmation')
async def handle_message(message: types.Message):
    if services == 'Employee':
        await send_admin_advertisement_employee_eng()
        await bot.send_message(chat_id=message.chat.id,
                               text='Your information has been received.')
    elif services == 'Employer':
        await send_admin_advertisement_employer_eng()
        await bot.send_message(chat_id=message.chat.id,
                               text='Your information has been received.')
    elif services == 'Find a job':
        await send_admin_employee_eng()
        await bot.send_message(chat_id=message.chat.id,
                               text='Your information has been received.')
    elif services == 'Use of HR service':
        await send_admin_HR_employer_eng()
        await bot.send_message(chat_id=message.chat.id,
                               text='Your information has been received.')


@db.callback_query_handler(lambda query: query.data in ['confirm_eng', 'cancel_eng'])
async def process_confirmation_callback(query: types.CallbackQuery):
    chat_id_group = -1002075927837
    user_choice = query.data
    try:
        if user_choice == 'confirm_eng':
            if services == 'Employee':
                await send_channel_advertisement_employee_eng()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Data has been sent to the channel."
                await bot.send_message(chat_id_group, text=confirmation_text)
            elif services == 'Employer':
                await send_channel_advertisement_employer_eng()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Data has been sent to the channel."
                await bot.send_message(chat_id_group, text=confirmation_text)
        elif user_choice == 'cancel_eng':
            await bot.delete_message(chat_id_group, query.message.message_id)
            user_id = query.from_user.id
            cancel_confirmation_text = "Your application was not accepted, please try again"
            await bot.send_message(user_id, text=cancel_confirmation_text)
    except MessageToDeleteNotFound:
        pass


@db.message_handler(lambda message: message.text in ['🔚Back', '⬅Back', 'Cancellation'])
async def handle_message(message: types.Message):
    await back_func_eng(message)


# '============================================================================================================================================================='

''' Find a job'''


@db.message_handler(lambda message: message.text == 'Find a job')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await user_info_start_eng(message)


@db.message_handler(state=UserInfoEng.name)
async def handle_message(message: types.Message, state: FSMContext):
    await user_name_eng(message, state)


@db.message_handler(state=UserInfoEng.user_year)
async def handle_message(message: types.Message, state: FSMContext):
    await user_year_eng(message, state)


@db.message_handler(state=UserInfoEng.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number_eng(message, state)


@db.message_handler(state=UserInfoEng.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number1_eng(message, state)


@db.message_handler(state=UserInfoEng.specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await user_specialty_eng(message, state)


@db.message_handler(state=UserInfoEng.info)
async def handle_message(message: types.Message, state: FSMContext):
    await user_info_eng(message, state)


@db.message_handler(state=UserInfoEng.experience)
async def handle_message(message: types.Message, state: FSMContext):
    await user_experience_eng(message, state)


@db.message_handler(state=UserInfoEng.know_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_list_eng(message, state)


@db.message_handler(state=UserInfoEng.know_language)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_know_eng(message, state)


@db.message_handler(state=UserInfoEng.language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_level_eng(message, state)


@db.message_handler(state=UserInfoEng.certificate_yes_no)
async def handle_message(message: types.Message, state: FSMContext):
    await user_certificate_eng(message, state)


@db.message_handler(state=UserInfoEng.certificate_image, content_types=types.ContentTypes.PHOTO)
async def handle_message(message: types.Message, state: FSMContext):
    if message.photo:
        await certificate_image_eng(message, state)
    else:
        await message.answer(text='Error.Image enter')


@db.message_handler(state=UserInfoEng.address)
async def handle_message(message: types.Message, state: FSMContext):
    await user_address_eng(message, state)


@db.message_handler(content_types=types.ContentTypes.PHOTO, state=UserInfoEng.image)
async def handle_message(message: types.Message, state: FSMContext):
    if message.photo:
        await user_image_eng(message, state)
    else:
        await message.answer(text='Error.Image enter')


@db.message_handler(state=UserInfoEng.comment)
async def handle_message(message: types.Message, state: FSMContext):
    await user_comment_eng(message, state)


# '============================================================================================================================='


''' Use of HR service '''


@db.message_handler(lambda message: message.text == 'Use of HR service')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await employer_info_start_func_eng(message)


@db.message_handler(state=Employer_Info_State_Eng.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_company_name_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.responsible_person_name)
async def handle_message(message: types.Message, state: FSMContext):
    await responsible_user_name_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number1_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.employer_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_direct_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.employer_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_number_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.employer_duty)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_duty_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.work_time)
async def handle_message(message: types.Message, state: FSMContext):
    await work_time_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.employer_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_experience_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.employer_salary)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_salary_func_eng(message, state)


@db.message_handler(state=Employer_Info_State_Eng.working_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_vocation_func_eng(message, state)


# '==================================================================================================================================='

''' The Employer fills out the part of the advertisement '''


@db.message_handler(lambda message: message.text == 'Employer')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employer_start_eng(message)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.staff_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.staff_count)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff_count_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_company_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.salary)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_salary_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_vocation_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.employer_suggestion)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_suggestion_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.employer_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_request_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.employer_phone_number,
                    content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.employer_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number1_eng(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Eng.employer_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_comment_eng(message, state)


# '==================================================================================================================================='


''' Elon joylash qismining Ishchi  to'ldiradigan qismi '''


@db.message_handler(lambda message: message.text == 'Employee')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employee_start_eng(message)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_specialty_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_experience_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await employee_lang_level_eng1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await employee_lang_list_eng1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_language_know)
async def handle_message(message: types.Message, state: FSMContext):
    await employee_lang_know_eng1(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_info)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_info_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_request_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_vocation_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_phone_number,
                    content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number1_eng(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Eng.employee_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_comment_eng(message, state)


# '=================================================================================================================================================='

'''Russia part'''


@db.message_handler(lambda message: message.text == 'Подтверждение')
async def handle_message(message: types.Message):
    if services == 'Сотрудник':
        await send_admin_advertisement_employee_rus()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ваша информация получена.')
    elif services == 'Работодатель':
        await send_admin_advertisement_employer_rus()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ваша информация получена.')
    elif services == 'Найти работу':
        await send_admin_employee_rus()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ваша информация получена.')
    elif services == 'Использование HR-сервиса':
        await send_admin_HR_employer_rus()
        await bot.send_message(chat_id=message.chat.id,
                               text='Ваша информация получена.')


@db.message_handler(lambda message: message.text in ['🔚Назад', '⬅Назад', 'Отмена'])
async def handle_message(message: types.Message):
    await back_func_rus(message)


@db.message_handler(lambda message: message.text in ['🇷🇺Russia'])
async def uzb_start(message: types.Message):
    await message.answer(text='Выберите тип услуги', reply_markup=services_type_rus)


@db.message_handler(lambda message: message.text == 'Найти сотрудника')
async def handle_message(message: types.Message):
    await services_start_rus(message)


@db.message_handler(lambda message: message.text == 'Посмотреть список открытых сотрудников')
async def handle_message(message: types.Message):
    await message.answer(text='Перейти на сайт', reply_markup=inline_keyboard_rus)


@db.message_handler(lambda message: message.text == 'Разместить объявление')
async def handle_message(message: types.Message):
    await advertisement_start_rus(message)


@db.callback_query_handler(lambda query: query.data in ['confirm_rus', 'cancel_rus'])
async def process_confirmation_callback(query: types.CallbackQuery):
    chat_id_group = -1002075927837
    user_choice = query.data
    try:
        if user_choice == 'confirm_rus':
            if services == 'Сотрудник':
                await send_channel_advertisement_employee_rus()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Данные отправлены в канал."
                await bot.send_message(chat_id_group, text=confirmation_text)
            elif services == 'Работодатель':
                await send_channel_advertisement_employer_rus()
                await bot.delete_message(chat_id_group, query.message.message_id)
                confirmation_text = "Данные отправлены в канал."
                await bot.send_message(chat_id_group, text=confirmation_text)
        elif user_choice == 'cancel_rus':
            await bot.delete_message(chat_id_group, query.message.message_id)
            user_id = query.from_user.id
            cancel_confirmation_text = "Ваша заявка не принята, попробуйте еще раз"
            await bot.send_message(user_id, text=cancel_confirmation_text)
    except MessageToDeleteNotFound:
        pass


# '============================================================================================================================================================='

''' Find a job rus'''


@db.message_handler(lambda message: message.text == 'Найти работу')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await user_info_start_rus(message)


@db.message_handler(state=UserInfoRus.name)
async def handle_message(message: types.Message, state: FSMContext):
    await user_name_rus(message, state)


@db.message_handler(state=UserInfoRus.user_year)
async def handle_message(message: types.Message, state: FSMContext):
    await user_year_rus(message, state)


@db.message_handler(state=UserInfoRus.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number_rus(message, state)


@db.message_handler(state=UserInfoRus.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await user_phone_number1_rus(message, state)


@db.message_handler(state=UserInfoRus.specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await user_specialty_rus(message, state)


@db.message_handler(state=UserInfoRus.info)
async def handle_message(message: types.Message, state: FSMContext):
    await user_info_rus(message, state)


@db.message_handler(state=UserInfoRus.experience)
async def handle_message(message: types.Message, state: FSMContext):
    await user_experience_rus(message, state)


@db.message_handler(state=UserInfoRus.know_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_list_rus(message, state)


@db.message_handler(state=UserInfoRus.know_language)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_know_rus(message, state)


@db.message_handler(state=UserInfoRus.language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await user_lang_level_rus(message, state)


@db.message_handler(state=UserInfoRus.certificate_yes_no)
async def handle_message(message: types.Message, state: FSMContext):
    await user_certificate_rus(message, state)


@db.message_handler(state=UserInfoRus.certificate_image, content_types=types.ContentTypes.PHOTO)
async def handle_message(message: types.Message, state: FSMContext):
    if message.photo:
        await certificate_image_rus(message, state)
    else:
        await message.answer(text='Xatolik')


@db.message_handler(state=UserInfoRus.address)
async def handle_message(message: types.Message, state: FSMContext):
    await user_address_rus(message, state)


@db.message_handler(content_types=types.ContentTypes.PHOTO, state=UserInfoRus.image)
async def handle_message(message: types.Message, state: FSMContext):
    if message.photo:
        await user_image_rus(message, state)
    else:
        await message.answer(text='Xatolik')


@db.message_handler(state=UserInfoRus.comment)
async def handle_message(message: types.Message, state: FSMContext):
    await user_comment_rus(message, state)


# '============================================================================================================================='


''' Use of HR service '''


@db.message_handler(lambda message: message.text == 'Использование HR-сервиса')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await employer_info_start_func_rus(message)


@db.message_handler(state=Employer_Info_State_Rus.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_company_name_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.responsible_person_name)
async def handle_message(message: types.Message, state: FSMContext):
    await responsible_user_name_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.phone_number, content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_phone_number1_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.employer_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_direct_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.employer_number)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_number_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.employer_duty)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_duty_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.work_time)
async def handle_message(message: types.Message, state: FSMContext):
    await work_time_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.employer_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_experience_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.employer_salary)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_salary_func_rus(message, state)


@db.message_handler(state=Employer_Info_State_Rus.working_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await employer_vocation_func_rus(message, state)


# '==================================================================================================================================='

''' The Employer fills out the part of the advertisement '''


@db.message_handler(lambda message: message.text == 'Работодатель')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employer_start_rus(message)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.staff_direct)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.staff_count)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_staff_count_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.company_name)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_company_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.salary)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_salary_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_vocation_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.employer_suggestion)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_suggestion_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.employer_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_request_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.employer_phone_number,
                    content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.employer_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_phone_number1_rus(message, state)


@db.message_handler(state=Advertisement_Emloyer_Info_State_Rus.employer_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employer_comment_rus(message, state)


# '==================================================================================================================================='


''' Elon joylash qismining Ishchi  to'ldiradigan qismi rus '''


@db.message_handler(lambda message: message.text == 'Сотрудник')
async def handle_message(message: types.Message):
    global services
    services = message.text
    await advertisement_employee_start_rus(message)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_specialty)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_specialty_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_experience)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_experience_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_language_level)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_lang_level_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_language_list)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_lang_list_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_language_know)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_lang_know_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_info)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_info_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_request)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_request_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_work_vocation)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_vocation_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_phone_number,
                    content_types=ContentTypes.CONTACT)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_phone_number)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_phone_number1_rus(message, state)


@db.message_handler(state=Advertisement_Emloyee_Info_State_Rus.employee_comment)
async def handle_message(message: types.Message, state: FSMContext):
    await advertisement_employee_comment_rus(message, state)


@db.message_handler()
async def echo(message: types.Message):
    await message.answer(
        text='Bizda bunday buyruq mavjud emas.   /    У нас нет такoгo приказа.  /   We do not have such an order.',
        reply=message.text)


async def on_startup(db):
    print("Bot has started")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(db, on_startup=on_startup, skip_updates=True)
