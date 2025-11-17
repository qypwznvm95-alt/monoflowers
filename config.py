import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

LINKS = {
    'azov_website': 'https://azov.monoflowers.ru',
    'rnd_website': 'https://rnd.monoflowers.ru', 
    'telegram_shop': 'https://t.me/monoflowerss_bot?profile',
    'mobile_app': 'https://apps.apple.com/app/id6742648513',
    'place_order': 'order'
}
