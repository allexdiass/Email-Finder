import requests
import re

print('[!] E-mail Finder [!]')

to_craw = []
to_craw.append(input('[*] Entre com o domínio alvo: '))
if to_craw[0].startswith('www'):
    to_craw[0] = 'http://' + to_craw[0]
crawled = set()
emails_found = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

for i in range(15):
    url = to_craw[0]
    try:
        req = requests.get(url, headers=header)
    except Exception as e:
        print(e)
        to_craw.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    emails = re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)
    print('Crawling: ', url)

    to_craw.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and links not in to_craw:
            to_craw.append(link)

    for email in emails:
        emails_found.add(email)

print('\n[*] E-mails encontrados:')
for email in emails_found:
    print(email)
