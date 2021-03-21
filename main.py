from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from conf import *

class AutoLoginBitrix24:
    def __init__(self, driver_path, url, password, username ):
        self.url = url
        self.driver_path = driver_path
        self.password = password
        self.username = username

    @property
    def firefox(self):
        bitriksBot = webdriver.Firefox(executable_path=self.driver_path)
        bitriksBot.get(self.url)
        bitriksBot.implicitly_wait(10)
        bitriksBot.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div[3]/div/form/div/div[4]/div/ul/div/li[2]/span").click()
        bitriksBot.implicitly_wait(10)
        active_tabs = bitriksBot.window_handles
        current_tab = bitriksBot.current_window_handle
        for new_tab in active_tabs:
            if new_tab != current_tab:
                bitriksBot.switch_to_window(new_tab)
                # print("new tap is ready")
                bitriksBot.implicitly_wait(25)  
                uname = bitriksBot.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/input")
                uname.send_keys(self.username + Keys.ENTER)
                uname.send_keys("nets.tj" + Keys.ENTER)
                bitriksBot.implicitly_wait(3)
                pwd_enter = bitriksBot.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/div/div/div/div/div/input")
                pwd_enter.send_keys(self.password + Keys.ENTER)
                bitriksBot.implicitly_wait(20)
                bitriksBot.switch_to_window(current_tab)
                # print("Authenticated successful")

        # print("switched to the main tab ")
        bitriksBot.implicitly_wait(50)

        modal_closer = bitriksBot.find_element_by_xpath("/html/body/div[14]/table/tbody/tr/td[2]/div/div/span")
        time_display = bitriksBot.find_element_by_xpath('//*[@id="timeman-timer"]')
        bitriksBot.implicitly_wait(30)

        if modal_closer:
            modal_closer.click()
        else:
            pass
            # print("modal not ready")
        bitriksBot.implicitly_wait(30)
        
        if time_display:
            time_display.click()
        else:
            pass
            # print("there is no timer display")

        start_btn = bitriksBot.find_element_by_xpath('/html/body/div[16]/div[1]/div/div[2]/table/tbody/tr/td[2]/div/button')
        bitriksBot.implicitly_wait(3)
        start_btn.click()
        time.sleep(10000)
        close_btn = bitriksBot.find_element_by_xpath('/html/body/div[16]/div[1]/div/div[2]/table/tbody/tr/td[2]/div/button')
        bitriksBot.implicitly_wait(3)
        close_btn.click()





bitrix = AutoLoginBitrix24(url=b24url, driver_path=drv_path, username=b_username, password= b_pwd)
bitrix.firefox