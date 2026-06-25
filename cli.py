from translator import translate_auto 
from time import sleep

def type_words(text,delay=0.2):
    for word in text.split():
        print(word,end=" ",flush=True)
        sleep(delay)

    print()

print("---- 🤳AI TRANSLATOR CHATBOT 🤳---")
print("TYPE 'exit' to QUIT")


while True:
    text=input("YOU:")

    if text.lower()=="exit":
        print("goodbye👋")
        break

    result=translate_auto(text)



    print("BOT",end="")

    type_words(result)


