
import webbrowser as wb

def webAuto():
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    urls = [
        "https://docs.google.com/spreadsheets/d/1Z0e0oxf7dH28zbQS0S1gI4qt2EOEvNTT-gf_koaoOMY/edit#gid=1556281650",
        "https://app.ahrefs.com/positions-explorer/competing-domains/v2/subdomains/hk/all/all/all/all/all/1/common_keywords_percentage_desc?target=surfshark.com",
        "https://app.ahrefs.com/site-explorer/backlinks/v7/external-per-domain/subdomains/live/all/all/dofollow/7/domain_rank_desc?target=nordvpn.com&platform=wordpress",
        "gmail.com",
        "https://docs.google.com/spreadsheets/d/1ZXbjjYbVNvoa7NDAPhsY4aVRQMf9aUnZxGjjTceX-7s/edit#gid=1498022197",
        "buzzstream.com"
    ]

    for url in urls:
        print("Opening this :", url)
        wb.get(chrome_path).open(url)
        # wb.get(chrome_path).open_new("https://neverbounce.com")

webAuto()
