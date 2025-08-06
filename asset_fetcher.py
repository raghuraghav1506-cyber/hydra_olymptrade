from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_available_assets():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://olymptrade.com/platform")
        time.sleep(6)  # Wait for assets to load

        # Find asset elements (update selector if needed)
        asset_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "asset-name")]')
        assets = [el.text.strip() for el in asset_elements if el.text.strip()]
        return list(set(assets))  # Remove duplicates
    except Exception as e:
        print(f"Error fetching assets: {e}")
        return []
    finally:
        driver.quit()
