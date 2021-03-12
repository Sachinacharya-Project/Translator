import translators as ts

def translate_the_string(text, to, from_what, server):
    try:
        if server == 'b':
            return ts.bing(text, from_what, to)
        else:
            return ts.google(text, from_what, to)
    except Exception as e:
        return 'Sorry, Following Error Occured\n{}'.format(e)

if '__main__'==__name__:
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
    print('Translations')
    print(translated)