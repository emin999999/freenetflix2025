# Netflix-Gen 2.0
# Owner By Emin INC.

Bu Python kodu, Selenium ve bazı ek kütüphaneleri kullanır. Gerekli kütüphaneler şunlardır:

1. **Selenium**: Web otomasyonu yapmak için kullanılır. Web sayfalarını açma, form doldurma, butonlara tıklama ve sayfa üzerinde işlem yapma işlemleri için gereklidir.

2. **WebDriver**: Selenium ile bir web tarayıcısını kontrol etmek için kullanılır. Bu örnekte, Chrome tarayıcısı kullanıldığı için `chromedriver` gereklidir. Başka bir tarayıcı kullanacaksanız (Firefox, Edge vb.), ona uygun WebDriver'ı indirmeniz gerekecek.

3. **time**: Kodun belirli bir süre beklemesini sağlamak için kullanılır (örneğin, sayfanın yüklenmesini beklemek için).

### Gerekli Kütüphaneler:
1. **Selenium**:
   ```bash
   pip install selenium
   ```

2. **WebDriver (Chrome)**:
   - WebDriver için [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) indirmeniz gerekir. Chrome sürümünüze uygun olan sürümü indirip, bilgisayarınıza kurmalısınız.
   
   - WebDriver için ayrıca `webdriver-manager` kullanabilirsiniz. Bu, otomatik olarak gerekli WebDriver sürümünü indirip kurmanıza yardımcı olur:
     ```bash
     pip install webdriver-manager
     ```

3. **time**: Python'un yerleşik bir modülü olduğu için, ayrıca yüklemeniz gerekmez.

### ChromeDriver ve Selenium Kullanımı:
Eğer `webdriver-manager` kullanarak ChromeDriver'ı otomatik olarak indirip kurmak isterseniz, aşağıdaki gibi kodu güncelleyebilirsiniz:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver'ı otomatik olarak indirin ve başlatın
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.netflix.com/login')
```

Bu şekilde, ChromeDriver'ı manuel olarak indirip kurmanıza gerek kalmaz, `webdriver-manager` sizin için otomatik olarak indirip çalıştırır.

### Sonuç:
Bu kütüphaneleri ve araçları yükledikten sonra, Selenium ve WebDriver'ı sorunsuz bir şekilde kullanabilirsiniz.
