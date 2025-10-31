import streamlit as st
import time

st.set_page_config(layout="wide")

# style guide for the colored header
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
        My Ingredients
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# keeps the info for ingredients inputted by user
if "ingredients" not in st.session_state:
    st.session_state.ingredients = []

col1, col2 = st.columns([2,2])

# custom design for the warnings
def custom_warning(message):
    st.markdown(f"""
        <div style="
            background-color: #FCF7EC; 
            color: #856404; 
            border-radius: 15px; 
            padding: 15px; 
            margin-bottom: 10px;
        ">
            ⚠️ {message}
        </div>
    """, unsafe_allow_html=True)

# custom design for the info messages
def custom_info(message):
    st.markdown(f"""
        <div style="
            background-color: #D5E4CF; 
            color: #856404; 
            border-radius: 15px; 
            padding: 15px; 
            margin-bottom: 10px;
        ">
        {message}
        </div>
    """, unsafe_allow_html=True)

# Ingredient input on the left of the screen
with col1:
    st.subheader("Add an Ingredient")

    # Style guide for the input box
    st.markdown("""
        <style>
        
        div.stForm {
            background-color: #C3D5C1;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }

        div.stForm > div {
            margin-bottom: 10px;
        }

        div.stForm button {
            width: 100%;
            font-size: 16px;
            padding: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Setup for inputs in ingreident input box
    with st.form("ingredient_form", clear_on_submit=True):

        ingredient = st.text_input("Ingredient", placeholder="e.g. Tomato")

        amount = st.text_input("Amount", placeholder = "e.g. 2, 1 1/2")

        unit = st.selectbox("Unit", ["", "g", "kg", "ml", "L", "tsp", "tbsp", "cup", "oz", "lb", "pcs"])

        submitted = st.form_submit_button("Add Ingredient")

        # requires all fields to be filled before it will submit an ingredient
        if submitted:
            if ingredient and amount and unit:
                st.session_state.ingredients.append({
                    "ingredient": ingredient,
                    "amount": amount,
                    "unit": unit
                })
                st.success(f"Added {amount} {unit} of {ingredient}")
            else:
                custom_warning("Please fill in all fields before adding.")

# List of submitted ingredients on the right
with col2:
    st.subheader("Ingredient List")

    # Style guide for list box
    if st.session_state.ingredients:
        st.markdown("""
        <style>
        .ingredient-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #FCF7EC;
            border-radius: 10px;
            padding: 8px 12px;
            margin-bottom: 8px;
            box-shadow: 1px 1px 4px rgba(0,0,0,0.05);
        }
        </style>
        """, unsafe_allow_html=True)

        # Show the inputs given and leaves a option for a ingredient to be removed
        for i, item in enumerate(st.session_state.ingredients):
            col_a, col_b = st.columns([4, 1])
            with col_a:
                if isinstance(item, dict):
                    st.markdown(
                        f"<div class='ingredient-row'><b>{item['ingredient']}</b>: {item['amount']} {item['unit']}</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"<div class='ingredient-row'><b>{item}</b></div>", unsafe_allow_html=True)
            with col_b:
                if st.button("❌", key=f"remove_{i}"):
                    st.session_state.ingredients.pop(i)
                    st.rerun()
    else:
        custom_info("No ingredients added yet — add some on the left!")

    # only prompts the user to go to the next page once at least one ingredient has been listed
    if len(st.session_state.ingredients) >= 1:
        left, middle, right = st.columns([1, 1, 0.5])
        with middle:
            if st.button("See Recipes"):
                st.success("Ingredients saved! Redirecting to recipes... ")
                time.sleep(2)  
                st.switch_page("pages/Recipes.py")   

st.markdown("---")