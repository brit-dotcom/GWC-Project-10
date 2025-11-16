import streamlit as st
from testing import fetch_recipes

st.set_page_config(layout="wide")

# header styling
st.markdown("""
    <style>
    .header {
        background-color: #AFC2AE;   
        color: #60524bff;            
        text-align: center;          
        padding: 40px 0;           
        font-size: 40px;
        font-weight: 700;            
        border-radius: 0;            
    }
    </style>

    <div class="header">
        Recipes
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# colors for recipe cards
CARD_COLOR = "#D5E4CF"
TEXT_COLOR = "#60524bff"

# recipe data - converts list into a string 
def get_ingredient():
    items = st.session_state.get("ingredients", [])
    ingredient_names = [item["ingredient"] for item in items if "ingredient" in item]
    return ", ".join(ingredient_names)

#Calling API
ingredient_string = get_ingredient()
recipes = fetch_recipes(ingredient_string)


# style guide for the cards along with hover effects! fancy!
st.markdown(f"""
    <style>
    .recipe-card {{
        background-color: {CARD_COLOR};
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 30px;
    }}
    .recipe-card:hover {{
        transform: scale(1.03);
        box-shadow: 0px 6px 12px rgba(0,0,0,0.15);
    }}
    </style>
""", unsafe_allow_html=True)

# setup to display the cards
for i in range(0, len(recipes), 3):
    cols = st.columns(3, gap="large")
    for col, recipe in zip(cols, recipes[i:i+3]):
        with col:
            st.markdown(
                f"""
                <div class="recipe-card">
                    <h3 style="color:{TEXT_COLOR};">{recipe["title"]}</h3>
                    <p style="color:{TEXT_COLOR}; font-size:16px;"> Ingredients matched with your list.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )