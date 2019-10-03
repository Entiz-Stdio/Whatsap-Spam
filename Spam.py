
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "https://web.whatsapp.com"
driver = webdriver.Chrome()
driver.get(url)

def hubba():
    print("\t\t^^== CODED WITH LOVE FROM CÃLIN ==^^")
    print("\nI WON'T BE HELD RESPONSIBLE FOR WHAT YOU DO WITH THIS")
    print("USES SELENIUM TO ACCESS ELEMENTS FROM WEB WHATSAPP")
    print("For suggestions mail me -> 2xtaptap@gmail.com")
    
def grp():
    usr = input('Enter name of user or group:')
    search(usr)    #takes u inside the group UI
    print("Working on this:")
    
def flood():
    usr = input('Enter name of usr or grp:')
    msg = input("Enter the message to flood or send:")
    count = int(input("Enter the number of msgs:"))
    search(usr)
    #input("just a pause")
    go = int(input("Are you sure?(If yes enter 0!)\n"))
    if(go==0):
        for i in range(count):
            msg_box = driver.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[2]""")
            msg_box.send_keys(msg)
            button =driver.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[3]""")
            button.click() 
    else:
        print("Phew")
        
def search(usr):
    #user2 = driver.find_element_by_class_name("eiCXe")
    search_box = driver.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/input""") #finding search box
    search_box.click() #clicking search box
    search_box.send_keys(usr)  #typing user/grp name
    input("Waiting 3 seconds to fetch results and press enter:")
    search_box.send_keys(Keys.ENTER)
    
def fn():
    print("Choose the options Below,\n 1. Enter 1 to spam : )\n 2. Enter 2 exit!")
    choice = int(input("Enter Choice:"))
    if choice==1:
        try:
            flood()
            fn()
        except:
            print("\n___flood_fn error.. recovering___\n")
            fn()
    elif choice==2:
        print("\n___Exiting...___\n")
    else:
        print("\n___Invalid choice :(___\n")

hubba()    
fn()

