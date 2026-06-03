import math

# TRAVEL KNOWLEDGE BASE

city_info = {
    "Hyderabad": {
        "places": {
            "history": [
                "Charminar",
                "Golconda Fort",
                "Salar Jung Museum"
            ],
            "nature": [
                "Hussain Sagar",
                "NTR Garden"
            ],
            "food": [
                "Biryani Spots",
                "Irani Cafe"
            ]
        },

        "hotel_cost": {
            "low": 1000,
            "medium": 2500,
            "high": 5000
        },

        "daily_transport": 500,

        "food_items": {
            "veg": [
                "Veg Biryani",
                "Paneer Curry"
            ],
            "non-veg": [
                "Chicken Biryani",
                "Mutton Biryani"
            ]
        }
    }
}

def create_travel_plan(city_name, user_budget, total_days, user_interest, food_choice):

    if city_name not in city_info:
        print("City not available")
        return

    details = city_info[city_name]

    if user_budget < 5000:
        stay_type = "low"
    elif user_budget < 15000:
        stay_type = "medium"
    else:
        stay_type = "high"

    stay_cost = details["hotel_cost"][stay_type] * total_days
    travel_cost = details["daily_transport"] * total_days
    meal_cost = 400 * total_days

    final_cost = stay_cost + travel_cost + meal_cost

    selected_places = details["places"].get(user_interest, [])
    selected_foods = details["food_items"].get(food_choice, [])

    print("\nAI TRAVEL PLAN")
    print("-----------------------------")

    print("Destination :", city_name)
    print("Budget      : ₹", user_budget)
    print("Days        :", total_days)

    print("\nRecommended Places:")

    for place_name in selected_places:
        print("-", place_name)

    print("\nRecommended Food:")

    for food in selected_foods:
        print("-", food)

    print("\nHotel Type :", stay_type)

    print("\nEstimated Cost")
    print("Hotel Cost     : ₹", stay_cost)
    print("Transport Cost : ₹", travel_cost)
    print("Food Cost      : ₹", meal_cost)

    print("-----------------------------")
    print("Total Cost     : ₹", final_cost)

    print("\nDAY WISE PLAN")

    places_count = math.ceil(len(selected_places) / total_days)

    place_index = 0

    for day_no in range(1, total_days + 1):

        print("\nDay", day_no)

        for visit in range(places_count):

            if place_index < len(selected_places):
                print("- Visit", selected_places[place_index])
                place_index += 1

        if selected_foods:
            print("- Try:", selected_foods[0])


print("SMART AI TRAVEL PLANNER")

city = input("Enter city (Hyderabad): ")

budget = int(input("Enter budget: ₹"))

days = int(input("Enter number of days: "))

interest = input(
    "Enter interest "
    "(history/nature/food): "
).lower()

food_preference = input(
    "Food preference "
    "(veg/non-veg): "
).lower()

create_travel_plan(
    city,
    budget,
    days,
    interest,
    food_preference
)
