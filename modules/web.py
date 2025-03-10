from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
import colorama

# Function to setup discord browser
def setup_discord_browser():
    options = Options()
    
    # Create a user profile
    user_data_dir = os.path.join(os.getcwd(), "data/selenium_browser_profile")
    os.makedirs(user_data_dir, exist_ok=True)
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://discord.com/login")
    
    # Let the user login manually
    print(colorama.Fore.GREEN + "Please log in to Discord. The program will continue once you're logged in." + colorama.Fore.RESET)
    
    # Wait for Discord to fully load by looking for the friends button container
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='friendsButtonContainer']"))
    )
    
    return driver

# Function that navigates browser to link
def navigate_to_link(driver, link):
    driver.get(link)
    print(colorama.Fore.YELLOW + f"Navigated to link: {link}" + colorama.Fore.RESET)
    time.sleep(3)  