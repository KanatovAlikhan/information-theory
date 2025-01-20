import re, math
from collections import Counter
with open('jest_vek.txt', 'r') as fh:
    data = fh.read()
    text = ''.join(re.findall(r'[А-ЯЁа-яё]', data))
    abc = sorted(set(text.lower()))
    symbols = len(text)
    freq = Counter(text.lower())
    Px = {char: count / symbols for char, count in freq.items()}
    entropy = -sum(p * math.log2(p) for p in Px.values())
print(f"Алфавит (ABC): {abc}")
print(f"Частоты символов: {Px}")
print(f"Энтропия текста: {entropy} бит/символ")
