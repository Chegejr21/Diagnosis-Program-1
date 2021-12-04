name = input("Enter patients name")
age = str(input("Enter patients age"))
print("choose vomiting for Cholera,stomachache for TB,bleeding for Anaemia,headache for HIV"),
symptom = input("Enter patients symptom:")
if type(symptom) == str:
    if symptom == "vomiting":
        print("Cholera")
    elif symptom == "stomachache":
        print("TB")
    elif symptom == "bleeding":
        print("Anaemia")
    elif symptom == "headache":
        print("HIV")
    else:
        print("Unknown symptom")
print("Good morning " + name, "age " + age, " years you are sick and need medical attention right away")
