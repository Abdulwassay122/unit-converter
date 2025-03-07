import streamlit as st

def convert_units(value, unit_from, unit_to):

    converstions = {
        "meter_kilometer":0.001,
        "kilometer_meter":1000,
        "gram_kilogram":0.001,
        "kilogram_gram":1000,

    }

    key = f"{unit_from}_{unit_to}"

    if key in converstions:
        converstion = converstions[key]
        return value * converstion
    else:
        return "Converstion not Supported"
    
st.title("Unit Converter")

value = st.number_input("Enter a value:")

unit_from = st.selectbox("Convert from:", ["meter","kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter","kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")