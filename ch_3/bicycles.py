
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)#will print with brackets present
print(bicycles[0])#will print the first item in the list.
print(bicycles[0].title()) #title will make it a Trek
print(bicycles[-1].title()) # - position will start from the end (starting count at 1, not 0)
message = "I would like to say that I really enjoy my first bicycle that i had.\nIt was a " + bicycles[-1].title() + " with red paint and tassles on the handlebars."
print(message)
