
class książkaAdresowa():
    def __init__(self, imię, nazwisko, firma, email):
        self.imię = imię
        self.nazwisko = nazwisko
        self.firma = firma
        self.email = email

Pawlak = książkaAdresowa(imię = "Halina", nazwisko = "Pawlak", firma = "Żabka", email = "hp01@gmail.com")
Kawiatkowski = książkaAdresowa(imię = "Janusz", nazwisko="Kwiatkowski", firma = "Auchan", email = "j.kwiat@gmail.com")
Nowak = książkaAdresowa(imię = "Anna", nazwisko= "Nowak", firma = "Centrum", email = "anna.nowak@wp.pl")
Wojciechowski = książkaAdresowa(imię = "Rajmund", nazwisko = "Wojciechowski", firma = "Tesco", email = "rajwoj@wp.pl")
Piotrowski = książkaAdresowa(imię = "Mariusz", nazwisko="Piotrowski", firma = "Fresh", email = "piotrkowski.m@gmail.com")

osoby = [Pawlak, Kawiatkowski, Nowak, Wojciechowski, Piotrowski]
print(Pawlak.name, Pawlak.nazwisko, Pawlak.email)
