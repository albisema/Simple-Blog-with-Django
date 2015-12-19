from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.admin import User

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        User.objects.create_user('admin', None, '123')
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()


    def test_login(self):
        self.browser.get(self.live_server_url)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('123')
        password_field.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(3)

        inputbox = self.browser.find_element_by_id('id_description')
        inputbox.send_keys('The first blog post. Title should be unknown!')
        form = self.browser.find_element_by_tag_name('form')
        form.submit()

        panel = self.browser.find_element_by_id('id_list_table')
        titles = panel.find_element_by_class_name('panel-title')
        self.assertIn('Untitled Post', titles.text)

        descriptions = panel.find_element_by_class_name('panel-body')
        self.assertIn('The first blog post. Title should be unknown!', descriptions.text)