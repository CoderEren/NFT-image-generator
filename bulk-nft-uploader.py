from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import pyautogui

extension_path = r"LOCATION/OF/METAMASK/EXTENSION"
chrome_driver_path = r"LOCATION/OF/CHROMEDRIVER"
firefox_path = "LOCATION/OF/GECKODRIVER"
recovery_phase = "RECOVERY PHRASE OF YOUR CRYPTO WALLET"
password = "YOUR METAMASK WALLET PASSWORD"
images_folder = "LOCATION/OF/IMAGES/FOLDER"


def move_to_opensea():
    driver.execute_script('''window.open("https://opensea.io/collection/cryptosharkskingdom/assets/create","_blank")''')
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(3)


def upload_to_opensea():
    options = webdriver.FirefoxOptions()  # Configure options for Firefox.
    options.add_extension(extension_path)  # Add extension.
    driver = webdriver.Firefox(executable_path=firefox_path, options=options)
    driver.maximize_window()
    print("The driver started")
    

with open("C:/Users/Eren Geridonmez/Desktop/Crypto Sharks NFT/metadata/all-traits.json", "r") as f:
    data = json.load(f)


def working_setup_metamask():
    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.install_addon(extension_path)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    get_started = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div/button")
    get_started.click()
    import_wallet = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button")
    import_wallet.click()
    no_thanks = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]")
    no_thanks.click()
    recovery_phase_input = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input")
    recovery_phase_input.send_keys(recovery_phase)
    password_input = driver.find_element_by_xpath('//*[@id="password"]')
    password_input.send_keys(password)
    password_input2 = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    password_input2.send_keys(password)
    terms_checkbox = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/div[7]/div")
    terms_checkbox.click()
    import_button = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/button")
    import_button.click()
    time.sleep(15)

    new_changes_close = driver.find_element_by_css_selector(".fa-times")
    new_changes_close.click()
    #move to opensea
    driver.execute_script('''window.open("https://opensea.io/collection/cryptosharkskingdom/assets/create","_blank")''')
    #connect metamask wallet
    time.sleep(30)


    for i in data:
        driver.switch_to.window(driver.window_handles[2])
        file_drop = driver.find_element_by_css_selector('div.CenterAlignedreact__CenterAligned-sc-cjf6mn-0:nth-child(2)')
        time.sleep(2)
        file_drop.click()
        time.sleep(1)

        handles = driver.window_handles
        print(len(handles))
        
        pyautogui.write(images_folder + str(i['tokenId']) + '.png', interval=0.1)
        time.sleep(3)
        pyautogui.press('return')
        time.sleep(5)
        nft_name = driver.find_element_by_xpath('//*[@id="name"]')
        nft_name.send_keys("Crypto Shark #" + str(i["tokenId"]))
        properties_plus = driver.find_element_by_xpath("//html/body/div[1]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button")
        properties_plus.click()
        time.sleep(5)
        
        property_type1 = driver.find_element_by_css_selector("input.browser-default:nth-child(3)")
        property_type1.send_keys("Background")
        property_value1 = driver.find_element_by_css_selector(".AssetPropertiesForm--value-input > input:nth-child(2)")
        property_value1.send_keys(i['background'])
        add_more = driver.find_element_by_css_selector("button.Blockreact__Block-sc-1xf18x6-0:nth-child(3)")
        add_more.click()

        property_type2 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(2) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")
        property_type2.send_keys("Base")
        property_value2 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
        property_value2.send_keys(i['base'])
        add_more.click()

        property_type3 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(3) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")
        property_type3.send_keys("Eye")
        property_value3 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
        property_value3.send_keys(i['eye'])
        add_more.click()

        property_type4 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(4) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")
        property_type4.send_keys("Hat")
        property_value4 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
        property_value4.send_keys(i['hat'])
        add_more.click()

        property_type5 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(5) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")
        property_type5.send_keys("Mouth")
        property_value5 = driver.find_element_by_css_selector("tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(5) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
        property_value5.send_keys(i['mouth'])
        save_button = driver.find_element_by_css_selector("footer.Blockreact__Block-sc-1xf18x6-0 > button:nth-child(1)")
        save_button.click()

        create_button = driver.find_element_by_css_selector(".fzwDgL")
        create_button.click()
        print("Finished")

        #selling the nft
        time.sleep(10)
        close_button = driver.find_element_by_css_selector(".gWXeYL > button:nth-child(1)")
        close_button.click()
        time.sleep(3)
        sell_button = driver.find_element_by_css_selector(".OrderManager--cta-container > span:nth-child(2) > a:nth-child(1)")
        sell_button.click()
        time.sleep(8)
        price_input = driver.find_element_by_css_selector(".cYEToy > div:nth-child(2) > input:nth-child(1)")
        price_input.send_keys("0.005")
        complete_button = driver.find_element_by_css_selector("button.Blockreact__Block-sc-1xf18x6-0:nth-child(1)")
        complete_button.click()
        time.sleep(8)
        sign_sale = driver.find_element_by_css_selector("button.bhqEJb:nth-child(2)")
        sign_sale.click()
        time.sleep(4)

        handles = driver.window_handles
        print(len(handles))

        driver.switch_to.window(driver.window_handles[3])

        time.sleep(2)
        sign_metamask = driver.find_element_by_css_selector("button.button:nth-child(2)")
        sign_metamask.click()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(9)
        close_sale_button = driver.find_element_by_css_selector(".gWXeYL > button:nth-child(1)")
        close_sale_button.click()
        time.sleep(2)
        driver.execute_script('''window.open("https://opensea.io/collection/cryptosharkskingdom/assets/create", "_self")''')
        time.sleep(3)







def setup_metamask2():
    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.install_addon(extension_path)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    get_started = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div/button")
    get_started.click()
    import_wallet = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button")
    import_wallet.click()
    no_thanks = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]")
    no_thanks.click()
    recovery_phase_input = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input")
    recovery_phase_input.send_keys(recovery_phase)
    password_input = driver.find_element_by_xpath('//*[@id="password"]')
    password_input.send_keys(password)
    password_input2 = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    password_input2.send_keys(password)
    terms_checkbox = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/div[7]/div")
    terms_checkbox.click()
    import_button = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div/form/button")
    import_button.click()
    time.sleep(15)

    new_changes_close = driver.find_element_by_css_selector(".fa-times")
    new_changes_close.click()
    #move to opensea
    driver.execute_script('''window.open("https://opensea.io/collection/cryptosharkskingdom/assets/create","_blank")''')
    #connect metamask wallet
    time.sleep(30)


    for i in data:
        driver.switch_to.window(driver.window_handles[2])
        file_drop = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.CenterAlignedreact__CenterAligned-sc-cjf6mn-0:nth-child(2)")))
        file_drop.click()
        time.sleep(1)
        
        pyautogui.write(images_folder + str(i['tokenId']) + '.png', interval=0.1)
        time.sleep(4)
        pyautogui.press('return')
        time.sleep(7)
        nft_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="name"]')))
        nft_name.send_keys("Crypto Shark #" + str(i["tokenId"]))
        properties_plus = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/body/div[1]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button")))
        properties_plus.click()
        
        property_type1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.browser-default:nth-child(3)")))
        property_type1.send_keys("Background")
        property_value1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".AssetPropertiesForm--value-input > input:nth-child(2)")))
        property_value1.send_keys(i['background'])
        add_more = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.Blockreact__Block-sc-1xf18x6-0:nth-child(3)")))
        add_more.click()

        property_type2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(2) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")))
        property_type2.send_keys("Base")
        property_value2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")))
        property_value2.send_keys(i['base'])
        add_more.click()

        property_type3 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(3) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")))
        property_type3.send_keys("Eye")
        property_value3 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")))
        property_value3.send_keys(i['eye'])
        add_more.click()

        property_type4 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(4) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")))
        property_type4.send_keys("Hat")
        property_value4 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")))
        property_value4.send_keys(i['hat'])
        add_more.click()

        property_type5 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(5) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)")))
        property_type5.send_keys("Mouth")
        property_value5 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.AssetPropertiesFormreact__TrContainer-sc-g5scfi-0:nth-child(5) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")))
        property_value5.send_keys(i['mouth'])
        save_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.Blockreact__Block-sc-1xf18x6-0 > button:nth-child(1)")))
        save_button.click()

        create_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fzwDgL")))
        create_button.click()
        print("Finished")

        #selling the nft
        close_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".gWXeYL > button:nth-child(1)")))
        close_button.click()
        sell_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".OrderManager--cta-container > span:nth-child(2) > a:nth-child(1)")))
        sell_button.click()
        price_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cYEToy > div:nth-child(2) > input:nth-child(1)")))
        price_input.send_keys("0.005")
        complete_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.Blockreact__Block-sc-1xf18x6-0:nth-child(1)")))
        complete_button.click()
        sign_sale = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.bhqEJb:nth-child(2)")))
        sign_sale.click()
        time.sleep(4)

        handles = driver.window_handles
        print(len(handles))

        driver.switch_to.window(driver.window_handles[3])

        sign_metamask = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button:nth-child(2)")))
        sign_metamask.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[2])

        close_sale_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".gWXeYL > button:nth-child(1)")))
        close_sale_button.click()
        time.sleep(2)
        driver.execute_script('''window.open("https://opensea.io/collection/cryptosharkskingdom/assets/create", "_self")''')
        time.sleep(3)



