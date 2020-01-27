from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup
import urllib.request


resp = urllib.request.urlopen("http://iantarkel.correa-ataide.com.br/")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'),features="html.parser")

resumoLnk = soup.find('a', 'wpbf-post-image-link')['href']


resp2 = urllib.request.urlopen(resumoLnk)
soup2 = BeautifulSoup(resp2, "html.parser")

resumoTxtHtml = soup2.find('section', "entry-content")
resumoTxt = resumoTxtHtml.get_text()

paragraphs = [resumoTxt[i:i+500] for i in range(0, len(resumoTxt), 500)]


updater = Updater(token="895660103:AAF9e7UVdkuccawQNM8IVBtf9-iYYPkuaSA")

dispatcher = updater.dispatcher

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Comandos disponíveis:\n/+nome do personagem. Ex.: /durin\n/iantarkel - Livro de campanha\n/resumo - Link para último resumo no site\n/resumotexto - Texto do resumo direto no chat (FLOOOOOOOOD Alert)")

def iantarkel(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://log-de-iantarkel.000webhostapp.com/wp-content/uploads/DD-5e-CPG-Iantarkels-Guide.pdf')

def yoni(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Pedro.pdf')

def drexter(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Andr%C3%A9.pdf')

def raio(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Caio.pdf')

def durin(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Hugo-Silva.pdf')

def sombra(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Victor.pdf')

def alghurab(bot, update):
  bot.send_document(chat_id=update.message.chat_id, document='https://iantarkel.correa-ataide.com.br/wp-content/uploads/Elias.pdf')

def resumo(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=resumoLnk)

def resumotexto(bot, update):
  for i in paragraphs:
    bot.send_message(chat_id=update.message.chat_id, text=i)


start_handler = CommandHandler("start", start)
iantarkel_handler = CommandHandler("iantarkel", iantarkel)
yoni_handler = CommandHandler("yoni", yoni)
drexter_handler = CommandHandler("drexter", drexter)
raio_handler = CommandHandler("raio", raio)
durin_handler = CommandHandler("durin", durin)
sombra_handler = CommandHandler("sombra", sombra)
alghurab_handler = CommandHandler("alghurab", alghurab)
resumo_handler = CommandHandler("resumo", resumo)
resumotexto_handler = CommandHandler("resumotexto", resumotexto)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(iantarkel_handler)
dispatcher.add_handler(yoni_handler)
dispatcher.add_handler(drexter_handler)
dispatcher.add_handler(raio_handler)
dispatcher.add_handler(durin_handler)
dispatcher.add_handler(sombra_handler)
dispatcher.add_handler(alghurab_handler)
dispatcher.add_handler(resumo_handler)
dispatcher.add_handler(resumotexto_handler)


updater.start_polling()