import requests
from bs4 import BeautifulSoup
import csv

URL = "xxxxxxxxxxxxxx"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_firmalar():
    resp = requests.get(URL, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    firmalar = []
    # Tablodaki tüm a tag'lerini al
    for a in soup.select("table a[href]"):
        site = a['href'].strip()
        if site:
            firmalar.append({"Web Sitesi": site})
    
    return firmalar

def kaydet_csv(firmalar, dosya="siteler.csv"):
    with open(dosya, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Web Sitesi"])
        writer.writeheader()
        writer.writerows(firmalar)

if __name__ == "__main__":
    firmalar = get_firmalar()
    print(f"{len(firmalar)} site bulundu.")
    kaydet_csv(firmalar)
    print("CSV kaydedildi")
