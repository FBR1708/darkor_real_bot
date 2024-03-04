from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# TOKEN = '6922587117:AAGNdeyAghymZ66GaVkt5EAuBmCqV0doPIo'
TOKEN = '7137067696:AAGqhGEmz2Q4WQ1WjWafpmI__Aunkud9kvY'
bot = Bot(token=TOKEN)
db = Dispatcher(bot, storage=MemoryStorage())
db.middleware.setup(LoggingMiddleware())
