from web_keys.keys import Key

# 点击第一条热搜
key = Key('Chrome')
key.oppen('http://www.baidu.com')
key.click('xpath', '//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')
key.sleep(3)
key.quit()


# 点击登录提交证号密码
key = Key('Chrome')
key.oppen('http://www.baidu.com')
key.click('id', 's-top-loginbtn')
key.input('id', 'TANGRAM__PSP_11__userName', '18513006430')
key.input('id', 'TANGRAM__PSP_11__password', '20180914.l')
key.click('id', 'TANGRAM__PSP_11__submit')
key.sleep(5)
key.quit()