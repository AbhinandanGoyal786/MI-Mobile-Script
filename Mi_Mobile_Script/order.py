from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commonFunctions import initdic,reload,writefile,readfile
import requests as rq

def order(driver, url, config, cardDetails):
    reload(driver,url)
    urlCount = 1
    buynow = True
    while buynow:
        try:
            sleep(1)
            if len(driver.find_elements_by_xpath(
                    "/html/body/div[1]/main/div/article/section[12]/div[1]/div/button")) <= 0:
                writefile("input/msg.txt", "msg==0")
                if urlCount == 1:
                    reload(driver, config['url'])
                elif urlCount == 2:
                    reload(driver, config['url1'])
                elif urlCount == 3:
                    reload(driver, config['url2'])
                urlCount = urlCount + 1
                if urlCount >= 4:
                    urlCount = 1
            else:
                buynow = False
                msg = initdic("input/msg.txt")
                if msg['msg'] == "0":
                    #response = rq.get("http://www.alots.in/sms-panel/api/http/index.php?username=fdking&apikey=E3BC2-86A8F&apirequest=Text&sender=fdking&mobile=9034226621,9084000000,9015000000,9097950000,9050403080,9031000071&message=Mobile+"+config['price']+"+IS+Available+Now&route=TRANS&format=JSON")
                    writefile("input/msg.txt", "msg==1")
        except:
            pass
    driver.execute_script('''window.open("https://store.mi.com/in/cart","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/header/div[1]/div/div[3]/ul/li[1]/a").click()
    sleep(2)


    #for btn in driver.find_elements_by_xpath("/html/body/div[1]/main/section/article/section/button"):
    for btn in driver.find_elements_by_xpath('//*[@id="root"]/main/footer/div/button[2]'):

        btn.click()

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/footer/div[2]")))
        driver.find_element_by_xpath("/html/body/div[3]/div/div/footer/div[2]").click()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    element = driver.find_element_by_xpath("/html/body/div[1]/main/div/article/section[12]/div[1]/div/button")
    driver.execute_script("arguments[0].click();", element)
    sleep(1)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/a")))

    if len(driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/a")) <= 0:
        return
    reload(driver,"https://store.mi.com/in/cart")
    #print("abcd")

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/footer/div/button[2]")))
    driver.find_element_by_xpath("//*[@id='root']/main/footer/div/button[2]").click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='checkoutFormBtn']")))
    driver.find_element_by_xpath("//*[@id='J_gstCheckbox']").click()
    driver.find_element_by_xpath("//*[@id='J_gstInput']").send_keys(config['gstin'])
    driver.find_element_by_xpath("//*[@id='checkoutFormBtn']").click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/div/button")))

    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/fieldset[1]/div[1]/input").send_keys(
        cardDetails['card'])
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/fieldset[1]/div[2]/input").send_keys(
        cardDetails['name'])
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/fieldset[2]/div[1]/div[1]/select/option[text()='" +
        cardDetails['month'] + "']").click()
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/fieldset[2]/div[1]/div[2]/select/option[text()='" +
        cardDetails['year'] + "']").click()
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/fieldset[2]/div[2]/input").send_keys(
        cardDetails['cvv'])
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/form/div/button").click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='continue']")))
    driver.find_element_by_xpath("//*[@id='static']").click()
    driver.find_element_by_xpath("//*[@id='continue']").click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='sendotp']")))
    driver.find_element_by_xpath("//*[@id='enterPASS']").send_keys(cardDetails['password'])
    driver.find_element_by_xpath("//*[@id='sendotp']").click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/dl[1][@class='order-info-detail']")))


def login(driver, link, username, password):
    # Load page
    reload(driver,url=link)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='ChangeLoginType']")))
    sleep(1)
    driver.find_element_by_xpath("//*[@id='ChangeLoginType']").click()
    sleep(1)
    # Login
    driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//*[@id='pwd']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='login-button']").click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='logoutLink']")))
    sleep(1)


if __name__ == "__main__":
    chrome_binary = r"chrome.exe"  # Add your path here
    config = initdic("loginIds.txt")
    cardDetails = initdic("cardDetails.txt")

    #idCount = os.path.basename(sys.argv[0][:-3])

    options = wd.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver_binary = config['chromedriver']
    driver = wd.Chrome(options=options)
    idCount = "0"
    print(idCount + " " + config['order'])
    login(driver, "https://account.xiaomi.com/pass/serviceLogin", config['username' + idCount],
          config['password' + idCount])

    orderCount = 0
    while orderCount < 1:
        try:
            order(driver, config['url'], config, cardDetails)
            orderCount = orderCount + 1
            sleep(1)
        except:
            pass
