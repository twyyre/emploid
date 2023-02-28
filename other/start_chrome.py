from pywinauto import Desktop, Application

chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
page_url = 'http://10.10.20.44:4455/'
chrome = Application().start(chrome_dir+' --force-renderer-accessibility --incognito --start-maximized ' + page_url)
app_new_tab = Application(backend='uia').connect(path='chrome.exe', title_re='New Tab')
