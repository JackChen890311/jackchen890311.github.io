import datetime

IN_FILENAME = 'index.md'
OUT_FILENAME = 'index.md'
today = datetime.date.today().strftime('%Y/%m/%d') 

with open('embedded.txt','r', encoding="utf-8") as f:
    embedded = f.read()

# embedded = embedded.replace('#####URL#####','123123123')
# print(embedded)

with open(IN_FILENAME,'r', encoding="utf-8") as fin:
    text = fin.read()
    front = text.split('<!-- START -->')[0] + '<!-- START -->\n\n'
    content = text.split('---')


with open(OUT_FILENAME,'w', encoding="utf-8") as fout:
    fout.write(front)
    fout.write(f'<center>Last update on: {today}</center>\n')
    with open('button.txt','r') as f2:
        button = f2.read()
        fout.write(button+'\n\n---\n\n')
    for ramen in content:
        if '![]' in ramen:
            ramen = ramen.split('\n')[3:-2]
            url = ramen[-1].split("'")[1]
            embedded_ramen = embedded.replace('#####URL#####',url)

            fout.write(embedded_ramen)
            fout.write('\n')

            for line in ramen:
                if 'href' not in line:
                    fout.write(line)
                    fout.write('\n')
            fout.write('</center>\n\n---\n\n')

