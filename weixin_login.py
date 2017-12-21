import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4")
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('li', attrs={"class": "subject-item"})
# print(len(results))
first_result = results[0]
# print(first_result)

first_result_content = first_result.content
records = []
for result in results:
    pub_content = result.find("div", attrs={"class": "pub"}).text
    comment_number = result.find("span", attrs={"class": "pl"}).text
    description = result.find("div", attrs={"class": "info"}).find("p").text
    buy_link_a = result.find("span", attrs={"class": "market-info"})
    if buy_link_a:
        buy_link = result.find("span", attrs={"class": "market-info"}).find('a').get("href")
    else:
        buy_link = "no buy link"
    records.append((pub_content, comment_number, description, buy_link))
# print(records[0:3])
df = pd.DataFrame(records, columns=["publish_info", "commented", "summary", "how_to_buy"])
df.to_csv('/Users/liying/Documents/task/trump_lies.csv', index=False, encoding='utf-8')
