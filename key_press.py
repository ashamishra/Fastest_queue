import getch
def process(key):
    if key == 'x':
        exit('exitting')
    else:
        print(key, end="", flush=True)

if __name__ == "__main__":
    while True:
        key = getch.getch()
        if key == "i": print(key)
