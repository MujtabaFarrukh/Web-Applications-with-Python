import streamlit as st

def contact_form():
    st.write('Contact us')
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    if st.button('Send'):
        st.write('Message sent!')

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image('Myassets/DP.jpg', width=220)
with col2:
    st.title('Mujtaba Farrukh', anchor=False)
    st.write('Full Stack Developer')

if st.button('Contact us'):
    contact_form()