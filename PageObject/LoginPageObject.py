from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    # Locators
    txtbox_username_name=(By.NAME,'username')
    txtbox_password_name=(By.NAME,'password')
    button_login_xpath=(By.XPATH,"//button[normalize-space()='Login']")
    button_menu_xpath=(By.XPATH,"//img[@class='oxd-userdropdown-img']")
    button_logout_xpath=(By.XPATH,"//a[normalize-space()='Logout']")

    # Constructor
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    # Action Methods
    def enterUserName(self,username):
        self.wait.until(EC.presence_of_element_located(self.txtbox_username_name))
        self.driver.find_element(*Login.txtbox_username_name).send_keys(username)

    def enterPassword(self,password):
        self.wait.until(EC.presence_of_element_located(self.txtbox_password_name))
        self.driver.find_element(*Login.txtbox_password_name).send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.presence_of_element_located(self.button_login_xpath))
        self.driver.find_element(*Login.button_login_xpath).click()


    def login_status(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.button_menu_xpath))
            self.driver.find_element(*Login.button_menu_xpath)
            return True
        except (NoSuchElementException,TimeoutException):
            return False

    def click_Menu_Button(self):
        self.wait.until(EC.presence_of_element_located(self.button_menu_xpath))
        self.driver.find_element(*Login.button_menu_xpath).click()

    def click_Logout_Button(self):
        self.wait.until(EC.presence_of_element_located(self.button_logout_xpath))
        self.driver.find_element(*Login.button_logout_xpath).click()












