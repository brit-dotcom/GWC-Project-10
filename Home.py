import streamlit as st
from PIL import Image
import base64

st.set_page_config(layout="wide")

# info to override normal image look in streamlit
st.markdown(
    """
    <style>
    img {
        border-radius: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# columns creation
col1, col2 = st.columns([1,1])

# left side of screen
with col1:
    # style guide for the text bubble
    st.markdown(
        """
        <style>
        .bubble { 
            background-color: #AFC2AE;  
            border-radius: 15px;   
            padding: 10px;         
            margin-bottom: 15px;    
            font-size: 20px;       
            line-height: 1.6;     
            color: #60524bff;     
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
        }

        
        .bubble h3 {
            font-size: 50px;        
            color: #60524bff;         
            margin-top: 0;          
            margin-bottom: 10px;    
            font-weight: 700;      
        }
        </style>

        <div class="bubble">
            <h3>Welcome to PantryPal!</h3>
            <p>
                Find new recipes with just the ingredients already in your home! PantryPal will search through 100+ 
                recipes in it's database to find one you can make with just the ingredients in your home! Click below to
                try it out. 
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    #style guide for the button to next page
    st.markdown("""
    <style>
    div[data-testid="stButton"] {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    div[data-testid="stButton"] > button {
        background-color: #AFC2AE;
        color: 60524bff;
        padding: 18px 40px;        
        font-size: 20px;            
        border-radius: 12px;         
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    div[data-testid="stButton"] > button:hover {
        background-color: #D5E4CF;
        transform: scale(1.05);    
    }
    </style>
    """, unsafe_allow_html=True)


    col3, col4, col5 = st.columns([1,2,1])

    with col4:
        if st.button("Input my Ingredients ->"):
            st.switch_page("pages/Ingredients.py")

    
# placement of pantry pal on the right
with col2:
    img_col, bubble_col = st.columns([1.5, 1])

    # Load and display image
    img1 = Image.open("images/pantrypal.png")
    img1 = img1.resize((img1.width, int(img1.height * 0.8)))
    img_col.image(img1, use_container_width=True)

    # style guide for pnatrypal speech bubble
    bubble_col.markdown(
        """
        <style>
        .speech-bubble {
            position: relative;
            background: #D5E4CF;
            border-radius: 20px;
            padding: 20px;
            color: #60524bff;
            font-size: 18px;
            line-height: 1.5;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-top: 60px; 
        }

        .speech-bubble::before {
            content: "";
            position: absolute;
            left: -20px;  
            top: 40px;   
            border-width: 10px 20px 10px 0;
            border-style: solid;
            border-color: transparent #D5E4CF transparent transparent;
        }
        </style>

        <div class="speech-bubble">
            <h3 style="margin-top:0;">Hey there!</h3>
            <p>
                I'm <b>PantryPal</b>! Your personal kitchen assistant!  
                I'll look for recipes so you don't have to! Ready to get cooking?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# style guide for the pics on the bottom and the text
st.markdown("""
    <style>
    h2 {
        text-align: center;
        font-size: 36px;
        color: #3c2f2f;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .recipe-caption {
        color: #60524bff;
        text-align: center;
        margin-top: 10px;
        font-size: 18px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2>Many Recipes Available!</h2>", unsafe_allow_html=True)

# organization for the pics to keep them side by side and even
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    image = Image.open("images/beef_plate.jpg")
    new_image = image.resize((600, 400)) 
    st.image(new_image, caption="Beef with vegetables") 

with col2:
    image = Image.open("images/chickpea-salad.jpg")
    new_image = image.resize((600, 400))
    st.image(new_image, caption="Chickpea Salad")

with col3:
    image = Image.open("images/pasta-bowl.jpg")
    new_image = image.resize((600, 400)) 
    st.image(new_image, caption="Pasta Salad")

with col4:
    image = Image.open("images/grilled_chicken.jpg")
    new_image = image.resize((600, 400)) 
    st.image(new_image, caption="Grilled Chicken")

with col5:
    image = Image.open("images/penne-pasta.jpg")
    new_image = image.resize((600, 400))
    st.image(new_image, caption="Penne Pasta")
