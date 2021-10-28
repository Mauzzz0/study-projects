base = list()

def search_card(name: str):
    if name in base:
        print(base.index(name)+1)
    else:
        print("Not found")

def hello(name: str):
    print("In process...")
    search_card(name)