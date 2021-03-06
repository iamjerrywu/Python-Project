import requests
from bs4 import BeautifulSoup


def main():
    # url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    # source_code = requests.get(url)
    # # print(source_code)
    # html = source_code.text
    # soup = BeautifulSoup(html)
    # items = soup.find_all('td', {'class':'titleColumn'})
    # d = {}
    # for item in items:
    #     year = item.span.text
    #     if year not in d:
    #         d[year] = 1
    #     else:
    #         d[year] += 1
    # for key, value in sorted(d.items(), key=lambda t : t[1]):
    #     print(key, value)
    # items = soup.find_all('td', {'class':'ratingColumn imdbRating'})
    # d = {}
    # score = 0
    # cnt = 0
    # for item in items:
    #     score+= float(item.strong.text)
    #     cnt+=1
    # print(score/cnt)


    # href_tags = soup.find_all(href = True)
    # d = {}
    # print(href_tags)
    # # print(items.)
    url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
    source_code = requests.get(url)

    html = source_code.text
    soup = BeautifulSoup(html)
    items = soup.find_all('span', {'class':'lister-item-year text-muted unbold'})
    for item in items:
        print(item.text)







if __name__ == '__main__':
    main()

