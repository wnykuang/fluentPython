laxCoor = (33,-118)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travlerId = [('USA', '31195855'), ('BRA', 'CE342567')
,('ESP', 'XDA205856')]

for passport in sorted(travlerId):
    print("%s/%s" %passport)
    #However, the 
    #print("{}/{}".format(passport))
    #will not parse the passport var into two parts.