import telebot
from flask import Flask, request

TOKEN = "8345034042:AAH_JVfkFlX0lAwuz9vB8MP129dZH_QVcm8"
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)


#comandos
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! Bienvenido a taquería El Volcán, escribe /help para saber en qué te puedo ayudar.')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
        '/menu - Muestra el menú\n'
        '/horario - Horario de atención\n'
        '/ubicacion - Dirección del local\n'
        '/telefono - Número telefónico'
    )

@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.reply_to(message,
        '-Comidas\n'
        'Tacos de Asada: $28 c/u\n'
        'Tacos al Pastor: $25 c/u\n'
        'Tacos de Birria (con consomé): $45\n'
        'Quesadilla de Arrachera: $75\n'
        'Gringa al Pastor: $65\n'
        'Vampiro de Sirloin: $48\n'
        'Papas Locas “El Volcán”: $85\n\n'
        '-Bebidas\n'
        'Agua Horchata (500 ml): $25\n'
        'Agua de Jamaica (500 ml): $25\n'
        'Refrescos: $22'
    )

@bot.message_handler(commands=['horario'])
def send_horario(message):
    bot.reply_to(message, 'Estamos abiertos de Lunes a Domingo de 5:00pm a 12:00am.')

@bot.message_handler(commands=['ubicacion'])
def send_ubicacion(message):
    bot.reply_to(message, 'Av. Emiliano Zapata #1453, Col. Rosales, Culiacán, Sinaloa, México.')

@bot.message_handler(commands=['telefono'])
def send_telefono(message):
    bot.reply_to(message, 'Teléfono: 555-123-4567')


#webhook
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200


@app.route('/')
def home():
    return "Bot funcionando correctamente."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
