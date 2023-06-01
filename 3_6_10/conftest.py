import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='chrome',
                     help="Choose browser:  '--browser_name=chrome' or  '--browser_name=firefox'")
    parser.addoption("--language", action="store", default='en',
                     help="Choose language: '--language=en' or '--language=fr' or '--language=ru'")

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(service=service, options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()