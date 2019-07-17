from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        googleLogo_image = self.driver.find_element(
            *MainPageLocators.googleLogo_image)
        return googleLogo_image.is_displayed()

    def click_image_button(self):
        """Triggers the search"""
        camera_button = self.driver.find_element(
            *MainPageLocators.camera_button)
        camera_button.click()
        self.driver.implicitly_wait(1)

    def search_image_by_url(self, image_url):
        imageurl_text_field = self.driver.find_element(
            *MainPageLocators.imageUrl_textFiled)
        imageurl_text_field.send_keys(image_url)
        searchbyimage_button = self.driver.find_element(
            *MainPageLocators.searchByImage_button)
        searchbyimage_button.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def visit(self, visit_result):
        cell_links_xpath = SearchResultsPageLocators.matching_results.format(
            visit_result)
        search_result_cell_links = self.driver.find_elements_by_xpath(
            cell_links_xpath)
        if search_result_cell_links:
            search_result_cell_links[0].click()

    def wait_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body")))

    def is_related_to(self, image_content):
        return len([x for x in image_content if x in self.driver.page_source]) > 0
