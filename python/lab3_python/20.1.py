translatedText = ""
def continueX11_making_sure_the_function_name_is_correct(inp: str):
    global translatedText
    x = ""
    for g in inp:
        if g not in ["а", "е", "ё", "и", "о", "у", "ы", "э", "я", "ю"] :
            x += g
    translatedText = x
