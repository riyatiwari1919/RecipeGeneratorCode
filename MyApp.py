import spacy
import random

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Sample recipe dataset
recipes = {
    "pasta": {
        "ingredients": ["pasta", "tomato sauce", "garlic", "onion", "cheese"],
        "steps": [
            "Boil pasta until al dente.",
            "Sauté garlic and onion in olive oil.",
            "Add tomato sauce and simmer.",
            "Mix in pasta and top with cheese.",
        ],
    },
    "omelette": {
        "ingredients": ["eggs", "milk", "salt", "pepper", "butter"],
        "steps": [
            "Beat eggs with milk, salt, and pepper.",
            "Heat butter in a pan.",
            "Pour egg mixture and cook until firm.",
            "Fold and serve hot.",
        ],
    },
    "salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "olive oil", "lemon juice"],
        "steps": [
            "Chop all vegetables.",
            "Mix with olive oil and lemon juice.",
            "Toss well and serve fresh.",
        ],
    },
}

def generate_recipe(food_item):
    # Process food item with spaCy
    doc = nlp(food_item.lower())

    # Extract main food keyword
    for token in doc:
        if token.text in recipes:
            recipe = recipes[token.text]
            return f"Recipe for {token.text.capitalize()}:\n\n" \
                   f"🛒 Ingredients: {', '.join(recipe['ingredients'])}\n\n" \
                   f"📌 Steps:\n" + "\n".join([f"{i+1}. {step}" for i, step in enumerate(recipe["steps"])])
    
    return "Sorry, I don't have a recipe for that."

# Get user input and generate recipe
if __name__ == "__main__":
    food_item = input("Enter a food name: ")
    print(generate_recipe(food_item))
