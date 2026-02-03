from address import Address
from mailing import Mailing

my_mail = Mailing(
    to_address=Address("452170", "Ufa", "Lenina", "89", "5"),
    from_address=Address("101000", "Moscow", "Arbat", "20", "3"),
    cost="4500",
    track="R098456"
)
print(
    f"Отправление {my_mail.track} из {my_mail.from_address} "
    f"в {my_mail.to_address}. Стоимость {my_mail.cost} рублей."
)
