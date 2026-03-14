from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
from datetime import datetime

def convert_to_degrees(value):
    """Конвертация координат из формата EXIF в десятичные градусы"""
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def analyze_and_save(img_path):
    if not os.path.exists(img_path):
        print("[-] Файл не найден.")
        return

    report_content = []
    
    def log(text):
        """Функция для одновременного вывода в консоль и накопления данных для файла"""
        print(text)
        report_content.append(text)

    try:
        img = Image.open(img_path)
        exif_data = img._getexif()
        
        log(f"\n{'='*60}")
        log(f"ОТЧЕТ АНАЛИЗА ФАЙЛА: {os.path.basename(img_path)}")
        log(f"Дата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log(f"{'='*60}\n")

        summary = {
            "Производитель": "Неизвестно",
            "Устройство": "Неизвестно",
            "Дата съемки": "Не найдена",
            "Местоположение": "Отсутствует",
            "ПО/Редактор": "Системное/Оригинал",
            "ISO": "Нет данных",
            "Диафрагма": "Нет данных"
        }

        if exif_data:
            log("[*] Извлечение сырых EXIF данных...")
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                
                if tag == "Make": summary["Производитель"] = value
                if tag == "Model": summary["Устройство"] = value
                if tag == "DateTimeOriginal": summary["Дата съемки"] = value
                if tag == "Software": summary["ПО/Редактор"] = value
                if tag == "ISOSpeedRatings": summary["ISO"] = value
                if tag == "FNumber": summary["Диафрагма"] = f"f/{value}"
                if tag == "GPSInfo":
                    try:
                        lat = convert_to_degrees(value[2])
                        if value[1] == 'S': lat = -lat
                        lon = convert_to_degrees(value[4])
                        if value[3] == 'W': lon = -lon
                        summary["Местоположение"] = f"{lat},{lon}"
                    except:
                        summary["Местоположение"] = "Ошибка парсинга координат"

                log(f" [RAW] {tag:25}: {value}")
        else:
            log("[-] EXIF данные не обнаружены.")
        log("\n----Самое важное:")
        
        loc = summary["Местоположение"]
        log(f"Местоположение: {loc}")
        if loc != "Отсутствует":
            log(f"[!] Ссылка на карту: https://www.google.com/maps?q={loc}")
        
        log(f"Дата и время: {summary['Дата съемки']}")   
        log(f"У-во: {summary['Производитель']} {summary['Устройство']}")
    
        soft = summary['ПО/Редактор']
        log(f"Программная подпись: {soft}")
        if any(x in str(soft).lower() for x in ["adobe", "photoshop", "gimp", "canva", "picsart"]):
            log("⚠️ Обнаружены следы графического редактора")
        else:
            log("Вероятно, оригинальный файл без редактирования")
        log("developed by https://github.com/arivvs")

        filename = "osint-report.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n".join(report_content) + "\n\n")
        print(f"\nОтчет успешно сохранен в: {filename}")

    except Exception as e:
        print(f"[!] Критическая ошибка: {e}")

if __name__ == "__main__":
    file_path = input("Введите полный путь к фото: ").strip('"')
    analyze_and_save(file_path)