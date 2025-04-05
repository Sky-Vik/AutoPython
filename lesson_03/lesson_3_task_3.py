# 3. Вложенные классы

from address import Address
from mailing import Mailing

address1 = Address('191040', 'Москва', 'Садовая', '7/1', '24')
address2 = Address('185000', 'Петрозаводск', 'Лесная', '31', '15')
mailing = Mailing(address1, address2, cost=400, track='RU191400234456')

print(mailing.__str__())