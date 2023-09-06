from selenium import webdriver
import time
from bs4 import BeautifulSoup  
import random


def crawl(start):
    # 创建一个Chrome浏览器实例
    driver = webdriver.Chrome()
    
    # 打开网页
    url = 'https://ispl.mps.gov.cn/ispl/jsp/common/ProductList_Public.jsp'
    driver.get(url)
    try:
        for k in range(start,401):
            driver.execute_script("changeCurrentPageIndexAndSubmit("+str(k)+");")
            time.sleep(5)
            # 使用 execute_script 方法执行 JavaScript 代码，获取动态渲染的内容  
            tbody_content = driver.execute_script("return document.querySelector('tbody')")
            tbody_content_html = tbody_content.get_attribute("innerHTML")  
              
            # 使用BeautifulSoup解析innerHTML，并获取所有tr标签  
            soup = BeautifulSoup(tbody_content_html, 'html.parser')  
            trs = soup.find_all('tr')  
              
            # 打印每个tr标签的innerHTML
            with open("products.txt", "a", encoding="utf-8") as f:
                for tr in trs:  
                    tds = tr.find_all('td')  
                    allstr = ''
                    for i in range(len(tds)):
                        td = tds[i]
                        if i == len(tds) - 1:
                            strs = td.get_text().strip().strip('\n').split('\n')
                            allstr += (strs[0]+strs[1])
                        else:
                            allstr += (td.get_text().strip().strip('\n')+'-----')
                    f.write(allstr+"\n")
            time.sleep(random.randint(3,10))
            print(k,"/ 400 Complete")
        return "ok"
    except:
        m = k
        print("error with", k, "restarting")
        driver.quit()
        crawl(m)


print(crawl(42))