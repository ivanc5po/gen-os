import os

pool = input("XMR pool address : ")
wallet = input("XMR wallet address : ")
passwd = input("password (worker name) : ")

os.system("./xmrig -o "+pool+" -u "+wallet+" -p "+passwd)



