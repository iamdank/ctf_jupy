import zipfile

zip_file = zipfile.ZipFile('secret.zip')
output_verbose = 2  # increase that for long password list
with open('wordlist.txt', 'rb') as password_list:
    for index, line in enumerate(password_list):
        try:
            pwd = line.strip(b'\n')
            zip_file.extractall(pwd=pwd)
        except RuntimeError:
            if index % output_verbose == 0:
                print('{}. The {} word not matched.'.format(index + 1, pwd))
        else:
            print('{}. Wow ! found the password: {}'.format(index + 1, pwd))
            break

zip_file.close()