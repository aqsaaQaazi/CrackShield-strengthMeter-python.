# CrackShield – Password Strength Meter 
### & Random Password generator. 
###### _version: 2.4.0 _

## About 
CrackShield is a real-time password strength checker built with Python and Streamlit. It analyzes password length, character mix, and complexity to provide instant feedback and tips for stronger security.

## Features  
- ###### Password Strength Analysis: 
    Get real-time feedback on password security.

- ###### Score-Based Assessment: 
    Categorizes passwords as Weak, Can Be Stronger, Strong, or Solid.

- ###### Actionable Security Tips: 
    Provides suggestions to improve password strength.

- ###### Random Strong Password Generator: 
    One-click generation of highly secure passwords.

- ###### Copy-to-Clipboard Functionality: 
    Easily copy generated passwords for use.

- ###### Clean, Interactive UI: 
    Built with Streamlit for a smooth and user-friendly experience.

## How It Works  
The application assigns points based on the following conditions:  

- **Length Check**:
    Passwords longer  than 9 characters receive a point. 
- **Uppercase & Lowercase Check**:
    Passwords having  both uppercase and lowercase receive a point.
- **Number Check**:
    Passwords containing at least one number receive a point . 
- **Special Character Check**:
    Inclusion of symbols such as `@, #, $` contributes to the score.  

Based on the total points, the application provides categorized feedback along with recommendations for strengthening the password.  

## Technology Stack  
- **Python** for backend processing  
- **Streamlit** for interactive UI  
- **Regex (`re` module)** for pattern detection 
- **Pyperclip** for clipboard access  

## About Developer  
**Aqsaa Qaazi**  
A developer with expertise in Python, Streamlit,Next.js, React.js and other web technologies, committed to building interactive and security-focused applications.  

## License  
This project is open-source and available for use under the MIT License.  
