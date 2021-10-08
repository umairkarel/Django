import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search

BASE_CRAIGLIST_URL = "https://mumbai.craigslist.org/search/?query={}"
IMG_BASE_URL = "https://images.craigslist.org/{}_300x300.jpg"

# Create your views here.
def home(request):
    return render(request, 'my_app/base.html')

def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search) # Adding to database
    search_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(search_url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    posts = soup.find_all('li', class_='result-row')
    final_posts = []
    
    for post in posts:
        post_title = post.find('a', class_="result-title").text
        post_url   = post.find('a', class_="result-title")['href']
        data_ids    = post.find('a', class_="result-image")['data-ids']
        data_id    = data_ids.split(':')[1].split(',')[0]
        
        if data_id:
            img_url = IMG_BASE_URL.format(data_id)
        else:
            img_url = "https://craigslist.org/images/peace.jpg"

        try:
            post_price = post.find(class_='result-price').text
        except:
            post_price = 'N/A'

        final_posts.append((post_title, post_url, img_url, post_price))

    context = {
        'search': request.POST.get('search'),
        'posts': final_posts,
    }

    return render(request, 'my_app/new_search.html', context)