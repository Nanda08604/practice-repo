
Players = [
  {'name': 'Felix Anudike-Uzomah', 'position': 'DE', 'jerseynumber': '97', 'yards': 150, 'touchdowns': 4},
  {'name': 'Matt Araiza', 'position': 'P', 'jerseynumber': '14', 'yards': 400, 'touchdowns': 8}
]
#for i, player in enumerate(Players, start=1):
#  print(f"Player {i}")
#  print(f"Name: ", player['name'])
#  print(f"Position: ", player['position'])
#  print(f"Jersey number: ", player['jerseynumber'])
#  print(f"Yards gained: ", player['yards'])
#  print(f"Touchdowns: ", player['touchdowns'])
#  print("  ")

names = [player["name"] for player in Players]
positions = [player['position'] for player in Players]
average_yards = [sum(i['yards'] for i in Players)/ len(Players)]
average_touchdowns = [sum(i['touchdowns'] for i in Players)/len(Players)]

print(f"Players name: {names}")
print(f"positions: {positions}")
print(f"Average Yards Gained: {average_yards}")
print(f"Average Touchdowns: {average_touchdowns}")




