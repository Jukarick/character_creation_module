
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import random
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver.v2 as uc


print('write 1 to delete')
choice = input()
keys = Keys()
options = Options()

#options.add_argument("user-data-dir=C:\\Users\\Jukarick\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\cozxdzic.Ebashit")
#profile = webdriver.FirefoxProfile("C:\\Users\\Jukarick\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\cozxdzic.Ebashit")
#driver = webdriver.Firefox(profile, executable_path="C:\\Program Files\\geckodriver.exe")

options.add_argument("user-data-dir=C:\\Users\\jukarick\\AppData\\Local\\Google\\Chrome\\User Data\\Defaul\\Defpeace0922")
driver = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver.exe", options=options)


driver.get('https://ych.commishes.com/')


time.sleep(1)
global datetoday
datetoday = time.strftime("%d%m")

def first_nsfw_info():
    driver.get('https://ych.commishes.com/auction/create/')
    time.sleep(3)
    achains = ActionChains
    driver.find_element(by=By.XPATH, value="//*[@id='r2']").click()
    time.sleep(2)
    ##Select(driver.find_element(by=By.XPATH, value='//*[@id="category"]/select/option[3]')).select_by_value('furry')
    time.sleep(5)
    #Select(driver.find_element(By.TAG_NAME, 'select')).select_by_value('furry')
    selection = driver.find_element(by=By.XPATH, value='// *[ @ id = "category"] / select')
    #achains.move_to_element(selection)
    selection.click()
    time.sleep(3)
    #fur1 = driver.find_element(by=By.XPATH, value='// *[ @ id = "category"] / select / option[2]')
    # fur1.click()
    # time.sleep(2)
    # fur = driver.find_element(by=By.XPATH, value='// *[ @ id = "category"] / select / option[3]')
    # time.sleep(2)
    # achains.move_to_element_with_offset(fur,1,1).double_click(fur1)
    # time.sleep(3)
    # achains.key_down(2,fur)
    selection.send_keys(keys.DOWN, keys.DOWN, keys.ENTER)
    # fur.click()
    #Select(driver.find_element(by=By.TAG_NAME, value='select')).select_by_visible_text('Furry')
    print('yeap')
    #Select(hui).select()
    #hui.click()
    time.sleep(7)

def second_info():
    # driver.find_element(by=By.XPATH, value="//input[@value='Store']").click()
    time.sleep(4)
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/main/section/form/div[15]/div/div[1]/button').click()
    time.sleep(4)
    try:
        driver.find_element(by=By.XPATH, value="//input[@value='24']").click()
    except:
        Exception
        print('ne udalos')
    time.sleep(4)
    try:
        driver.find_element(by=By.XPATH, value="//input[@value='24']").click()
    except:
        Exception
    time.sleep(4)
    driver.find_element(by=By.XPATH, value="//button[@class='button']").click()
    time.sleep(4)

def first_sfw_info():
    driver.get('https://ych.commishes.com/auction/create/')
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//*[@id='r0']").click()
    time.sleep(2)
    #achains = ActionChains
    selection = driver.find_element(by=By.XPATH, value='// *[ @ id = "category"] / select')
    #achains.move_to_element(selection)
    selection.click()
    time.sleep(3)
    selection.send_keys(keys.DOWN, keys.DOWN, keys.ENTER)
    time.sleep(2)

def one():
    global datetoday

    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\1.jpg"
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/main/section/form/div[1]/div[1]/label/input').send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH latex $35')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH latex $35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Your character is'
    'wearing a latex costume element that denotes his sexy form')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Character can be any gender and any spices\n'
    '- Minor changes of body shape\n')

    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("One posted at ", time.strftime("%X"))


def two():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\2.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH dick $35 unlimited')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH dick $35 unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Hi-rendered, detailed'
    'picture of your characters dick and balls')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- It can be any shape and color, but some overly complex shapes may be slightly more expensive\n'
    '- Minor changes of body shape\n'
    '- I can add a lot of cum for 5usd extra\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Two posted at ", time.strftime("%X"))

def three():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\3.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $20 unlimited')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH $20 unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Your character manly '
    'shows what he got')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Character can be any spices\n'
    '- Minor changes of body shape\n'
    '- I can add extra cum for 5usd\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Three posted at ", time.strftime("%X"))

def four():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\4.jpg"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $20 unlimited')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH $20 unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Your character elegantly '
    'shows what she got')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Character can be any spices\n'
    '- Minor changes of body shape\n'
    '- I can add extra cum for 5usd\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Four posted at ", time.strftime("%X"))

def five():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\5.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $40')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Desired butt')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('$35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Minor changes of body shape\n'
    '- Any shape\n'
    '- Fixed price')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '40')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Five posted at ", time.strftime("%X"))

def six():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\6.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $20')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH $20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Minor changes of body shape\n'
    '- Any species\n'
    '- You can choose character for arm as well\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Six posted at ", time.strftime("%X"))

def seven():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\7.jpg"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Latex YCH $35')
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Latex YCH $35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Any species\n'
    '- Any body type\n'
    '- Female characters only\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '35')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Seven posted at ", time.strftime("%X"))

def eight():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\8.jpg"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $50')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH $50')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Minor changes of body type\n'
    '- Any dick type\n'
    '- Any species\n'
    '- Buffed female acceptable\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '50')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Eight posted at ", time.strftime("%X"))

def nine():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\9.jpg"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $25')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'YCH $25')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
    'Unlimited - you can get more than one for the same price if you want\nPaypal prepayment\n'
    'Picture will be ready within 20 days after payment\n'
    'Rules:\n'
    '- Possible changes for body type\n'
    '- Any species\n'
    '- Any dick type\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '25')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Nine posted at ", time.strftime("%X"))

def ten():
    global datetoday
    first_sfw_info()
    file1 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\10(1).png"
    file2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\10(2).png"
    file3 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\10(3).png"
    file4 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\10(4).png"
    filenumb = random.randint(1, 4)
    if filenumb == 1:
        file = file1
    if filenumb == 2:
        file = file2
    if filenumb == 3:
        file = file3
    if filenumb == 4:
        file = file4
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} Nature YCH $70')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Nature YCH $60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('The presented picture'
    ' is just an example of how the resulting landscape will look.\n'
    'Theme of the picture is how your character looking into beautiful nature, fresh and exhilarant.\n'
    'Picture will be ready within 25 days after payment\n'
    'Extra characters is possible.')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Ten posted at ", time.strftime("%X"))

def eleven():
    global datetoday
    first_sfw_info()
    file1 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\11(1).png"
    file2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\11(2).png"
    file3 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\11(3).png"
    filenumb = random.randint(1, 3)
    if filenumb == 1:
        file = file1
    if filenumb == 2:
        file = file2
    if filenumb == 3:
        file = file3

    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} City YCH $80')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'City YCH $60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('The presented picture'
    ' is just an example of how the resulting landscape will look.\n'
    'Idea of the picture is how your character looking into beautiful cityscape, with giant and '
    'futuristic buildings. Or shiny cyberpunk town, or something from your homeland.\n'
    'Usually I use 3d for that type of YCH, so we can can implement many of your'
    ' ideas :з (final result will be .png not an 3d object)\n'
    'Picture will be ready within 25 days after payment\n'
    'Extra characters is possible.')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Eleven posted at ", time.strftime("%X"))

def twelve():
    global datetoday
    first_sfw_info()
    file1 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\12(1).png"
    file2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\12(2).png"
    file3 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\12(3).png"
    file4 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\12(4).png"
    filenumb = random.randint(1,4)
    if filenumb == 1:
        file = file1
    if filenumb == 2:
        file = file2
    if filenumb == 3:
        file = file3
    if filenumb == 4:
        file = file4
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} Space YCH $70')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Space YCH $60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Unlimited')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('The presented picture'
    ' is just an example of how the resulting landscape will look.\n'
    'The main idea is how your character looking into outer space full of stars and planets\n'
    'Picture will be ready within 25 days after payment\n'
    'Extra characters is possible.')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '60')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Twelve posted at ", time.strftime("%X"))

def thirteen():
    global datetoday
    first_sfw_info()

    file1 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\13.png"
    file2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\13(1).png"
    file3 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\13(2).png"
    file4 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\13(3).jpg"
    file5 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\13(4).jpg"
    filenumb = random.randint(1, 5)
    print(f'file 13 is {filenumb}')
    if filenumb == 1:
        file = file1
    if filenumb == 2:
        file = file2
    if filenumb == 3:
        file = file3
    if filenumb == 4:
        file = file4
    if filenumb == 5:
        file = file5
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $35')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Cyberpunk/Industrial style'
                                                                               f' portrait with backgtound $45')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Portrait Commission')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
      'Unlimited - you can get more than one for the same price if you want\nWe can paint your character'
      ' in any type of background and environment:fantasy, cyberpunk, modern, space - anything\n'
      'Picture will be ready within 20 days after payment\n'
      'Rules:\n'
      '- Any species\n- Any gender\nmore examples of my portrait works: https://imgur.com/a/sZS01SG')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '45')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Thirteen posted at ", time.strftime("%X"))

def fourteen():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\14.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $35')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Open view')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('$25')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
      'Picture will be ready within 20 days after payment\nRules:\n'
      '- Any species\n'
      '- Any body type\n'
      '- Female characters only\n')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '25')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Thirteen posted at ", time.strftime("%X"))

def fiftheen():
    global datetoday
    first_nsfw_info()
    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\15.png"
    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $35')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Wet one :з')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('$20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Prepayment\n'
     'Picture will be ready within 20 days after payment\nRules:\n'
     '- Minor changes of body shape\n'
     '- Any species\n- Fixed price')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '20')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Fiftheen posted at ", time.strftime("%X"))

def sixteen():
    global datetoday
    first_sfw_info()

    file1 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\16.png"
    file2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\16(1).jpg"
    file3 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\16(2).jpg"
    file4 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\16(3).jpg"

    filenumb = random.randint(1 ,4)
    print(f'16 file is {filenumb}')
    if filenumb == 1:
        file = file1
    if filenumb == 2:
        file = file2
    if filenumb == 3:
        file = file3
    if filenumb == 4:
        file = file4

    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    # driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'{datetoday} YCH $35')
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'Medieval/Fantasy style portrait'
                                                                               f' with background')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Portrait Commission')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Fixed price\n'
      'Unlimited - you can get more than one for the same price if you want\nWe can paint your character'
      ' in any type of background and environment:fantasy, cyberpunk, modern, space - anything\n'
      'Picture will be ready within 20 days after payment\n'
      'Rules:\n'
      '- Any species\n- Any gender\nmore examples of my portrait works: https://imgur.com/a/sZS01SG')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '45')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Sixteen posted at ", time.strftime("%X"))

def seventeen():
    global datetoday
    first_sfw_info()

    file = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\pprn\\comm\\17.png"

    driver.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(file)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//input[@name='title']").send_keys(f'ANIMATED YCH Auction'
    f'"galaxy flight" ')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@name='subtitle']").send_keys('Looped animation '
    'that can be good for your phone as wallpaper, or anything else ')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//textarea[@name='description']").send_keys('Much Better quality preview here: \n'
      'Video: https://youtu.be/p-PPtax7gB8\nPng: https://imgur.com/a/q6NpWwX\n'
      '-Any gender (character with bests will get top clothes)\n'
      '-Any anthro speces\n'
      '-Can add any clothes for extra $30\n'
      '-Make it NSFW +$20\n-I can match resolution to your cellphone\n\nAuction rules\nFix price: $100')

    time.sleep(1)
    second_info()
    driver.find_element(by=By.XPATH, value="//input[@name='startingbid']").send_keys(keys.DELETE,
    keys.DELETE, keys.DELETE, keys.DELETE, '100')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
    print("Seventeen posted at ", time.strftime("%X"))


def deleting():
    print('deleting!')
    for i in range(16):
        try:
            driver.get('https://ych.commishes.com/account/')
            # driver.find_element_by_partial_link_text('End').click()
            # driver.find_element_by_partial_link_text('End').click()
            driver.find_element(by=By.PARTIAL_LINK_TEXT, value='End').click()
            driver.find_element(by=By.PARTIAL_LINK_TEXT, value='End').click()
            time.sleep(1)
        except: Exception

def all():
    time_delay = 50
    one()
    time.sleep(time_delay)
    nine()
    time.sleep(time_delay)
    two()
    time.sleep(time_delay)
    eight()
    time.sleep(time_delay)
    three()
    time.sleep(time_delay)
    seven()
    time.sleep(time_delay)
    four()
    time.sleep(time_delay)
    six()
    time.sleep(time_delay)
    five()
    time.sleep(time_delay)
    ten()
    time.sleep(time_delay)
    eleven()
    time.sleep(time_delay)
    twelve()
    time.sleep(time_delay)
    thirteen()
    time.sleep(time_delay)
    fourteen()
    time.sleep(time_delay)
    fiftheen()
    time.sleep(time_delay)
    sixteen()
    time.sleep(time_delay)
    seventeen()
try:
    if int(choice) == 1:
        #deleting()
        all()
except ValueError:
    all()

driver.quit()