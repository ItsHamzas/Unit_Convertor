# import streamlit as st 

# st.title("Unit convertor")
# st.markdown("### Converts Length, Weight and Time")
# st.write("Welcom! Select a Category,  and enter a value then get the result")

# category = st.selectbox("Choose a Category", ["Length","Weight","Time"])

# def convert_units(category, value,units):
#     if category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value /  0.621371
        
#         elif category =="Weight":
#             if unit == "Kilograms to Pounds":
#                 return value * 2.20462
#             elif unit == "Pounds to Kilograms":
#                 return value /  2.20462
            
#         elif category == "Time":
#                 if unit == "Seconds to Minutes":
#                     return value / 60
#                 elif unit == "Minutes to Seconds":
#                     return value * 60
#                 elif unit == "Minutes to Hours":
#                     return value / 60
#                 elif unit == "Hours to  Minutes":
#                     return value * 60
#                 elif unit == "Days  to Hours":
#                     return value * 24
                
                

#                 if category == "Length":
#                     unit = st.selectbox("Select Conversation",["Miles to kilometers","Kilometers to Miles"])
#                 elif category == "Weight":
#                     unit = st.selectbox("⚖ Select Conversation",["Kilograms to pounds","Pounds to kilograms"])
#                 elif category == "Time":
#                     unit = st.selectbox("⏲ Selrct Conversation",["Seconds to minutes","Minutes to seconds","Minutes to hours","Hours to minutes","Hours to days","Days to hours"])
#                     value = st.number_input("Enter the value to convert")
#                     if st.button("Convert"):
#                         result = convert_units(category,value,unit)
#                         st.success(f"The result is {result:.2f}")

 
                        


import streamlit as st

st.title("Unit convertor")
st.markdown("### Converts Length, Weight and Time")
st.write("Welcom! Select a Category,  and enter a value then get the result")

category = st.selectbox("Choose a Category", ["Length","Weight","Time"])


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Miles to kilometers":
            return value * 1.60934
        elif unit == "Kilometers to Miles":
            return value / 1.60934
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Time"])

if category == "Length":
    unit = st.selectbox("Select Conversion", ["Miles to kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏲ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
