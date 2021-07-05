from selenium.webdriver.common.by import By

from locators.review_page import ReviewPageLocators
from pages.base_page import BasePage
from utilities.generic_utilities import generate_a_random_review, generate_a_random_rating

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReviewPage(BasePage):

    def fill_and_save_review(self):
        self.review = generate_a_random_review()
        self.rating = generate_a_random_rating()
        self.type(ReviewPageLocators.REVIEW_DETAILS_FIELD_BY_ID, self.review)
        self.click_by_id(ReviewPageLocators.REVIEW_NUMBER_BY_ID)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, ReviewPageLocators.RATING_BY_ID)))
        self.click_index(ReviewPageLocators.RATING_BY_ID, self.rating)
        self.click_by_id(ReviewPageLocators.SAVE_REVIEW_BUTTON_BY_ID)

    def fill_and_save_review_with_only_rating(self):
        self.rating = generate_a_random_rating()
        self.click_by_id(ReviewPageLocators.REVIEW_NUMBER_BY_ID)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, ReviewPageLocators.RATING_BY_ID)))
        self.click_index(ReviewPageLocators.RATING_BY_ID, self.rating)
        self.click_by_id(ReviewPageLocators.SAVE_REVIEW_BUTTON_BY_ID)

