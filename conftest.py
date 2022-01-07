import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup(request):
    """ setup : entry point for the project
        install and configures the chrome driver as per defined specifications
    """
    _driver = None
    options = webdriver.ChromeOptions()

    # To avoid undesired logging on console
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # To opt notification block option
    options.add_argument("--disable-infobars")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    options.add_argument("start-maximized")
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-extensions")

    # download and install latest version of chrome driver  automatically
    # Note - may take time to download in case current version is not found in cache
    _driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    _driver.implicitly_wait(10)
    _driver.set_page_load_timeout(30)
    print("Launching Chrome...")

    # maximise the window
    _driver.maximize_window()
    request.cls.driver = _driver
