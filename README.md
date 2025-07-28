## Alibaba RFQ Scraper 

This project is a Python-based web scraper that automatically extracts RFQ (Request for Quotation) listings from [Alibaba's RFQ sourcing portal](https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y). It collects details such as product title, description, quantity, buyer info, country, posted time, and quote links, saving all of it into a clean CSV file for further analysis or sourcing intelligence.

---

## Problem Statement

Alibaba’s RFQ sourcing platform does not offer a public API to retrieve buyer quotations. For procurement, business development, or competitive research purposes, it’s essential to have a structured and exportable view of recent RFQ activity.

---

## Solution Overview 🌍

We created a fully automated web scraper using **Python + Selenium** that:

- Navigates the dynamic RFQ listing pages.
- Extracts all relevant RFQ data across multiple pages.
- Handles missing data and pagination gracefully.
- Outputs everything into a structured CSV file.

---

## Features

- Scrapes product RFQ titles and descriptions ✅
- Extracts quantity, country, quotes left, buyer name ✅
- Handles pagination until last available page ✅
- Saves data into `alibaba_rfq_scraped.csv` ✅
- Uses `Selenium` with ChromeDriver automation ✅

---

## Tech Stack

- **Python 3**
- **Selenium** (Browser automation)
- **ChromeDriver** (Controlled via `webdriver_manager`)
- **CSV Module** (for structured output)
- **VS Code** (for development)

---

## Use Cases

- Market research for suppliers
- Competitive RFQ intelligence
- Buyer trend tracking in UAE
- Data enrichment for B2B tools


**This project is for educational and research purposes only. Always respect website terms of service before scraping.**
**- Made with curiosity and code by Prathmesh Udanshiv**

---

## Sample Output
<img width="1121" height="3241" alt="outputcsv" src="https://github.com/user-attachments/assets/2a902f25-c32f-43fa-b61a-cf41977b4cc5" />

