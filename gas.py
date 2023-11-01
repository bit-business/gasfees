import requests
import telegram
import os

def send_telegram_message(bot_token, chat_id, message):
    try:
        bot = telegram.Bot(token=bot_token)
        bot.sendMessage(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Error sending message: {e}")

def check_gas_price():
    try:
        response = requests.get('https://explorer-v1.mxc.com/api/v2/stats')
        data = response.json()
        return data['gas_prices']['slow']
    except Exception as e:
        print(f"Error fetching gas price: {e}")
        return None

def main():
    try:
        bot_token = os.environ['TELEGRAM_BOT_TOKEN']
        chat_id = os.environ['TELEGRAM_CHAT_ID']
        threshold = 4000000

        slow_gas_price = check_gas_price()
        if slow_gas_price and slow_gas_price < threshold:
            send_telegram_message(bot_token, chat_id, f'MXC SMALL GAS PRICE: {slow_gas_price}')
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()
