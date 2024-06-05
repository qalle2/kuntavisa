# a quiz of Finnish cities/municipalities and regions
# source: https://fi.wikipedia.org/wiki/Luettelo_Suomen_kunnista
# the information is up to date as of June 2024
# TODO: hard/easy mode: correct and incorrect region are always/never neighbors

import random, sys  # note: "random" is not for cryptographic use

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
    10: "Pirkanmaalla",
    11: "Pohjanmaalla",
    12: "Pohjois-Karjalassa",
    13: "Pohjois-Pohjanmaalla",
    14: "Pohjois-Savossa",
    15: "Päijät-Hämeessä",
    16: "Satakunnassa",
    17: "Uudellamaalla",
    18: "Varsinais-Suomessa",
}

# cities/municipalities (value: region number)
CITIES = {
    "Akaa": 10,
    "Alajärvi": 2,
    "Alavieska": 13,
    "Alavus": 2,
    "Asikkala": 15,
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
    "Haapajärvi": 13,
    "Haapavesi": 13,
    "Hailuoto": 13,
    "Halsua": 6,
    "Hamina": 8,
    "Hammarland": 0,
    "Hankasalmi": 7,
    "Hanko": 17,
    "Harjavalta": 16,
    "Hartola": 15,
    "Hattula": 5,
    "Hausjärvi": 5,
    "Heinola": 15,
    "Heinävesi": 12,
    "Helsinki": 17,
    "Hirvensalmi": 3,
    "Hollola": 15,
    "Huittinen": 16,
    "Humppila": 5,
    "Hyrynsalmi": 4,
    "Hyvinkää": 17,
    "Hämeenkyrö": 10,
    "Hämeenlinna": 5,
    "Ii": 13,
    "Iisalmi": 14,
    "Iitti": 15,
    "Ikaalinen": 10,
    "Ilmajoki": 2,
    "Ilomantsi": 12,
    "Imatra": 1,
    "Inari": 9,
    "Inkoo": 17,
    "Isojoki": 2,
    "Isokyrö": 2,
    "Janakkala": 5,
    "Joensuu": 12,
    "Jokioinen": 5,
    "Jomala": 0,
    "Joroinen": 14,
    "Joutsa": 7,
    "Juuka": 12,
    "Juupajoki": 10,
    "Juva": 3,
    "Jyväskylä": 7,
    "Jämijärvi": 16,
    "Jämsä": 7,
    "Järvenpää": 17,
    "Kaarina": 18,
    "Kaavi": 14,
    "Kajaani": 4,
    "Kalajoki": 13,
    "Kangasala": 10,
    "Kangasniemi": 3,
    "Kankaanpää": 16,
    "Kannonkoski": 7,
    "Kannus": 6,
    "Karijoki": 2,
    "Karkkila": 17,
    "Karstula": 7,
    "Karvia": 16,
    "Kaskinen": 11,
    "Kauhajoki": 2,
    "Kauhava": 2,
    "Kauniainen": 17,
    "Kaustinen": 6,
    "Keitele": 14,
    "Kemi": 9,
    "Kemijärvi": 9,
    "Keminmaa": 9,
    "Kemiönsaari": 18,
    "Kempele": 13,
    "Kerava": 17,
    "Keuruu": 7,
    "Kihniö": 10,
    "Kinnula": 7,
    "Kirkkonummi": 17,
    "Kitee": 12,
    "Kittilä": 9,
    "Kiuruvesi": 14,
    "Kivijärvi": 7,
    "Kokemäki": 16,
    "Kokkola": 6,
    "Kolari": 9,
    "Konnevesi": 7,
    "Kontiolahti": 12,
    "Korsnäs": 11,
    "Koski Tl": 18,
    "Kotka": 8,
    "Kouvola": 8,
    "Kristiinankaupunki": 11,
    "Kruunupyy": 11,
    "Kuhmo": 4,
    "Kuhmoinen": 10,
    "Kumlinge": 0,
    "Kuopio": 14,
    "Kuortane": 2,
    "Kurikka": 2,
    "Kustavi": 18,
    "Kuusamo": 13,
    "Kyyjärvi": 7,
    "Kärkölä": 15,
    "Kärsämäki": 13,
    "Kökar": 0,
    "Lahti": 15,
    "Laihia": 11,
    "Laitila": 18,
    "Lapinjärvi": 17,
    "Lapinlahti": 14,
    "Lappajärvi": 2,
    "Lappeenranta": 1,
    "Lapua": 2,
    "Laukaa": 7,
    "Lemi": 1,
    "Lemland": 0,
    "Lempäälä": 10,
    "Leppävirta": 14,
    "Lestijärvi": 6,
    "Lieksa": 12,
    "Lieto": 18,
    "Liminka": 13,
    "Liperi": 12,
    "Lohja": 17,
    "Loimaa": 18,
    "Loppi": 5,
    "Loviisa": 17,
    "Luhanka": 7,
    "Lumijoki": 13,
    "Lumparland": 0,
    "Luoto": 11,
    "Luumäki": 1,
    "Maalahti": 11,
    "Maarianhamina": 0,
    "Marttila": 18,
    "Masku": 18,
    "Merijärvi": 13,
    "Merikarvia": 16,
    "Miehikkälä": 8,
    "Mikkeli": 3,
    "Muhos": 13,
    "Multia": 7,
    "Muonio": 9,
    "Mustasaari": 11,
    "Muurame": 7,
    "Mynämäki": 18,
    "Myrskylä": 17,
    "Mäntsälä": 17,
    "Mänttä-Vilppula": 10,
    "Mäntyharju": 3,
    "Naantali": 18,
    "Nakkila": 16,
    "Nivala": 13,
    "Nokia": 10,
    "Nousiainen": 18,
    "Nurmes": 12,
    "Nurmijärvi": 17,
    "Närpiö": 11,
    "Orimattila": 15,
    "Oripää": 18,
    "Orivesi": 10,
    "Oulainen": 13,
    "Oulu": 13,
    "Outokumpu": 12,
    "Padasjoki": 15,
    "Paimio": 18,
    "Paltamo": 4,
    "Parainen": 18,
    "Parikkala": 1,
    "Parkano": 10,
    "Pedersören kunta": 11,
    "Pelkosenniemi": 9,
    "Pello": 9,
    "Perho": 6,
    "Pertunmaa": 3,
    "Petäjävesi": 7,
    "Pieksämäki": 3,
    "Pielavesi": 14,
    "Pietarsaari": 11,
    "Pihtipudas": 7,
    "Pirkkala": 10,
    "Polvijärvi": 12,
    "Pomarkku": 16,
    "Pori": 16,
    "Pornainen": 17,
    "Porvoo": 17,
    "Posio": 9,
    "Pudasjärvi": 13,
    "Pukkila": 17,
    "Punkalaidun": 10,
    "Puolanka": 4,
    "Puumala": 3,
    "Pyhtää": 8,
    "Pyhäjoki": 13,
    "Pyhäjärvi": 13,
    "Pyhäntä": 13,
    "Pyhäranta": 18,
    "Pälkäne": 10,
    "Pöytyä": 18,
    "Raahe": 13,
    "Raasepori": 17,
    "Raisio": 18,
    "Rantasalmi": 3,
    "Ranua": 9,
    "Rauma": 16,
    "Rautalampi": 14,
    "Rautavaara": 14,
    "Rautjärvi": 1,
    "Reisjärvi": 13,
    "Riihimäki": 5,
    "Ristijärvi": 4,
    "Rovaniemi": 9,
    "Ruokolahti": 1,
    "Ruovesi": 10,
    "Rusko": 18,
    "Rääkkylä": 12,
    "Saarijärvi": 7,
    "Salla": 9,
    "Salo": 18,
    "Saltvik": 0,
    "Sastamala": 10,
    "Sauvo": 18,
    "Savitaipale": 1,
    "Savonlinna": 3,
    "Savukoski": 9,
    "Seinäjoki": 2,
    "Sievi": 13,
    "Siikainen": 16,
    "Siikajoki": 13,
    "Siikalatva": 13,
    "Siilinjärvi": 14,
    "Simo": 9,
    "Sipoo": 17,
    "Siuntio": 17,
    "Sodankylä": 9,
    "Soini": 2,
    "Somero": 18,
    "Sonkajärvi": 14,
    "Sotkamo": 4,
    "Sottunga": 0,
    "Sulkava": 3,
    "Sund": 0,
    "Suomussalmi": 4,
    "Suonenjoki": 14,
    "Sysmä": 15,
    "Säkylä": 16,
    "Taipalsaari": 1,
    "Taivalkoski": 13,
    "Taivassalo": 18,
    "Tammela": 5,
    "Tampere": 10,
    "Tervo": 14,
    "Tervola": 9,
    "Teuva": 2,
    "Tohmajärvi": 12,
    "Toholampi": 6,
    "Toivakka": 7,
    "Tornio": 9,
    "Turku": 18,
    "Tuusniemi": 14,
    "Tuusula": 17,
    "Tyrnävä": 13,
    "Ulvila": 16,
    "Urjala": 10,
    "Utajärvi": 13,
    "Utsjoki": 9,
    "Uurainen": 7,
    "Uusikaarlepyy": 11,
    "Uusikaupunki": 18,
    "Vaala": 13,
    "Vaasa": 11,
    "Valkeakoski": 10,
    "Vantaa": 17,
    "Varkaus": 14,
    "Vehmaa": 18,
    "Vesanto": 14,
    "Vesilahti": 10,
    "Veteli": 6,
    "Vieremä": 14,
    "Vihti": 17,
    "Viitasaari": 7,
    "Vimpeli": 2,
    "Virolahti": 8,
    "Virrat": 10,
    "Vårdö": 0,
    "Vöyri": 11,
    "Ylitornio": 9,
    "Ylivieska": 13,
    "Ylöjärvi": 10,
    "Ypäjä": 5,
    "Ähtäri": 2,
    "Äänekoski": 7,
}

# how many choices; 2-7 because a region may have as few as 6 cities (Kymenlaakso)
ANSWER_COUNT = 4

def which_city_in_region():
    # question: "Which city is in region X?"
    # return: (question, region, correct_city, wrong_cities)

    correctCity = random.choice(list(CITIES))
    region = CITIES[correctCity]
    wrongCitiesAll = [c for c in CITIES if CITIES[c] != region]
    wrongCities = set(random.sample(wrongCitiesAll, ANSWER_COUNT - 1))
    return ("Mikä kunta on {:s}?", REGION_NAMES[region], correctCity, wrongCities)

def which_city_not_in_region():
    # question: "Which city is NOT in region X?"
    # return: (question, region, correct_city, wrong_cities)

    region = CITIES[random.choice(list(CITIES))]
    wrongCitiesAll = {c for c in CITIES if CITIES[c] == region}
    correctCity = random.choice(list(set(CITIES) - wrongCitiesAll))
    wrongCities = set(random.sample(list(wrongCitiesAll), ANSWER_COUNT - 1))
    return ("Mikä kunta EI ole {:s}?", REGION_NAMES[region], correctCity, wrongCities)

def which_city_in_same_region():
    # question: "Which city is in the same region as city X?"
    # return: (question, city, correct_city, wrong_cities)

    questionCity = random.choice(list(CITIES))
    correctCitiesAll = {c for c in CITIES if CITIES[c] == CITIES[questionCity]}
    return (
        "Mikä kunta on samassa maakunnassa kuin {:s}?",
        questionCity,
        random.choice(list(correctCitiesAll - {questionCity})),
        set(random.sample(list(set(CITIES) - correctCitiesAll), ANSWER_COUNT - 1))
    )

def which_city_not_in_same_region():
    # question: "Which city is NOT in the same region as city X?"
    # return: (question, city, correct_city, wrong_cities)

    questionCity = random.choice(list(CITIES))
    wrongCitiesAll = {c for c in CITIES if CITIES[c] == CITIES[questionCity]}
    return (
        "Mikä kunta EI ole samassa maakunnassa kuin {:s}?",
        questionCity,
        random.choice(list(set(CITIES) - wrongCitiesAll)),
        set(random.sample(list(wrongCitiesAll - {questionCity}), ANSWER_COUNT - 1))
    )

def where_city():
    # question: "Where is city X?"
    # return: (question, city, correct_region, wrong_regions)

    city = random.choice(list(CITIES))
    correctRegion = CITIES[city]
    wrongRegions = random.sample(list(set(REGION_NAMES) - {correctRegion}), ANSWER_COUNT - 1)
    wrongRegionNames = {REGION_NAMES[r] for r in wrongRegions}
    return ("Missä {:s} on?", city, REGION_NAMES[correctRegion], wrongRegionNames)

def ask_inner(question, answers):
    # print a question and answers, wait for valid input
    # question: str, answers: set of strings, return answer as str

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
    # explain why the answer was correct

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
    # explain why the answer was wrong

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
    # ask a question, give feedback; return: was the answer correct?

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
    allAnswers = {rightAnswer} | wrongAnswers
    answer = ask_inner(text, allAnswers)
    print()

    if answer == rightAnswer:
        print("Oikein. " + explain_right_answer(question, cityOrRegion, answer))
        return True
    print("Väärin. " + explain_wrong_answer(question, cityOrRegion, answer, rightAnswer))
    return False

def main():
    points = 0
    for round_ in range(NUMBER_OF_ROUNDS):
        print("Kysymys {:d}/{:d}:".format(round_ + 1, NUMBER_OF_ROUNDS))
        points += ask_outer()
        print()
    print("Pisteesi: {:d}/{:d}".format(points, NUMBER_OF_ROUNDS))

main()
