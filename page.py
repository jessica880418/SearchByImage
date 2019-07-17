from element import BasePageElement
from locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        googleLogo_image = self.driver.find_element(*MainPageLocators.googleLogo_image)
        return googleLogo_image.is_displayed()

    def click_image_button(self):
        """Triggers the search"""
        camera_button = self.driver.find_element(*MainPageLocators.camera_button)
        camera_button.click()
        self.driver.implicitly_wait(1)

    def input_imageurl_andgo(self, image_url):
        imageurl_text_field = self.driver.find_element(*MainPageLocators.imageUrl_textFiled)
        imageurl_text_field.send_keys(image_url)
        searchbyimage_button = self.driver.find_element(*MainPageLocators.searchByImage_button)
        searchbyimage_button.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def visit(self, visit_result):
        matching_results = self.driver.find_element(*MainPageLocators.matching_results)
        visit_page = '/div[visit_result]'
        visit_page.click()



