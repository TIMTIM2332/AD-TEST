import requests

def fetch_user(username='octocat'):
    url = f'https://api.github.com/users/{username}'
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    print('Name:', data.get('name'))
    print('Public repos:', data.get('public_repos'))
    print('Profile URL:', data.get('html_url'))

if __name__ == '__main__':
    fetch_user('octocat')
