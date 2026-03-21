graph = {
    "Hbf": {"BrandenburgGate": 4, "Babelsberg": 7},
    "BrandenburgGate": {"Hbf": 3, "Sanssouci": 1, "Klinikum Ernst von Bergmann": 5},
    "Sanssouci": {"BrandenburgGate": 1, "University": 5},
    "University": {"Sanssouci": 5, "Klinikum Ernst von Bergmann": 6, "Park": 2},
    "Park": {"University": 2, "St. Josefs Krankenhaus": 5},
    "Babelsberg": {"Hbf": 7, "FilmPark": 2},
    "FilmPark": {"Babelsberg": 2, "St. Josefs Krankenhaus": 4},
    "Klinikum Ernst von Bergmann": {"BrandenburgGate": 5, "University": 6},
    "St. Josefs Krankenhaus": {"Park": 5, "FilmPark": 4}
}

hospitals = ["Klinikum Ernst von Bergmann", "St. Josefs Krankenhaus"]