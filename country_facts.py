from countryinfo import CountryInfo


def country_info(iso_code):
    country = CountryInfo(iso_code)
    
    capital = country.capital()
    languages = country.languages()
    borders = country.borders()
    provinces = country.provinces()
    area = country.area()
    calling_codes = country.calling_codes()
    pop = country.population()

    return [capital, languages, borders, provinces, area, calling_codes, pop]