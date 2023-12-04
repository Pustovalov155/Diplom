import time
import pytest
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert


@pytest.mark.usefixtures('setup')
class Testspectehnika:
    browser = None

    @allure.feature('Тест сайта')
    @allure.story('Тест функционала')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_2(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[2]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_3(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[3]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_4(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[4]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_5(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[5]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_6(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[2]/a').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[9]/div/div[1]/img').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



    def test_7(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[1]/a[2]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def test_8(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[10]/a[2]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div[1]/div/div/div[2]/div/p').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



    def test_9(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[3]/a[2]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div[1]/div/div/div[2]/div/p').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_10(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://spectehnika62.ru/index.php')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/nav/div[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div[2]/div/div[5]/a[2]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div[1]/div/div/div[2]/div/p').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

