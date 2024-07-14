from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7335411399:AAFIqx2qxCDNUy6rQpPvnLHqBOsG-Ytrr0M')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб-страницу', web_app=WebAppInfo(url='https://artem-mutaf.github.io/Tele3/')))
    await message.answer('Привет, мой дорогой друг!', reply_markup=markup)


#@dp.message_handler(content_types=['photo']) #Можно принимать значения
#async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    #await message.answer('Hello')
    #await message.reply('Hello') # Вывод сообщения с ответом
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)

#@dp.message_handler(commands=['inline'])
#async def info(message: types.Message):
    #markup = types.InlineKeyboardMarkup() # Для создания кнопок
    # Добавление кнопки с сайтом
    #markup.add(types.InlineKeyboardButton('Site', url='https://www.bmw.com/en/index.html'))
    #markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    #await message.reply('Hello', reply_markup=markup)

#@dp.callback_query_handler()
#async def callback(call):
    #await call.message.answer(call.data)

#@dp.message_handler(commands=['reply'])
#async def reply(message: types.Message):
 #   markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) # one_time_keyboard=True кнопки будут показаны только один раз
  #  markup.add(types.InlineKeyboardButton('Site'))
   # markup.add(types.InlineKeyboardButton('Website'))
    #await message.answer('Hello', reply_markup=markup)




executor.start_polling(dp)