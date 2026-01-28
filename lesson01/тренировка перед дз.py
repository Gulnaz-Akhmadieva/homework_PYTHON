def print_letter(let):
    print(let, end='')


print_letter('с')
print_letter('т')
print_letter('у')
print_letter('д')
print_letter('е')
print_letter('н')
print_letter('т')

pet_name = input("Как зовут вашего питомца? ")
if not pet_name:  # если пользователь ничего не ввел
    pet_name = "Шарик"  # используется "Барон" как значение по умолчанию
print("Мой любимчик - " + pet_name)