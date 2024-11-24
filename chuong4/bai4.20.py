import pandas as pd

euro12 = pd.read_csv('chuong4\euro2012.csv')

print(euro12['Goals'])

print("Số đội:", euro12['Team'].nunique())

print(euro12.info())

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(discipline_sorted)

print("Average Yellow Cards:", discipline['Yellow Cards'].mean())

teams_more_than_6_goals = euro12[euro12['Goals'] > 6]['Team']
print("\nTeams with more than 6 goals:")
print(teams_more_than_6_goals)

teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]['Team']
print("\nTeams starting with 'G':")
print(teams_start_with_G)

print("\nTeam, Yellow Cards, Red Cards:")
print(euro12[['Team', 'Yellow Cards', 'Red Cards']])

avg_yellow_cards_by_team = euro12.groupby('Team')['Yellow Cards'].mean()
print("\nAverage Yellow Cards by Team:")
print(avg_yellow_cards_by_team)

teams_to_check = ['England', 'Italy', 'Russia']
shooting_accuracy = euro12[euro12['Team'].isin(teams_to_check)][['Team', 'Shooting Accuracy']]
print("\nShooting Accuracy of England, Italy, and Russia:")
print(shooting_accuracy)
