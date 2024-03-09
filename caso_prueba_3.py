from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.NAME, "search")
    search_term = "Universidad Iberoamericana (UNIBE)"
    search_input.send_keys(search_term)
    search_input.send_keys(Keys.RETURN)

    wait.until(EC.title_contains("Universidad Iberoamericana (UNIBE)"))

    language_dropdown_button = wait.until(EC.element_to_be_clickable((By.ID, "p-lang-btn")))
    language_dropdown_button.click()

    english_language_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "English")))
    english_language_link.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html[lang="en"]')))
    assert "English" in driver.title

finally:
    time.sleep(5)
    driver.quit()