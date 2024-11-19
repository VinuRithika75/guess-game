import streamlit as st
import random

st.title("Number Guessing Game")


if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

st.write("Guess the number between 1 and 100")


user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key='guess')

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.random_number:
        st.write("Too low! Try again.")
    elif user_guess > st.session_state.random_number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0