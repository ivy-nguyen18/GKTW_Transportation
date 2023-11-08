import streamlit as st
from datetime import time
import pandas as pd
import control
from database import createTable, addData

marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')
st.set_page_config(layout="wide")

def onDataChange():
    print(st.session_state.df1)
    st.session_state.ada_df = pd.DataFrame(st.session_state.df2)
    st.session_state.standard_df = pd.DataFrame(st.session_state.df1)


def main():
    st.title(':telephone_receiver: GKTW Dispatcher')
    guest = None
    #createTable()
    if 'ada_df' not in st.session_state:
        st.session_state.ada_df = pd.DataFrame(columns=['name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status', 'travelTime', 'timeFromPrev' ])
    if 'standard_df' not in st.session_state:
        st.session_state.standard_df = pd.DataFrame(columns=['name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status', 'travelTime', 'timeFromPrev' ])

    form_col, standard_col, ada_col = st.columns(3)
    with form_col:
        with st.form(key='form1', clear_on_submit = True):
            st.info('Please update queue with Driver\'s status before adding')
            st.text_input('Name', key = 'name')
            col1, col2 = st.columns(2)
            col1.time_input('Pick Up Time', value = 'now', key = 'reservation')
            col2.selectbox('Num. of People', list(range(1,8)), key='numOfPeople', index = 0)
            st.selectbox('Pick Up Location',marker['Name'], key='pickup', index = None)
            st.selectbox('Drop Off Location',marker['Name'], key='dropoff', index = None)
            st.checkbox('ADA', key = 'ADA')
            submit_button = st.form_submit_button("ADD")
            if submit_button:
                if st.session_state.ADA == True:
                    guest = control.controller(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.ada_df)
                    st.session_state.ada_df = st.session_state['ada_df'].append([guest.to_dict()], ignore_index=True)
                else:
                    guest = control.controller(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.standard_df)
                    st.session_state.standard_df = st.session_state['standard_df'].append([guest.to_dict()], ignore_index=True)
                st.success(f"{guest.name} has been added to queue with a wait time of {guest.waitTime} min(s)")
    with standard_col:
        st.header(':oncoming_taxi: Standard Shuttle')
        edited_df1 = st.data_editor(st.session_state.standard_df, 
                                    hide_index=True, 
                                    num_rows = 'dynamic', 
                                    key = 'df1', 
                                    on_change = onDataChange,
                                    disabled = ('name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople'),
                                    column_order = ('name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status'),
                                    column_config={
                                        'status': st.column_config.SelectboxColumn(
                                            "status",
                                            help = 'What is the Driver doing?',
                                            options=[
                                                'Picking Up',
                                                'Dropping Off'
                                            ],
                                            required = True
                                        )
                                    })
    
    with ada_col:
        ada_col.header(':manual_wheelchair: ADA Shuttle')
        edited_df2 = ada_col.data_editor(st.session_state.ada_df, 
                                    hide_index=True, 
                                    num_rows = 'dynamic', 
                                    key = 'df2', 
                                    on_change = onDataChange,
                                    disabled = ('name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople'),
                                    column_order = ('name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status'),
                                    column_config={
                                        'status': st.column_config.SelectboxColumn(
                                            "status",
                                            help = 'What is the Driver doing?',
                                            options=[
                                                'Picking Up',
                                                'Dropping Off'
                                            ],
                                            required = True
                                        )
                                    })
        #addData()

main()