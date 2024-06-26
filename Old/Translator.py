import translators as ts
import tkinter
from tkinter import filedialog

def choose_files():
    root = tkinter.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.title("Choose Text Files")
    files = filedialog.askopenfilename(title='Choose Text File', filetypes=(('Plain Text', '*.txt'), ('List Files', '*.lst'), ('All Files', '*.*')))
    return files

def translate_the_string(text, to, from_what, server):
    try:
        if server == 'b':
            return ts.bing(text, from_what, to)
        else:
            return ts.google(text, from_what, to)
    except Exception as e:
        return 'Sorry, Following Error Occured\n{}'.format(e)

if '__main__'==__name__:
    ask = input("From File(F) or From User-Input(U): ").lower()
    if ask == 'f':
        print("Chooose File")
        filename = choose_files()
        file = open(filename, 'r')
        filename = "translated_{}".format(str(filename).split('/')[-1])
        print(filename)
        text = "".join(file.readlines())
    else:
        filename = "translated_{}.txt".format(input("Ouput Filename: "))
        print('Please Enter your Text')
        text = ''
        while True:
            gets = input()
            if gets == '':
                break
            else:
                text += "{}\n".format(gets)
    to_lang = input("Which language you wanna translate to?\n").lower()
    if len(to_lang) > 3:
        print('Sorry, Literal is incorrect\nPlease Open LITERALS.md for LITERALS')
        print('Defaulting to English: EN')
        to_lang = 'en'
    elif to_lang == '':
        print("Defaulting to English: EN")
        to_lang = 'en'
    print("""Choose Engine
    1. Is Accurate but has less Translation Language
    2. Might be Inaccurate but has large variety of Translation Lang.
    """)
    ask = input(": ").lower()
    if ask == '1':
        ask = 'b'
    else:
        ask = 'g'
    translated = translate_the_string(text, to_lang, 'auto', ask)
    getfl = open(filename, 'w')
    getfl.write(translated)
    getfl.close()
    print("File is Outputted to {}".format(filename))