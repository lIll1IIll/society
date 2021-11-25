import hashlib

def original(data):
    return data

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()