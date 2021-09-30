from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

chromepath=r"C:\Users\Admin\OneDrive\Desktop\keerthiAngela\chromedriver.exe"
promised_down=100
prom_up=10
tw_mail="Ur_Twitter@gmail.com"
tw_pass="ITS_Password"

class interetTweetBot:
    def __init__(self,drive_path):
        self.drive=webdriver.Chrome(drive_path)
        self.down=0
        self.up=0

    def get_net_speed(self):
        self.drive.get("https://www.speedtest.net/")
        self.drive.maximize_window()
        go= self.drive.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        sleep(40)
        gotdown= self.drive.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down=gotdown.text
        gotup= self.drive.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up=gotup.text

    def tweet(self):
        self.drive.get("https://twitter.com/")
        self.drive.maximize_window()
        sleep(2)
        signin = self.drive.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
        signin.click()
        withmail = self.drive.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        withmail.click()
        sleep(5)
        email = self.drive.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(tw_mail)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.drive.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        password.send_keys(tw_pass)
        password.send_keys(Keys.ENTER)
        sleep(10)
        maketweetbtn = self.drive.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        maketweetbtn.click()

        type = self.drive.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        type.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/ {self.up} up when I pay for {promised_down}down/{prom_up}up?")
        sleep(5)
        tweetbtn = self.drive.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        tweetbtn.click()
        sleep(5)
        self.drive.quit()

bot=interetTweetBot(chromepath)
bot.get_net_speed()
bot.tweet()
