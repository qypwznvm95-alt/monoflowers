from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes
from config import LINKS

def create_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🌐 Азов (АР)", url=LINKS['azov_website']),
            InlineKeyboardButton("🌐 Ростов-на-Дону (РО)", url=LINKS['rnd_website'])
        ],
        [
            InlineKeyboardButton("🤖 Оформить заказ в Telegram", url=LINKS['telegram_shop'])
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
    welcome_text = """
🌸 *Добро пожаловать в monoflowers!* 🌸

Мы создаём прекрасные букеты с доставкой в Азове и Ростове-на-Дону.

Выберите, что вас интересует:
• 🌐 *Сайты магазинов* - посмотрите наши работы и акции
• 🤖 *Оформить заказ* - умный помощник соберёт идеальный букет
• 📱 *Мобильное приложение* - заказывайте еще удобнее
• 🛍️ *Оформить заказ здесь* - начните оформление в этом чате

*Доставка цветов — это наша страсть!* 💐
    """
    
    keyboard = create_main_keyboard()
    
    if update.message:
        await update.message.reply_text(
            welcome_text, 
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    else:
        await update.callback_query.message.reply_text(
            welcome_text,
            reply_markup=keyboard,
            parse_mode='Markdown'
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data == "place_order_here":
        order_text = "🎉 *Отлично! Вы выбрали оформление заказа здесь!*\n\nСейчас я помогу вам собрать идеальный букет.\n\n*Что бы вы хотели заказать?*"
        
        order_keyboard = [
            [InlineKeyboardButton("💐 Собрать букет", callback_data="build_bouquet")],
            [InlineKeyboardButton("🌹 Готовые букеты", callback_data="ready_bouquets")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")]
        ]
        
        await query.edit_message_text(
            order_text,
            reply_markup=InlineKeyboardMarkup(order_keyboard),
            parse_mode='Markdown'
        )
    
    elif callback_data == "contact_manager":
        contact_text = """
📞 *Связь с менеджером*

Вы можете написать нам напрямую:
• Телефон: +7 918 899-90-06
• WhatsApp: wa.me/79188999006
• Telegram: @rose_azov

Мы ответим в ближайшее время! ⏰
        """
        
        contact_keyboard = [
            [
                InlineKeyboardButton("📞 Позвонить", url="tel:+79188999006"),
                InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/79188999006")
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
            parse_mode='Markdown'
        )
    
    elif callback_data == "back_to_main":
        await start(update, context)
    
    elif callback_data in ["build_bouquet", "ready_bouquets"]:
        await query.edit_message_text(
            "🚀 *Эта функция скоро будет доступна!*\n\nА пока вы можете:\n• Перейти в наш Telegram-магазин\n• Посмотреть каталог на сайте\n• Связаться с менеджером",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="place_order_here")],
                [InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main")]
            ]),
            parse_mode='Markdown'
        )
