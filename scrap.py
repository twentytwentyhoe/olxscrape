from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to the ChromeDriver
chromedriver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'

# Initialize the ChromeDriver
options = Options()
options.headless = True  # Run in headless mode (without opening a browser window)
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the specific search results page for "AirPods"
driver.get("https://www.olx.ro/oferte/q-airpods/")

# Smoothly scroll to the bottom of the page in 1 second
driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
time.sleep(1)

# Extract the titles, prices, and promotion status of the first 20 listings
listings = driver.find_elements(By.CSS_SELECTOR, "div.css-1g5933j")
for i in range(20):
    listing = listings[i]
    title_element = listing.find_element(By.CSS_SELECTOR, "h4.css-1sq4ur2")
    price_element = listing.find_element(By.CSS_SELECTOR, "p[data-testid='ad-price']")
    title = title_element.text.replace("Prețul e negociabil", "").strip()
    price = price_element.text.replace("Prețul e negociabil", "").strip()

    # Check if the listing is promoted
    try:
        promoted_element = listing.find_element(By.CSS_SELECTOR, "div.css-hiw74r")
        if "PROMOVAT" in promoted_element.text:
            title = "PROMOVAT " + title
    except:
        pass
    
    print(f"Title {i+1}: {title}, Price: {price}")

# Close the browser
driver.quit()
