planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet.get('name'))
planet = {
    'name': 'Mars',
    'moons': 2
}
print(planet.get('name'))
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')