#made by IvanLiu (yanjun)
#系統需求: Macbook Arm, 32GB RAM (未滿，請勿嘗試)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://kham.com.tw/application/UTK02/UTK0201_.aspx?PRODUCT_ID=P10APX87"
driver.get(url)

wait = WebDriverWait(driver, 10)

def safe_click(by, value, desc, retries=3, sleep_time=2, skip_if_fail=False):
    """try click element with retry+refresh, optionally skip if fail"""
    for i in range(retries):
        try:
            btn = wait.until(EC.element_to_be_clickable((by, value)))
            btn.click()
            print(f"✅ clicked {desc}")
            return True
        except Exception as e:
            if skip_if_fail:
                print(f"⚠️ skip {desc}, cannot click")
                return False
            print(f"⚠️ fail {desc}, retry {i+1}/{retries}")
            driver.refresh()
            time.sleep(sleep_time)
    return False

ok_xpath = "//button[contains(@class,'ui-button') and text()='Ok']"
safe_click(By.XPATH, ok_xpath, "OK btn", retries=1, sleep_time=1)

safe_click(By.ID, "GO_BUY", "buy btn", retries=5, sleep_time=2)

date_xpath = "//button[contains(text(),'2025/08/26(二)12:00 啟售')]"
print("⏳ start trying to click sale button...")
while True:
    try:
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        btn.click()
        print("✅ clicked sale button! proceed to next step")
        break
    except:
        print("⚠️ click failed, retrying...")
        time.sleep(1)

print("🪬剩下的請手動操作")
time.sleep(9999)
driver.quit()
3
