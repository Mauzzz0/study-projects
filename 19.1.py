def continue_continue_continue_continue_continue_making_sure_the_function_name_is_correct(month: int, lang: str) -> str:
    # Function must RETURN month name
    dict = {
        "1": ["jan", "янв"],
        "2": ["feb", "фев"],
        "3": ["mar", "мар"],
        "4": ["apr", "апр"],
        "5": ["may", "май"],
        "6": ["jun", "июн"],
        "7": ["jul", "июл"],
        "8": ["aug", "авг"],
        "9": ["sep", "сен"],
        "10": ["oct", "окт"],
        "11": ["nov", "ноя"],
        "12": ["dec", "дек"]
    }
    lang = 0 if lang == "en" else 1
    return(dict[str(month)][lang])
