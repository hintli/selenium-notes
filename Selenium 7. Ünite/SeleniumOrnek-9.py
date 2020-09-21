from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.maximize_window()
tarayici.get("https://tr.khanacademy.org/")

try:
    print("Bekliyorum")
    tarayici.implicitly_wait(10)
    print("Bekleme bitti.")
    #element = WebDriverWait(tarayici,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="outer-wrapper"]/div[1]/div/div/div/div/span/div/div/a')))
    element = tarayici.find_element_by_xpath('//*[@id="outer-wrapper"]/div[1]/div/div/div/div/span/div/div/a')
    element.click()
    sleep(4)
    tarayici.quit()


except:
    print("Hata!")
    tarayici.quit()

#web sitesine eriştiğimiz zaman bazı butonlar felan geç gelebiliyor
#element bulama hatalarından kurtulmak için bekleme felan kullanıyoruz

#as EC
#element = WebDriverWait(tarayici,10).until(
# ECÇpresence_of_element_located(By.XPATH,"Element"))
#_clickable ->elemente tıklama işlemi
#tavsiye edilen:WebDriverWait bekleme bu eleman varolana kadar 10 saniye beklet
#implicitly_wait dahada kısa direk tarayıcı ile etkileşim kurup tarayıcıyı bekletiyor