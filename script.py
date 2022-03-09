
import webbrowser as wb

def webAuto():
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    urls = [
        "google.com",
        "youtube.com",
        "facebook.com"
    ]

    for url in urls:
        print("Opening this :", url)
        wb.get(chrome_path).open(url)
        # wb.get(chrome_path).open_new("https://neverbounce.com")

webAuto()
