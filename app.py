import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from PIL import Image 

# loading in the model to predict on the data 
pickle_in = open('classifier1.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction(num_of_time_greater_than_30_dpd, revolving_utlisation_credit_line, very_high_credit_utilization,
			   num_of_real_estate_loans_or_lines, age, monthly_income_per_credit_line, num_of_open_credit_line_loan,
				high_debt_income_present, debt_ratio, monthly_income, monthly_income_per_dependent,
				num_of_dependents): 

	prediction = classifier.predict( 
		[[num_of_time_greater_than_30_dpd, revolving_utlisation_credit_line, very_high_credit_utilization,
			   num_of_real_estate_loans_or_lines, age, monthly_income_per_credit_line, num_of_open_credit_line_loan,
				high_debt_income_present, debt_ratio, monthly_income, monthly_income_per_dependent,
				num_of_dependents]]) 
	print(prediction) 
	return prediction 
	

# this is the main function in which we define our webpage 
def main(): 
	# giving the webpage a title 
	st.title("Eligible for Credit?") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<div style ="background-color:yellow;padding:13px"> 
	<h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) 
    
	num_of_time_greater_than_30_dpd = st.text_input("Number of Time Greater Than 30 DPD", "Type Here")
	revolving_utlisation_credit_line = st.text_input("Revolving Utilization of Unsecured Lines", "Type Here")
	age = st.text_input("Age", "Type Here")
	num_of_open_credit_line_loan = st.text_input("Number of Open Credit Line or Loans", "Type Here")
	monthly_income_per_credit_line = st.text_input("Monthly Income Per Credit Line", "Type Here")
	num_of_real_estate_loans_or_lines = st.text_input("Number of Real Estate Loans or Lines", "Type Here")
	monthly_income = st.text_input("Monthly Income", "Type Here")
	monthly_income_per_dependent = st.text_input("Monthly Income Per Dependent", "Type Here")
	very_high_credit_utilization = st.text_input("Is credit utilization high?", "Type Here")
	num_of_dependents = st.text_input("Number of Dependents", "Type Here")
	high_debt_income_present = st.text_input("Is High Debt Income Present?", "Type Here")
	debt_ratio = st.text_input("Debt Ratio", "Type Here")
	result =""


	# the below line ensures that when the button called 'Predict' is clicked, 
	# the prediction function defined above is called to make the prediction 
	# and store it in the variable result 
	if st.button("Predict"): 
		result = prediction(num_of_time_greater_than_30_dpd, revolving_utlisation_credit_line, very_high_credit_utilization,
			   num_of_real_estate_loans_or_lines, age, monthly_income_per_credit_line, num_of_open_credit_line_loan,
				high_debt_income_present, debt_ratio, monthly_income, monthly_income_per_dependent,
				num_of_dependents) 
	st.success('The output is {}'.format(result)) 
	
if __name__=='__main__': 
	main() 
