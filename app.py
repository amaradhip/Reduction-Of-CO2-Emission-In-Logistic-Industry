import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

model = pickle.load(open('C:/Users/91913/model.pkl', 'rb'))
scalar = pickle.load(open('C:/Users/91913/scaling.pkl','rb'))

#@app.route('/')
def welcome():
    return "Welcome All"




def main():
    st.title("Overall Emission")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Overall Emission ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Year = st.text_input("Year","Type Here")
    Jet_Fuel_avi_BTU = st.text_input("Jet_Fuel_avi_BTU","Type Here")
    Gasoline_avi_BTU = st.text_input("Gasoline_avi_BTU","Type Here")
    LDV_SWB_road_BTU = st.text_input("LDV_SWB_road_BTU","Type Here")
    LDV_LWB_road_BTU = st.text_input("LDV_LWB_road_BTU","Type Here")
    Combination_Truck_road_BTU = st.text_input("Combination_Truck_road_BTU","Type Here")
    Bus_Road_BTU = st.text_input("Bus_Road_BTU","Type Here")
    Passenger_Car_EFF = st.text_input("Passenger_Car_EFF","Type Here")
    Passenger_Car_Age = st.text_input("Passenger_Car_Age","Type Here")
    Demand_petroleum_transportation = st.text_input("Demand_petroleum_transportation","Type Here")
    Average_MC = st.text_input("Average_MC","Type Here")
    CO2_emission_million_metric_tons = st.text_input("CO2_emission_million_metric_tons","Type Here")
    CO_emission_million_shots_tons = st.text_input("CO_emission_million_shots_tons","Type Here")
    NOx_emission_million_shots_tons = st.text_input("NOx_emission_million_shots_tons","Type Here")
    SOx_emission_million_shots_tons = st.text_input("SOx_emission_million_shots_tons","Type Here")
    Volatile_compound_million_shots_tons = st.text_input("Volatile_compound_million_shots_tons","Type Here")
    
    result=''
    if st.button("Predict"):
        result = scalar.transform([[Year, Jet_Fuel_avi_BTU, Gasoline_avi_BTU, LDV_SWB_road_BTU, LDV_LWB_road_BTU, Combination_Truck_road_BTU, Bus_Road_BTU, Passenger_Car_EFF, Passenger_Car_Age, Demand_petroleum_transportation, Average_MC, CO2_emission_million_metric_tons, CO_emission_million_shots_tons, NOx_emission_million_shots_tons, SOx_emission_million_shots_tons, Volatile_compound_million_shots_tons]])
        result=model.predict(result)
    st.success('The overall emission is {}'.format(result))
    
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
