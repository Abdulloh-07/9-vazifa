import random


class Film:
    def __init__(self, nom, janr, reyting):
        self.nom = nom
        self.janr = janr
        self.reyting = reyting

    def __str__(self):
        return f"{self.nom} ({self.janr}) - Reyting: {self.reyting}"


class TavsiyaTizimi:
    def __init__(self):
        self.filmlar = []

    def film_qoshish(self, film):
        self.filmlar.append(film)

    def tavsiya_berish(self, afzallik_janri):
        mos_filmlar = [film for film in self.filmlar if film.janr.lower() == afzallik_janri.lower()]

        if not mos_filmlar:
            print(f"{afzallik_janri} janrida film topilmadi.")
            return None

        tavsiya_qilingan_film = random.choice(mos_filmlar)
        return tavsiya_qilingan_film

tavsiya_tizimi = TavsiyaTizimi()

savol = "Film qo'shish uchun 'stop' deb yozmaguncha davom eting."

while True:
    nom = input("Film nomini kiriting (stop - tugatish): ")
    if nom.lower() == 'stop':
        break
    janr = input("Film janrini kiriting: ")
    reyting = float(input("Film reytingini kiriting: "))

    tavsiya_tizimi.film_qoshish(Film(nom, janr, reyting))

afzallik_janri = input("Sizning afzal ko'rgan janringizni kiriting: ")

tavsiya_film = tavsiya_tizimi.tavsiya_berish(afzallik_janri)

if tavsiya_film:
    print(f"Tavsiya etilgan film: {tavsiya_film}")