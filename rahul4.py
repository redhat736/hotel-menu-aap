import streamlit as st
import datetime
import webbrowser

# Function to open WhatsApp Web
def open_whatsapp():
    whatsapp_url = "https://web.whatsapp.com/"
    webbrowser.open(whatsapp_url)

st.title("Menu Based Application")

# Display menu options
menu = ["Select an option", "Show Current Date", "Show Calendar", "Open WhatsApp"]
choice = st.selectbox("Choose an option:", menu)

if choice == "Show Current Date":
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write("Current Date and Time:", current_date)

elif choice == "Show Calendar":
    import calendar
    year = st.number_input("Enter Year", value=datetime.datetime.now().year)
    month = st.number_input("Enter Month", min_value=1, max_value=12, value=datetime.datetime.now().month)
    cal = calendar.month(year, month)
    st.text(cal)

elif choice == "Open WhatsApp":
    st.write("Opening WhatsApp Web...")
    open_whatsapp()

else:
    st.write("Please select an option from the menu.")