with open('input.txt', 'r') as f:
    lines = f.readlines()
input = {}

for line in lines:
    game, data = line.split(':')
    #print(game)
    int_game = int(game[5:]) 
    input[int_game] = data
    


games = {}
for key, value in input.items():
    drawn_cubes = value.split(';')
    #print("Game number = ", key)
    draws = {}
    for item in drawn_cubes:
        for x in item.split(','):
            x = x.strip()
            count, color = x.split(' ')
            #print(item)
            #print(count, color)
            if not color in draws:
                draws[color] = int(count)
            else:
                if draws[color] < int(count):
                    draws[color] = int(count)
            #print('')
    games[key] = draws
colors = {'red': 12, 'green': 13, 'blue': 14}
results = {}

for key, value in games.items():
    #print("game number = ", key)
    #print(value)
    success = True
    for color in colors:
        if color in value:
            if value[color] <= colors[color]:
                pass
            else:
                success = False
            # if value[color] > colors[color]:
            #     results[key] = f"{colors[color]} was the maximum available {color}, but {value[color]} {color} blocks were drawn from the bag."
    results[key] = success    
    
final = 0
for idx in results.keys():
    if results[idx]:
        final += idx
    
print(final)
    
