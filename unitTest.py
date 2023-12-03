

from app.orderManager import *
from app.stlsManager import *
from app.userManager import *


adressObj = Address("1726 spring","rochester",48306)
order1 = Order(adressObj,"cat","ab39")

print("start unit test:")

print(order1.address)

confirmation = order1.makePayment(Payment("andersen","ball",adressObj,1))
print("order confirmed:",confirmation)
print("status:",order1.status)
