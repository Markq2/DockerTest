import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Choose lang')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_argument('--headless')
        option_chrome.add_argument('--window-size=1920,1200')
        option_chrome.add_experimental_option('excludeSwitches',
                                              ['enable-logging'])
        option_chrome.add_experimental_option(
                                    'prefs',
                                    {'intl.accept_languages': user_language})
        service = Service()
        browser = webdriver.Chrome(
            service=service,
            # service=Service(ChromeDriverManager().install()),
            options=option_chrome)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        option_firefox = webdriver.FirefoxOptions()
        option_firefox.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        option_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(executable_path=r'C:\foxdriver\geckodriver.exe', options=option_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

    def pytest_make_parametrize_id(config, val): return repr(val)
