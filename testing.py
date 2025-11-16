import requests

def fetch_recipes(ingredients):
    api_key = "b63e282b61c148f79650cde3ab962537"
    
    if isinstance(ingredients, list):
        ingredients = [item["ingredient"] for item in ingredients]
        ingredients = ", ".join(ingredients)

    ingredients = ingredients.replace(" ", "")  # remove spaces for URL
    
    # Spoonacular API call
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def display():
    # Ask user for ingredients
    ingredients_input = input("Enter ingredients you have, separated by commas: ")

    # Get data from back end
    data = fetch_recipes(ingredients_input)

    # Print results
    for recipe in data:
        print("🍽️ ", recipe["title"])
        print("Used ingredients:", [i["name"] for i in recipe["usedIngredients"]])
        print("Missing ingredients:", [i["name"] for i in recipe["missedIngredients"]])
        print()
    
if __name__ == "__main__":
    display()