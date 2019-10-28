
from selenium import webdriver

class Automate:

    driver = None

    def setup(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        self.driver = webdriver.Firefox(firefox_options=options)

    def login(self, url,username,password):
        self.driver.get(url)
        self.driver.find_element_by_id('ap_email').send_keys(username)
        self.driver.find_element_by_id('continue').click()
        self.driver.find_element_by_id('ap_password').send_keys(password)
        self.driver.find_element_by_id('signInSubmit').click()
    
    def search(self, url, search):
        self.driver.get(url)
        self.driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
        self.driver.find_element_by_class_name('nav-search-submit').click()

    def getInventory(self, url):
        self.driver.get(url)
        reviews = self.driver.find_element_by_id('acrCustomerReviewText').text
        price = self.driver.find_element_by_id('priceblock_ourprice').text
        weight = self.driver.find_elements_by_css_selector('.size-weight .value')
        rankings = self.driver.find_elements_by_css_selector('#SalesRank > td.value')
        print(reviews)
        print(price)
        print(rankings)


    def close(self):
        self.driver.save_screenshot("screenshot.png")
        self.driver.close()

if __name__ == "__main__":
    auto = Automate()
    try:
        auto.setup()
        url = 'https://www.amazon.co.uk/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=gbflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk'
        # auto.login(url=url, username='rodrigo.pitta@gmail.com', password='')
        # auto.search('https://amazon.co.uk', 'umbrella')
        auto.getInventory('https://www.amazon.co.uk/Travel-Umbrella-Lifetime-Replacement-Warranty/dp/B07JCYCZX9/ref=sr_1_9?keywords=umbrella&qid=1572159567&sr=8-9')
    finally:
        auto.close()
        pass



