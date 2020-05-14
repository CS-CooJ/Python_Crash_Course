states = ['connecticut', 'maine', 'new york', 'alabama', 'alaska', 'missouri', 'kansas', 'texas', 'arkansas', 'new mexico', 'arizona', 'florida', 'california', 'washington', 'oregon', 'south dakota', 'north dakota', 'viginia', 'west virginia', 'georgia']
print("This is the original list: \n")
print(states)

print("\nThis is the list sorted in reverse alphabetical order: \n")
states.sort(reverse=True)
print(states)
print("\nNow this is the list sorted alphabetically:\n")
states.sort()
print(states)

print("\nHere is the original list again to work from: \n")
states = ['connecticut', 'maine', 'new york', 'alabama', 'alaska', 'missouri', 'kansas', 'texas', 'arkansas', 'new mexico', 'arizona', 'florida', 'california', 'washington', 'oregon', 'south dakota', 'north dakota', 'viginia', 'west virginia', 'georgia']
print(states)

print("\nThe list sorted alphabetically temporarily:\n")
print(sorted(states))
print("\nAnd back to the original:\n")
print(states)

print('\nWe are going to remove the first and then the last states:\n')
last_state = states.pop()
first_state = states.pop(0)
print(states)
print(last_state)
print(first_state)

print('\nNow we will reinsert the first state and then the last state:\n')
states.insert(0, 'connecticut')
states.insert(-1, 'georgia')
print(states)

print('\nThis will add a state to the list (append puts it last):\n')
states.append('oklahoma')
print(states)

print('\nThis is the # of states currently in the list: ' + str(len(states)))

print('\nLet us see if we can remove some:\n')
states.remove('california')
states.remove("new york")
states.pop()
print('We now have ' + str(len(states)) + ' states.\n')
print(states)

states_string = str(states)
states_string1 = states_string.title()
print('\nThey look a little ugly, lets try to clean them up:\n' + states_string1)
#this may not be the correct way to do it, but I did it myself and was pretty proud at the time.


