heading = "temperature and facts about the moon"
print (heading.title())
mars_temperature = "The highest temperature on Mars is about 30 C"
print(mars_temperature.split())
for items in mars_temperature.split():
    if items.isnumeric():
        print(items)
