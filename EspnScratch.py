from bs4 import BeautifulSoup
import requests

def scartchEspn(gameNum):
    response = requests.get('https://www.espn.com/soccer/matchstats?gameId='+ gameNum)
    soup = BeautifulSoup(response.text, 'html.parser')

    gameInfo = []
    gameInfo = espn(gameInfo, soup, 'home')
    gameInfo = espn(gameInfo, soup, 'away')

    return gameInfo

def espn(gameInfo, soup,homeAway):
    try:
        if homeAway == 'home':
            gameInfo.append(soup.find('body').find('div', {'class': 'competitors sm-score'}).find('div', {'class': 'team away'}).find('span', {'class': 'abbrev'}).text)
        else:
            gameInfo.append(soup.find('body').find('div', {'class': 'competitors sm-score'}).find('div', {'class': 'team home'}).find('span', {'class': 'abbrev'}).text)
    except:
        if homeAway == 'home':
            gameInfo.append(soup.find('body').find('div', {'class': 'competitors sm-score'}).find('div', {'class': 'team away tied'}).find('span', {'class': 'abbrev'}).text)
        else:
            gameInfo.append(soup.find('body').find('div', {'class': 'competitors sm-score'}).find('div', {'class': 'team home tied'}).find('span', {'class': 'abbrev'}).text)


    gameInfo.append(soup.find('body').find('span', {'data-stat': 'score', 'data-home-away': homeAway}).text[15:16])
    gameInfo.append(soup.find('body').find('span', {'class': 'chartValue', 'data-home-away': homeAway}).text[:-1])
    shots = soup.find('body').find('span', {'data-stat': 'shotsSummary', 'data-home-away': homeAway}).text
    gameInfo.append(shots[:shots.find('(')-1])
    gameInfo.append(shots[shots.find('(')+1:shots.find(')')])
    gameInfo.append(soup.find('body').find('td', {'data-stat': 'foulsCommitted', 'data-home-away': homeAway}).text)
    gameInfo.append(soup.find('body').find('td', {'data-stat': 'yellowCards', 'data-home-away': homeAway}).text)
    gameInfo.append(soup.find('body').find('td', {'data-stat': 'redCards', 'data-home-away': homeAway}).text)
    gameInfo.append(soup.find('body').find('td', {'data-stat': 'offsides', 'data-home-away': homeAway}).text)
    gameInfo.append(soup.find('body').find('td', {'data-home-away': homeAway, 'data-stat': 'wonCorners'}).text)
    gameInfo.append(soup.find('body').find('td', {'data-stat': 'saves', 'data-home-away': homeAway}).text)

    gameInfo.append(soup.find('body').find('div', {'id':'gamepackage-team-form-'+homeAway}).find('a', {'class':'webview-internal'}).get('href')[21:])
    return gameInfo


