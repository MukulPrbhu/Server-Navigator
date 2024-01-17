import telebot
import os
import string

path = 'D:\\' #Give any directory address 
bot = telebot.TeleBot("") #Token

@bot.message_handler(commands=['list']) #Lists the current directory
def list(message):
    global path
    text=""
    text += f"Current directory : {path}\n\n"
    for i,j,k in os.walk(path):
        for x in range (len(j)):
            text += f"{str(x)} {j[x]}\n"
        for y in range(len(k)):
            text += f"{str(len(j)+y)} {k[y]}\n"
        break
    bot.reply_to(message, text) #Can use send_message too

@bot.message_handler(commands=['goto']) #Enters a folder 
def list(message):
    num = int(message.text[6:])
    global path
    text=""
    for i,j,k in os.walk(path):
        for x in range (len(j)):
            continue
        for y in range(len(k)):
            continue
        break
    
    if num < len(j):
        path = path +chr(92)+ j[num] #chr(92) is \
        text += f"Current directory : {path}\n\n"
        for i,j,k in os.walk(path):
            for x in range (len(j)):
                text += f"{str(x)} {j[x]}\n"
            for y in range(len(k)):
                text += f"{str(len(j)+y)} {k[y]}\n"
            break
    else:
        text += f"Not a folder"
    
    bot.reply_to(message, text)

@bot.message_handler(commands=['back']) #Goes back a directory
def back(message):
    text=""
    global path
    text += f"Previous directory : {path}\n\n"
    a = os.path.dirname(path)
    path = a 
    text += f"Current directory : {a}\n\n"
    for i,j,k in os.walk(a):
        for x in range (len(j)):
            text += f"{str(x)} {j[x]}\n"
        for y in range(len(k)):
            text += f"{str(len(j)+y)} {k[y]}\n"
        break
    bot.reply_to(message, text)
    
@bot.message_handler(commands=['drive']) #Lists the current directory
def drive(message):
    d = f"{message.text[7:].upper()}:"
    global path
    text = ''
    available_drives = ['%s:' % q for q in string.ascii_uppercase if os.path.exists('%s:' % q)]
    if d not in available_drives:
        text += f"Drive {d} not present, available drives are:\n"
        for drives in available_drives:
            text += f"{drives}\n"
    else:
        path = f"{d}\\"
    text += f"Current directory : {path}\n\n"
    bot.reply_to(message, text)



bot.polling()


