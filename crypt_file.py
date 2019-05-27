from cryptography.fernet import Fernet

# создаем файл с ключем
def generate_new_key(key_file_name):
    '''
    создаем ключ шифрования в файле с указанным названием
    '''
    with open(key_file_name, 'wb') as key_file:
        cipher_key = Fernet.generate_key()
        key_file.write(cipher_key)
        # print(cipher_key)


def encrypting_file(input_file, encrypted_file_name, key_file):
    '''
    создаем файл с шифровкой encrypted_file_name
    из данных, которые берем из файла input_file
    Шифруем ключем из key_file
    '''
    with open(key_file, 'rb') as key_file:
        # вынимаем ключ из файла
        cipher_key = key_file.readline()
        # Экземпляр класса шифрования с полученным ключем
        cipher = Fernet(cipher_key)
        with open(input_file, 'r', encoding='utf-8') as text_for_encription:
            # и файл для записи шифровок
            with open(encrypted_file_name, 'wb') as encrypted_file:
                for line in text_for_encription.readlines():
                    converted_to_bite = bytes(line, 'utf-8')
                    encrypted_text = cipher.encrypt(converted_to_bite)
                    encrypted_file.write(encrypted_text + b'\n')


def decrypting_file(encrypted_file_name, output_file, key_file):
    '''
    расшифровываем файл encrypted_file_name
    и сохраняем результат в output_file
    Ключ берем из файла key_file
    '''
    with open(key_file, 'rb') as key_file:
        # вынимаем ключ из файла
        cipher_key = key_file.readline()
        # Экземпляр класса шифрования с полученным ключем
        cipher = Fernet(cipher_key)
        with open(encrypted_file_name, 'rb') as encrypted_file:
            with open(output_file, 'w', encoding='utf-8') as decrypted_file:
                for line in encrypted_file.readlines():
                    decrypted_text = cipher.decrypt(line)
                    converted_to_str = str(decrypted_text, 'utf-8')
                    decrypted_file.write(converted_to_str)


if __name__ == '__main__':
    encrypting_file('text_for_encription.txt', 'encripted_file.txt', 'key.key')
    decrypting_file('encripted_file.txt', 'result.txt', 'key.key')
