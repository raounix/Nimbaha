import requests

from bs4 import BeautifulSoup
import ipaddress


def get_content(page):
    URL = 'https://www.proxyhub.me/en/ir-free-proxy-list.html'
    cookies = {'page': str(page)}
    page = requests.get(URL,cookies=cookies)

    soup = BeautifulSoup(page.content, 'html.parser')

    ip_list = []


    find_attr= soup.find_all("tbody")
    for body in find_attr:
        table_row=body.find_all("tr")
        for row in table_row:
            listed_row=row.find_all("td")
            ip=listed_row[0].text
            port=listed_row[1].text
            Type=listed_row[2].text
            Anonymity=listed_row[3].text
            json_obj={"ip":ip,"port":port,"type":Type,"anonymity":Anonymity}
            ip_list.append(json_obj)
    return ip_list


last_page=3
counter=1
print("Tedad IP : {} \n\n".format(str(last_page*20)))
for i in range(1,last_page+1):

    ip_list=get_content(i)

    
    for ip in ip_list:
        response = requests.post('https://api.linkirani.ir/apiv1/shortlink', json={'url': ip['ip']})

        is_registered=response.json()['isRegistered']
        
        if(is_registered==True):
            print(str(counter) ," - Dakheli : " ,ip)
        else:
            print(str(counter) ," - Dakheli Nist")
        counter+=1