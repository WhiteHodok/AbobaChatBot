import aiogram
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="-")
dp = Dispatcher(bot)
openai.api_key = "-"
def openai_request(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "Здравствуйте! Я бот, который может помочь вам с чем-то. Напишите ваш вопрос и я постараюсь ответить на него. Чтобы начать, нажмите кнопку Start.")
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # Отправляем пользователю сообщение о начале работы
    await bot.send_message(message.chat.id, "Здесь вы можете задавать вопросы связанные с чем-то. Напишите любой вопрос и я постараюсь на него ответить.")
# Обрабатываем сообщения от пользователя
@dp.message_handler()
async def handle_message(msg: types.Message):
    # Передаем сообщение пользователя в OpenAI API
    response = openai_request(msg.text)
    # Отправляем ответ пользователю
    await bot.send_message(msg.chat.id, response)
# Обработчик приветственного сообщения, который будет вызываться при первом заходе пользователя в бота
dp.register_message_handler(send_welcome, commands="start")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
