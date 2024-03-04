from bs4 import BeautifulSoup
import requests
import re
import codecs

def get_series_info(series_url):
    series_page = requests.get(series_url)
    series_soup = BeautifulSoup(series_page.text, features="html5lib")

    title = series_soup.find('title')
    series_title = title.string.split("|")[0].strip()

    series_description = series_soup.select("h2.short-description")[0].get_text()

    data = {
        'title' : series_title,
        'description' : series_description
    }

    return data

def get_series_episodes(series_url):
    series_page = requests.get(series_url)
    series_soup = BeautifulSoup(series_page.text, features="html5lib")

    data = series_soup.findAll('div',attrs={'id':'list-layer'})
    episodes_urls = []
    for div in data:
        links = div.findAll('a')
        for a in links:
            video_url = a['href'].replace("/videos/detail/", "")
            episodes_urls.append(video_url)
    
    return episodes_urls

def get_episode_details(episode_url):
    episode_page = requests.get(episode_url)
    episode_soup = BeautifulSoup(episode_page.text, features="html5lib")

    episode_info = episode_soup.find('div',attrs={'id':'content-info'})

    episode_title = episode_info.select("h3.name")[0].get_text()
    episode_description = episode_info.select("p.description")[0].get_text()

    title_parts = episode_title.split("|")
    episode_name = title_parts[0].strip()
    episode_number = int(re.findall("(\d+)", title_parts[1])[0])
    
    episode_data = {
        'name' : episode_name,
        'number' : episode_number,
        'description' : episode_description
    }

    return episode_data

def get_episode_m3u8(video_url):
    video_page = requests.get(video_url)
    video_raw_text = video_page.text

    master_url = codecs.decode(re.findall("(https:.*master\.m3u8)", video_raw_text)[0], 'unicode-escape')

    return master_url



