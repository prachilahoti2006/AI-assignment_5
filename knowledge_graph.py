# KNOWLEDGE GRAPH USING FACT TRIPLES

graph_data = [

    ("Charminar", "located_in", "Hyderabad"),
    ("Golconda Fort", "located_in", "Hyderabad"),
    ("Hyderabad", "famous_for", "Biryani"),
    ("Charminar", "type", "Historical"),
    ("Hussain Sagar", "type", "Nature"),
    ("Laad Bazaar", "type", "Shopping"),
    ("Paradise Restaurant", "serves", "Biryani")

]

# DISPLAY ALL FACTS

print("KNOWLEDGE GRAPH TRIPLES")
print("----------------------------------")

for fact in graph_data:
    print(fact)

# SEARCH DETAILS OF A PLACE

def find_place(place):

    print("\nSearching Information for:", place)

    match_found = False

    for source, relation, target in graph_data:

        if source.lower() == place.lower():

            print(source,
                  "-->",
                  relation,
                  "-->",
                  target)

            match_found = True

    if match_found == False:
        print("No information found")

# TAKE USER INPUT

search_name = input("\nEnter place name to search: ")

find_place(search_name)
