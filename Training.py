def human_years_cat_years_dog_years(human_years):
    
    catYears = 0
    dogYears = 0

    for year in range (1, human_years):
        if year == 1:
            dogYears += 15
            catYears += 15
        elif year == 2:
            dogYears += 9
            catYears += 9
        else:
            dogYears += 5
            catYears += 4

    return [human_years, catYears, dogYears]