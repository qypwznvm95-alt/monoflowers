from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes
from config import LINKS

def create_start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔴 ▶️ PLAY", callback_data="start_main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🌐 Азов (АР)", url=LINKS['azov_website']),
            InlineKeyboardButton("🌐 Ростов-на-Дону (РО)", url=LINKS['rnd_website'])
        ],
        [
            InlineKeyboardButton("📱 Скачать приложение (iOS)", url=LINKS['mobile_app'])
        ],
        [
            InlineKeyboardButton("🛍️ Оформить заказ здесь", callback_data="place_order_here")
        ],
        [
            InlineKeyboardButton("📞 Связаться с менеджером", callback_data="contact_manager")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем видео/гиф с красной кнопкой PLAY
    try:
        # Пробуем отправить видео
        await update.message.reply_video(
            video=open('welcome_video.mp4', 'rb'),
            caption="💐 <b>MONOFLOWERS</b>\n\n⬇️ <b>НАЖМИ PLAY ЧТОБЫ ПЕРЕЙТИ В МЕНЮ</b> ⬇️",
            reply_markup=create_start_keyboard(),
            parse_mode='HTML'
        )
    except FileNotFoundError:
        # Если видео нет, пробуем гиф
        try:
            await update.message.reply_animation(
                animation=open('welcome.gif', 'rb'),
                caption="💐 <b>MONOFLOWERS</b>\n\n⬇️ <b>GIF автозапуск</b> ⬇️",
                reply_markup=create_start_keyboard(),
                parse_mode='HTML'
            )
        except FileNotFoundError:
            # Если нет ни видео ни гиф
            await update.message.reply_text(
                "💐 <b>MONOFLOWERS</b>\n\nНажмите PLAY чтобы начать",
                reply_markup=create_start_keyboard(),
                parse_mode='HTML'
            )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data == "start_main":
        # Главное меню после нажатия PLAY
        welcome_text = """
<b>MONOFLOWERS</b>

Группа проектов monoflowers / roseazov / roserostov / dorogobogato / 
сервис номер один по доставке цветов
расширяем географию / возможности / качество / ваш выбор

<b>ДЕЛАТЬ ШИКАРНО - НАШ ПРОФИЛЬ</b>

Выберите, что вас интересует:
        """
        
        # Удаляем предыдущее сообщение с медиа и отправляем новое
        await query.message.delete()
        await query.message.chat.send_message(
            welcome_text,
            reply_markup=create_main_keyboard(),
            parse_mode='HTML'
        )
    
    elif callback_data == "contact_manager":
        # Обработка кнопки "Связаться с менеджером"
        contact_text = """
<b>📞 Связь с менеджером</b>

Вы можете написать нам напрямую:
• Телефон: 8 918 899 90 04
• WhatsApp: wa.me/79188999004
• Telegram: @rose_azov

Мы ответим в ближайшее время! ⏰
        """
        
        contact_keyboard = [
            [
                InlineKeyboardButton("📞 Позвонить", url="tel:+79188999004"),
                InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/79188999004")
            ],
            [
                InlineKeyboardButton("✈️ Telegram", url="https://t.me/rose_azov"),
                InlineKeyboardButton("📧 Email", url="mailto:info@monoflowers.ru")
            ],
            [InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")]
        ]
        
        await query.edit_message_text(
            contact_text,
            reply_markup=InlineKeyboardMarkup(contact_keyboard),
            parse_mode='HTML'
        )
    
    elif callback_data == "place_order_here":
        order_text = "🎉 <b>Отлично! Вы выбрали оформление заказа здесь!</b>\n\nСейчас я помогу вам собрать идеальный букет.\n\n<b>Что бы вы хотели заказать?</b>"
        
        order_keyboard = [
            [InlineKeyboardButton("💐 Собрать букет", callback_data="build_bouquet")],
            [InlineKeyboardButton("🌹 Готовые букеты", callback_data="ready_bouquets")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")]
        ]
        
        await query.edit_message_text(
            order_text,
            reply_markup=InlineKeyboardMarkup(order_keyboard),
            parse_mode='HTML'
        )
    
    elif callback_data == "back_to_main":
        welcome_text = """
<b>MONOFLOWERS</b>

Группа проектов monoflowers / roseazov / roserostov / dorogobogato / 
сервис номер один по доставке цветов
расширяем географию / возможности / качество / ваш выбор

<b>ДЕЛАТЬ ОЧКАК - НАШ ПРОФИЛЬ</b>

Выберите, что вас интересует:
        """
        await query.edit_message_text(
            welcome_text,
            reply_markup=create_main_keyboard(),
            parse_mode='HTML'
        )
    
    elif callback_data in ["build_bouquet", "ready_bouquets"]:
        await query.edit_message_text(
            "🚀 <b>Эта функция скоро будет доступна!</b>\n\nА пока вы можете:\n• Перейти в наш Telegram-магазин\n• Посмотреть каталог на сайте\n• Связаться с менеджером",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="place_order_here")],
                [InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main")]
            ]),
            parse_mode='HTML'
        )
