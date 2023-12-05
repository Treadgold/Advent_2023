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
    draws = []
    for item in drawn_cubes:
        sample = {}
        for x in item.split(','):
            x = x.strip()
            count, color = x.split(' ')
            sample[color] = int(count)
        draws.append(sample)
    games[key] = draws
games

maxes = {}
for key, value in games.items():
    #print(key, value)
    mr, mg, mb = 0, 0, 0
    for draw in value:        
        for color in draw:
            match color:
                case 'red':
                    mr = max(mr, draw[color])
                case 'green':
                    mg = max(mg, draw[color])
                case 'blue':
                    mb = max(mb, draw[color])
    maxes[key] = (mr, mg, mb)
    
                
                    
                
sums = 0
for key, value in maxes.items():
    x, y, z = value[0], value[1], value[2]
    cb = x*y*z
    sums += cb
    
print(sums)