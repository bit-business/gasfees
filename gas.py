import asyncio
import requests
import telegram

async def send_telegram_message(bot_token, chat_id, message):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

def check_gas_price():
    response = requests.get('https://explorer-v1.mxc.com/api/v2/stats')
    data = response.json()
    return data['gas_prices']['slow']

async def main():
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    threshold = 40000000

    slow_gas_price = check_gas_price()
    if slow_gas_price < threshold:
        await send_telegram_message(bot_token, chat_id, f'Gas Price Alert: {slow_gas_price}')

if __name__ == '__main__':
    asyncio.run(main())
