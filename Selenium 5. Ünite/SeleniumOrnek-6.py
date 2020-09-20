from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("OLUŞTURULAN index.html DOSYASININ YOLU")
tarayici.maximize_window()

try:
    tarayici.find_element_by_id("show-prompt").click()
    sleep(2)
except:
    print("Tıklama işlemi başarısız oldu!")

try:
    uyari_kutusu = tarayici.switch_to_alert()#alert kutusu çıkarsa al
    sleep(2)
    uyari_kutusu.accept()#Uyarı kutusundaki okeye basmış oluyoruz
    #.dismiss tersi
    print("Uyarı kutusunu onayladım!")

except:
    print("Hata")

sleep(3)
tarayici.quit()

#test yapcağımız sitede uyarı kutuları varsa nasıl paş ediceğiz