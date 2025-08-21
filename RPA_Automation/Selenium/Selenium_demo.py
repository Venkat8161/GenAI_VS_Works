from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# --- FILE SETTINGS ---
excel_path = "Msg_Details.ods"  # Change path to your file

# --- READ DATA FROM FILE ---
file_ext = os.path.splitext(excel_path)[1].lower()
if file_ext == ".ods":
    df = pd.read_excel(excel_path, engine="odf")
else:
    df = pd.read_excel(excel_path)  # For .xlsx, .xls

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check required columns
required_cols = {"Contact_Name", "Message_Text"}
if not required_cols.issubset(set(df.columns)):
    raise ValueError(f"Excel file must have columns: {required_cols}")

# --- SETUP CHROME DRIVER ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

# --- STEP 1: QR Code Scan ---
input("🔐 Scan the QR Code on browser and press ENTER here to continue...")

# --- LOOP THROUGH ALL CONTACTS ---
for index, row in df.iterrows():
    contact_name = str(row["Contact_Name"]).strip()
    message_text = str(row["Message_Text"]).strip()

    try:
        # --- STEP 2: Search for Contact ---
        search_box = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )

        # Close popup if it appears
        try:
            close_btn = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
            close_btn.click()
            time.sleep(1)
        except:
            pass

        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)

        # ✅ WAIT UNTIL CHAT TITLE MATCHES THE CONTACT
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//header//span[@dir="auto"]'),
                contact_name
            )
        )

        print(f"✅ Opened chat with: {contact_name}")

        # --- STEP 3: Send Personalized Message ---
        msg_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']"))
        )
        msg_box.click()
        msg_box.send_keys(f"Hi {contact_name}, {message_text}")
        msg_box.send_keys(Keys.ENTER)
        print(f"📨 Message sent to {contact_name}")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Could not send to '{contact_name}': {e}")
        continue

# --- Close Browser ---
print("✅ All messages processed.")
time.sleep(5)
driver.quit()