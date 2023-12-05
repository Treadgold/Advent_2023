import os
with open('input.txt', 'r') as f:
    lines = f.readlines()

cards = []    

for line in lines:
    sections = line.split(':')
    card_number = sections[0].split()[1]
    card_winning = sections[1].split('|')[0].split()
    card_drawn = sections[1].split('|')[1].split()
    cards.append((card_number, card_winning, card_drawn))
total = 0
for card in cards:
    matches = 0
    for number in card[2]:
        if number in card[1]:
            if matches == 0:
                matches = 1
            else:
                matches *= 2
    total += matches
    
print(total)
    