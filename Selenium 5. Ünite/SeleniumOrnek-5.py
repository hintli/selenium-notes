from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("http://canilgu.com")
tarayici.maximize_window()

try:#a etiketinin hrefini aldık,linke gitcek sonra 0. elemana gelcez
    tarayici.find_element_by_xpath("//*[@id='work']/div/a[2]").click()
    sleep(3)

except:
    print("Tıklama işlemi başarısız oldu!")

try:
    sleep(2)
    print("İlk sekmeye geçiyorum..")
    tarayici.window_handles#sekmeleri bir arraye atıyor
    tarayici.switch_to_window(tarayici.window_handles[0])#arrayden kaçıncıyı seçersek ona gider

except:
    print("Hata!")

sleep(3)
tarayici.quit()

#sekmeler arası hareket etme
#tarayici.current_window_handler //ilk tarayıcı