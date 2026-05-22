class TelefonRaqam:
    def __init__(self, ism, balans):
        self.ism = ism
        self.__balans = balans

    def get_balans(self):
        return self.__balans

    def set_balans(self, balans):
        if balans >= 0:
            self.__balans = balans
            print("Balans yangilandi")
        else:
            print("Noto'g'ri balans")


r1 = TelefonRaqam("Ali", 15000)
print(r1.get_balans())
