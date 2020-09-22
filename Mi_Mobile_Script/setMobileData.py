from order import  order,login
from commonFunctions import initdic
from time import sleep
from selenium import webdriver as wd
import threading



def placeOrder(driver_path,loginids,card_details,idCount):
    print(driver_path)
    chrome_binary = driver_path#r"chrome.exe"  # Add your path here
    #print(driver_path,loginids,card_details,idCount)
    config = initdic(loginids)#"loginIds.txt")
    cardDetails = initdic(card_details)#"cardDetails.txt")

    #idCount = os.path.basename(sys.argv[0][:-3])

    options = wd.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    #driver_binary = config['chromedriver']
    driver = wd.Chrome(options=options)
    #print(idCount + " " + config['order'])
    idCount=str(idCount)
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

def set_quantity(driver_path='',loginids='',card_details='',qty=1):
    thredlist = []
    for i in range(qty):
        thredlist.append(threading.Thread(target=placeOrder, args=(driver_path,loginids,card_details,i,)))
    for i in thredlist:
        i.start()

    for i in thredlist:
        i.join()

def main(filename):
    data=initdic(filename)
    loginids = data["loginids"]  # "loginIds.txt"
    driver_path = data["driver_path"]  # r"chrome.exe"
    card_details = data["card_details"]  # "cardDetails.txt"
    qty = data["qty"]
    set_quantity(driver_path=driver_path, loginids=loginids, card_details=card_details, qty=qty)


if __name__ == "__main__":
    main('data.json')
