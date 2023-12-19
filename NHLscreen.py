import requests
from bs4 import BeautifulSoup

def scrape_nhl_stats():
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.nhl.com/stats/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting player names
        player_names = []
        player_name_tags = soup.select('.playerName')
        for tag in player_name_tags:
            player_names.append(tag.get_text())

        # Example: Extracting player points
        player_points = []
        player_point_tags = soup.select('.points')
        for tag in player_point_tags:
            player_points.append(tag.get_text())

        # Print the scraped data
        for name, points in zip(player_names, player_points):
            print(f"Player: {name}, Points: {points}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_nhl_stats()