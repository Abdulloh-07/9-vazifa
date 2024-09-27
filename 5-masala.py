import random

class Savol:
    def __init__(self, savol_matni, variantlar, togri_javob):
        self.savol_matni = savol_matni
        self.variantlar = variantlar
        self.togri_javob = togri_javob

    def javobni_tekshirish(self, javob):
        return javob == self.togri_javob


class Test:
    def __init__(self):
        self.savollar = []

    def savol_qoshish(self, savol):
        self.savollar.append(savol)

    def test_olish(self):
        random.shuffle(self.savollar)
        ball = 0

        for savol in self.savollar:
            print(savol.savol_matni)
            for idx, variant in enumerate(savol.variantlar):
                print(f"{idx + 1}. {variant}")

            javob = int(input("Javobni kiriting (raqam): ")) - 1

            if savol.javobni_tekshirish(savol.variantlar[javob]):
                print("Togri!")
                ball += 1
            else:
                print(f"Xato! Togri javob: {savol.togri_javob}")

        print(f"Test tugadi! Sizning ballingiz: {ball}/{len(self.savollar)}")


test_fizika = Test()
test_matematika = Test()

while True:
    buyruq = input("1 - Savol qo'shish, 2 - Test o'tkazish: ")
    if buyruq == '1':
        tanlov = input("1 - Fizika, 2 - Matematika: ")
        savol_soni = int(input("Nechta savol qo'shmoqchisiz? "))

        for _ in range(savol_soni):
            savol_matni = input("Savol matnini kiriting: ")
            variantlar = [input(f"{i + 1}-variantni kiriting: ") for i in range(4)]
            togri_javob = variantlar[int(input("To'g'ri javobni (1-4 raqami) kiriting: ")) - 1]

            if tanlov == '1':
                test_fizika.savol_qoshish(Savol(savol_matni, variantlar, togri_javob))
            elif tanlov == '2':
                test_matematika.savol_qoshish(Savol(savol_matni, variantlar, togri_javob))

    elif buyruq == '2':
        tanlov = input("1 - Fizika, 2 - Matematika: ")
        if tanlov == '1':
            test_fizika.test_olish()
        elif tanlov == '2':
            test_matematika.test_olish()