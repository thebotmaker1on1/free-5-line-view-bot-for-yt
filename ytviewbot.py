import webbrowser, time
url = input("url: ")
duration = input("enter duration: ")
for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))