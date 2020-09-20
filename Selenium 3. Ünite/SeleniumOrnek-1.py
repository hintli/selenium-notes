from selenium import webdriver
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")

try:
    tarayici.get("https://www.yazilimatolyesiakademi.com/")
    tarayici.maximize_window()#normalde tam ekran açılmıyor,bazen ekran küçük olduğu için clickde felan sıkıntı çıkabilir
except:
    print("Belirtilen url açılamıyor!")

try:#url adresinin titleı
    print("Sayfa başlığı: " + tarayici.title)

except:
    print("Sayfa başlığı alınamadı!")

try:#url yazdır-https://www.yazilimatolyesiakademi.com/
    print("Sayfa URL: {}".format(tarayici.current_url))

except:
    print("Sayfa URL alınamadı!")

sleep(2)
tarayici.quit()#ya da close

#python3 SeleniumOrnek-1.py
#web driver ile ilk giriş metodumuzu yazdık

