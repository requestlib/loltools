# coding=utf-8
import re
import json

result = {}
with open("champion.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    pattern = r'<p class="hero-name">.{0,10}</p></div> <a href="#/hero-detail\?heroid=\d+" class="">'
    all_hero = re.findall(pattern, data)
    for hero in all_hero:
        info = hero.split('</p></div> <a href="#/hero-detail?heroid=')
        name = info[0].split('<p class="hero-name">')[1]
        heroid = info[1].split('" class="">')[0]
        result[heroid] = name
print(len(result))
with open("name_id.json", 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)
