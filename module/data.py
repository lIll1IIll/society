import time
from random import randint
from string import ascii_letters, digits

printable = ascii_letters + digits + '!?/.,<>()-=+&^$#@'

def data_generator(cnt: int=500):
    data = ()
    for _ in range(cnt):
        age = randint(18, 60)
        name = ''.join([chr(randint(97, 122)) for _ in range(randint(1, 10))])
        address = ['서울', '인천', '대구', '경기', '경북', '경남', '부산', '대전', '울산', '세종', '충북', '충남', '전북', '전남', '광주', '제주'][randint(0, 15)]
        phone = "010-" + str(randint(1000, 9999)) + "-" + str(randint(1000, 9999))
        pw = ''.join([printable[randint(0, len(printable) - 1)] for _ in range(randint(1, 128))])
        data += (name, age, address, phone, pw),

    with open(str(time.time()) + ".txt" , 'w', encoding='utf-8') as f:
        f.write('\n'.join([' '.join(map(str, d)) for d in data]))
    return data