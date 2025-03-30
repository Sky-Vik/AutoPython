# 2. Список объектов

from smartphone import Smartphone

smart1 = Smartphone("Nokia", "3310", "+79113456754")
smart2 = Smartphone("Samsung", "A71", "+79217775859")
smart3 = Smartphone("Xiaomi", "13T", "+79059998877")
smart4 = Smartphone("Realme", "Note 60x", "+79111234567")
smart5 = Smartphone("Apple iPhone", "16 Pro", "+79216473829")
catalog = [smart1, smart2, smart3, smart4, smart5]

for smart in catalog:
    print(f"{smart.mark} - {smart.model}. {smart.number}")