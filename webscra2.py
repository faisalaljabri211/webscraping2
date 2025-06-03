from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# 🔧 إعداد متصفح Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 📍 افتح الموقع
driver.get("https://books.toscrape.com/")
time.sleep(2)

# 📦 قائمة لحفظ بيانات الكتب
books = []

# 🔄 ابحث عن كل الكتب في الصفحة
book_elements = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

for book in book_elements:
    # 📘 العنوان
    title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")

    # 💰 السعر
    price = book.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()

    # 📦 التوفر
    availability = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()

    # ⭐ التقييم (مثل: "One", "Three", ...)
    star_element = book.find_element(By.CSS_SELECTOR, "p.star-rating")
    star_rating = star_element.get_attribute("class").s_
