import streamlit as st
import pandas as pd
import base64

# Load the xlsx file into a pandas dataframe
df = pd.read_excel('20230214_data_dictionary_all.xlsx')

# Create a Streamlit app
st.title('AI/QI Data Dictionary Search App')
#st.image("Picture2.jpg", width=300)

# Create a search bar for the user to search for features
search_query = st.text_input("Search for a feature:", key='search')

# Create a dropdown for the user to select a file
file_options = df['File'].unique().tolist()
file_options.insert(0, 'All')
selected_file = st.selectbox("Select a file:", file_options)

# Filter the dataframe based on the user's selections
if search_query:
    filtered_df = df[df['Feature'].str.contains(search_query, case=False)]
else:
    filtered_df = df

if selected_file != 'All':
    filtered_df = filtered_df[filtered_df['File'] == selected_file]

# Display the filtered dataframe
st.dataframe(filtered_df)

#Add a button to download the filtered data as an Excel file
#if not filtered_df.empty:
#    csv = filtered_df.to_csv(index=False)
#   b64 = base64.b64encode(csv.encode()).decode()
#    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download Filtered Features as CSV</a>'
#    st.markdown(href, unsafe_allow_html=True)
#else:
#    st.warning("No data to download.")

# Provide additional information or notes
st.write("Note: This data dictionary is a work in progress. Download filtered Data")
