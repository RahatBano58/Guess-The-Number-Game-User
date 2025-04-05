import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Guess the Number Game (User)",
    page_icon="🎮",
    layout="centered",
)

# Add custom CSS for background image, red text, and footer
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://st2.depositphotos.com/3442145/10403/i/450/depositphotos_104033390-stock-photo-spiraling-numbers-energy.jpg"); /* New background image */
        background-size: cover;
        background-position: center;
    }
    .title {
        font-size: 3rem;
        color: red;
        text-align: center;
        animation: fadeIn 2s;
    }
    .feedback {
        font-size: 1.5rem;
        color: red;
        text-align: center;
        animation: slideIn 1s;
    }
    .attempts {
        font-size: 1.2rem;
        color: red;
        text-align: center;
        animation: fadeIn 2s;
    }
    .input-label {
        font-size: 1.2rem;
        color: red;
        text-align: center;
    }
    .stNumberInput label {
        color: red;
    }
    .stButton button {
        color: red;
        background-color: white;
        border-radius: 5px;
        border: 1px solid red;
    }
    footer {
        visibility: hidden;
    }
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.7);
        color: red;
        text-align: center;
        padding: 10px;
        font-size: 1rem;
        border-top: 2px solid red;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and instructions
st.markdown('<h1 class="title">Guess the Number Game 🎮</h1>', unsafe_allow_html=True)
st.markdown('<p class="input-label">I\'ve picked a number between 1 and 100. Can you guess it?</p>', unsafe_allow_html=True)

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "guess" not in st.session_state:
    st.session_state.guess = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.game_over = False

# User input for guessing the number
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

# Check the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.markdown('<p class="feedback">Too low! Try a higher number. ⬆️</p>', unsafe_allow_html=True)
    elif guess > st.session_state.number:
        st.markdown('<p class="feedback">Too high! Try a lower number. ⬇️</p>', unsafe_allow_html=True)
    else:
        st.session_state.game_over = True
        st.balloons()
        st.markdown(f'<p class="feedback">🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!</p>', unsafe_allow_html=True)

# Display the number of attempts
st.markdown(f'<p class="attempts">Attempts: {st.session_state.attempts}</p>', unsafe_allow_html=True)

# Reset button
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        reset_game()

# Custom footer
st.markdown(
    """
    <div class="custom-footer">
        © 2025 Guess the Number Game | Developed with ❤️ by Rahat Bano
    </div>
    """,
    unsafe_allow_html=True,
)
