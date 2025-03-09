# CrackShield – Password Strength Meter  

## About 
CrackShield is a password strength evaluator built with Python and Streamlit. It provides real-time feedback on password security by analyzing key factors such as length, character diversity, and complexity.  

## Features  
- Evaluates password strength based on predefined security criteria  
- Provides a score-based assessment: Weak, Can Be Stronger, Strong, and Solid  
- Offers actionable suggestions to improve password security  
- Interactive and user-friendly interface powered by Streamlit  

## How It Works  
The application assigns points based on the following conditions:  

- **Length Check**:                 Passwords longer than 9 characters receive a point. 
- **Uppercase & Lowercase Check**:  Passwords having both uppercase and lowercase receive a point.
- **Number Check**:                 Passwords containing at least one number receive a point . 
- **Special Character Check**:      Inclusion of symbols such as `@, #, $` contributes to the score.  

Based on the total points, the application provides categorized feedback along with recommendations for strengthening the password.  

## Technology Stack  
- **Python** for backend processing  
- **Streamlit** for interactive UI  
- **Regex (`re` module)** for pattern detection   

## About Developer  
**Aqsaa Qaazi**  
A developer with expertise in Python, Streamlit, and web technologies, committed to building interactive and security-focused applications.  

## License  
This project is open-source and available for use under the MIT License.  
