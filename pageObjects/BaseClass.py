import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as ec

class BaseClass:
    """
    Base class contains keyword functions used by all the page object classes
    """

    def __init__(self, driver):
        """__init__ function :is private member function of this class  """
        self.driver = driver
        self.wait_time_out = 30
        self.webWait = ww(self.driver, self.wait_time_out)

    def click(self, byObj):
        """ click : to click a html element """
        self.webWait.until(ec.element_to_be_clickable(byObj)).click()

    def enter_text(self, byObj, txt):
        """enter_text : to enter text in text fields"""
        self.webWait.until(ec.element_to_be_clickable(byObj)).send_keys(txt)

    def click_enter(self, byObj):
        """click_enter : to enter the return key in text fields"""
        self.webWait.until(ec.element_to_be_clickable(byObj)).send_keys(Keys.ENTER)

    def select_frame(self, frameObj):
        """select_frame : to switch to a frame"""
        self.webWait.until(ec.frame_to_be_available_and_switch_to_it(frameObj))

    def switch_to_default_frame(self):
        """switch_to_default_frame : to switch back onto a main frame"""
        self.driver.switch_to.default_content()

    def get_list_of_links(self):
        """get_list_of_links : to get list of links on search result page"""
        results = self.webWait.until(ec.element_to_be_clickable((By.CLASS_NAME, "results-wrapper")))
        list_of_articles = results.find_elements_by_class_name("title")

        return list_of_articles

    def is_element_present(self, how, what):
        """is_element_present : returns true if element is present else return false"""
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def verify_title(self, expected_Title):
        """verify_title : return if the current page title is same as expected_title else return fales """
        actual_title = ""
        try:
            actual_title = self.driver.title
            assert  actual_title == expected_Title
            print("Title Verification Pass : expected [" + expected_Title+"]")
            return True
        except:
            print("Title Verification Fail : expected [" + expected_Title+"], however, found ["+actual_title+"]")
            return False

    def scroll_to_locale(self):
        """scroll_to_locale : to select the language"""
        self.click((By.CSS_SELECTOR, "#language-dropdown-flag img"))
        self.driver.execute_script("document.getElementById('nav-languages').scrollDown += 5000")
        time.sleep(10)


