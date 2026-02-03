from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S9", "+79863456793"),
    Smartphone("iPhone", "15 Pro", "+79162345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79163456789"),
    Smartphone("Google", "Pixel 8", "+79164567890"),
    Smartphone("Nokia", "3310", "+79165678901")]

for phone in catalog:
    output = (phone.phone_mark +
              " - " +
              phone.phone_model +
              ". " +
              phone.phone_number)

    print(output)
