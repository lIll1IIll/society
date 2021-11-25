# CUSTOM RSA
class RSA:
    def __init__(self, strength: int=2):
        self.n = None
        self.pb = None
        self.pv = None

        self.max = None
        self.max_strength = [256, 512, 768, 1024, 2048, 4096]
        self.set_max(strength)

    def set_max(self, strength: int=2):
        self.max = self.max_strength[strength]

    def key_generator(self, n_min: int=128, n_max: int=300000, max: int=0):
        from random import randint

        if max == 0:
            max = self.max

        n = 0
        p = 0
        q = 0
        primes = self.get_prime_number(max)

        while n <= n_min or n >= n_max:
            p = primes[randint(0, len(primes) - 1)]
            q = primes[randint(0, len(primes) - 1)]
            if p == q or (p - 1) * (q - 1) == 2: continue
            n = p * q

        e = 0
        pi = (p - 1) * (q - 1)

        while not e:
            r = randint(0, pi * 2) % pi
            if 1 < r and r < pi:
                e = r
                cnt = 0
                for i in range(1, e):
                    if e % i == 0 and pi % i == 0:
                        cnt += 1
                if cnt >= 2:
                    e = 0

        d = 0

        while not d:
            rand = randint(0, pi * 2) % pi + 1
            if (e * rand) % pi == 1:
                d = rand

        self.n = n
        self.pb = e
        self.pv = d
        return True

    def get_pb_key(self):
        return self.pb

    def get_pv_key(self):
        return self.pv

    def get_n(self):
        return self.n

    def encrypt(self, msg: str):
        if self.pb == None:
            return False

        buffer = []

        for v in msg:
            sum = 1
            v = ord(v)
            for i in range(0, self.pb):
                sum = sum * v % self.n
            buffer.append(sum)

        return buffer

    def decrypt(self, buffer: list):
        if self.pv == None:
            return False

        msg = ''

        for v in buffer:
            sum = 1
            for i in range(0, self.pv):
                sum = sum * v % self.n
            msg += chr(sum)

        return msg

    def get_prime_number(self, max: int):
        res = []
        arr = [0] * max
        arr[0] = arr[1] = 1

        for i in range(2, max):
            if arr[i] == 0:
                for j in range(i * 2, max, i):
                    arr[j] = 1
                res.append(i)

        return res