"""
http://fi.wikipedia.org/wiki/Luettelo_Suomen_kunnista
"""

import random  # not for cryptographic use!

# maakunnat sijaintimuodossa (inessiivi/adessiivi)
REGIONS = {
    0: "Ahvenanmaalla",
    1: "Etelä-Karjalassa",
    2: "Etelä-Pohjanmaalla",
    3: "Etelä-Savossa",
    4: "Kainuussa",
    5: "Kanta-Hämeessä",
    6: "Keski-Pohjanmaalla",
    7: "Keski-Suomessa",
    8: "Kymenlaaksossa",
    9: "Lapissa",
    10: "Päijät-Hämeessä",
    11: "Pirkanmaalla",
    12: "Pohjanmaalla",
    13: "Pohjois-Karjalassa",
    14: "Pohjois-Pohjanmaalla",
    15: "Pohjois-Savossa",
    16: "Satakunnassa",
    17: "Uudellamaalla",
    18: "Varsinais-Suomessa",
}

# kunnat (maakunnan numero, onko kaupunki, asukasluku)
CITIES = {
    "Akaa": (11, True, 16779),
    "Alajärvi": (2, True, 9817),
    "Alavieska": (14, False, 2610),
    "Alavus": (2, True, 11672),
    "Asikkala": (10, False, 8222),
    "Askola": (17, False, 4978),
    "Aura": (18, False, 3994),
    "Brändö": (0, False, 453),
    "Eckerö": (0, False, 957),
    "Enonkoski": (3, False, 1414),
    "Enontekiö": (9, False, 1906),
    "Espoo": (17, True, 280247),
    "Eura": (16, False, 11880),
    "Eurajoki": (16, False, 9528),
    "Evijärvi": (2, False, 2498),
    "Finström": (0, False, 2579),
    "Forssa": (5, True, 17119),
    "Föglö": (0, False, 530),
    "Geta": (0, False, 500),
    "Haapajärvi": (14, True, 7236),
    "Haapavesi": (14, True, 6944),
    "Hailuoto": (14, False, 962),
    "Halsua": (6, False, 1164),
    "Hamina": (8, True, 20425),
    "Hammarland": (0, False, 1547),
    "Hankasalmi": (7, False, 4999),
    "Hanko": (17, True, 8506),
    "Harjavalta": (16, True, 7125),
    "Hartola": (10, False, 2855),
    "Hattula": (5, False, 9552),
    "Hausjärvi": (5, False, 8467),
    "Heinola": (10, True, 19060),
    "Heinävesi": (3, False, 3424),
    "Helsinki": (17, True, 645482),
    "Hirvensalmi": (3, False, 2225),
    "Hollola": (10, False, 23755),
    "Honkajoki": (16, False, 1703),
    "Huittinen": (16, True, 10173),
    "Humppila": (5, False, 2253),
    "Hyrynsalmi": (4, False, 2312),
    "Hyvinkää": (17, True, 46675),
    "Hämeenkyrö": (11, False, 10551),
    "Hämeenlinna": (5, True, 67681),
    "Ii": (14, False, 9939),
    "Iisalmi": (15, True, 21588),
    "Iitti": (8, False, 6802),
    "Ikaalinen": (11, True, 7069),
    "Ilmajoki": (2, False, 12186),
    "Ilomantsi": (13, False, 5070),
    "Imatra": (1, True, 27203),
    "Inari": (9, False, 6839),
    "Inkoo": (17, False, 5481),
    "Isojoki": (2, False, 2013),
    "Isokyrö": (12, False, 4645),
    "Janakkala": (5, False, 16553),
    "Joensuu": (13, True, 76063),
    "Jokioinen": (5, False, 5279),
    "Jomala": (0, False, 4895),
    "Joroinen": (3, False, 4890),
    "Joutsa": (7, False, 4542),
    "Juuka": (13, False, 4764),
    "Juupajoki": (11, False, 1904),
    "Juva": (3, False, 6304),
    "Jyväskylä": (7, True, 140240),
    "Jämijärvi": (16, False, 1851),
    "Jämsä": (7, True, 20789),
    "Järvenpää": (17, True, 42876),
    "Kaarina": (18, True, 33193),
    "Kaavi": (15, False, 3030),
    "Kajaani": (4, True, 37181),
    "Kalajoki": (14, True, 12487),
    "Kangasala": (11, True, 31476),
    "Kangasniemi": (3, False, 5515),
    "Kankaanpää": (16, True, 11538),
    "Kannonkoski": (7, False, 1401),
    "Kannus": (6, True, 5514),
    "Karijoki": (2, False, 1316),
    "Karkkila": (17, True, 8864),
    "Karstula": (7, False, 4113),
    "Karvia": (16, False, 2394),
    "Kaskinen": (12, True, 1276),
    "Kauhajoki": (2, True, 13566),
    "Kauhava": (2, True, 16248),
    "Kauniainen": (17, True, 9608),
    "Kaustinen": (6, False, 4298),
    "Keitele": (15, False, 2290),
    "Kemi": (9, True, 21218),
    "Kemijärvi": (9, True, 7456),
    "Keminmaa": (9, False, 8246),
    "Kemiönsaari": (18, False, 6758),
    "Kempele": (14, False, 17709),
    "Kerava": (17, True, 35792),
    "Keuruu": (7, True, 9849),
    "Kihniö": (11, False, 1951),
    "Kinnula": (7, False, 1650),
    "Kirkkonummi": (17, False, 39306),
    "Kitee": (13, True, 10444),
    "Kittilä": (9, False, 6394),
    "Kiuruvesi": (15, True, 8246),
    "Kivijärvi": (7, False, 1119),
    "Kokemäki": (16, True, 7336),
    "Kokkola": (6, True, 47641),
    "Kolari": (9, False, 3844),
    "Konnevesi": (7, False, 2734),
    "Kontiolahti": (13, False, 14793),
    "Korsnäs": (12, False, 2139),
    "Koski Tl": (18, False, 2353),
    "Kotka": (8, True, 53263),
    "Kouvola": (8, True, 84001),
    "Kristiinankaupunki": (12, True, 6603),
    "Kruunupyy": (12, False, 6552),
    "Kuhmo": (4, True, 8470),
    "Kuhmoinen": (7, False, 2259),
    "Kumlinge": (0, False, 314),
    "Kuopio": (15, True, 118100),
    "Kuortane": (2, False, 3604),
    "Kurikka": (2, True, 21139),
    "Kustavi": (18, False, 925),
    "Kuusamo": (14, True, 15310),
    "Kyyjärvi": (7, False, 1349),
    "Kärkölä": (10, False, 4496),
    "Kärsämäki": (14, False, 2612),
    "Kökar": (0, False, 237),
    "Lahti": (10, True, 119730),
    "Laihia": (12, False, 8052),
    "Laitila": (18, True, 8620),
    "Lapinjärvi": (17, False, 2710),
    "Lapinlahti": (15, False, 9679),
    "Lappajärvi": (2, False, 3119),
    "Lappeenranta": (1, True, 72725),
    "Lapua": (2, True, 14471),
    "Laukaa": (7, False, 18958),
    "Lemi": (1, False, 3059),
    "Lemland": (0, False, 2028),
    "Lempäälä": (11, False, 22881),
    "Leppävirta": (15, False, 9765),
    "Lestijärvi": (6, False, 771),
    "Lieksa": (13, True, 11264),
    "Lieto": (18, False, 19632),
    "Liminka": (14, False, 10154),
    "Liperi": (13, False, 12162),
    "Lohja": (17, True, 46661),
    "Loimaa": (18, True, 16105),
    "Loppi": (5, False, 7993),
    "Loviisa": (17, True, 15013),
    "Luhanka": (7, False, 723),
    "Lumijoki": (14, False, 2081),
    "Lumparland": (0, False, 390),
    "Luoto": (12, False, 5261),
    "Luumäki": (1, False, 4725),
    "Maalahti": (12, False, 5478),
    "Maarianhamina": (0, True, 11723),
    "Marttila": (18, False, 1993),
    "Masku": (18, False, 9645),
    "Merijärvi": (14, False, 1114),
    "Merikarvia": (16, False, 3133),
    "Miehikkälä": (8, False, 1974),
    "Mikkeli": (3, True, 54047),
    "Muhos": (14, False, 9025),
    "Multia": (7, False, 1620),
    "Muonio": (9, False, 2323),
    "Mustasaari": (12, False, 19389),
    "Muurame": (7, False, 10102),
    "Mynämäki": (18, False, 7793),
    "Myrskylä": (17, False, 1973),
    "Mäntsälä": (17, False, 20739),
    "Mänttä-Vilppula": (11, True, 10144),
    "Mäntyharju": (3, False, 6013),
    "Naantali": (18, True, 19155),
    "Nakkila": (16, False, 5525),
    "Nivala": (14, True, 10805),
    "Nokia": (11, True, 33425),
    "Nousiainen": (18, False, 4790),
    "Nurmes": (13, True, 7735),
    "Nurmijärvi": (17, False, 42305),
    "Närpiö": (12, True, 9503),
    "Orimattila": (10, True, 16147),
    "Oripää": (18, False, 1376),
    "Orivesi": (11, True, 9261),
    "Oulainen": (14, True, 7481),
    "Oulu": (14, True, 202058),
    "Outokumpu": (13, True, 6910),
    "Padasjoki": (10, False, 3013),
    "Paimio": (18, True, 10756),
    "Paltamo": (4, False, 3421),
    "Parainen": (18, True, 15254),
    "Parikkala": (1, False, 4939),
    "Parkano": (11, True, 6558),
    "Pedersören kunta": (12, False, 11088),
    "Pelkosenniemi": (9, False, 955),
    "Pello": (9, False, 3492),
    "Perho": (6, False, 2858),
    "Pertunmaa": (3, False, 1715),
    "Petäjävesi": (7, False, 3907),
    "Pieksämäki": (3, True, 18165),
    "Pielavesi": (15, False, 4588),
    "Pietarsaari": (12, True, 19369),
    "Pihtipudas": (7, False, 4117),
    "Pirkkala": (11, False, 19289),
    "Polvijärvi": (13, False, 4406),
    "Pomarkku": (16, False, 2159),
    "Pori": (16, True, 84585),
    "Pornainen": (17, False, 5118),
    "Porvoo": (17, True, 50219),
    "Posio": (9, False, 3295),
    "Pudasjärvi": (14, True, 8065),
    "Pukkila": (17, False, 1915),
    "Punkalaidun": (11, False, 2941),
    "Puolanka": (4, False, 2648),
    "Puumala": (3, False, 2189),
    "Pyhtää": (8, False, 5262),
    "Pyhäjoki": (14, False, 3156),
    "Pyhäjärvi": (14, True, 5313),
    "Pyhäntä": (14, False, 1594),
    "Pyhäranta": (18, False, 2079),
    "Pälkäne": (11, False, 6559),
    "Pöytyä": (18, False, 8412),
    "Raahe": (14, True, 24961),
    "Raasepori": (17, True, 27863),
    "Raisio": (18, True, 24174),
    "Rantasalmi": (3, False, 3549),
    "Ranua": (9, False, 3953),
    "Rauma": (16, True, 39492),
    "Rautalampi": (15, False, 3229),
    "Rautavaara": (15, False, 1674),
    "Rautjärvi": (1, False, 3390),
    "Reisjärvi": (14, False, 2790),
    "Riihimäki": (5, True, 28981),
    "Ristijärvi": (4, False, 1302),
    "Rovaniemi": (9, True, 62351),
    "Ruokolahti": (1, False, 5180),
    "Ruovesi": (11, False, 4420),
    "Rusko": (18, False, 6275),
    "Rääkkylä": (13, False, 2220),
    "Saarijärvi": (7, True, 9568),
    "Salla": (9, False, 3562),
    "Salo": (18, True, 52792),
    "Saltvik": (0, False, 1854),
    "Sastamala": (11, True, 24751),
    "Sauvo": (18, False, 3003),
    "Savitaipale": (1, False, 3484),
    "Savonlinna": (3, True, 34390),
    "Savukoski": (9, False, 1014),
    "Seinäjoki": (2, True, 62871),
    "Sievi": (14, False, 5025),
    "Siikainen": (16, False, 1463),
    "Siikajoki": (14, False, 5333),
    "Siikalatva": (14, False, 5398),
    "Siilinjärvi": (15, False, 21643),
    "Simo": (9, False, 3086),
    "Sipoo": (17, False, 20364),
    "Siuntio": (17, False, 6150),
    "Sodankylä": (9, False, 8529),
    "Soini": (2, False, 2114),
    "Somero": (18, True, 8881),
    "Sonkajärvi": (15, False, 4044),
    "Sotkamo": (4, False, 10401),
    "Sottunga": (0, False, 93),
    "Sulkava": (3, False, 2570),
    "Sund": (0, False, 1021),
    "Suomussalmi": (4, False, 7996),
    "Suonenjoki": (15, True, 7219),
    "Sysmä": (10, False, 3823),
    "Säkylä": (16, False, 6875),
    "Taipalsaari": (1, False, 4736),
    "Taivalkoski": (14, False, 4038),
    "Taivassalo": (18, False, 1645),
    "Tammela": (5, False, 6114),
    "Tampere": (11, True, 232407),
    "Tervo": (15, False, 1570),
    "Tervola": (9, False, 3065),
    "Teuva": (2, False, 5261),
    "Tohmajärvi": (13, False, 4542),
    "Toholampi": (6, False, 3173),
    "Toivakka": (7, False, 2392),
    "Tornio": (9, True, 21929),
    "Turku": (18, True, 189930),
    "Tuusniemi": (15, False, 2578),
    "Tuusula": (17, False, 38773),
    "Tyrnävä": (14, False, 6749),
    "Ulvila": (16, True, 13156),
    "Urjala": (11, False, 4823),
    "Utajärvi": (14, False, 2743),
    "Utsjoki": (9, False, 1228),
    "Uurainen": (7, False, 3743),
    "Uusikaarlepyy": (12, True, 7504),
    "Uusikaupunki": (18, True, 15757),
    "Vaala": (14, False, 2940),
    "Vaasa": (12, True, 67248),
    "Valkeakoski": (11, True, 21158),
    "Valtimo": (13, False, 2191),
    "Vantaa": (17, True, 224397),
    "Varkaus": (15, True, 21075),
    "Vehmaa": (18, False, 2313),
    "Vesanto": (15, False, 2093),
    "Vesilahti": (11, False, 4454),
    "Veteli": (6, False, 3222),
    "Vieremä": (15, False, 3704),
    "Vihti": (17, False, 29245),
    "Viitasaari": (7, True, 6368),
    "Vimpeli": (2, False, 2942),
    "Virolahti": (8, False, 3180),
    "Virrat": (11, True, 6781),
    "Vårdö": (0, False, 430),
    "Vöyri": (12, False, 6621),
    "Ylitornio": (9, False, 4072),
    "Ylivieska": (14, True, 15276),
    "Ylöjärvi": (11, True, 32999),
    "Ypäjä": (5, False, 2367),
    "Ähtäri": (2, True, 5858),
    "Äänekoski": (7, True, 19092),
}

# montako vastausvaihtoehtoa; 2-8, koska maakunnissa on vähimmillään 7 kuntaa
# (Kymenlaakso)
ANSWER_COUNT = 4

QUESTION_FUNCTIONS = [
    "which_city_in_region",
    "which_city_not_in_region",
    "where_city",
]

NUMBER_OF_ROUNDS = 10

def which_city_in_region():
    """Question: "Which city is in region X?"
    return: (question format, question region, right answer, wrong answers)"""
    rightCity = random.choice(list(CITIES))
    region = CITIES[rightCity][0]
    citiesElsewhere = set(city for city in CITIES if CITIES[city][0] != region)
    return (
        "Mikä kunta on {:s}?",
        REGIONS[region],
        rightCity,
        set(random.sample(citiesElsewhere, ANSWER_COUNT - 1)),
    )

def which_city_not_in_region():
    """Question: "Which city is not in region X?"
    return: (question format, question region, right answer, wrong answers)"""
    city = random.choice(list(CITIES))
    region = CITIES[city][0]
    citiesInRegion = set(city for city in CITIES if CITIES[city][0] == region)
    citiesElsewhere = set(CITIES) - citiesInRegion
    return (
        "Mikä kunta EI ole {:s}?",
        REGIONS[region],
        random.choice(list(citiesElsewhere)),
        set(random.sample(citiesInRegion, ANSWER_COUNT - 1)),
    )

def where_city():
    """Question: "Where is city X?"
    return: (question format, question city, right answer, wrong answers)"""
    rightCity = random.choice(list(CITIES))
    rightRegion = CITIES[rightCity][0]
    wrongRegions = set(region for region in REGIONS if region != rightRegion)
    wrongAnswers = set(
        REGIONS[region] for region
        in random.sample(wrongRegions, ANSWER_COUNT - 1)
    )
    return (
        "Missä {:s} on?",
        rightCity,
        REGIONS[rightRegion],
        wrongAnswers,
    )

def ask_inner(question, answers):
    """Print question and answers, wait for valid input.
    return: answer as string"""
    answers = random.sample(answers, len(answers))
    while True:
        print(question)
        for (i, answer) in enumerate(answers):
            print("  {:d}) {:s}".format(i + 1, answer))
        inp = input("? ")
        try:
            inp = int(inp, 10)
            if 1 <= inp <= ANSWER_COUNT:
                return answers[inp - 1]
        except ValueError:
            pass

def explain_right_answer(function, questionPlace, answer):
    if function == "where_city":
        return "Oikein, {:s} on {:s}.".format(questionPlace, answer)
    if function == "which_city_in_region":
        return "Oikein, {:s} on {:s}.".format(answer, questionPlace)
    if function == "which_city_not_in_region":
        return "Oikein, {:s} ei ole {:s} vaan {:s}.".format(
            answer, questionPlace, REGIONS[CITIES[answer][0]]
        )
    exit("Error: question type not found.")

def explain_wrong_answer(function, questionPlace, answer, rightAnswer):
    if function == "where_city":
        return "Väärin, {:s} on {:s} eikä {:s}.".format(
            questionPlace, REGIONS[CITIES[questionPlace][0]], answer
        )
    if function == "which_city_in_region":
        return "Väärin, {:s} on {:s}.".format(
            answer, REGIONS[CITIES[answer][0]]
        )
    if function == "which_city_not_in_region":
        return "Väärin, {:s} on {:s}. ({:s} on sen sijaan {:s}.)".format(
            answer, questionPlace, rightAnswer, REGIONS[CITIES[rightAnswer][0]]
        )
    exit("Error: question type not found.")

def ask_outer():
    """Create question, ask, give feedback.
    return: points (1 = correct, 0 = incorrect)"""
    function = random.choice(QUESTION_FUNCTIONS)
    (questionFormat, questionPlace, rightAnswer, wrongAnswers) = \
    globals()[function]()

    question = questionFormat.format(questionPlace)
    allAnswers = set((rightAnswer,)) | wrongAnswers
    answer = ask_inner(question, allAnswers)

    if answer == rightAnswer:
        print(explain_right_answer(function, questionPlace, answer))
        return 1
    print(explain_wrong_answer(function, questionPlace, answer, rightAnswer))
    return 0

def main():
    points = 0
    for round in range(NUMBER_OF_ROUNDS):
        print("Kysymys {:d}/{:d}:".format(round + 1, NUMBER_OF_ROUNDS))
        points += ask_outer()
        print()
    print("Pisteesi: {:d}/{:d}".format(points, NUMBER_OF_ROUNDS))

if __name__ == "__main__":
    main()
