import time
from module.encrypt.symmetric.RSA import RSA

rsa = RSA(1)
start = time.time()
rsa.key_generator()
end = time.time()

print("n:", rsa.get_n())
print("pb:", rsa.get_pb_key())
print("pv:", rsa.get_pv_key())
print("time:", end - start)

origin = "Hello, world!"
encreypted = rsa.encrypt(origin)

print("origin:", origin)
print("encreypted:", ", ".join(map(str, encreypted)))
print("decreypted:", rsa.decrypt(encreypted))