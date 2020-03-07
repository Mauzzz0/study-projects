import requests
from bs4 import BeautifulSoup

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         
    soup = BeautifulSoup(html, 'lxml')
    results = soup.findAll("div", { "class" : "date_text" })
    print(results.text)
    
    
def main():
    url = 'https://www.mirea.ru/'
    get_page_data(get_html(url))
    input()

if __name__ == '__main__':
        main()
