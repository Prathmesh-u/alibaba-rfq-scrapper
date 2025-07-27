from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Initialize Chrome
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Optional: run silently

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Target URL
base_url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y"
driver.get(base_url)
time.sleep(5)  # allow page to fully load

# Prepare CSV
csv_file = open("alibaba_rfq_scraped.csv", "w", newline='', encoding="utf-8-sig")
writer = csv.writer(csv_file)
writer.writerow(["Title", "Description", "Quantity", "Country", "Quotes Left", "Posted", "Buyer Name", "Quote URL"])

page = 1
while True:
    print(f"📄 Scraping Page {page}...")
    time.sleep(4)  # Give JS time to load content

    rfq_cards = driver.find_elements(By.CSS_SELECTOR, "div.brh-rfq-item")

    if not rfq_cards:
        print("❌ No RFQs found. Possibly end of pagination.")
        break

    for card in rfq_cards:
        try:
            title = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__subject-link").text.strip()
            desc = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__detail").text.strip()
            quantity = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quantity-num").text.strip()
            country = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__country").text.strip()
            quotes_left = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quote-left span").text.strip()
            posted = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__publishtime").text.strip()
            buyer_name = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__other-info .text").text.strip()
            quote_url = card.find_element(By.CSS_SELECTOR, ".brh-rfq-quote-now a").get_attribute("href")

            writer.writerow([title, desc, quantity, country, quotes_left, posted, buyer_name, quote_url])
        except Exception as e:
            print(f"⚠️ Error scraping RFQ: {e}")

    # Try to click "Next" button
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, ".next-pagination .next-btn.next-medium.next-btn-normal.next-pagination-item.next")
        if "next-disabled" in next_btn.get_attribute("class"):
            print("✅ Reached last page.")
            break
        else:
            next_btn.click()
            page += 1
    except Exception as e:
        print("❌ 'Next' button not found or pagination ended.")
        break

driver.quit()
csv_file.close()
print("✅ Scraping Complete! Output saved to 'alibaba_rfq_scraped.csv'")
