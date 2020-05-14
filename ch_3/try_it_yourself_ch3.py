#3-1
names = ['joanna', 'eliana', 'carol', 'mark', 'carissa', 'davin', 'ricardo']
print(names[0].title())
print(names[-1].title())
print(names[1].title())
print(names[2].title())
print(names[-2].title())
print(names[-3].title())
print(names[3].title())

#3-2
number = 7
message = "I have " + str(number) + " members in my family including " + names[0].title() + "."
message2 = "I have " + str(number) + " members in my family including " + names[-1].title() + "."
print(message)
print(message2)

#3-3
fav_games = ['rocket league', 'fallout', 'minecraft', 'runescape', 'super smash bros']
message3 = "I really enjoy playing games. The games on computer I like to play include\n" + fav_games[0].title() + ", " + fav_games[1].title() + ", " + fav_games[2].title() + " and, " + fav_games[3].title() + ". \nI like to play " + fav_games[-1].title() + ", but can't play that on the computer."
print(message3)

#3-4
musicians = ['rhcp', 'jack johnson', 'john mayer', 'manchester orchestra']
print(musicians)
pop_rhcp = musicians.pop(0)
message_rhcp = "\nDear " + pop_rhcp.upper() + ",\nI would like to invite you to dinner.\nSincerly,\nCody"
print(message_rhcp)
pop_jj = musicians.pop(0)
message_jj = "\nDear " + pop_jj.title() + ",\nI would like to invite you to dinner.\nSincerly,\nCody"
print(message_jj)
print(musicians)
musicians.insert(0, 'jack johnson')
musicians.insert(0, 'rhcp')
print(musicians)

#3-5
rsvp_no = 'john mayer'
print(rsvp_no)
musicians.remove(rsvp_no)
print(musicians)

#3-6
musicians.insert(0, 'billie eilish')
musicians.insert(0, 'john lennon')
musicians. insert(0, 'bwtmc')
print(musicians)
pop_be = musicians.pop(2)
message_more_space = "To the following: " + pop_be.title() + "\nI have found a larger table and am able to invite more guests. Please join me for an evening of dinner and dancing."
print(message_more_space)

#3-7
message_2 = ": I am sorry to inform you that only 2 individuals will be able to attend the party and you are not one of those 2. I am sorry for the inconvenience."
print(musicians)
pop_manchester = musicians.pop(-1)
print(pop_manchester.title() + message_2)
pop_jj = musicians.pop(-1)
print(pop_jj.title() + message_2)
pop_jl = musicians.pop(0)
print(pop_jl.title() + message_2)
print(musicians)
musicians.remove('rhcp')
musicians.remove('john lennon')
print(musicians)

#3-8
seeworld = ['thailand', 'austria', 'japan', 'china', 'australia']
print(seeworld)
print("\nHere is locations sorted:")
print(sorted(seeworld))
print(seeworld)

print("\nHere is locations sorted reverse to the original list (permanent):")
seeworld.reverse()
print(seeworld)

print("\nBut don't worry, it is easy to undo by reverse sort again:")
seeworld.reverse()
print(seeworld)

print("\nHere is locations alphabetically reverse sorted (temporary):")
seeworld.sort(reverse=True)
print(seeworld)

print("\nHere is locationsorted alphabetically:")
seeworld.sort()
print(seeworld)

#3-9
musicians = ['rhcp', 'jack johnson', 'john mayer', 'manchester orchestra']
print(musicians)
print("\nThis is the number of musicians/bands in the list: " + str(len(musicians))) 
#len make an integer, so to display it as a string in the print, it needs to be placed as one using str()

#3-11
print('\nHeh, I make no errrs.')
