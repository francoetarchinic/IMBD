import time
import web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Script_selenium:

    def __init__(self):
        #self.__log = log.Log().get_logger(config.LOG_FILE)
        self.__cookies = {}

    def login(self):

        try:
            #grid_url = config.GRID_URL
            chrome_driver="C:\\Users\\Autoscraping-web\\Desktop\\Desarrollo - Franco\\ChromeDrivers\\chromedriver-win64-143.0.7499.192\\chromedriver.exe"

            webdriver = web_driver.WebDriver()
            driver = webdriver.get_driver(driver_path=chrome_driver)
            if not driver:
                print('No se pudo iniciar el driver')
                return None
        except Exception as e:
            print(f"Can't get driver from login - Error: {e}")
            return None

        # Starting login
        try:

            wait = WebDriverWait(driver, 120)
            driver.get('https://www.imdb.com/es/chart/top/?ref_=hm_nv_menu')
                       
            # try:
            #     button_login = wait.until(
            #         ec.visibility_of_element_located((By.XPATH, './/a[contains(text(),"login")]')))
            #     time.sleep(1)
            #     button_login.click()
            # except Exception as e:
            #     print(f'Login button not found - Error: {e}')
            #     return None

            time.sleep(1)

            
            # host = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "login-container")))

            # email = driver.execute_script(
            #     "return arguments[0].shadowRoot.querySelector('input[name=\"email\"]')",
            #     host
            # )
            # password = driver.execute_script(
            #     "return arguments[0].shadowRoot.querySelector('input[name=\"password\"]')",
            #     host
            # )
            # btn = driver.execute_script(
            #     "return arguments[0].shadowRoot.querySelector('#login-button')",
            #     host
            # )

            # email.send_keys("")
            # password.send_keys("")
            # btn.click()

            time.sleep(2)

          

            try:
                films_name = wait.until(ec.visibility_of_all_elements_located((By.XPATH, '//div[contains(@class,"ipc-page-grid__item")]//h3')))
                print("Top films:",films_name[0])
            except Exception as e:
                print(f'Username input not found or the credential values are wrong - Error: {e}')
                return None

            input('Enter to continue')
            # time.sleep(1)

            # try:
            #     input_password = wait.until(ec.visibility_of_element_located((By.NAME, "password")))
            #     input_password.send_keys('')
            # except Exception as e:
            #     print(f'Password input not found or the credential values are wrong - Error: {e}')
            #     return None

            # time.sleep(1)

            # try:
            #     button_login = wait.until(
            #         ec.visibility_of_element_located((By.XPATH, './/button[contains(text(),"Login")]')))
            #     button_login.click()

            # except Exception as e:
            #     print(f'Login button not found - Error: {e}')
            #     return None

            # time.sleep(2)
            # input('Enter to continue')

            # # cookies = driver.get_cookies()

            # # for cookie in list(cookies):
            # #     if cookie.get('name') == 'sessionid':
            # #         self.__cookies['sessionid'] = cookie.get('value')
            # #     if cookie.get('name') == 'csrftoken':
            # #         self.__cookies['csrftoken'] = cookie.get('value')

            driver.quit()

        except Exception as e:
            print(f"Can't login! - Error: {e}")
        
            return None

    def run(self):

        try:
            self.login()
            return self.__cookies

        except Exception as e:
            print(f'Has been an error on get cookies - Error: {e}')
            return {}



if __name__ == "__main__":
    Script_selenium().run()