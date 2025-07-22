# RPA Automation Examples

This repository contains examples of Robotic Process Automation (RPA) using different Python frameworks including Playwright, Selenium, and PyAutoGUI.

## 🚀 Projects

### 1. Amazon Product Scraper (Playwright)
Located in [RPA_Automation/Playwright/](RPA_Automation/Playwright/):
- Scrapes product information from Amazon India
- Saves data to both Excel and text files
- Captures product title, price, rating, and URLs

### 2. WhatsApp Web Automation (Selenium)
Located in [RPA_Automation/Selenium/](RPA_Automation/Selenium/):
- Automates WhatsApp Web message sending
- Includes QR code scanning pause
- Handles popups and dynamic content loading

### 3. Mouse Automation (PyAutoGUI)
Located in [RPA_Automation/pyautogui/](RPA_Automation/pyautogui/):
- Demonstrates mouse movement and clicking
- Shows keyboard input automation
- Includes position tracking functionality

## 🛠️ Setup

1. Create a virtual environment:
```sh
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```sh
venv\Scripts\activate
```
- Unix/MacOS:
```sh
source venv/bin/activate
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

## 📦 Dependencies

- Playwright
- Selenium
- PyAutoGUI
- OpenPyXL
- Other dependencies listed in requirements.txt

## 🚦 Running the Projects

### Playwright Amazon Scraper:
```sh
python RPA_Automation/Playwright/Playwright.py
```

### Selenium WhatsApp Automation:
```sh
python RPA_Automation/Selenium/Selenium_demo.py
```

### PyAutoGUI Demo:
```sh
python RPA_Automation/pyautogui/pyautogui_demo.py
```

## 📝 Notes

- Make sure to have Chrome browser installed for Selenium scripts
- Playwright will install browsers automatically
- For WhatsApp automation, you'll need to scan the QR code manually
- The PyAutoGUI script contains both active and commented example code

## 🔒 .gitignore

The repository includes a comprehensive .gitignore file that excludes:
- Python cache files
- Virtual environments
- IDE specific files
- Log files
- Build directories
