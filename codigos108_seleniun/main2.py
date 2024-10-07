from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVE_PATH = ROOT_FOLDER / 'drives' / 'chromedriver.exe'

def make_chrome_browser(*options:str)-> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path= CHROME_DRIVE_PATH,
    )
    #caso tenha erro de tipagem e so usar str('CHROME_DRIVE_PATH')
    

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
)

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # opçoes do que fazer no navegador, tem muitas opções que so deve ser usada sabendo oque vai fazer, --opção, cada opção separado por virgula
    # options = ('--check-for-update-interval, --headless') 
    options = ()
    browser = make_chrome_browser(*options)

browser.get('https://www.google.com/')
#esperar para encotra o input
search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, 'q')
    )
)
search_input.send_keys('Hello World!')
search_input.send_keys(Keys.ENTER) # quando importado o keys,o send_keys vai ativar teclas
sleep(TIME_TO_WAIT)


