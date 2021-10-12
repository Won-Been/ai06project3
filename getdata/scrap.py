import requests
import json
from bs4 import BeautifulSoup


BASE_URL = 'https://www.aladin.co.kr/'

def get_page(page_url):
    """
    해당 페이지의 html 정보 가져오기
    """
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return page, soup

def get_id(page_num=4):
    """
    베스트 셀러(1위-200위) 책들의 id 가져오기
    """
    bestseller_id = []
    for i in range(1,page_num+1):
        bestseller_url = f'{BASE_URL}/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={i}&cnt=1000&SortOrder=1'
        page_id, soup_id = get_page(bestseller_url)

        id_url = soup_id.select('.bo3') #클래스 bo3중 가장 위에 있는 값 가져오기
        
        for d in id_url:
            d = d.get('href') #href속성 가져오기
            ids = int(d.split('=')[1]) #id값만 가져와 정수형으로 바꾸기
            bestseller_id.append(ids) #리스트에 넣기
        
    return bestseller_id



def info(ItemId):

    book_url = f'{BASE_URL}/shop/wproduct.aspx?ItemId={ItemId}'
    page_book, soup_book = get_page(book_url)
    
    #Sales Point, 평점, 장르 가져오기
    sales_point = soup_book.find('div',style='display:inline-block;').find('strong').text
    rating = float(soup_book.find(class_='Ere_sub_pink Ere_fs16 Ere_str').text)
    genre = soup_book.select('#ulCategory>li>a')[1].text

    return [sales_point, rating, genre] #리스트로 만들기







