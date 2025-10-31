import requests

def fetch_recipes():
    api_key = "b63e282b61c148f79650cde3ab962537"
    
    # Ask user for ingredients
    ingredients_input = input("Enter ingredients you have, separated by commas: ")
    ingredients = ingredients_input.replace(" ", "")  # remove spaces for URL
    
    # Spoonacular API call
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Print results
    for recipe in data:
        print("🍽️", recipe["title"])
        print("Used ingredients:", [i["name"] for i in recipe["usedIngredients"]])
        print("Missing ingredients:", [i["name"] for i in recipe["missedIngredients"]])
    

# Call the function 
fetch_recipes()
