import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Folder to save downloaded posters
save_dir = "animation4test"
os.makedirs(save_dir, exist_ok=True)

# Open Chrome browser
driver = webdriver.Chrome()
driver.get("https://letterboxd.com/films/popular/genre/animation%20-action%20-adventure%20-comedy%20-crime%20-documentary%20-drama%20-family%20-fantasy%20-history%20-horror%20-music%20-mystery%20-romance%20-science-fiction%20-thriller%20-tv-movie%20-war%20-western/page/4/")

poster_urls = []

total_posters = 1350
current_page = 1

while len(poster_urls) < total_posters:
    print(f"Processing page {current_page}...")

    WebDriverWait(driver, 13).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 5);")
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    posters = soup.find_all("li", class_="poster-container")

    count_this_page = 0
    for index, poster in enumerate(posters):
        link = poster.find("a", class_="frame")
        if link:
            film_url = "https://letterboxd.com" + link.get("href")

            driver.get(film_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            img_link = soup.find("a", {"data-js-trigger": "postermodal"})
            if img_link:
                img_url = img_link.get("href")

                if img_url and img_url not in poster_urls:
                    poster_urls.append(img_url)
                    img_data = requests.get(img_url).content
                    file_name = os.path.join(save_dir, f"poster_{len(poster_urls)}.jpg")
                    with open(file_name, "wb") as f:
                        f.write(img_data)
                    print(f"Poster {len(poster_urls)} downloaded: {img_url}")
                    count_this_page += 1

            driver.back()
            time.sleep(2)

        if len(poster_urls) >= total_posters:
            break

    print(f"{count_this_page} posters downloaded and saved (Page {current_page})")

    # Go to the next page
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.paginate-nextprev a.next"))
        )
        next_button.click()
        current_page += 1
        time.sleep(3)
    except Exception as e:
        print(f"Could not click next button: {e}")
        break

driver.quit()

print(f"A total of {len(poster_urls)} posters have been successfully downloaded and saved to the '{save_dir}' folder.")
