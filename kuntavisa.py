"""A quiz of Finnish cities and regions.

TODO: update city info.
TODO: hard/easy mode: correct and incorrect region are always/never neighbors.
"""

import random  # not for cryptographic use!
import sys

NUMBER_OF_ROUNDS = 10

# regions ("maakunnat") in "locative" (inessive/adessive)
REGION_NAMES = {
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

# cities (value: region number)
CITIES = {
    "Akaa": 11,
    "Alajärvi": 2,
    "Alavieska": 14,
    "Alavus": 2,
    "Asikkala": 10,
    "Askola": 17,
    "Aura": 18,
    "Brändö": 0,
    "Eckerö": 0,
    "Enonkoski": 3,
    "Enontekiö": 9,
    "Espoo": 17,
    "Eura": 16,
    "Eurajoki": 16,
    "Evijärvi": 2,
    "Finström": 0,
    "Forssa": 5,
    "Föglö": 0,
    "Geta": 0,
    "Haapajärvi": 14,
    "Haapavesi": 14,
    "Hailuoto": 14,
    "Halsua": 6,
    "Hamina": 8,
    "Hammarland": 0,
    "Hankasalmi": 7,
    "Hanko": 17,
    "Harjavalta": 16,
    "Hartola": 10,
    "Hattula": 5,
    "Hausjärvi": 5,
    "Heinola": 10,
    "Heinävesi": 3,
    "Helsinki": 17,
    "Hirvensalmi": 3,
    "Hollola": 10,
    "Honkajoki": 16,
    "Huittinen": 16,
    "Humppila": 5,
    "Hyrynsalmi": 4,
    "Hyvinkää": 17,
    "Hämeenkyrö": 11,
    "Hämeenlinna": 5,
    "Ii": 14,
    "Iisalmi": 15,
    "Iitti": 8,
    "Ikaalinen": 11,
    "Ilmajoki": 2,
    "Ilomantsi": 13,
    "Imatra": 1,
    "Inari": 9,
    "Inkoo": 17,
    "Isojoki": 2,
    "Isokyrö": 12,
    "Janakkala": 5,
    "Joensuu": 13,
    "Jokioinen": 5,
    "Jomala": 0,
    "Joroinen": 3,
    "Joutsa": 7,
    "Juuka": 13,
    "Juupajoki": 11,
    "Juva": 3,
    "Jyväskylä": 7,
    "Jämijärvi": 16,
    "Jämsä": 7,
    "Järvenpää": 17,
    "Kaarina": 18,
    "Kaavi": 15,
    "Kajaani": 4,
    "Kalajoki": 14,
    "Kangasala": 11,
    "Kangasniemi": 3,
    "Kankaanpää": 16,
    "Kannonkoski": 7,
    "Kannus": 6,
    "Karijoki": 2,
    "Karkkila": 17,
    "Karstula": 7,
    "Karvia": 16,
    "Kaskinen": 12,
    "Kauhajoki": 2,
    "Kauhava": 2,
    "Kauniainen": 17,
    "Kaustinen": 6,
    "Keitele": 15,
    "Kemi": 9,
    "Kemijärvi": 9,
    "Keminmaa": 9,
    "Kemiönsaari": 18,
    "Kempele": 14,
    "Kerava": 17,
    "Keuruu": 7,
    "Kihniö": 11,
    "Kinnula": 7,
    "Kirkkonummi": 17,
    "Kitee": 13,
    "Kittilä": 9,
    "Kiuruvesi": 15,
    "Kivijärvi": 7,
    "Kokemäki": 16,
    "Kokkola": 6,
    "Kolari": 9,
    "Konnevesi": 7,
    "Kontiolahti": 13,
    "Korsnäs": 12,
    "Koski Tl": 18,
    "Kotka": 8,
    "Kouvola": 8,
    "Kristiinankaupunki": 12,
    "Kruunupyy": 12,
    "Kuhmo": 4,
    "Kuhmoinen": 7,
    "Kumlinge": 0,
    "Kuopio": 15,
    "Kuortane": 2,
    "Kurikka": 2,
    "Kustavi": 18,
    "Kuusamo": 14,
    "Kyyjärvi": 7,
    "Kärkölä": 10,
    "Kärsämäki": 14,
    "Kökar": 0,
    "Lahti": 10,
    "Laihia": 12,
    "Laitila": 18,
    "Lapinjärvi": 17,
    "Lapinlahti": 15,
    "Lappajärvi": 2,
    "Lappeenranta": 1,
    "Lapua": 2,
    "Laukaa": 7,
    "Lemi": 1,
    "Lemland": 0,
    "Lempäälä": 11,
    "Leppävirta": 15,
    "Lestijärvi": 6,
    "Lieksa": 13,
    "Lieto": 18,
    "Liminka": 14,
    "Liperi": 13,
    "Lohja": 17,
    "Loimaa": 18,
    "Loppi": 5,
    "Loviisa": 17,
    "Luhanka": 7,
    "Lumijoki": 14,
    "Lumparland": 0,
    "Luoto": 12,
    "Luumäki": 1,
    "Maalahti": 12,
    "Maarianhamina": 0,
    "Marttila": 18,
    "Masku": 18,
    "Merijärvi": 14,
    "Merikarvia": 16,
    "Miehikkälä": 8,
    "Mikkeli": 3,
    "Muhos": 14,
    "Multia": 7,
    "Muonio": 9,
    "Mustasaari": 12,
    "Muurame": 7,
    "Mynämäki": 18,
    "Myrskylä": 17,
    "Mäntsälä": 17,
    "Mänttä-Vilppula": 11,
    "Mäntyharju": 3,
    "Naantali": 18,
    "Nakkila": 16,
    "Nivala": 14,
    "Nokia": 11,
    "Nousiainen": 18,
    "Nurmes": 13,
    "Nurmijärvi": 17,
    "Närpiö": 12,
    "Orimattila": 10,
    "Oripää": 18,
    "Orivesi": 11,
    "Oulainen": 14,
    "Oulu": 14,
    "Outokumpu": 13,
    "Padasjoki": 10,
    "Paimio": 18,
    "Paltamo": 4,
    "Parainen": 18,
    "Parikkala": 1,
    "Parkano": 11,
    "Pedersören kunta": 12,
    "Pelkosenniemi": 9,
    "Pello": 9,
    "Perho": 6,
    "Pertunmaa": 3,
    "Petäjävesi": 7,
    "Pieksämäki": 3,
    "Pielavesi": 15,
    "Pietarsaari": 12,
    "Pihtipudas": 7,
    "Pirkkala": 11,
    "Polvijärvi": 13,
    "Pomarkku": 16,
    "Pori": 16,
    "Pornainen": 17,
    "Porvoo": 17,
    "Posio": 9,
    "Pudasjärvi": 14,
    "Pukkila": 17,
    "Punkalaidun": 11,
    "Puolanka": 4,
    "Puumala": 3,
    "Pyhtää": 8,
    "Pyhäjoki": 14,
    "Pyhäjärvi": 14,
    "Pyhäntä": 14,
    "Pyhäranta": 18,
    "Pälkäne": 11,
    "Pöytyä": 18,
    "Raahe": 14,
    "Raasepori": 17,
    "Raisio": 18,
    "Rantasalmi": 3,
    "Ranua": 9,
    "Rauma": 16,
    "Rautalampi": 15,
    "Rautavaara": 15,
    "Rautjärvi": 1,
    "Reisjärvi": 14,
    "Riihimäki": 5,
    "Ristijärvi": 4,
    "Rovaniemi": 9,
    "Ruokolahti": 1,
    "Ruovesi": 11,
    "Rusko": 18,
    "Rääkkylä": 13,
    "Saarijärvi": 7,
    "Salla": 9,
    "Salo": 18,
    "Saltvik": 0,
    "Sastamala": 11,
    "Sauvo": 18,
    "Savitaipale": 1,
    "Savonlinna": 3,
    "Savukoski": 9,
    "Seinäjoki": 2,
    "Sievi": 14,
    "Siikainen": 16,
    "Siikajoki": 14,
    "Siikalatva": 14,
    "Siilinjärvi": 15,
    "Simo": 9,
    "Sipoo": 17,
    "Siuntio": 17,
    "Sodankylä": 9,
    "Soini": 2,
    "Somero": 18,
    "Sonkajärvi": 15,
    "Sotkamo": 4,
    "Sottunga": 0,
    "Sulkava": 3,
    "Sund": 0,
    "Suomussalmi": 4,
    "Suonenjoki": 15,
    "Sysmä": 10,
    "Säkylä": 16,
    "Taipalsaari": 1,
    "Taivalkoski": 14,
    "Taivassalo": 18,
    "Tammela": 5,
    "Tampere": 11,
    "Tervo": 15,
    "Tervola": 9,
    "Teuva": 2,
    "Tohmajärvi": 13,
    "Toholampi": 6,
    "Toivakka": 7,
    "Tornio": 9,
    "Turku": 18,
    "Tuusniemi": 15,
    "Tuusula": 17,
    "Tyrnävä": 14,
    "Ulvila": 16,
    "Urjala": 11,
    "Utajärvi": 14,
    "Utsjoki": 9,
    "Uurainen": 7,
    "Uusikaarlepyy": 12,
    "Uusikaupunki": 18,
    "Vaala": 14,
    "Vaasa": 12,
    "Valkeakoski": 11,
    "Valtimo": 13,
    "Vantaa": 17,
    "Varkaus": 15,
    "Vehmaa": 18,
    "Vesanto": 15,
    "Vesilahti": 11,
    "Veteli": 6,
    "Vieremä": 15,
    "Vihti": 17,
    "Viitasaari": 7,
    "Vimpeli": 2,
    "Virolahti": 8,
    "Virrat": 11,
    "Vårdö": 0,
    "Vöyri": 12,
    "Ylitornio": 9,
    "Ylivieska": 14,
    "Ylöjärvi": 11,
    "Ypäjä": 5,
    "Ähtäri": 2,
    "Äänekoski": 7,
}

# how many choices; 2-8 because a region may have as few as 7 cities (Kymenlaakso)
ANSWER_COUNT = 4

def which_city_in_region():
    """Question: "Which city is in region X?"
    return: (question, region, correct city, wrong cities)"""

    correctCity = random.choice(list(CITIES))
    region = CITIES[correctCity]
    wrongCitiesAll = set(city for city in CITIES if CITIES[city] != region)
    wrongCities = set(random.sample(wrongCitiesAll, ANSWER_COUNT - 1))
    return ("Mikä kunta on {:s}?", REGION_NAMES[region], correctCity, wrongCities)

def which_city_not_in_region():
    """Question: "Which city is NOT in region X?"
    return: (question, region, correct city, wrong cities)"""

    region = CITIES[random.choice(list(CITIES))]
    wrongCitiesAll = set(city for city in CITIES if CITIES[city] == region)
    correctCity = random.choice(list(set(CITIES) - wrongCitiesAll))
    wrongCities = set(random.sample(wrongCitiesAll, ANSWER_COUNT - 1))
    return ("Mikä kunta EI ole {:s}?", REGION_NAMES[region], correctCity, wrongCities)

def which_city_in_same_region():
    """Question: "Which city is in the same region as city X?"
    return: (question, city, correct city, wrong cities)"""

    questionCity = random.choice(list(CITIES))
    correctCitiesAll = set(city for city in CITIES if CITIES[city] == CITIES[questionCity])
    return (
        "Mikä kunta on samassa maakunnassa kuin {:s}?",
        questionCity,
        random.choice(list(correctCitiesAll - set((questionCity,)))),
        set(random.sample(set(CITIES) - correctCitiesAll, ANSWER_COUNT - 1))
    )

def which_city_not_in_same_region():
    """Question: "Which city is NOT in the same region as city X?"
    return: (question, city, correct city, wrong cities)"""

    questionCity = random.choice(list(CITIES))
    wrongCitiesAll = set(city for city in CITIES if CITIES[city] == CITIES[questionCity])
    return (
        "Mikä kunta EI ole samassa maakunnassa kuin {:s}?",
        questionCity,
        random.choice(list(set(CITIES) - wrongCitiesAll)),
        set(random.sample(wrongCitiesAll - set((questionCity,)), ANSWER_COUNT - 1))
    )

def where_city():
    """Question: "Where is city X?"
    return: (question, city, correct region, wrong regions)"""

    city = random.choice(list(CITIES))
    correctRegion = CITIES[city]
    wrongRegions = random.sample(set(REGION_NAMES) - set((correctRegion,)), ANSWER_COUNT - 1)
    wrongRegionNames = set(REGION_NAMES[region] for region in wrongRegions)
    return ("Missä {:s} on?", city, REGION_NAMES[correctRegion], wrongRegionNames)

def ask_inner(question, answers):
    """Print question and answers, wait for valid input.
    question: str
    answers: set of strings
    return: answer as string"""

    answers = list(answers)
    random.shuffle(answers)
    print(question)
    for (i, answer) in enumerate(answers):
        print("  {:d}) {:s}".format(i + 1, answer))

    while True:
        inp = input("Vastaus ({:d}-{:d} tai Enter=lopeta)? ".format(1, ANSWER_COUNT))
        if inp == "":
            sys.exit()
        try:
            inp = int(inp, 10)
            if 1 <= inp <= ANSWER_COUNT:
                return answers[inp - 1]
        except ValueError:
            pass

def explain_right_answer(question, questionPlace, answer):
    """Explain why the answer was correct."""

    if question is which_city_in_region:
        return "{city} on {region}.".format(
            city=answer,
            region=questionPlace
        )
    if question is which_city_not_in_region:
        return "{city} on {region}.".format(
            city=answer,
            region=REGION_NAMES[CITIES[answer]]
        )
    if question is which_city_in_same_region:
        return "{questionCity} ja {answerCity} ovat {region}.".format(
            questionCity=questionPlace,
            answerCity=answer,
            region=REGION_NAMES[CITIES[answer]]
        )
    if question is which_city_not_in_same_region:
        return "{questionCity} on {questionRegion} ja {answerCity} {answerRegion}.".format(
            questionCity=questionPlace,
            questionRegion=REGION_NAMES[CITIES[questionPlace]],
            answerCity=answer,
            answerRegion=REGION_NAMES[CITIES[answer]]
        )
    if question is where_city:
        return "{city} on {region}.".format(
            city=questionPlace,
            region=answer
        )
    sys.exit(1)  # should never happen

def explain_wrong_answer(question, questionPlace, answer, rightAnswer):
    """Explain why the answer was wrong."""

    if question is which_city_in_region:
        return "{correctCity} on {correctRegion}, {answerCity} {answerRegion}.".format(
            correctCity=rightAnswer,
            correctRegion=REGION_NAMES[CITIES[rightAnswer]],
            answerCity=answer,
            answerRegion=REGION_NAMES[CITIES[answer]]
        )
    if question is which_city_not_in_region:
        return "{answerCity} on {answerRegion} mutta {correctCity} {correctRegion}.".format(
            answerCity=answer,
            answerRegion=REGION_NAMES[CITIES[answer]],
            correctCity=rightAnswer,
            correctRegion=REGION_NAMES[CITIES[rightAnswer]]
        )
    if question is which_city_in_same_region:
        return "{questionCity} ja {correctCity} ovat {questionRegion} mutta {answerCity} " \
        "{answerRegion}.".format(
            questionCity=questionPlace,
            correctCity=rightAnswer,
            questionRegion=REGION_NAMES[CITIES[questionPlace]],
            answerCity=answer,
            answerRegion=REGION_NAMES[CITIES[answer]]
        )
    if question is which_city_not_in_same_region:
        return "{questionCity} ja {answerCity} ovat {questionRegion} mutta {correctCity} " \
        "{correctRegion}.".format(
            questionCity=questionPlace,
            answerCity=answer,
            questionRegion=REGION_NAMES[CITIES[questionPlace]],
            correctCity=rightAnswer,
            correctRegion=REGION_NAMES[CITIES[rightAnswer]]
        )
    if question is where_city:
        return "{questionCity} on {questionRegion}.".format(
            questionCity=questionPlace,
            questionRegion=REGION_NAMES[CITIES[questionPlace]]
        )
    sys.exit(1)  # should never happen

def ask_outer():
    """Create question, ask, give feedback.
    return: was answer correct"""

    question = random.choice((
        which_city_in_region,
        which_city_not_in_region,
        which_city_in_same_region,
        which_city_not_in_same_region,
        where_city,
    ))
    (text, cityOrRegion, rightAnswer, wrongAnswers) = question()
    #print("Oikea vastaus:", rightAnswer)

    text = text.format(cityOrRegion)
    allAnswers = set((rightAnswer,)) | wrongAnswers
    answer = ask_inner(text, allAnswers)

    if answer == rightAnswer:
        print("Oikein. " + explain_right_answer(question, cityOrRegion, answer))
        return True
    print("Väärin. " + explain_wrong_answer(question, cityOrRegion, answer, rightAnswer))
    return False

def main():
    """The main function."""

    points = 0
    for round_ in range(NUMBER_OF_ROUNDS):
        print("Kysymys {:d}/{:d}:".format(round_ + 1, NUMBER_OF_ROUNDS))
        points += ask_outer()
        print()
    print("Pisteesi: {:d}/{:d}".format(points, NUMBER_OF_ROUNDS))

if __name__ == "__main__":
    main()

