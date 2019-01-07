def login_weibo_via_mobile_page(driver):
    user_name = ''
    pw = ''
    weibo_mobile_login_page = 'https://passport.weibo.cn/signin/login'
    driver.get(weibo_mobile_login_page)
    time.sleep(3)
    driver.find_element_by_id('loginName').send_keys(user_name)
    time.sleep(3)
    driver.find_element_by_id('loginPassword').send_keys(pw)
    time.sleep(3)
    driver.find_element_by_id('loginAction').click()
    time.sleep(20)
    try:
        if driver.title == '请先验证身份':
            print('验证身份')
            if len(driver.find_elements_by_class_name('geetest_item_wrap')) > 0:
                print('顺序点击多个字')
            if len(driver.find_elements_by_class_name('geetest_wait')) > 0:
                print('点按')
                verify_button = driver.find_element_by_class_name('geetest_wait')
                # left, top, right, bottom = get_element_location(verify_button)

                # first wrong click
                x_offset = random.randint(-30, -3)
                y_offset = random.randint(-30, -3)
                ActionChains(driver).move_to_element_with_offset(verify_button, x_offset, y_offset).click().perform()
                # second correct click
                x_offset = random.randint(0,20)
                y_offset = random.randint(0, 20)
                time.sleep(5)
                ActionChains(driver).move_to_element_with_offset(verify_button,x_offset,y_offset).click().perform()
            time.sleep(10)
            if len(driver.find_elements_by_class_name('geetest_wrap')) > 0:
                print('slide verify')
                slider_button = driver.find_element_by_class_name('geetest_slider_button')
                slider_track = driver.find_element_by_class_name('geetest_slider_track')
                drag_offset_x = slider_track.size['width']
                drag_offset_y = 0
                while(driver.title == '请先验证身份'):
                    ActionChains(driver).drag_and_drop_by_offset(slider_button, drag_offset_x,drag_offset_y).perform()
                    time.sleep(4)
                    drag_offset_x = drag_offset_x*0.95
                print('login_succeed')
    except:
        print('verify error')

def login_weibo_via_QQ_page(driver):
    user_name = ''
    pw = ''
    driver.get('https://www.weibo.com/us#_loginLayer_')
    driver.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[3]/div[2]/ul/li[3]').click()
    time.sleep(30)
    driver.find_element_by_xpath('//*[@id="layer_15468639796201"]/div[2]/div[3]/div[3]/div[7]/a').click()


    driver.find_element_by_class_name('')
    qq_login_page = 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=101019034&response_type=code&scope=get_info%2Cget_user_info&redirect_uri=https%3A%2F%2Fpassport.weibo.com%2Fothersitebind%2Fbind%3Fsite%3Dqq%26state%3DCODE-gz-1GGts4-PfsLN-RT2twFaHAUwktc21ffa8e%26bentry%3Dminiblog%26wl%3D&display='
    driver.get(weibo_mobile_login_page)
    time.sleep(3)
    driver.find_element_by_id('loginName').send_keys(user_name)
    time.sleep(3)
    driver.find_element_by_id('loginPassword').send_keys(pw)
    time.sleep(3)
    driver.find_element_by_id('loginAction').click()
    time.sleep(20)
    try:
        if driver.title == '请先验证身份':
            print('验证身份')
            if len(driver.find_elements_by_class_name('geetest_item_wrap')) > 0:
                print('顺序点击多个字')
            if len(driver.find_elements_by_class_name('geetest_wait')) > 0:
                print('点按')
                verify_button = driver.find_element_by_class_name('geetest_wait')
                # left, top, right, bottom = get_element_location(verify_button)

                # first wrong click
                x_offset = random.randint(-30, -3)
                y_offset = random.randint(-30, -3)
                ActionChains(driver).move_to_element_with_offset(verify_button, x_offset, y_offset).click().perform()
                # second correct click
                x_offset = random.randint(0,20)
                y_offset = random.randint(0, 20)
                time.sleep(5)
                ActionChains(driver).move_to_element_with_offset(verify_button,x_offset,y_offset).click().perform()
            time.sleep(10)
            if len(driver.find_elements_by_class_name('geetest_wrap')) > 0:
                print('slide verify')
                slider_button = driver.find_element_by_class_name('geetest_slider_button')
                slider_track = driver.find_element_by_class_name('geetest_slider_track')
                drag_offset_x = slider_track.size['width']
                drag_offset_y = 0
                while(driver.title == '请先验证身份'):
                    ActionChains(driver).drag_and_drop_by_offset(slider_button, drag_offset_x,drag_offset_y).perform()
                    time.sleep(4)
                    drag_offset_x = drag_offset_x*0.95
                print('login_succeed')
    except:
        print('verify error')
