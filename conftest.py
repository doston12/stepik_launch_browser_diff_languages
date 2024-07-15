# main conftest.py file for the whole project
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def pytest_addoption(parser):
    parser.addoption("--language", action="store",
                     default=None, help="Choose the language to load the website in")


@pytest.fixture(scope="function")
def browser(request):
    logging.debug("\nStarting the browser...")
    language = request.config.getoption("language")
    logging.debug(f"Website will be loaded in the language: {str(language)}")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': str(language)})

    browser = webdriver.Chrome(options=options)

    url = f"http://selenium1py.pythonanywhere.com/{str(language)}/catalogue/coders-at-work_207/"
    logging.debug("Opening url: %s", url)
    browser.get(url)

    yield browser

    logging.debug("\nQuitting the browser...")
    browser.quit()
