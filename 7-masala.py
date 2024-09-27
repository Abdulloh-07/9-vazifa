import os
from abc import ABC, abstractmethod
import requests

class Download(ABC):
    @abstractmethod
    def download(self):
        pass

class ImageDownload(Download):
    def __init__(self, url, file_name):
        self.__url = url
        self.__file_name = f"images/{file_name}"

    def download(self):
        image = requests.get(self.__url)
        with open(self.__file_name, "wb") as file:
            print(f"{file.name} yuklab olinmoqda...")
            file.write(image.content)
            print(f"{file.name} yuklab olindi...")

class VideoDownload(Download):
    def __init__(self, url, file_name):
        self.__url = url
        self.__file_name = f"videos/{file_name}"

    def download(self):
        video = requests.get(self.__url)
        with open(self.__file_name, "wb") as file:
            print(f"{file.name} yuklab olinmoqda...")
            file.write(video.content)
            print(f"{file.name} yuklab olindi...")

class DocumentDownload(Download):
    def __init__(self, url, file_name):
        self.__url = url
        self.__file_name = f"documents/{file_name}"

    def download(self):
        doc = requests.get(self.__url)
        with open(self.__file_name, "wb") as file:
            print(f"{file.name} yuklab olinmoqda...")
            file.write(doc.content)
            print(f"{file.name} yuklab olindi...")

def yuklash():
    while True:
        try:
            buyruq = int(input("1. Rasm yuklash\n2. Video yuklash\n3. Dokument yuklash\n4. Barcha rasmlar\n5. Barcha videolar\n6. Barcha dokumentlar >>> "))
            match(buyruq):
                case 1:
                    url = input("Urlni kiriting: ")
                    file_path = input("Fayl nomini kiriting: ")
                    image = ImageDownload(url, file_path)
                    image.download()
                case 2:
                    url = input("Urlni kiriting: ")
                    file_path = input("Fayl nomini kiriting: ")
                    video = VideoDownload(url, file_path)
                    video.download()
                case 3:
                    url = input("Urlni kiriting: ")
                    file_path = input("Fayl nomini kiriting: ")
                    doc = DocumentDownload(url, file_path)
                    doc.download()
                case 4:
                    manage_files('images')
                case 5:
                    manage_files('videos')
                case 6:
                    manage_files('documents')
                case _:
                    print("Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.")
        except Exception as e:
            print(f"xato: {e}")

def manage_files(folder):
    res = []
    for path in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, path)):
            res.append(path)

    answer = 'y'
    while answer == 'y':
        print("\n\n")
        for ind, i in enumerate(res):
            print(f"{ind}. {i}")

        a = input("\nO'chirishni hohlaysizmi? (y/n): ")
        if a != 'y':
            break
        else:
            try:
                num = int(input("Rasm indeksini kiriting: "))
                if 0 <= num < len(res):
                    os.remove(os.path.join(folder, res[num]))
                    print("O'chirildi")
                    res.pop(num)
                else:
                    print("Noto'g'ri indeks!")
            except Exception as e:
                print(f"xato: {e}")

if __name__ == "__main__":
    yuklash()