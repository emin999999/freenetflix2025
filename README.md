# Netflix 2.0
# Emin INC.

**Legal Issues: Violating Netflix's terms of use may result in your account being permanently terminated. We strongly recommend you turn on a VPN!**


# Please For Understand in all languages Use Translate! -----> https://translate.google.com/


![Netflix](https://i.pinimg.com/originals/bb/74/04/bb74046420c4c992b8cabc6e667abe40.gif)



# This project is used to get a free Netflix account. It is for entertainment purposes. Do not use it for malicious purposes!

$$$$$$$$$$$$$$$$$$$$$$$$$$

# Functions of the files;

**netflix generator.py: Main Python script used to create Netflix accounts.**

**netflix checker.py: Python script used to check created Netflix accounts.**

**netflix checker rgb.py: [Run as RGB] Python script used to check created Netflix accounts.**

**netflix.txt: A text file listing created or checked Netflix accounts.**

**netflix_worksAcc.txt: A text file listing valid and working Netflix accounts.**

**listAcc.txt: A text file listing accounts to be checked or created.**

This Python code uses Selenium and some additional libraries. The required libraries are:

1. **Selenium**: Used for web automation. It is required for opening web pages, filling out forms, clicking buttons and performing actions on the page.

2. **WebDriver**: Used to control a web browser with Selenium. In this example, `chromedriver` is required because the Chrome browser is used. If you are going to use another browser (Firefox, Edge etc.), you will need to download the appropriate WebDriver for it.

3. **time**: Used to make the code wait for a certain amount of time (for example, to wait for the page to load).

### Required Libraries:
1. **Selenium**:
```bash
pip install selenium
```

2. **WebDriver (Chrome)**:
- For WebDriver, you need to download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/). You should download the version that is suitable for your Chrome version and install it on your computer.

- You can also use `webdriver-manager` for WebDriver. This will automatically help you download and install the required WebDriver version:
```bash
pip install webdriver-manager
```

3. **time**: Since it is a built-in module of Python, you do not need to install it separately.

### Using ChromeDriver and Selenium:
If you want to automatically download and install ChromeDriver using `webdriver-manager`, you can update the code as follows:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# Download and start ChromeDriver automatically
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.netflix.com/login')
```

In this way, you do not need to download and install ChromeDriver manually, `webdriver-manager` will automatically download and run it for you.

### Conclusion:
After installing these libraries and tools, you can use Selenium and WebDriver without any problems.
