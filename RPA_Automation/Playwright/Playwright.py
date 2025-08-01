import os
import time
import openpyxl
from playwright.sync_api import sync_playwright


SEARCH_QUERY = "Painless heel shoes"
AMAZON_URL = "https://www.amazon.in"

# Setup Excel
excel_file = "amazon_products.xlsx"
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Products"
ws.append(["Title", "Price", "Rating", "Product URL"])

# Setup text file
text_file = open("amazon_products.txt", "w", encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("🌐 Opening Amazon...")
    page.goto(AMAZON_URL)

    print(f"🔍 Searching for: {SEARCH_QUERY}")
    page.fill("input[name='field-keywords']", SEARCH_QUERY)
    page.press("input[name='field-keywords']", "Enter")
    page.wait_for_load_state("load")  # or "domcontentloaded"

    #page.wait_for_load_state("networkidle")

    product_blocks = page.locator("div.s-main-slot div[data-component-type='s-search-result']")
    count = min(product_blocks.count(), 3)  # Limit to first 20 results

    for i in range(count):
        product = product_blocks.nth(i)

        try:
            title = product.locator("h2 span").inner_text()
        except:
            title = "N/A"

        try:
            url = product.locator("h2 a").get_attribute("href")
            full_url = "https://www.amazon.in" + url if url else "N/A"
        except:
            full_url = "N/A"

        try:
            price = product.locator(".a-price .a-offscreen").first.inner_text()
        except:
            price = "N/A"

        try:
            rating = product.locator("span.a-icon-alt").first.inner_text()
        except:
            rating = "N/A"

        print(f"[{i+1}] {title}")
        print(f"     Price: {price}, Rating: {rating}")
        print(f"     URL: {full_url}")

        # Write to Excel
        ws.append([title, price, rating, full_url])

        # Write to text file
        text_file.write(f"\n--- Product {i+1} ---\n")
        text_file.write(f"Title: {title}\n")
        text_file.write(f"Price: {price}\n")
        text_file.write(f"Rating: {rating}\n")
        text_file.write(f"URL: {full_url}\n")

    browser.close()

# Save output
wb.save(excel_file)
text_file.close()
print("\n✅ Scraping complete! Data saved to:")
print(f"   📄 Excel: {excel_file}")
print(f"   📄 Text : amazon_products.txt")