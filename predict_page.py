from re import A
from jinja2 import TemplateSyntaxError
import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('BernoulliNB.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

BernoulliNB = data["model"]

def show_predict_page():
    st.title("DIABETES PREDICTION TEST")

    st.write("""### Please Enter the details """)

    age_groups = ("18-24", 
                  "25-29", 
                  "30-34", 
                  "35-39", 
                  "40-44", 
                  "45-49", 
                  "50-54", 
                  "55-59", 
                  "60-64", 
                  "65-69", 
                  "70-74", 
                  "75-79",
                  "80 =< ")

    income_groups = ('less than $10,000',
                     'less than $15,000',
                     'less than $20,000',
                     'less than $25,000',
                     'less than $30,000',
                     'less than $35,000',
                     'less than $50,000',
                     'less than $60,000',
                     'more than $75,000',)
                     
    edu_groups = ('Never attended school or only kindergarten',
                  'Grades 1 through 8 (Elementary)',
                  'Grades 9 through 11 (Some high school)',
                  'Grade 12 or GED (High school graduate)',
                  'College 1 year to 3 years (Some college or technical school)',
                  'College 4 years or more (College graduate)')

    HighBP = st.radio("1. Do you have High Blood Pressure ?", ('Yes', 'No'))
    HighCol = st.radio("2. Do you have High Cholesterol ?", ('Yes', 'No'))
    CholCheck = st.radio("3. Have you check your Cholesterol level in last 5 years?", ('Yes', 'No'))
    Bmi = st.number_input('BMI', min_value = 9.0, max_value = 70.0)
    Smoker = st.radio("5. Are you a Smoker?", ('Yes', 'No'))
    Stroke = st.radio("6. Did you eve had a Stroke?", ('Yes', 'No'))
    HeartDiseaseorAttack = st.radio("7. Heart Disease or Had Heart Attacks?", ('Yes', 'No'))   
    PhysActivity = st.radio("8. Have you engage in any Physical Activities in past 30 days?", ('Yes', 'No'))   
    Fruits = st.radio("9. Do you consume Fruit 1 or more times per day", ('Yes', 'No'))   
    Veggies = st.radio("10. Do you consume Veggies 1 or more times per day", ('Yes', 'No'))
    HvyAlcoholConsump = st.radio("11. Heavy alcohol consumption", ('Yes', 'No')) 
    GenHlth = st.radio("12. General health", ('Yes', 'No'))
    MentHlth = st.slider("13. MentHlth (1-30)", 0, 30, 10)  
    PhysHlth = st.slider("14. PhysHlth (1-30)", 0, 30, 10) 
    DiffWalk = st.radio("15. Difficulty to walking?", ('Yes', 'No')) 
    Sex = st.selectbox("16. What is your gender?", ('Male', 'Female')) 
    Age = st.selectbox("17. What is your age Category?", age_groups) 
    Income = st.selectbox("18. What is your income range?", income_groups) 
    Education = st.selectbox("19. What is your Education level ?", edu_groups) 


    ok = st.button("See the Prediction")

    def convert_sex(argument):
            if argument == 'Male':
                return 1
            elif argument == 'Female':
                return 0   
        
    Sex = convert_sex(Sex)

    def convert_age(argument):

            if argument == '18-24':
                return 1.0
            elif argument == '25-29':
                return 2.0
            elif argument == '30-34':
                return 3.0
            elif argument == '35-39':
                return 4.0
            elif argument == '40-44':
                return 5.0
            elif argument == '45-49':
                return 6.0
            elif argument == '50-54':
                return 7.0
            elif argument == '55-59':
                return 8.0
            elif argument == '60-64':
                return 9
            elif argument == '65-69':
                return 10.0
            elif argument == '70-74':
                return 11.0
            elif argument == '75-79':
                return 12.0
            else:
                return 13.0

    Age = convert_age(Age)

    def convert_income(argument):
            if argument == 'less than $10,000':
                return 1.0
            elif argument == 'less than $15,000':
                return 2.0
            elif argument == 'less than $20,000':
                return 3.0
            elif argument == 'less than $25,000':
                return 4.0
            elif argument == 'less than $35,000':
                return 5.0
            elif argument == 'less than $50,000':
                return 6.0
            elif argument == 'less than $60,000':
                return 7.0
            elif argument == 'less than $75,000':
                return 8.0

    Income = convert_income(Income)

    def convert_edu(argument):
            if argument == 'Never attended school or only kindergarten':
                return 1.0
            elif argument == 'Grades 1 through 8 (Elementary)':
                return 2.0
            elif argument == 'Grades 9 through 11 (Some high school)':
                return 3.0
            elif argument == 'Grade 12 or GED (High school graduate)':
                return 4.0
            elif argument == 'College 1 year to 3 years (Some college or technical school)':
                return 5.0
            elif argument == 'College 4 years or more (College graduate)':
                return 60.

    Education = convert_edu(Education)

    def trans_binary(item):
            if item == 'Yes':
                item = 1.0
                return item
            elif item == 'No':
                item = 0.0
                return item                             
            else:
                item = float(item)
                return item


    if ok:
        # binary_set = ('HighBP', 'HighCol', 'ColCheck', 'Smoker', 'HeartDisease', 'PhysActivities', 'Fruit', 'Veggies', 'HeavyAlcoCon', 'Genhealth', 'Diffwalk')
        
        var_set = (HighBP, HighCol, CholCheck, Bmi, Smoker, Stroke,
                   HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
                   HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth, DiffWalk,
                   Sex, Age, Education, Income)


        updated_list = list()

        
        for i in var_set:
            updated_list.append(trans_binary(i))

        # test = [0,0,1,47.51,1,1,1,1,1,1,0,0,25,25,0,1,1,6,6,]        
        # X = np.array([test])

        X = np.array([updated_list])
        
        diabetes = BernoulliNB.predict(X)

        if diabetes[0] == 0:
            st.subheader('You are at low risk of having DIABETES')
        elif diabetes[0] == 1:
            st.subheader('You are at high risk of having PRE DIABETES')
        elif diabetes[0] == 2:
            st.subheader('You are at high risk of having DIABETES')