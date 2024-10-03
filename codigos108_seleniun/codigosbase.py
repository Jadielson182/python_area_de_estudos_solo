from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVE_EXE = ROOT_FOLDER / 'drives' / 'chromedriver.exe'
 
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=CHROMEDRIVE_EXE)
crhome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)
crhome_browser.get('https://www.google.com/')
time.sleep(20)


# chrome_options.add_argument()
