# Import necessary libraries and modules
import streamlit as st
import pandas as pd

# Read in the Excel spreadsheet and create a DataFrame object for each sheet
xlsx = pd.ExcelFile('data_dictionary.xlsx')
data = {}
for sheet_name in xlsx.sheet_names:
    data[sheet_name] = xlsx.parse(sheet_name)

# Create a dictionary object to track the usage of features
feature_tracking = {}

# Create a function that displays the drop-down menu and extracts the data from the selected sheet
def show_data(sheet_name):
    # Extract the data from the selected sheet and display it in the web app
    sheet_data = data[sheet_name].to_html()
    st.write(sheet_data, unsafe_allow_html=True)

# Create a Streamlit app
st.title('AI/QI Data Dictionary Search')

# Add a search bar widget
query = st.text_input('Search for a feature')

# Loop through each tab or sheet in the DataFrame
for sheet_name, df in data.items():
  # Filter the DataFrame based on the search query
  results = data[sheet_name][data[sheet_name]['Feature'].str.contains(query, case=False)]

  # Update the feature tracking dictionary
  for feature in results['Feature']:
      if feature in feature_tracking:
          feature_tracking[feature]['used'] += 1
      else:
          feature_tracking[feature] = {'used': 1, 'not used': 0}

 # Extract the sheet name description from the Description sheet
   # sheet_description = data['Description'][data['Description']['Sheet Name'] == sheet_name]['Description'].values[0]
  # Extract the sheet name description from the Description sheet
  #description_sheet = data['Description']
  #sheet_description = description_sheet.loc[description_sheet['Description'] == sheet_name]['Description'].iloc[0]


  # Display the search results as a table
  if not results.empty:
    st.subheader(sheet_name)
    #st.subheader(sheet_description)
    st.table(results)

# Add drop-down menu for selecting a sheet
sheet_name = st.selectbox('Select a sheet to view all features', list(data.keys()))


# Use Streamlit to create the web app
st.title('Data Table Viewer')

# Display the drop-down menu for selecting a sheet
#sheet_name = st.sidebar.selectbox('Select a sheet', list(data.keys()))

# Display the data from the selected sheet
show_data(sheet_name)