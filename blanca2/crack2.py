import zipfile
zFile = zipfile.ZipFile('secret.zip')
passFile = open('wordlist.txt')
for line in passFile.readlines():
        password = line.strip('\n')
        try:
            zFile.extractall(pwd=password)
            print(('[+] Password = ' + password + '\n'))
            exit(0)
        except Exception as e:
            pass