class KsiążkaAdresowa():

    def __init__(self, imię, nazwisko):
        self.imię = imię
        self.nazwisko = nazwisko
        
    def contact(self):
        print("Kontaktuje się")
        # print(f"Kontaktuję się z {self.imię}, {self.nazwisko} {self.email}.")
    
    def name_and_surname_length(self):
        return len(self.imię) + len(self.nazwisko) + 1


class BaseContact(KsiążkaAdresowa):

    def __init__(self, telefon, email, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.email = email
       self = telefon    

    def contact(self):
        print(f"wybieram numer {self.telefon} i dzwonię do: {self.imię} {self.nazwisko}.")


class BusinessContact(KsiążkaAdresowa):

    def __init__(self, firma,  telefon_służbowy, stanowisko, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.firma = firma
       self.stanowisko = stanowisko
       self.telefon_służbowy = telefon_służbowy

    def contact(self):
        print(f"wybieram numer {self.telefon_służbowy} i dzwonię do {self.firma}.")



Pawlak = BusinessContact(imię = "Halina", nazwisko = "Pawlak", firma = "Żabka", stanowisko="dyrektor", telefon_służbowy="797722199" )
# Kwiatkowski = BusinessContact(imię = "Janusz", nazwisko="Kwiatkowski", firma = "Auchan", email = "j.kwiat@gmail.com")
# Nowak = BusinessContact(imię = "Anna", nazwisko= "Nowak", firma = "Centrum", email = "anna.nowak@wp.pl")
# Wojciechowski = BusinessContact(imię = "Rajmund", nazwisko = "Wojciechowski", firma = "Tesco", email = "rajwoj@wp.pl")
# Piotrowski = BusinessContact(imię = "Mariusz", nazwisko="Piotrowski", firma = "Fresh", email = "piotrkowski.m@gmail.com")

# BaseContact.contact(Pawlak)
BusinessContact.contact(Pawlak)
print(BusinessContact.name_and_surname_length(Pawlak))
# result = BusinessContact.create_contacts(Pawlak, 5)
# print(result)
# Kwiatkowski.contact()
# Nowak.contact()


# osoby = [Pawlak, Kawiatkowski, Nowak, Wojciechowski, Piotrowski]
# by_name = sorted(osoby, key=lambda książkaAdresowa: książkaAdresowa.imię)
# by_surname = sorted(osoby, key=lambda książkaAdresowa: książkaAdresowa.nazwisko)
# by_email = sorted(osoby, key=lambda książkaAdresowa: książkaAdresowa.email)
# print(by_name)
# print(by_surname)
# print(by_email)

# print(Pawlak.imię, Pawlak.nazwisko, Pawlak.email)
# print(Kwiatkowski.imię, Kwiatkowski.nazwisko, Kwiatkowski.email)
# print(Nowak.imię, Nowak.nazwisko, Nowak.email)
# print(Wojciechowski.imię, Wojciechowski.nazwisko, Wojciechowski.email)
# print(Piotrowski.imię, Piotrowski.nazwisko, Piotrowski.email)