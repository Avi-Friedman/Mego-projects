class Customers:
    _amount = 0
    @staticmethod
    def _club_amount():
        print (f"There are {Customers._amount} club members in the system")

    def __init__(self, first_name, last_name, age, phone_number, club):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.club = club


    def add_club(self):
        if self.club == True:
            Customers._amount += 1
yoel = Customers ("yoel","shtineberg", 37,"052765656",False)
yoel.club = True
menachem = Customers ("menachem","gertner", 31, "052767788", True)
yoel.add_club()
menachem.add_club()
Customers._club_amount()

# class Messages:
#     def message(self, a):
#
#         if a == 5:
#             print("fffffff")
#
# b = 5
# s = Messages()
# s.message(b)



















