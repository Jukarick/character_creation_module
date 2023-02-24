from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random


keys = Keys()
options = Options()
options.add_argument("user-data-dir=C:\\Users\\jukarick\\AppData\\Local\\Google\\Chrome\\User Data\\Defaul")
driver = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver.exe", options=options)
# while True:
#     try:
namex1='YСH $70 Space'
namez1="Get more details:\nhttps://www.furaffinity.net/view/36213970/\nhttps://www.furaffinity.net/view/36213970/\nhttps://www.furaffinity.net/view/36213970/"
namex2='YСH $80 City'
namez2="Get more details:\nhttps://www.furaffinity.net/view/36213991/\nhttps://www.furaffinity.net/view/36213991/\nhttps://www.furaffinity.net/view/36213991/"
namex3='YСH $70 Nature'
namez3="Get more details:\nhttps://www.furaffinity.net/view/36213932/\nhttps://www.furaffinity.net/view/36213932/\nhttps://www.furaffinity.net/view/36213932/"

sumnote = 0
sumcom = 0

ga1, ga2, ga3 = "14.jpg", "25.jpg", "35.jpg"

startingf = open("turnchr.txt", 'r')
seq = int(startingf.read())
startingf.close()

notific = open('chrnots.txt', 'w')
notific.write('0')
notific.close()
comment = open('chcom.txt', 'w')
comment.write('0')
comment.close()


i5 = -1
i6 = -1
for i in range(1):
    if i%5==0:
        i5=-1
    if i%6==0:
        i6=-1
    i5 += 1
    i6 += 1
    print("Round:",i," i5=",i5,"i6=",i6)


    def dell():
        try:
            time.sleep(1)
            driver.get('https://www.furaffinity.net/controls/submissions/')
            time.sleep(1)
            dell = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="YСH")
            while len(dell) > 1: #how many ychs are used right now, default = 1
                driver.get('https://www.furaffinity.net/controls/submissions/')
                time.sleep(1)
                dell = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="YСH")
                # print(len(dell))
                dell[len(dell) - 1].click()
                time.sleep(2)

                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(1)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q')
                time.sleep(1)
                passw.send_keys(Keys.ENTER)
                dell.pop()
        except Exception:
            quit('it was dell')

    def analyse():
        views = driver.find_element(by=By.XPATH, value="//span[@class='font-large']").text
        likes = driver.find_element(by=By.XPATH, value="//span//a").text
        picture_link = driver.find_element(by=By.XPATH, value="//img[@id='submissionImg']")
        name_of_picture = picture_link.get_attribute("data-fullview-src")
        name_of_picture = name_of_picture[-6:]
        analyse = open("analyse.txt", 'a')
        analyse.write(f'\n{time.strftime("%d-%m-%y %X")} || {name_of_picture} || Views: {views} || Likes: {likes}\n')
        analyse.close()

    def checknote():
        global sumnote
        driver.get("https://www.furaffinity.net/msg/pms/")
        try:
            checkn = driver.find_element(by=By.XPATH, value="//a[@class='notification-container inline'][@href='/msg/pms/']")
            getnote = checkn.get_attribute("title")
            if sumnote == 0:
                print("\n", getnote, "\n")
                notific = open('chrnots.txt', 'w')
                notific.write(getnote)
                notific.close()
            sumnote = 1
        except NoSuchElementException:
            sumnote = 0
            notific = open('chrnots.txt', 'w')
            notific.write('0')
            notific.close()

    def checkcomm():
        global sumcom
        driver.get("https://www.furaffinity.net/msg/pms/")
        try:
            checkc = driver.find_element(by=By.XPATH, value="//a[@class='notification-container inline'][@href='/msg/others/#comments']")
            getcom = checkc.get_attribute("title") #copying comment
            if sumcom == 0:
                print("\n", getcom, "\n") #printing comment notification
                comment = open('chcom.txt', 'w')
                comment.write(getcom)
                comment.close()
                try:
                    driver.get("https://www.furaffinity.net/msg/others/#comments")
                    driver.find_element(by=By.XPATH, value="//input[@name='comments-submissions[]']")
                    commentlink = driver.find_elements(by=By.XPATH, value="//ul/li/strong/a")
                    thelinks = []
                    for k in range(len(commentlink)):
                        thelinks.append(commentlink[k].get_attribute('href'))
                    for l in range(len(thelinks)):
                        driver.get(thelinks[l])
                        time.sleep(1)
                        driver.save_screenshot(f'peyz-{time.strftime("%d-%m-%y %H-%M")}.png')
                        time.sleep(1)
                except Exception:
                    print('something goes wrong with comments')
            sumcom = 1
        except NoSuchElementException:
            sumcom = 0
            comment = open('chcom.txt', 'w')
            comment.write('0')
            comment.close()


    def preload():
        time.sleep(1)
        driver.find_element(by=By.LINK_TEXT, value='Upload').click()
#        time.sleep(2)
#        wait = WebDriverWait(driver, 2)
#        next1 = wait.until(EC.element_to_be_clickable([By.XPATH, "//button[@value='Next']"]))
 #       next1.click()
        time.sleep(2)

    def delay():
        driver.quit()
        stats = driver.find_element(by=By.XPATH, value="//div[@id='footer']/div[3]")
        stats_t = stats.text
        stats_str = str(stats_t).split(sep=" ", maxsplit=-1)
        people = int(stats_str[6])
        koef_people = 12000 / people

        tme = int(time.strftime("%H"))
        if 13 <= tme < 22:
            gt = 86400 + random.randrange(-300, 300, 1)
            print(f"slowmode, time is {tme} and gt is {gt}")
        else:
            gt = 87500 + random.randrange(-150, 150, 1)
        ct = 300
        kt = gt
        if int(gt/2) < (gt * koef_people) < int(gt*2):
            kt = int(gt * koef_people)
            st = kt // ct
        else:
            st = gt // ct

        for ts in range(st):
            checknote()
            checkcomm()
            time.sleep(ct)
        time.sleep(kt % ct)

    def posted():
        postedfile = open('testik.txt', 'r+')
        postedfile.seek(0)
        content = postedfile.readlines()
        content[0] = f'Peyzazhik: Последняя запощена {time.strftime("%d/%m в %X")}\n'
        postedfile.seek(0)
        postedfile.writelines(content)
        postedfile.close()

    def turn_with_five():
        turn_five_file = open('turnfivefile.txt', 'w')
        # turn_five_in = '1'
        turn_five_file.write('1')
        turn_five_file.close()

    def one():
        global ga1
        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs1 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex1)
            while len(howmanysubs1) >= 1: #checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs11 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex1)
                howmanysubs11[-1].click()
                time.sleep(2)
                if i == 0: # choice of next upload name (connected with 'perem')
                    address = driver.find_element(by=By.XPATH, value="//img[@id='submissionImg']")
                    ga1 = address.get_attribute("data-fullview-src")
                time.sleep(2)
                analyse()
                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs1.pop()
        except NoSuchElementException:
            ga1 = "14.jpg"

        preload()

        z10 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\10.jpg"
        z11 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\11.jpg"
        z12 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\12.jpg"
        z13 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\13.jpg"
        z14 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\14.jpg"
        z1 = [z10, z11, z12, z13, z14]

        shortg1 = ga1[-6:]
        if shortg1 == "10.jpg":
            perem = 2
        if shortg1 == "11.jpg":
            perem = 3
        if shortg1 == "12.jpg":
            perem = 4
        if shortg1 == "13.jpg":
            perem = 5
        if shortg1 == "14.jpg":
            perem = 1

        #perem = 4  # с какой начать

        if perem == 5:
            z1[0], z1[1], z1[2], z1[3], z1[4] = z1[4], z1[0], z1[1], z1[2], z1[3]
        if perem == 4:
            z1[0], z1[1], z1[2], z1[3], z1[4] = z1[3], z1[4], z1[0], z1[1], z1[2]
        if perem == 3:
            z1[0], z1[1], z1[2], z1[3], z1[4] = z1[2], z1[3], z1[4], z1[0], z1[1]
        if perem == 2:
            z1[0], z1[1], z1[2], z1[3], z1[4] = z1[1], z1[2], z1[3], z1[4], z1[0]

        tz2=z1[i5]
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='0']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex1, Keys.TAB, namez1)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("1")
        finishingf.close()

        turn_five_file = open('turnfivefile.txt', 'w')
        turn_five_file.write('1')
        turn_five_file.close()

        delay()


    def two():
        global ga2
        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs2 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex2)
            while len(howmanysubs2) >= 1:  # checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs21 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex2)
                howmanysubs21[-1].click()
                time.sleep(2)
                if i == 0:  # choice of next upload name (connected with 'perem')
                    address = driver.find_element(by=By.XPATH, value="//img[@id='submissionImg']")
                    ga2 = address.get_attribute("data-fullview-src")
                time.sleep(2)
                analyse()
                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs2.pop()
        except NoSuchElementException:
            ga2 = "25.jpg"

        preload()

        z20 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\20.jpg"
        z21 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\21.jpg"
        z22 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\22.jpg"
        z23 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\23.jpg"
        z24 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\24.jpg"
        z25 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\25.jpg"
        z2 = [z20, z21, z22, z23, z24, z25]

        shortg2 = ga2[-6:]
        if shortg2 == "20.jpg":
            perem = 2
        if shortg2 == "21.jpg":
            perem = 3
        if shortg2 == "22.jpg":
            perem = 4
        if shortg2 == "23.jpg":
            perem = 5
        if shortg2 == "24.jpg":
            perem = 6
        if shortg2 == "25.jpg":
            perem = 1

        #perem = 4  # с какой начать

        if perem == 6:
            z2[0], z2[1], z2[2], z2[3], z2[4], z2 [5] = z2[5], z2[0], z2[1], z2[2], z2[3], z2[4]
        if perem == 5:
            z2[0], z2[1], z2[2], z2[3], z2[4], z2 [5] = z2[4], z2[5], z2[0], z2[1], z2[2], z2[3]
        if perem == 4:
            z2[0], z2[1], z2[2], z2[3], z2[4], z2 [5] = z2[3], z2[4], z2[5], z2[0], z2[1], z2[2]
        if perem == 3:
            z2[0], z2[1], z2[2], z2[3], z2[4], z2 [5] = z2[2], z2[3], z2[4], z2[5], z2[0], z2[1]
        if perem == 2:
            z2[0], z2[1], z2[2], z2[3], z2[4], z2 [5] = z2[1], z2[2], z2[3], z2[4], z2[5], z2[0]

        tz2 = z2[i6]
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='0']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex2, Keys.TAB, namez2)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("2")
        finishingf.close()

        turn_five_file = open('turnfivefile.txt', 'w')
        turn_five_file.write('2')
        turn_five_file.close()

        delay()


    def three():
        global ga3
        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs3 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex3)
            while len(howmanysubs3) >= 1:  # checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs31 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex3)
                howmanysubs31[-1].click()
                time.sleep(2)
                if i == 0:  # choice of next upload name (connected with 'perem')
                    address = driver.find_element(by=By.XPATH, value="//img[@id='submissionImg']")
                    ga3 = address.get_attribute("data-fullview-src")
                time.sleep(2)
                analyse()
                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs3.pop()
        except NoSuchElementException:
            ga3 = "35.jpg"

        preload()

        z30 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\30.jpg"
        z31 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\31.jpg"
        z32 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\32.jpg"
        z33 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\33.jpg"
        z34 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\34.jpg"
        z35 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\35.jpg"
        z3 = [z30, z31, z32, z33, z34, z35]

        shortg3 = ga3[-6:]
        if shortg3 == "30.jpg":
            perem = 2
        if shortg3 == "31.jpg":
            perem = 3
        if shortg3 == "32.jpg":
            perem = 4
        if shortg3 == "33.jpg":
            perem = 5
        if shortg3 == "34.jpg":
            perem = 6
        if shortg3 == "35.jpg":
            perem = 1

        #perem = 4  # с какой начать

        if perem == 6:
            z3[0], z3[1], z3[2], z3[3], z3[4], z3[5] = z3[5], z3[0], z3[1], z3[2], z3[3], z3[4]
        if perem == 5:
            z3[0], z3[1], z3[2], z3[3], z3[4], z3[5] = z3[4], z3[5], z3[0], z3[1], z3[2], z3[3]
        if perem == 4:
            z3[0], z3[1], z3[2], z3[3], z3[4], z3[5] = z3[3], z3[4], z3[5], z3[0], z3[1], z3[2]
        if perem == 3:
            z3[0], z3[1], z3[2], z3[3], z3[4], z3[5] = z3[2], z3[3], z3[4], z3[5], z3[0], z3[1]
        if perem == 2:
            z3[0], z3[1], z3[2], z3[3], z3[4], z3[5] = z3[1], z3[2], z3[3], z3[4], z3[5], z3[0]
        tz2 = z3[i6]
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='0']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex3, Keys.TAB, namez3)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("3")
        finishingf.close()

        turn_five_file = open('turnfivefile.txt', 'w')
        turn_five_file.write('3')
        turn_five_file.close()

        delay()

    def four():
        global ga4
        namex4 = 'Unlimited YCHS $25 reminder'
        namez4 = "Get more details:\nhttps://www.furaffinity.net/view/47649263/\nhttps://www.furaffinity.net/view/47649263/\nhttps://www.furaffinity.net/view/47649263/"

        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs4 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex4)
            while len(howmanysubs4) >= 1:  # checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs41 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex4)
                howmanysubs41[-1].click()
                time.sleep(2)

                analyse()
                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs4.pop()
        except NoSuchElementException:
            ga4 = "4.jpg"


        preload()

        tz2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\4.jpg"
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='1']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex4, Keys.TAB, namez4)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("4")
        finishingf.close()

        turn_five_file = open('turnfivefile.txt', 'w')
        turn_five_file.write('4')
        turn_five_file.close()

        delay()

    def five():
        global ga5
        namex5 = 'ANIMATED YCH reminder'
        url5 = str(https://www.furaffinity.net/view/50969183/)
        namez5 = f'Get more details:{url5}\n{url5}\n{url5}'

        time_of_five_posted = open('timeof5.txt', 'r')
        time_of_five_posted_int = int(time_of_five_posted.read())
        time_of_five_posted.close()
        if 2200 < time_of_five_posted_int < 2400:
            time_of_five_posted_int = time_of_five_posted_int - 2400

        time_now = time.strftime("%H%M")

        if 2200 < int(time_now) < 2400:
            time_now = int(time_now) - 2400
            print(time_now)

        if int(time_now) < time_of_five_posted_int:
            print(f'Too early! Wait until {time_of_five_posted_int}')
            #driver.quit()

        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs4 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex5)
            while len(howmanysubs4) >= 1:  # checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs41 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex5)
                howmanysubs41[-1].click()
                time.sleep(2)

                analyse()

               # driver.find_element(by=By.XPATH, value="//span[@class=popup_date]".title())

                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs4.pop()
        except NoSuchElementException:
            ga4 = "5.jpg"


        preload()

        tz2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\8.png"
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='0']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex5, Keys.TAB, namez5)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        write_five_posted = open('timeof5.txt', 'w')
        write_five_posted.write(str(time_now))
        write_five_posted.close()
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("5")
        finishingf.close()

        delay()

    def six():
        global ga5
        namex5 = 'Banner for FA reminder'
        namez5 = "Get more details:\nhttps://www.furaffinity.net/view/50793309/\nhttps://www.furaffinity.net/view/50793309/\nhttps://www.furaffinity.net/view/50793309/"

        time_of_five_posted = open('timeof5.txt', 'r')
        time_of_five_posted_int = int(time_of_five_posted.read())
        time_of_five_posted.close()
        if 2200 < time_of_five_posted_int < 2400:
            time_of_five_posted_int = time_of_five_posted_int - 2400

        time_now = time.strftime("%H%M")

        if 2200 < int(time_now) < 2400:
            time_now = int(time_now) - 2400
            print(time_now)

        if int(time_now) < time_of_five_posted_int:
            print(f'Too early! Wait until {time_of_five_posted_int}')
            driver.quit()

        try:
            driver.get('https://www.furaffinity.net/controls/submissions/')
            howmanysubs4 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex5)
            while len(howmanysubs4) >= 1:  # checking and DELETING of any excess submissions
                driver.get('https://www.furaffinity.net/controls/submissions/')
                howmanysubs41 = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=namex5)
                howmanysubs41[-1].click()
                time.sleep(2)

                analyse()

               # driver.find_element(by=By.XPATH, value="//span[@class=popup_date]".title())

                driver.find_element(by=By.NAME, value='delete_submissions_submit').click()
                time.sleep(2)
                passw = driver.find_element(by=By.NAME, value='password')
                passw.send_keys('123123123q', Keys.ENTER)
                howmanysubs4.pop()
        except NoSuchElementException:
            ga4 = "7.png"


        preload()

        tz2 = "C:\\Users\\Jukarick\\Downloads\\кайфучьки\\kek\\Новая реальность\\prices\\7.png"
        load1 = driver.find_element(by=By.XPATH, value="//input[@name='submission']")
        load1.send_keys(tz2)
        next2 = driver.find_element(by=By.XPATH, value="//button[@class='button standard']")
        next2.click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value="//input[@value='0']").click()
        driver.find_element(by=By.XPATH, value="//input[@id='title']").send_keys(namex5, Keys.TAB, namez5)
        driver.find_element(by=By.XPATH, value="//input[@id='finalize']").click()
        time.sleep(2)
        print(tz2, " posted at ", time.strftime("%X"))
        write_five_posted = open('timeof5.txt', 'w')
        write_five_posted.write(str(time_now))
        write_five_posted.close()
        posted()

        finishingf = open("turnchr.txt", 'w')
        finishingf.write("6")
        finishingf.close()

        delay()

   # seq = 3 # какая последняя запощена
    if seq == 1:

        two()
        three()
        #four()
        one()
    if seq == 2:

        three()
        #four()
        one()
        two()
    if seq == 3:

        #four()
        one()
        two()
        three()
    if seq == 4:
        five()
        one()
        two()
        three()
        four()
    # if seq == 5:
    #     look_five_turn = open('turnfivefile.txt', 'r+')
    #     turn_five_out = look_five_turn.read()
    #     look_five_turn.close()
    #     if turn_five_out == '1':
    #         two()
    #     if turn_five_out == '2':
    #         three()
    #     if turn_five_out == '3':
    #         four()
    #     if turn_five_out == '4':
    #         one()
    #
    #     two()
    #
    #     three()
    #     five()
    #     four()

    # except Exception:
    #     print('perezapusk')
    #     time.sleep(120)
    #     continue