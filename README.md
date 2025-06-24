# Automated HR Email Scraper and Job Application Sender

This repository contains a Python-based solution to:

- Scrape company websites from a given page.
- Discover HR-related email addresses from these websites.
- Automatically send a job application email with an attachment.

## 📂 Project Structure

- `webScrapingSite.py`  
  Scrapes a table of company websites from a given URL and saves them to `siteler.csv`.

- `scrapingMail.py`  
  Visits each site from `siteler.csv`, navigates to potential contact/career pages, and extracts HR-related email addresses. Saves the results to `ik_mailleri.csv`.

- `sendMail.py`  
  Reads `ik_mailleri.csv` and sends a pre-designed HTML email with an attached PDF (resume) to each HR contact.

## ⚙️ Requirements

requests beautifulsoup4 python-dotenv

## 🔑 Environment Variables

Create a `.env` file in the project root:
\`\`\`
SMTP_SERVER=smtp.yourprovider.com
SMTP_PORT=465
SENDER_EMAIL=your-email@example.com
SENDER_PASSWORD=your-email-password
\`\`\`

⚠️ **Security Tip:** Use an app-specific password or token instead of your main email password.

## 🚀 How to Run

1️⃣ Scrape company websites:
\`\`\`bash
python webScrapingSite.py
\`\`\`
Generates `siteler.csv`.

---

2️⃣ Scrape HR emails:
\`\`\`bash
python scrapingMail.py
\`\`\`
Generates `ik_mailleri.csv`.

---

3️⃣ Send applications:
\`\`\`bash
python sendMail.py
\`\`\`
Sends emails with your resume.

## 📌 Notes

✅ The email is sent **to your own email address (\`SENDER_EMAIL\`)** for testing purposes. Update `send_email()` in `sendMail.py` if you want to send to scraped HR emails.

✅ The email content is generated with a clean HTML template in `build_html_body()`.

✅ A `cv.pdf` file should exist in the same directory.

## 🛡 Disclaimer

- This tool is designed for educational purposes.
- Please use responsibly and comply with GDPR / KVKK and other local data protection laws.
- Make sure you have permission before contacting companies.

## 🌐 Author

[Davut Samet Kaplan](https://www.dsametkaplan.com.tr)  
[GitHub Profile](https://github.com/dsametkaplan)

---

💼 **Feel free to contribute or open issues!**
