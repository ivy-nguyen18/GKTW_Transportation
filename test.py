import streamlit as st
import pandas as pd

# Initialize session state with dataframes
# Include initialization of "edited" slots by copying originals
if 'df1' not in st.session_state:
    st.session_state.df1 = pd.DataFrame({
        "col1": ["a1", "a2", "a3"],
        "Values": [1, 2, 3]
    })
    st.session_state.edited_df1 = st.session_state.df1.copy()
    st.session_state.df2 = pd.DataFrame({
        "col1": ["b1", "b2", "b3"], 
        "Values": [1, 2, 3]
    })
    st.session_state.edited_df2 = st.session_state.df2.copy()

# Save edits by copying edited dataframes to "original" slots in session state
def save_edits():
    st.session_state.df1 = st.session_state.edited_df1.copy()
    st.session_state.df2 = st.session_state.edited_df2.copy()

# Sidebar to select page and commit changes upon selection
page = st.sidebar.selectbox("Select: ", ("A","B"), on_change=save_edits)

# Convenient shorthand notation
df1 = st.session_state.df1
df2 = st.session_state.df2

# Page functions commit edits in real time to "editied" slots in session state
def funct1():
    st.session_state.edited_df1 = st.data_editor(df1, num_rows="dynamic")
    return

def funct2():
    st.session_state.edited_df2 = st.data_editor(df2, num_rows="dynamic")
    return

if  page == "A":
    st.header("Page A")
    funct1()
elif page == "B":
    st.header("Page B")
    funct2()