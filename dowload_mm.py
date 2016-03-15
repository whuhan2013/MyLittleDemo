import urllib.request
import os
import random
def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
    '''iplist=['1.193.162.123:8000','1.193.162.91:8000','1.193.163.32:8000']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener=urllib.request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER')]

    urllib.request.install_opener(opener)'''
    
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
def get_page(url):
        
    html=url_open(url).decode('utf-8')
    a=html.find('current-comment-page')+23
    b=html.find(']',a)
        
    #print(html[a:b])
    return html[a:b]
    
    
def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs=[]

    a=html.find('img src=')
    while a!=-1:
        b=html.find('.jpg',a,a+140)
        if b!=-1:
            if html[a+9]!='h':
                img_addrs.append('http:'+html[a+9:b+4])
            else:
                img_addrs.append(html[a+9:b+4])
        else:
            b=a+9

        a=html.find('img src=',b)
    
    for each in img_addrs:
        print(each+'我的打印')
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        #print('one was saved')
        filename=each.split('/')[-1]
        with open(filename,'wb') as f:
            img=url_open(each)
            f.write(img)
        

        
def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://jandan.net/ooxx/"
    page_num=int(get_page(url))

    for i in range(pages):
        page_num=page_num-1
        page_url=url+'page-'+str(page_num)+'#comments'
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__=='__main__':
    download_mm()
