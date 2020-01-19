import bs4
import requests as rq
import os

def pre_append(list, string):
    temp_list = []
    for item in list:
        temp_item = string + item
        temp_list.append(temp_item)
    return temp_list

def main():
    os.mkdir('downloads')
    url = input('Enter a url: ')
    headers = {'User-Agent': 'Guptaji\'s_request'}
    r = rq.get(url, headers = headers)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    list_of_urls = []
    for item in images:
        list_of_urls.append(item['src'])
    list_of_urls = pre_append(list_of_urls, 'https:')
    i = 0
    for item in list_of_urls:
        if 'static' in item:
            continue # not downloading static images
        else:
            r = rq.get(item)
            file_name = str(i+1) + ".jpg"
            with open(os.path.join('downloads', file_name), 'wb+') as f:
                f.write(r.content)
            print("image" + str(i+1) + " downloaded")
        i = i + 1

main()