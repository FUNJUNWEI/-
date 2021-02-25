import requests
import time

url0 = 'https://pan.ltyuanfang.cn/%E8%A7%86%E9%A2%91/%E5%8A%A8%E6%BC%AB/%E5%93%86%E5%95%A6a%E6%A2%A62020/'
for i in range(588,636):
    url = url0 + str(i) + '.mp4'
    file_name = str(i)+'.mp4'
    r = requests.get(url,stream = True)
    with open('./'+file_name, 'wb') as f:
       for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
    f.close()
    print(file_name)
    time.sleep(1)
