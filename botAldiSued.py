from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.support.select import Select
import random
import time
import telegram_send
import requests

wd = wd.Chrome()
wd.implicitly_wait(10)

#An Donnerstag erst
wd.get("https://www.sued.aldi-liefert.de/kategorie/Technik-Multimedia/Gaming-PC-Engineer-X10-MD-34515.html")

#Verfügbar
#wd.get("https://www.sued.aldi-liefert.de/kategorie/Technik-Multimedia/Multimedia-PC-MEDION-AKOYA-E33005.html")
#wd.get("https://www.sued.aldi-liefert.de/kategorie/Grillen/GRILL-MAGS-magnetischer-Gewuerzhalter.html")

def timeBreak():
    randomWaitTime = random.randrange(1.0, 4.0)
    print(randomWaitTime)
    time.sleep(randomWaitTime)

timeBreak()

#CookiesCheck
cookieButton =  wd.find_element_by_id('cookie-modal')
propCookie = cookieButton.get_attribute('aria-modal')
print('cookie visible:' + propCookie)
if propCookie:
    wd.find_element_by_xpath('//*[@id="cookie-modal"]/div/div/div[3]/div/div[2]/button').click()

#timeBreak()   


#anzahl auf zwei erhöhen
#erhoehe_menge = wd.find_element_by_xpath('//*[@id="detailToBasket"]/div[1]/div[2]/span[2]/button')
#prop = erhoehe_menge.get_property('disabled')
#if prop == True:
#    print('Nicht genug Ware vorhanden')
#    time.sleep(2)
#    wd.refresh()
#elif prop == False:
#    erhoehe_menge.click()
    

#buyButton    
buyButtonActive = False
while not buyButtonActive:
    add_to_cart_button = addButton = wd.find_element_by_id("toBasket")
    prop = add_to_cart_button.get_property('disabled')
    if prop == True:
        print('Button not ready')
        time.sleep(1)
        wd.refresh()
    elif prop == False:
        buyButtonActive = True

add_to_cart_button.click()
    
#timeBreak()
plz = wd.find_element_by_id("checkPLZ")
plz.send_keys("90419")

#timeBreak()
plzButton = wd.find_element_by_id("submitOk")
plzButton.click()

timeBreak()
toCart = wd.find_element_by_xpath('//*[@id="basketModal"]/div/div/div[3]/a')
toCart.click()

timeBreak()
zurKasse = wd.find_element_by_xpath('//*[@id="cartButtonBuy"]/button')
zurKasse.click()

timeBreak()
anredeRadio = wd.find_element_by_xpath('//*[@id="shippingAddressForm"]/div[1]/div[1]/div[1]/label/span')
anredeRadio.click()

timeBreak()
vorname = wd.find_element_by_xpath('//*[@id="shippingAddressForm"]/div[2]/div/input')
vorname.send_keys("Kubilay")

timeBreak()
nachname = wd.find_element_by_xpath('//*[@id="shippingAddressForm"]/div[3]/div/input')
nachname.send_keys("Yildiz")

timeBreak()
wd.find_element_by_id("userLoginName").send_keys("kubi.y@hotmail.de")

timeBreak()
wd.find_element_by_id("userLoginName2").send_keys("kubi.y@hotmail.de")

timeBreak()
wd.find_element_by_xpath('//*[@id="shipping_option_0"]/div[1]/div/input').send_keys("Poppenreuther Straße")

timeBreak()
wd.find_element_by_xpath('//*[@id="shipping_option_0"]/div[2]/div/input').send_keys("41")

timeBreak()
wd.find_element_by_xpath('//*[@id="shipping_option_0"]/div[4]/div/input').send_keys("90419")

timeBreak()
wd.find_element_by_xpath('//*[@id="shipping_option_0"]/div[5]/div/input').send_keys("Nürnberg")

timeBreak()
wd.find_element_by_id("userNextStepBottom").click()

timeBreak()
wd.find_element_by_xpath('//*[@id="payment"]/div[2]/div[2]/div[2]/dl/dt/div/label/span').click()

timeBreak()
wd.find_element_by_xpath('//*[@id="payment"]/div[2]/div[2]/div[2]/dl/dd/div[1]/div[1]/label/span').click()

timeBreak()
wd.find_element_by_id("paymentNextStepBottom").click()

timeBreak()
wd.find_element_by_id("cardNumber").send_keys("4546179316131015")

timeBreak()
wd.find_element_by_id("cardholderName").send_keys("Kubilay Yildiz")

timeBreak()
jahr = wd.find_element_by_id("expiryMonth")
Select(jahr).select_by_value('11')

#dropdown Jahr
timeBreak()
jahr = wd.find_element_by_id("expiryYear")
Select(jahr).select_by_value('2025')

timeBreak()
wd.find_element_by_id("cardCode_masked").send_keys("378")

timeBreak()
wd.find_element_by_id("nextBtn").click()

#Telegram Bot
def send_msg(text):
    token = "1735947787:AAGURO9Lc3LVNvxsvofZN1mXZgZf69Kbc9A"
    chat_id = "1556934687"

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())
    
send_msg("LOS! Der PC ist im Warenkorb und muss bezahlt werden.")
