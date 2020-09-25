import re # 載入正規表達式

with open("test.txt", 'r') as f:
    lines = f.read()

relus = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.edu+\.tw")
emails = relus.findall(lines)
print(emails)