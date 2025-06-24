import requests
from bs4 import BeautifulSoup
import re
import csv
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}
PATHS = [
    "",
    "/iletisim",
    "/contact",
    "/contact-us",
    "/contactus",
    "/contact_us",
    "/bize-ulasin",
    "/bizimle-iletisim",
    "/bizimle-iletisime-gecin",
    "/insan-kaynaklari",
    "/ik",
    "/kariyer",
    "/kariyer-firsatlari",
    "/human-resources",
    "/hr",
    "/jobs",
    "/careers",
    "/hakkimizda",
    "/about-us",
    "/aboutus",
    "/about_us",
    "/kurumsal",
    "/kurumsal-iletisim",
    "/kurumsal_iletisim",
    "/support",
    "/destek",
    "/yardim",
    "/iletisim-formu",
    "/en/iletisim",
    "/en/contact",
    "/en/careers",
    "/en/human-resources"
]

def extract_emails(text):
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return list(set(emails))

def find_hr_email(site):
    hr_email = ""
    try:
        for path in PATHS:
            url = site.rstrip("/") + path
            print(f"Taranıyor: {url}")
            resp = requests.get(url, headers=HEADERS, timeout=5)
            if resp.status_code != 200:
                continue
            emails = extract_emails(resp.text)
            for email in emails:
                if any(x in email.lower() for x in ["ik", "hr", "kariyer", "iletisim"]):
                    return email
            if not hr_email and emails:
                hr_email = emails[0]
            time.sleep(1)
    except Exception as e:
        print(f"Hata: {e}")
    return hr_email

def load_sites_from_csv(filepath):
    sites = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                sites.append(row[0].strip())
    return sites

def main():
    sites = load_sites_from_csv("siteler.csv")
    results = []
    for site in sites:
        email = find_hr_email(site)
        results.append({"Web Sitesi": site, "IK E-posta": email})
    
    with open("ik_mailleri.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Web Sitesi", "IK E-posta"])
        writer.writeheader()
        writer.writerows(results)
    
    print("CSV oluşturuldu")

if __name__ == "__main__":
    main()
