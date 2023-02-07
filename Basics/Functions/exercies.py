def list_benifits():
    return "I am learning Python","it is more organized","it is easier to read"

def build_sentence(benefit):
    return "One benefit is that %s" % benefit

def name_the_benefis_of_functions():
    list_of_benefis = list_benifits()
    for benefit in list_of_benefis:
        print(build_sentence(benefit))

name_the_benefis_of_functions()