from .database import store_call_in_db
import time
import sys
from bs4 import BeautifulSoup
import colorama

def extract_call_data(driver, conn):
    seen_calls = set()  # To avoid storing duplicate calls
    
    print(colorama.Fore.YELLOW + "Starting call extraction (Press CTRL+C to stop)" + colorama.Fore.RESET)

    try:
        while True:
            # Get page source and parse with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # Find all call elements
            call_elements = soup.find_all("div", class_="content__235ca")

            for element in call_elements:
                # Extract username
                username_element = element.find("span", class_="username__703b9")
                if not username_element:
                    continue
                username = username_element.text

                # Extract call duration
                call_text = element.get_text()
                duration_text = call_text.split("lasted ")[1].split(".")[0] if "lasted " in call_text else ""

                # Extract timestamp
                timestamp_element = element.find("time")
                timestamp = timestamp_element.get("datetime") if timestamp_element else ""

                # Unique call identifier (to avoid duplicates)
                call_id = f"{username}-{duration_text}-{timestamp}"
                if call_id in seen_calls:
                    continue  # Skip already processed calls

                # Store the extracted data immediately
                call = {
                    "username": username,
                    "duration": duration_text,
                    "timestamp": timestamp
                }
                store_call_in_db(conn, call)  # Store in DB instantly

                # Print in green to make it more visible
                print(colorama.Fore.LIGHTBLUE_EX + "Extracted call: " + colorama.Fore.RESET + str(call) )

                # Mark this call as seen
                seen_calls.add(call_id)

            # Scroll up
            driver.execute_script("window.scrollTo(0, 0);")

            # Wait for content to load
            time.sleep(1)

    except KeyboardInterrupt:
        print(colorama.Fore.YELLOW + "Stopping call extraction..." + colorama.Fore.RESET)
        sys.exit(0)
