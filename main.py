import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# masukan api key dan api token yang di butuhkan
openai.api_key = "isi api key akun openai"
bot = AsyncTeleBot('isi api token bot telegram')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Halo salam kenal dengan saya jono,ada yang bisa saya bantu?\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())
