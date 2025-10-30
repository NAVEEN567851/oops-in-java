class Jharkhand:
    def capital(self):
        print("Ranchi")
    def language(self):
        print("Bindi and English")

class Bihar:
    def capital(self):
        print("Patna")
    def language(self):
        print("Bindi and English and Bhojpuri")

# creating objects.
obj1 = Jharkhand()
obj2 = Bihar()

# Use for loop access different objects.
for state in (obj1, obj2):
    state.capital()
    state.language()
