import telebot
from flask import Flask, request

TOKEN = "8345034042:AAH_JVfkFlX0lAwuz9vB8MP129dZH_QVcm8"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

#Creacion de comandos
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! bienvenido a taqueria El Volcan, escribe /help para saber en que te puedo ayudar')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, '/menu - muestra el menu que maneja nuestro establecimiento \n/horario - muestra el horario en el que estamos abiertos al publico \n/ubicacion - muestra la direccion en la que nos puedes encontrar \n/telefono - muestra el numero de telefono de la taqueria, mediante el cual podras hacer pedidos')

@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.reply_to(message, '-Comidas\n Tacos de Asada: $28 c/u\n Tacos al Pastor: $25 c/u\n Tacos de Birria (con consomé): $45\n Quesadilla de Arrachera (tortilla de harina): $75\n Gringa al Pastor: $65\n Vampiro de Sirloin: $48\n Papas Locas “El Volcan”: $85\n -Bebidas\n Agua Horchata (500 ml): $25\n Agua de Jamaica (500 ml): $25\n Refrescos: $22')

@bot.message_handler(commands=['horario'])
def send_horario(message):
    bot.reply_to(message, 'Estamos abiertos de Lunes a Domingo 5:00pm a 12:00am')

@bot.message_handler(commands=['ubicacion'])
def send_ubicacion(message):
    bot.reply_to(message, 'Nos puedes encontrar en: Av. Emiliano Zapata #1453, Col. Rosales Culiacán, Sinaloa, México. C.P. 80230')

@bot.message_handler(commands=['telefono'])
def send_pedido(message):
    pedido = True
    bot.reply_to(message, '555 168 549 328')

# Webhook
@app.route('/' + TOKEN, methods=['POST'])
def receive_update():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def home():
    return "Bot funcionando"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)