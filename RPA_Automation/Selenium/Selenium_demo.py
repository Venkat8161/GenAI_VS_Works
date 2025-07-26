from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- RPA Automation using Selenium for WhatsApp Web ---
# --- CONFIGURATION ---
contact_name = "DET 2011 RNAIPL" #Change your contact name here
message_text = "hi it's automoted your acount has been hacked" #Change your message here

# --- SETUP CHROME DRIVER ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

# --- STEP 1: QR Code Scan ---
input("🔐 Scan the QR Code on browser and press ENTER here to continue...")

# --- STEP 2: Search for Contact ---
try:
    # Wait until search box is clickable
    search_box = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )

    # Try closing any popup (like WhatsApp tips)
    try:
        close_btn = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
        close_btn.click()
        time.sleep(1)
    except:
        pass  # No popup

    # Retry click to avoid interception errors
    for attempt in range(3):
        try:
            search_box.click()
            break
        except Exception as e:
            print(f"⚠️ Search box click failed (attempt {attempt+1}): {e}")
            time.sleep(2)

    # Type the contact name and open the chat
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    print(f"✅ Opened chat with: {contact_name}")

except Exception as e:
    print(f"❌ Failed to open chat for '{contact_name}': {e}")
    driver.quit()
    exit()

# --- STEP 3: Send the Message ---
try:
    # Wait for message box to be ready (updated CSS selector for current WhatsApp)
    msg_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']"))
    )
    time.sleep(1)
    msg_box.click()
    msg_box.send_keys(message_text)
    msg_box.send_keys(Keys.ENTER)
    print("✅ Message sent successfully!")

except Exception as e:
    print(f"❌ Failed to send message: {e}")

# --- Optional: Keep browser open briefly before quitting ---
time.sleep(10)
driver.quit()