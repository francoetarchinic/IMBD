# -*- coding: utf-8 -*-
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.ie.service import Service

class WebDriver:

    def __init__(self):

        #self.__log = log.Log().get_logger(config.LOG_FILE)
        self.dir = os.path.normpath(tempfile.mkdtemp())

    def get_driver(self, grid_url=None, driver_path=None):

        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--window-size=2560x1440')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--hide-scrollbars")
            # chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument(
                "--disable-web-security"
            )  # Desabilita la politica del mismo origen
            chrome_options.add_argument("--disable-extensions")  # Evita que carguen las extenciones
            chrome_options.add_argument("--disable-notifications")  # Bloquea las notificaciones
            chrome_options.add_argument("--ignore-certificate-errors")  # Para ignorar el aviso de "Su conexion no es privada"
            # For local testing #

            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            # For local testing #
            # driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)
            return driver
        except Exception as e:
            print(f"Can't init driver! - Error: {e}")
