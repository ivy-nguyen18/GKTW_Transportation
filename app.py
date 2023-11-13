import streamlit as st
import time
import pandas as pd
import control
from database import createTable, addData

createTable()
# Initialize session state with dataframes
# Include initialization of "edited" slots by copying originals
if 'ada_df' not in st.session_state:
    # print('Initializing ada_df')
    st.session_state.ada_df = pd.DataFrame(columns=['name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status', 'travelTime', 'timeFromPrev', 'ADA' ])
    st.session_state.edited_ada_df = st.session_state.ada_df.copy()
if 'standard_df' not in st.session_state:
    # print('Initializing standard_df')
    st.session_state.standard_df = pd.DataFrame(columns=['name', 'waitTime', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status', 'travelTime', 'timeFromPrev', 'ADA' ])
    st.session_state.edited_standard_df = st.session_state.standard_df.copy()

# Save edits by copying edited dataframes to "original" slots in session state
def save_edits():
    st.session_state.ada_df = st.session_state.edited_ada_df.copy()
    st.session_state.standard_df = st.session_state.edited_standard_df.copy()

st.set_page_config(layout="wide")
marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')

st.title(':telephone_receiver: GKTW Dispatcher')
guest = None

form_col, standard_col, ada_col = st.columns(3)
with form_col:
    # print('Going through Forms')
    with st.form(key='form1', clear_on_submit = True):
        st.info('Please update queue with Driver\'s status before adding')
        st.text_input('Name', key = 'name')
        col1, col2 = st.columns(2)
        col1.time_input('Pick Up Time', value = 'now', key = 'reservation')
        col2.selectbox('Num. of People', list(range(1,8)), key='numOfPeople', index = 0)
        st.selectbox('Pick Up Location',marker['Name'], key='pickup', index = None)
        st.selectbox('Drop Off Location',marker['Name'], key='dropoff', index = None)
        st.checkbox('ADA', key = 'ADA')
        submit_button = st.form_submit_button("ADD", on_click=save_edits)
        if submit_button:
            # print('Added someone...')
            if st.session_state.ADA == True:
                guest = control.controller(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.ada_df)
                st.session_state.ada_df = pd.concat([st.session_state.ada_df, pd.DataFrame([guest.to_dict()])], ignore_index=True)
            else:
                guest = control.controller(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.standard_df)
                st.session_state.standard_df = pd.concat([st.session_state.standard_df, pd.DataFrame([guest.to_dict()])], ignore_index=True)
            st.success(f"{guest.name} has been added to queue with a wait time of {guest.waitTime} min(s)")
            # Write to Excel File
            with pd.ExcelWriter('/Users/ivynguyen/Desktop/GKTW_Transportation_Data.xlsx', engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:  
                pd.DataFrame([guest.to_dict()]).to_excel(writer, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, index=False, header=False)

            # Write to SQL DB
            addData(str(guest.name), str(guest.pickup), str(guest.dropoff), str(guest.reservation), str(guest.ADA), str(guest.waitTime), str(guest.numOfPeople))
with standard_col:
    # print('Adding to shuttle')
    st.header(':oncoming_taxi: Standard Shuttle')
    st.session_state.edited_standard_df = st.data_editor(st.session_state.standard_df, 
                                hide_index=True, 
                                num_rows = 'dynamic', 
                                key = 'df1',
                                disabled = ('name', 'reservation','pickup', 'dropoff', 'numOfPeople'),
                                column_order = ('name', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status'),
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
                                }).reset_index(drop = True)

with ada_col:
    ada_col.header(':manual_wheelchair: ADA Shuttle')
    st.session_state.edited_ada_df = ada_col.data_editor(st.session_state.ada_df, 
                                hide_index=True, 
                                num_rows = 'dynamic',
                                key = 'df2',
                                disabled = ('name', 'reservation','pickup', 'dropoff', 'numOfPeople'),
                                column_order = ('name', 'reservation','pickup', 'dropoff', 'numOfPeople', 'status'),
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

