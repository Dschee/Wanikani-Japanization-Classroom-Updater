from bs4 import BeautifulSoup

from web_client import WebClient


WANIKANI_PROFILE_URL = 'https://www.wanikani.com/users/'


class WKProfileFetcher:
    def __init__(self, username):
        self.username = username

    def get_items(self):
        web_client = WebClient(WANIKANI_PROFILE_URL + self.username)
        wanikani_soup = BeautifulSoup(web_client.html, features='html.parser')
        apprentice_element = wanikani_soup.find('li', {'id': 'apprentice'})
        apprentice_count = apprentice_element.find('span').text if apprentice_element else None
        guru_element = wanikani_soup.find('li', {'id': 'guru'})
        guru_count = guru_element.find('span').text if apprentice_element else None
        master_element = wanikani_soup.find('li', {'id': 'master'})
        master_count = master_element.find('span').text if apprentice_element else None
        enlightened_element = wanikani_soup.find('li', {'id': 'enlightened'})
        enlightened_count = enlightened_element.find('span').text if apprentice_element else None
        burned_element = wanikani_soup.find('li', {'id': 'burned'})
        burned_count = burned_element.find('span').text if apprentice_element else None
        level_element = wanikani_soup.find('span', {'class': 'level'})
        level = level_element.text if level_element else None
        return {'apprentice': apprentice_count, 'guru': guru_count, 'master': master_count,
                'enlightened': enlightened_count, 'burned': burned_count, 'level': level}
