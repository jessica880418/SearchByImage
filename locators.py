from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    googleLogo_image = (By.XPATH, "//div[@id='hplogo']")
    camera_button = (By.XPATH, "//div[@class='FiqGxd']")
    imageUrl_textFiled = (By.XPATH, "//input[@id='qbui']")
    searchByImage_button = (By.XPATH, "//input[@class='gbqfb kpbb']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    matching_results = "//div[@class='srg']//div[@class='g'][{0}]//a"
