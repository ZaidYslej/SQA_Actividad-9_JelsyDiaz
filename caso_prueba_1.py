from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.NAME, "search")
    search_term = "Universidad Iberoamericana (UNIBE)"
    search_input.send_keys(search_term)
    search_input.send_keys(Keys.RETURN)
    
    wait = WebDriverWait(driver, 15)
    first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.mw-search-result-heading a')))
    
    first_result.click()
    
    wait.until(EC.presence_of_element_located((By.ID, 'firstHeading')))
    assert search_term in driver.title, "El título del artículo no coincide con el término de búsqueda."
finally:
    driver.quit()