from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_products():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    url = "https://books.toscrape.com/"
    driver.get(url)

    products = []
    for item in driver.find_elements(By.CLASS_NAME, "product_pod")[:10]:
        title = item.find_element(By.TAG_NAME, "h3").text
        price = item.find_element(By.CLASS_NAME, "price_color").text
        availability = item.find_element(By.CLASS_NAME, "availability").text.strip()
        rating = item.get_attribute("class").split()[-1]
        image = item.find_element(By.TAG_NAME, "img").get_attribute("src")
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

        products.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "image_url": image,
            "product_page": link
        })

    driver.quit()
    return products
