import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота из .env файла
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Ссылки для кнопок
LINKS = {
    'azov_website': 'https://azov.monoflowers.ru',
    'rnd_website': 'https://rnd.monoflowers.ru', 
    'telegram_shop': 'https://t.me/monoflowerss_bot?start=shop',
    'mobile_app': 'https://apps.apple.com/app/id6742648513',
    'place_order': 'order'  # Для команды заказа
}
