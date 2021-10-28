"""
class Months:
    jan = 31

    class feb:
        normal = 28
        leap = 29

    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31

def automaker():
    global Months1
    for i in range(13):
        mon, le = input().split()
        Months1[mon] = le
    print(Months1)

def summunator(day, month, year, plus):
    remain = plus
    for i in range(remain//28 + 1):
        None
"""

Months1 = {
    'jan': '31',
    'febnormal': '28',
    'febleap': '29',
    'mar': '31',
    'apr': '30',
    'may': '31',
    'jun': '30',
    'jul': '31',
    'aug': '31',
    'sep': '30',
    'oct': '31',
    'nov': '30',
    'dec': '31'
}

codeMonths = {
    "1" : "jan",
    "3" : "mar",
    "4" : "apr",
    "5" : "may",
    "6" : "jun",
    "7" : "jul",
    "8" : "aug",
    "9" : "sep",
    "10" : "oct",
    "11" : "nov",
    "12" : "dec"
}

def leap(year):
    year=int(year)
    return True if year%400 == 0 or ( year%4 == 0 and year%100 != 0 ) else False

def inputer():
    start_data = input("Print start data like a dd.mm.yyyy\n")
    start_day, start_month, start_year = [int(o) for o in start_data.split(".")]
    plus = int(input("plus days\n"))
    return [start_day,start_month,start_year,plus]

def algorithm(day, month, year, plus):

    global codeMonths, Months1

    new=day+plus

    if month != 2:
        maxday= int( Months1[str(codeMonths[str(month)])] )
    else:
        if leap(year) is True:
            maxday = 29
        else:
            maxday = 28

    if new <= maxday:
        print(day+plus,month,year)
        return

    else:
        plus -= (maxday-day+1)

        if month != 12:
            month += 1
            day = 1
        else:
            year += 1
            month = 1
            day = 1
        algorithm(day,month,year,plus)


day,month,year,plus=inputer()
algorithm(day,month,year,plus)