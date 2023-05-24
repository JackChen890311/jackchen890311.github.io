import json
import datetime
import requests


UID = 6338711946186074
with open('../../../tokens/IG token.txt','r') as f:
    ACCESS_TOKEN = f.read()
FIELDS = 'id,caption,media_url,permalink,timestamp'
URL = f'https://graph.instagram.com/{UID}/media'
today = datetime.date.today().strftime('%Y/%m/%d') 

params = {'access_token': ACCESS_TOKEN, 'fields': FIELDS, 'limit': 18}
response = requests.get(URL, params=params)
data = json.loads(response.text)['data']
print('Total posts:', len(data))
# print(data[0]['id'])
# print(data[0]['caption'])
# print(data[0]['media_url'])
# print(data[0]['permalink'])
# print(data[0]['timestamp'])

with open('embedded.txt','r', encoding="utf-8") as f:
    embedded = f.read()

with open('index.md','r', encoding="utf-8") as f:
    text = f.read()
    front = text.split('<!-- START -->')[0] + '<!-- START -->\n\n'

with open('index.md','w', encoding="utf-8") as f:
    f.write(front)
    f.write(f'<center>Last update on: {today}</center>\n')
    with open('button.txt','r') as f2:
        button = f2.read()
        f.write(button+'\n\n---\n\n')
    for post in data:
        embedded_ramen = embedded.replace('#####URL#####',post['permalink'])
        # f.write(f"![]({post['media_url']})\n")
        f.write(embedded_ramen+'\n')
        f.write('<center>\n')
        caption = post['caption'][:post['caption'].find('推薦指數') + 10]
        caption = caption.split('\n')
        for c in caption:
            f.write(c + '<br>\n')
        # f.write(f"<a href='{post['permalink']}'>詳閱全文點我</a>")
        f.write('</center>\n\n---\n\n')

print('Last post is on:',post['timestamp'])
