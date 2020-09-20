from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://www.facebook.com/")
tarayici.maximize_window()

try:
    element = tarayici.find_element_by_name("email")#input alanına eriş
    element.send_keys("canilgu@hotmail.com", Keys.PAGE_DOWN)#maili gir,sayfayı aşağı kaydır

    sleep(3)
    element.send_keys(Keys.PAGE_UP)#scrool yukayı kaydır
    sleep(3)
    element.clear()#veriyi sil(maili)

except:
    print("Email girilemedi!")

tarayici.quit()

#from selenium.webriver.support.ui import Select
#selectbox da countryi turkey yapma
#sec=Select(element)
#sec.select_by_visible_text("Turkey")