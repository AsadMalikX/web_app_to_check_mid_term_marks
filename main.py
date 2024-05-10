import streamlit as st
import pandas as pd
import os

# Set the page config
st.set_page_config(page_title='Mid Term Marks',
                   layout='centered',
                   page_icon='📚')


# Set the working directory to the script location
os.chdir(os.path.dirname(__file__))

mid_term_marks = pd.read_csv('data/mid_term_marks.csv')

st.title("Convention Based WebApp to check Mid Term Marks 📚")

input_option = st.selectbox('Select input option', ['Full Name', 'Roll Number'])

if input_option == 'Full Name':
    input_value = st.text_input('Please, enter your full name in CAPITAL LETTERS')
else:
    input_value = st.text_input('Please, enter your roll number')

search_button = st.button('Search')

def search_marks(df, input_value, input_option):
    if input_option == 'Full Name':
        result = df[df['Full Name'] == input_value]
    else:
        result = df[df['Roll Number'] == input_value]
    
    if not result.empty:
        marks = result['Mid Term Marks'].values[0]
        st.write('Your Mid Term Marks are:', marks)
        
        if marks >= 20:
            st.write('Excellent work! Congratulations')
        elif marks > 15:
            st.write('Great job! Keep up and stay focused')
        else:
            st.write('Thanks for your effort! Keep it up')
    else:
        st.write('No record found')

if search_button:
    search_marks(mid_term_marks, input_value, input_option)

