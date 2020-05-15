from selenium import webdriver
import pickle
blocked = ["Isohunt.com", "thepiratebay.org", "thepiratebay.se","torrentz.eu","kat.ph","torlock.com","kickasstorrents.com","torrentfunk.com","fenopy.eu"]
try:
    with open("web_block_info.pickle","rb")  as file:
        blocked += pickle.load(file)['blocked_websites']
        print("success reading pickle")
except IOError:
    print("""You are in the setup mode of this application
             Enter keywords in the websites to block :- 
             (separated by space eg. com,org,net,coep etc...)""")
    l = {}
    l['blocked_websites'] = list(input().split())
    blocked += l['blocked_websites']
    with open("web_block_info.pickle","wb")  as file:
        pickle.dump(l,file)
    print("setup completed")

data = []
for i in blocked:
    if i[0] == '.':
        data.append(i[1:])
    keys = i.split('.')
    data += keys[:-1]
    if len(keys) == 1:
        data.append(keys[0])

print(data)
while 1:
    url = input("Enter the name of the website : ")
    keywords = url.split(".")
    t =[]
    for i in keywords:
        if i in data:
            t.append(i)
    if not t == []:
        print("""This website is blocked :(
Surf Again : """)
        continue
    try:
        print("Redirecting ......")
        # driver = webdriver.Firefox("./webdrivers/geckodriver.exe")
        driver = webdriver.Chrome("./webdrivers/chromedriver.exe")
        driver.get("https://" + url)
    except Exception as e:
        print("""An error occured !!
                    You can try these things : 
                    1. Check that you have the correct webdriver (Chrome/Firefox)
                    2. Check the version of webdriver with the browser
                    3. Proxy Check
                    4.Recheck the URL you typed in...""")
        print(e)
    break
