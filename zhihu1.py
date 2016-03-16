from zhihu import ZhihuClient

Cookies_File = 'cookies.json'

client = ZhihuClient(Cookies_File)
dict={}

author = client.author('https://www.zhihu.com/people/zhang-jia-wei')
#author = client.author('https://www.zhihu.com/people/mo-ming-42-91')
print('--- Followers ---')
for follower in author.followers:
   
   
   if(follower.education!='unknown'):
      print(follower.name,follower.education)
      with open('zhihu.txt','a') as f:
         f.write(follower.name+": "+follower.education+"\n")
      if(follower.education in dict):
         dict[follower.education]+=1
      else:
         dict[follower.education]=1

'''print('--- Followees ---')
for followee in author.followees:
   print(followee.name,followee.education)'''
print(dict)
with open('zhihu.txt','a') as f:
      f.write(str(dict)+"\n")
