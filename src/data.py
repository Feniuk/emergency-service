graph = {
    "Hbf": {"Brandenburger Tor": 4, "Babelsberg": 7},
    "Brandenburger Tor": {"Hbf": 4, "Sanssouci": 1, "Klinikum Ernst von Bergmann": 5},
    "Sanssouci": {"Brandenburger Tor": 1, "University": 5},
    "University": {"Sanssouci": 5, "Klinikum Ernst von Bergmann": 6, "Park": 2},
    "Park": {"University": 2, "Alexianer St. Josefs Krankenhaus": 5},
    "Babelsberg": {"Hbf": 7, "FilmPark": 2},
    "FilmPark": {"Babelsberg": 2, "Alexianer St. Josefs Krankenhaus": 4},
    "Klinikum Ernst von Bergmann": {"Brandenburger Tor": 5, "University": 6},
    "Alexianer St. Josefs Krankenhaus": {"Park": 5, "FilmPark": 4}
}

hospitals = ["Klinikum Ernst von Bergmann", "Alexianer St. Josefs Krankenhaus"]