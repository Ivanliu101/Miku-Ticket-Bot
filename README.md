# Miku Ticket Bot 🎫✨
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

## 系統需求
macbook Arm    
32GB RAM  
Chrome.app  

## 🌟 Overview
Miku Ticket Bot is a Python-based automation tool that helps users quickly navigate the ticketing website for Miku concerts.  
It automatically clicks through the steps until the ticket selection page, allowing you to manually fill in your details afterward.
url = https://kham.com.tw/application/UTK02/UTK0201_.aspx?PRODUCT_ID=P10APX87

## 🛠 Features
- Automatically click the initial "OK" popup
- Click "我要購票" (Buy Ticket) button
- Keep trying the sale date button until it becomes clickable
- Browser remains open after automation so you can manually complete ticket purchase

## ⚡ Tech Stack
- Python 3.x
- Selenium WebDriver
- Chrome + ChromeDriver
- Webdriver Manager (auto installs chromedriver)

## 🚀 Usage
1. Install required packages:
```bash
pip install selenium webdriver-manager
