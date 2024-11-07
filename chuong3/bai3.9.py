import numpy as np

data = np.genfromtxt('euro2012.csv', delimiter=',', dtype=None, encoding=None, skip_header=1)

print("Type của euro12:", type(data))
print("Shape của euro12:", data.shape)
print("Danh sách các cột:", data.dtype.names)

goals_column = data['Goals']
print("\nGiá trị cột Goals:")
print(goals_column)

teams_count = len(np.unique(data['Team']))
print(f"\nCó {teams_count} đội tham gia Euro2012.")

print("\nThông tin của Euro2012:")
print(data)

discipline = data[['Team', 'Yellow Cards', 'Red Cards']]
print("\nData frame discipline:")
print(discipline)

average_yellow_cards = np.mean(discipline['Yellow Cards'])
print(f"\nTrung bình Yellow Cards: {average_yellow_cards:.2f}")

discipline_sorted = discipline[np.lexsort((-discipline['Red Cards'], -discipline['Yellow Cards']))]
print("\nDiscipline sau khi sắp xếp:")
print(discipline_sorted)

teams_more_than_6_goals = data[data['Goals'] > 6]
print("\nCác đội đã ghi hơn 6 bàn thắng:")
print(teams_more_than_6_goals[['Team', 'Goals']])

teams_starting_with_G = data[np.char.startswith(data['Team'], 'G')]
print("\nCác đội có tên bắt đầu bằng 'G':")
print(teams_starting_with_G[['Team']])

print("\n7 cột đầu của euro12:")
print(data[:, :7])

print("\nTất cả các cột, trừ 3 cột cuối:")
print(data[:, :-3])

print("\nCác cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:")
print(data[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

selected_teams = data[np.isin(data['Team'], ['England', 'Italy', 'Russia'])]
print("\nCác cột 'Team','Shooting Accuracy' từ 'England', 'Italy', 'Russia':")
print(selected_teams[['Team', 'Shooting Accuracy']])
