#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Provide the full path to the Chrome driver executable
driver_path = 'C:/path/to/chromedriver.exe'

# Set Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--webdriver.chrome.driver=" + driver_path)

# Create the WebDriver instance using the specified options
driver = webdriver.Chrome(options=chrome_options)

# Step 1: Go to "https://amazon.in"
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

# Step 2: Search for "Wrist Watches" with specific filters
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Wrist Watches")

# Filter: Display - Analogue
try:
    display_analogue_checkbox = driver.find_element(By.XPATH, "//span[contains(text(), 'Analogue')]/../preceding-sibling::input")
    display_analogue_checkbox.click()
except NoSuchElementException:
    print("Element for 'Analogue' filter not found.")

# Filter: Brands Material - Leather
try:
    brands_material_leather_checkbox = driver.find_element(By.XPATH, "//span[contains(text(), 'Leather')]/../preceding-sibling::input")
    brands_material_leather_checkbox.click()
except NoSuchElementException:
    print("Element for 'Leather' filter not found.")

# Filter: Brand - Titan
try:
    brand_titan_checkbox = driver.find_element(By.XPATH, "//span[contains(text(), 'Titan')]/../preceding-sibling::input")
    brand_titan_checkbox.click()
except NoSuchElementException:
    print("Element for 'Titan' filter not found.")

# Filter: Discount - "25% Off or more"
try:
    discount_checkbox = driver.find_element(By.XPATH, "//span[contains(text(), '25% Off or more')]/../preceding-sibling::input")
    discount_checkbox.click()
except NoSuchElementException:
    print("Element for 'Discount' filter not found.")

search_box.send_keys(Keys.RETURN)

# Step 3: Get the Fifth Element from the search
try:
    fifth_element = driver.find_element(By.XPATH, "(//div[@class='sg-col-inner']//span[@class='a-size-medium a-color-base a-text-normal'])[5]")
    print("Fifth Element:", fifth_element.text)
except NoSuchElementException:
    print("Fifth element not found.")

# Close the browser
driver.quit()

