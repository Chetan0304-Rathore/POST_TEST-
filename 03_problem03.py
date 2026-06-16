#Create Abstract class Payment with:

from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass


# Child Class GPay
class GPay(Payment):
    def pay(self):
        print("Payment made using GPay")

    def receipt(self):
        print("GPay receipt generated")


# Child Class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")

    def receipt(self):
        print("Credit Card receipt generated")


# Creating objects
gpay = GPay()
card = CreditCard()

# Calling methods
print("GPay:")
gpay.pay()
gpay.receipt()

print("\nCredit Card:")
card.pay()
card.receipt()