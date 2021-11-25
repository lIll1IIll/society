import module.encrypt.hash as hash

origin = 'hello world!'
sha256 = hash.sha256(origin)
md5 = hash.md5(origin)

print("origin:", origin)
print("sha256:", sha256)
print("md5:", md5)