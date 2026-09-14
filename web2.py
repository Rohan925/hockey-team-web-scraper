import requests
from bs4 import BeautifulSoup
import csv

base_url = "your url"

with open("hockey_teams.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Team Name",
        "Year",
        "Wins",
        "Losses",
        "OT Losses",
        "Win %",
        "Goals For",
        "Goals Against",
        "+/-"
    ])

    for page in range(1, 25):

        response = requests.get(
            base_url,
            params={"page_num": page}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        teams = soup.find_all("tr", class_="team")

        for team in teams:

            team_name = team.find("td", class_="name").text.strip()
            year = team.find("td", class_="year").text.strip()
            wins = team.find("td", class_="wins").text.strip()
            losses = team.find("td", class_="losses").text.strip()
            ot_losses = team.find("td", class_="ot-losses").text.strip()
            win_pct = team.find("td", class_="pct").text.strip()
            goals_for = team.find("td", class_="gf").text.strip()
            goals_against = team.find("td", class_="ga").text.strip()
            difference = team.find("td", class_="diff").text.strip()

            writer.writerow([
                team_name,
                year,
                wins,
                losses,
                ot_losses,
                win_pct,
                goals_for,
                goals_against,
                difference
            ])

print("Scraping completed!")