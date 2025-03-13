import streamlit as st
import re
import random
import string
import clipboard

st.set_page_config(
    page_title="CrackShield | Aqsaa Qaazi", 
    page_icon="🔐", 
    layout="centered")


# ----------------------SEO TAGS----------------------------

st.markdown("""
    <meta name="description" content="CrackShield - A password strength meter that helps you detect weak passwords and generate strong ones."/>
    <meta name="keywords" content="password strength, password security, strong password generator, secure password checker"/>
    <meta name="author" content="Aqsaa Qaazi"/>
    <meta property="og:title" content="CrackShield | Password Strength Meter"/>
    <meta property="og:description" content="Check your password strength and generate a secure password with CrackShield."/>
    <meta property="og:image" content="https://crackshield.streamlit.app/preview-image.png"/>
    <meta property="og:url" content="https://crackshield.streamlit.app"/>
    <meta name="twitter:card" content="summary_large_image"/>
""", unsafe_allow_html=True)

# -------------UI/UX---------------------------

# i could've used headings here but markdown is good for searchengines,


st.markdown("# CrackShield | Password Strength Meter")
st.markdown("### Detect and Strengthen Weak Passwords")
st.markdown("###### (Or generate one if you're unsure)")


# -----------------------------STATES---------------------------------

if "password" not in st.session_state:
    st.session_state.password = ""
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "copy_success" not in st.session_state:
    st.session_state.copy_success = False 

# ---------------------------------VARIABLES----------------------------


col1, col2 = st.columns([6, 3]) 

with col1:
    password = st.text_input(
            "Enter your password:", 
            placeholder="Type your password here...", 
            value=st.session_state.password,
            type="password",
            key = "password_input",
            disabled=st.session_state.disabled,
            label_visibility="collapsed"            
            )
    copy_message = st.empty()

with col2:
    if st.session_state.disabled:
        if st.button("Copy", help="Copy to clipboard"):
            try:
                clipboard.copy(st.session_state.password)
                st.success("Copied to clipboard!")
            except Exception as e:
                st.error(f"Clipboard copy failed: {e}")
            

# -------------------------------------FUNCTIONS--------------------------
def generate_password(length=10):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()_+{}:;,.?~/-"
    return "".join(random.choice(chars) for _ in range (length))

def evaluate_password(password):
    if not password: 
        return "Enter a password to check its strength, or Roll the dice if unsure‼", []
    
    points= 0
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
        

    # print(f"DEBUG:this returns => points={points}, strength={strength}, suggestions={suggestions}")

    return points, strength, suggestions 


#------------------------------CONDITIONS---------------------------------

if st.button("🎲", help = "Generate a random strong password"):
    st.session_state.password = generate_password()
    st.session_state.disabled = True
    
if st.session_state.copy_success:
    with col1:
        copy_message.success("Copied to Clipboard!")
    
if password:
    points, strength, suggestions = evaluate_password(password)
    st.markdown(f"_Your password is {strength}_")

    if suggestions:
        st.write("**Suggestions to Improve:**")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")


