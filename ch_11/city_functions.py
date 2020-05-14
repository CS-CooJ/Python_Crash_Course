#11-2
def city_proper(city_name, state_name, population=''):
	"""Return proper city/state name structure."""
	
	if population:
		return(city_name.title() + ', ' + state_name.title() + ' - population: '
			+ str(population))
	else:
		return(city_name.title() + ', ' + state_name.title())
