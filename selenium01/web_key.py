from web_keys.keys import Key

# # 点击第一条热搜
# key = Key('Chrome')
# key.oppen('http://www.baidu.com')
# key.click('xpath', '//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')
# key.sleep(3)
# key.quit()
#
# # 点击登录提交证号密码
# key = Key('Chrome')
# key.oppen('http://www.baidu.com')
# key.click('id', 's-top-loginbtn')
# key.input('id', 'TANGRAM__PSP_11__userName', '18513006430')
# key.input('id', 'TANGRAM__PSP_11__password', '20180914.l')
# key.click('id', 'TANGRAM__PSP_11__submit')
# key.sleep(5)
# key.quit()

key = Key('Chrome')
key.oppen('https://test-office.ptdplat.com/?#/login')
key.click('id', 'tab-1')
key.input('xpath', '//*[@id="pane-1"]/div[1]/div/div/input', 'F1G27')
key.input('xpath', '//*[@id="pane-1"]/div[2]/div/div/input', '123456')
key.click('xpath', '//*[@id="app"]/div/div[3]/div[2]/form/button/span')
key.click('xpath', '//*[text()="涂多多商城"]')
key.click('xpath', '//*[@id="app"]/div[1]/div/div/div/div[2]/div[3]/div[1]/span')
key.sleep(3)
key.quit()
