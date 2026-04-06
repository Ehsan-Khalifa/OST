from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

time.sleep(2)

driver.maximize_window()

search_box = wait = WebDriverWait(driver, 10)
search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)
search_box.send_keys("open source software")

search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
