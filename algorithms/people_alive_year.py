class Person():
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death



def get_year_most_people_alive(people):
    """
    Given a list of people and their years of birth and death, find out the year that had the most people alive
    """
    year_count = {}

    for person in people:
        if person.birth not in year_count:
            year_count[person.birth] = 1
        else:
            year_count[person.birth] += 1

        if person.death + 1 not in year_count:
            year_count[person.death + 1] = -1
        else:
            year_count[person.death + 1] -= 1

    peak_year = 0
    peak_people = 0

    ordered_years = year_count.keys()
    ordered_years.sort()

    current_people = 0
    for year in ordered_years:
        current_people += year_count[year]

        if current_people > peak_people:
            peak_people = current_people
            peak_year = year

    return peak_year, peak_people