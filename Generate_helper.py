import random



def generate_good_password(lenght):
    # задать алфавить
    alphabet = 'abcdefgh4ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012356789!@#$%^&*()_+?<>.,'
    # выбрать случайный символ из алфавита
    # повторить lenght раз
    password = ''
    for i in range(lenght):
        symbol = random.choice(alphabet)
        password += symbol
    # склеить символы в строку
    return password


print(generate_good_password(10))
print(generate_good_password(11))
print(generate_good_password(12))

popular_passwords = [
    'admin',
    'password',
    '123',
    'qwerty',
    '123456',
    '12345',
]

def generate_bad_password():
    for i in len(popular_passwords):
        password = popular_passwords[i]
    return password