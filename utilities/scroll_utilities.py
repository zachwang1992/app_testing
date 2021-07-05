class ScrollUtil:

    @staticmethod
    def scroll_to_search_for_review(text, driver):
        elements = driver.find_elements_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))")
        return elements
