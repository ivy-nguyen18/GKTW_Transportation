import streamlit as st
import pandas as pd
import control
from database import createTable, addData, repopulateTable
from datetime import datetime 
from PIL import Image

st.set_page_config(layout = 'wide')
image = Image.open('GKTW.png')
st.image(image, width = 200)
createTable()

# Initialize session state with dataframes
if 'ada_df' not in st.session_state:
    # print('Initializing ada_df')
    df = repopulateTable(str(datetime.today().strftime('%m/%d/%Y')), 'True')
    st.session_state.ada_df = pd.DataFrame(df, columns=['name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople', 'ADA' ])
    st.session_state.edited_ada_df = st.session_state.ada_df.copy()
if 'standard_df' not in st.session_state:
    # print('Initializing standard_df')
    df = repopulateTable(str(datetime.today().strftime('%m/%d/%Y')), 'False')
    st.session_state.standard_df = pd.DataFrame(df, columns=['name', 'res_date','res_time','pickup', 'dropoff', 'numOfPeople', 'ADA' ])
    st.session_state.edited_standard_df = st.session_state.standard_df.copy()

# Save edits by copying edited dataframes to "original" slots in session state
def save_edits():
    st.session_state.ada_df = st.session_state.edited_ada_df.copy()
    st.session_state.standard_df = st.session_state.edited_standard_df.copy()

marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')

st.title(':telephone_receiver: GKTW Shuttle Dispatcher (Reservation Ver.)')
guest = None

form_col, standard_col, ada_col = st.columns(3)
with form_col:
    # print('Going through Forms')
    with st.form(key='form1', clear_on_submit = True):
        st.text_input('Name', key = 'name')
        col1, col2, col3 = st.columns(3)
        col1.date_input('Pick Up Date', value = 'today',format="MM/DD/YYYY", key = 'date')
        col2.time_input('Pick Up Time', value = 'now', key = 'reservation')
        col3.selectbox('Num. of People', list(range(1,8)), key='numOfPeople', index = 0)
        st.selectbox('Pick Up Location',marker['Name'], key='pickup', index = None)
        st.selectbox('Drop Off Location',marker['Name'], key='dropoff', index = None)
        st.checkbox('ADA', key = 'ADA')
        submit_button = st.form_submit_button("ADD", on_click=save_edits)
        if submit_button:
            # print('Added someone...')
            if st.session_state.ADA == True:
                guest = control.getInputs(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.date)
                st.session_state.ada_df = pd.concat([st.session_state.ada_df, pd.DataFrame([guest.to_dict()])], ignore_index=True).sort_values(by=['res_date','res_time']).reset_index(drop = True)
            else:
                guest = control.getInputs(st.session_state.name, st.session_state.reservation, st.session_state.numOfPeople, st.session_state.pickup, st.session_state.dropoff, st.session_state.ADA, st.session_state.date)
                st.session_state.standard_df = pd.concat([st.session_state.standard_df, pd.DataFrame([guest.to_dict()])], ignore_index=True).sort_values(by=['res_date','res_time']).reset_index(drop = True)
            st.success(f"{guest.name} has been added to queue!")
            # Write to Excel File
            with pd.ExcelWriter('GKTW_Transportation_Data_Res.xlsx', engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:  
                pd.DataFrame([guest.to_dict()]).to_excel(writer, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, index=False, header=False)

            # Write to SQL DB
            addData(str(guest.name), str(guest.res_date),str(guest.res_time), str(guest.pickup), str(guest.dropoff), str(guest.ADA), str(guest.numOfPeople))
with standard_col:
    # print('Adding to shuttle')
    st.header(':oncoming_taxi: Standard Shuttle')
    st.session_state.edited_standard_df = st.data_editor(st.session_state.standard_df, 
                                hide_index=True, 
                                num_rows = 'dynamic', 
                                key = 'df1',
                                disabled = ('name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople'),
                                column_order = ('name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople'),
                            )

with ada_col:
    ada_col.header(':manual_wheelchair: ADA Shuttle')
    st.session_state.edited_ada_df = ada_col.data_editor(st.session_state.ada_df, 
                                hide_index=True, 
                                num_rows = 'dynamic',
                                key = 'df2',
                                disabled = ('name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople'),
                                column_order = ('name', 'res_date', 'res_time','pickup', 'dropoff', 'numOfPeople')
                            )