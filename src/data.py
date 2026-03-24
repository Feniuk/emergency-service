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

coordinates = {
    "Hbf": (52.391, 13.066),
    "Brandenburger Tor": (52.396, 13.055),
    "Sanssouci": (52.404, 13.038),
    "University": (52.401, 13.015),
    "Park": (52.395, 13.010),
    "Babelsberg": (52.390, 13.090),
    "FilmPark": (52.391, 13.095),
    "Klinikum Ernst von Bergmann": (52.400, 13.060),
    "Alexianer St. Josefs Krankenhaus": (52.384, 13.045)
}