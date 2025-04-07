import streamlit as st

about_page = st.Page(
    page='Pages/About_us.py',
    title='About us',
    icon=':material/person:',
    default=True,
)

project_one= st.Page(
    page='Pages/Sales.py',
    title='Our Sales',
    icon=':material/bar_chart:',
)

project_two= st.Page(
    page='Pages/Help.py',
    title='Help',
    icon=':material/support:',
)   

# pg = st.navigation(pages=[about_page, project_one, project_two])

pg = st.navigation(
    {
    'information':[about_page],
    'Company Info and Support': [project_one, project_two],
    }
)

# Share on all pages
st.logo('Myassets/logo.png')
st.sidebar.text('Made by Mujtaba Farrukh')

# Run the app
pg.run()