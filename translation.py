import urllib.request
import urllib.parse
import os
import json
while(1):
    content=input("请输入需要翻译的内容:")
    if(content=='exit'):
        break
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data={}

    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom:fanyi']='web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    data=urllib.parse.urlencode (data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    print("翻译结果为:%s"%(target['translateResult'][0][0]['tgt']))
#input ('按任意键退出：')
os.system('pause')
#print(html)
