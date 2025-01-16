# Twitter Trending Scraper - Stir Tech Internship Task

## 📌 Overview
This project automates **Twitter trending topic scraping** using **Selenium** and stores the data in **MongoDB** with **ProxyMesh** for IP rotation. A simple **Flask web app** allows users to trigger the scraper and display the results dynamically.

## 🚀 Features
- ✅ **Selenium Automation**: Scrapes the top 5 trending topics from Twitter.
- ✅ **ProxyMesh Integration**: Uses rotating proxies to fetch data from different IPs.
- ✅ **MongoDB Storage**: Saves scraped data with a unique ID, timestamp, and IP address.
- ✅ **Flask Web App**: Provides a button to trigger scraping and display results in HTML.

Use MongoDB Atlas (cloud) or install MongoDB locally.
Create a database called stir_tech and a collection named trending_topics.
Write this command in terminal
pip install selenium pymongo flask webdriver-manager requests

Step 1:Run MongoDB if it's installed locally:
Step 2: Run Flask Server
Step 3: Open in Browser
Click "Run Script" to trigger Selenium.

