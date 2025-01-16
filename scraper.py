import time
import json
import random
import requests
import uuid
import pymongo
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# ProxyMesh settings
PROXY_LIST = [
    "proxy1.proxymesh.com:31280",
    "proxy2.proxymesh.com:31280"
]

# MongoDB setup
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["stir_tech"]
collection = db["trending_topics"]

def get_random_proxy():
    return random.choice(PROXY_LIST)

def scrape_twitter():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument(f"--proxy-server={get_random_proxy()}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://twitter.com/home")
        time.sleep(5)  # Wait for page to load
        
        # Login to Twitter manually before running script OR automate login
        trends = driver.find_elements(By.XPATH, "//section[contains(@aria-label,'Trending')]//span")[:5]
        trending_topics = [trend.text for trend in trends]

        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = requests.get("https://api64.ipify.org?format=json").json()["ip"]

        data = {
            "_id": unique_id,
            "trend1": trending_topics[0] if len(trending_topics) > 0 else "",
            "trend2": trending_topics[1] if len(trending_topics) > 1 else "",
            "trend3": trending_topics[2] if len(trending_topics) > 2 else "",
            "trend4": trending_topics[3] if len(trending_topics) > 3 else "",
            "trend5": trending_topics[4] if len(trending_topics) > 4 else "",
            "timestamp": timestamp,
            "ip_address": ip_address
        }

        collection.insert_one(data)
        driver.quit()
        return data

    except Exception as e:
        driver.quit()
        return {"error": str(e)}

if __name__ == "__main__":
    print(scrape_twitter())
