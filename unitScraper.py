import requests, json, time, re
from bs4 import BeautifulSoup

class unitScraper:
    def __init__(self):
        param_keys = json.load(open("param.json"))
        self.type = list(param_keys['type'].values())
        self.cid = list(param_keys['cid'].values())
        self.brand = list(param_keys['brand'].values())
        self.goods_list_url = "http://unit808.com/shop/goods_list_baleno.php"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        }
        self.payload = {
            "cid": "",
            "brand": "",
            "type": "",
            "orderby": "",
            "max": "24",
            "page": 1
        }
    
    def extract_goods_single(self, link):
        goods_url = link
        r = requests.get(goods_url, headers=self.headers)
        if r.status_code == 200:
            # with open ('soup.txt', 'w', encoding='utf-8-sig') as f:
            #     f.write(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            price_info = soup.find('div', {'class': 'goods_info_text1'}).find_all('li')
            data = {
                'imageLink': soup.find('img', {'id': 'main_img'})['src'],
                'name': re.sub('[\r\n]','',soup.find('li', {'class': 'goods_name_new'}).text),
                'sellPrice': re.sub('[\r\n]','',price_info[0].find('dd').text),
                'memberPrice': re.sub('[\r\n]','',price_info[1].find('dd').text),
                'id': re.sub('[\r\n]','',price_info[2].find('dd').text),
                'country': re.sub('[\r\n]','',soup.find('td', {'class':'country'}).text),
                'optionNames': [],
            }
            try:
                data['optionNames'] = [option['title'] for option in soup.find_all('select', {'class': 'goods_options'})]
                for option in data['optionNames']:
                    i = data['optionNames'].index(option)
                    data[f'{option}'] = (",").join([value.text for value in soup.find_all('select', {'class': 'goods_options'})[i].find_all('option')][1:])
            except:
                pass
            try:
                data['html'] = re.sub('[\t\n\s]','',str(soup.find('div', {'class':'goods_view_type1'})))
            except:
                data['html'] = None
            return data
        else:
            with open('error.txt', 'a', encoding='utf-8-sig') as f:
                f.write(goods_url)
            return


    def extract_goods_list(self): 
        for t in self.type:
            for c in self.cid:
                for b in self.brand:
                    self.payload['cid'] = c
                    self.payload['brand'] = b
                    self.payload['type'] = t
                    self.extract_goods_links()
        return
    
    def extract_goods_links(self):
        extracted = []
        self.payload['page'] = 1
        r = requests.get(self.goods_list_url, params=self.payload, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        goods_count = int(soup.find('span', {'style': ' font-weight: 600;'}).text.replace(',',''))
        print({'cid': self.payload['cid'], 'brand': self.payload['brand'], 'type': self.payload['type'], 'count': goods_count})
        while len(extracted) < goods_count:
            r = requests.get(self.goods_list_url, params=self.payload, headers=self.headers)
            print(self.payload['page'])
            soup = BeautifulSoup(r.text, 'html.parser')
            goods_list = soup.find('div', {'class': 'goods_list_new'}).find_all('li', {'class': 'roop_class'})
            for goods in goods_list:
                link = goods.find('a')['href']
                extracted.append(link)
                with open(f"links/{self.payload['cid']}_{self.payload['brand']}_{self.payload['type']}.txt", 'a') as f:
                    f.write(link+"\n")
            time.sleep(0.2)
            self.payload['page'] += 1
            if len(extracted) >= goods_count:
                break
            if self.payload['page'] >= 417:
                break
            
