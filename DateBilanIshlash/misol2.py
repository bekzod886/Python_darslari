import datetime

dt = datetime.datetime.now().second
while True:
    if dt + 3 == datetime.datetime.now().second:
        print('Vaqtingiz tugadi')
        break
