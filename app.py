import streamlit as st
import re


st.set_page_config(
    page_title="CrackShield | Aqsaa Qaazi", 
    page_icon="🔐", 
    layout="centered")


st.header("CrackShield | Password Strength Meter")
st.subheader("Detect and Strengthen Weak Passwords")

password = st.text_input(
    "Enter your password:", 
    placeholder="Type your password here...", 
    type="password")

def evaluate_password(password):
    points = 0
    suggestions = []

    if len(password) > 9:
        points += 1
    else:
        suggestions.append("Increase password length to more than 9 characters.")

    # case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        points += 1
    else:
        suggestions.append("Use both uppercase and lowercase letters.")

    if re.search(r'\d', password): #\d checks for numbers 0-1
        points += 1
    else:
        suggestions.append("Add at least one number.")

    if re.search(r'[!@#$^&*()_+{}:;,.?~/-]', password):
        points += 1
    else:
        suggestions.append("Include special characters like @, #, $, etc.")

    if points == 4:
        strength = "🟢 Solid!"
    elif points == 3:
        strength = "🟡 Strong, but can be better.."
    elif points == 2:
        strength = "🟠 Can be stronger.!"
    else:
        strength = "🔴 Weak.."

    return strength, suggestions


if password:
    strength, suggestions = evaluate_password(password)
    st.markdown(f"_Your password is {strength}_")

    if suggestions:
        st.write("**Suggestions to Improve:**")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")
