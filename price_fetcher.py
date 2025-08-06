from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_live_price(asset_name="EURUSD"):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://olymptrade.com/platform")
        time.sleep(6)

        # Select asset (update selector if needed)
        asset_button = driver.find_element(By.XPATH, f"//div[contains(text(), '{asset_name}')]")
        asset_button.click()
        time.sleep(3)

        # Get live price
        price_element = driver.find_element(By.XPATH, '//div[contains(@class, "price-value")]')
        price = float(price_element.text.replace(',', ''))
        return price
    except Exception as e:
        print(f"[PriceFetcher] Error fetching price for {asset_name}: {e}")
        return None
    finally:
        driver.quit()
