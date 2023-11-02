import streamlit as st
from datetime import time
import pandas as pd

marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')

def main():
    st.title('GKTW Dispatcher')

    with st.form(key='form1', clear_on_submit = True):
        st.text_input('Name', key = 'name')
        st.selectbox('Input Pick Up Location',marker['Name'], key='pickup', index = None)
        st.selectbox('Input Drop Off Location',marker['Name'], key='dropoff', index = None)
        st.checkbox('ADA', key = 'ADA')
        st.time_input('Input Pick Up Time', value = 'now', key = 'reservation')
        st.selectbox('Num. of People', list(range(1,8)), key='numOfPeople', index = None)
        submit_button = st.form_submit_button("ADD")
    if submit_button:
        st.success(f"{st.session_state.name} has been added and is being picked up at {st.session_state.pickup} and dropped off at {st.session_state.dropoff}, they put ADA: {st.session_state.ADA}, reserved: {st.session_state.reservation}")


main()