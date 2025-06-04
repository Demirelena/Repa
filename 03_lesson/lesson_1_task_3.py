from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Ленина", "10", "15")
to_address = Address("654321", "Санкт-Петербург", "Невский", "25", "8")
mail = Mailing(to_address, from_address, 350, "TRACK123456")

print(f"Отправление {mail.track} из "
      f"{mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")