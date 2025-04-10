# Selenium Login Automation Script

This repository contains a Python script that automates the login process for a website using **Selenium WebDriver**. It interacts with the login form, switches to a new tab after clicking the login button, and fills in the credentials to log in.

## Features
- Supports full browser window manipulation to prevent UI issues like hidden elements in the mobile menu.
- Automates the login process on the target website.
- Waits for elements to be visible or clickable before interacting with them.
- Switches to a newly opened tab after the login button is clicked.
- Works with **Chrome WebDriver**.

## Prerequisites
Before you run the script, make sure you have the following installed:

- **Python 3.x**
- **Selenium**: For web automation. You can install it using pip:
  ```bash
  pip install selenium
