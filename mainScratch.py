import EspnScratch
from xlwt import Workbook


def teamScratch(teamName, gameNum, numberOfGame):
    gameInfo = EspnScratch.scartchEspn(str(gameNum))
    games = [gameInfo]
    for i in range(numberOfGame - 1):
        print(gameInfo)
        if teamName == gameInfo[0]:
            gameInfo = EspnScratch.scartchEspn(gameInfo[11])
        else:
            gameInfo = EspnScratch.scartchEspn(gameInfo[23])
        games.append(gameInfo)
    return games



wb = Workbook("MLS.xls")

teams = [['ATL','533005'],['NE','533005'],['ORL','532999'],['CHI','532999'],['LAFC','533000'],['COL','533000'],['TOR','533001'],['CLB','533001'],
         ['DC','533002'],['CIN','533002'],['DAL','533010'],['SKC','533010'],['HOU','533003'],['LA','533003'],['MIN','533004'],['SEA','533004'],
         ['MTL','533007'],['NY','533007'],['PHI','533006'],['NYC','533006'],['POR','533009'],['SJ','533009'],['RSL','533008'],['VAN','533008']]

for i in teams:
    teamName = i[0]
    games = teamScratch(teamName, i[1], 32)

    sheet = wb.add_sheet(teamName)

    sheet.write(0, 0, 'Win')
    sheet.write(0, 1, 'HomeOrAway')
    sheet.write(0, 2, 'Goals')
    sheet.write(0, 3, 'Possession')
    sheet.write(0, 4, 'Shots')
    sheet.write(0, 5, 'Shots on Target')
    sheet.write(0, 6, 'Fouls')
    sheet.write(0, 7, 'Yellow Cards')
    sheet.write(0, 8, 'Red Cards')
    sheet.write(0, 9, 'Offsides')
    sheet.write(0, 10, 'Corner Kicks')
    sheet.write(0, 11, 'Saves')
    sheet.write(0, 12, 'Opponent')
    sheet.write(0, 13, 'Opponent Goals')
    sheet.write(0, 14, 'Opponent Possession')
    sheet.write(0, 15, 'Opponent Shots')
    sheet.write(0, 16, 'opponent Shots on Target')
    sheet.write(0, 17, 'Opponent Fouls')
    sheet.write(0, 18, 'Opponent Yellow Cards')
    sheet.write(0, 19, 'Opponent Red Cards')
    sheet.write(0, 20, 'Opponent Offsides')
    sheet.write(0, 21, 'Opponent Corner Kicks')
    sheet.write(0, 22, 'Opponent Opponent Saves')

    for i in range(len(games)):
        g = games[i]
        if g[0] == teamName:

            if g[1] > g[13]:
                sheet.write(i + 1, 0, 1)
            elif g[1] == g[13]:
                sheet.write(i + 1, 0, 0.5)
            else:
                sheet.write(i + 1, 0, 0)

            sheet.write(i + 1, 1, 1)

            for j in range(10):
                sheet.write(i + 1, j + 2, int(g[j + 1]))
            sheet.write(i + 1, 12, g[12])
            for j in range(10):
                sheet.write(i + 1, j + 13, int(g[j + 13]))
        else:

            if g[13] > g[1]:
                sheet.write(i + 1, 0, 1)
            elif g[13] == g[1]:
                sheet.write(i + 1, 0, 0.5)
            else:
                sheet.write(i + 1, 0, 0)

            sheet.write(i + 1, 1, 0)

            for j in range(10):
                sheet.write(i + 1, j + 2, int(g[j + 13]))
            sheet.write(i + 1, 12, g[0])
            for j in range(10):
                sheet.write(i + 1, j + 13, int(g[j + 1]))

wb.save("MLS.xls")
