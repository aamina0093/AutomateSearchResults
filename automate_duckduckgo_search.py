from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# --- Config ---
search_query = "latest trends in automation testing"
url = "https://duckduckgo.com/"

# --- Setup ---
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    # Wait and locate the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.result__a"))
    )

    # Extract results
    results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")

    print("\nTop Search Results:\n")
    for index, result in enumerate(results[:10], start=1):
        title = result.text
        link = result.get_attribute("href")
        print(f"{index}. {title}\n   {link}\n")

except Exception as e:
    print("❌ Error during automation:", str(e))

finally:
    driver.quit()
