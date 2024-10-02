from email import header
import streamlit as st
import pandas as pd
import joblib
import pandas as pd

st.title("HI, Welcome To Vedachat")
st.markdown("---")
st.subheader("व्यायामात् लभते स्वास्थ्यं दीर्घायुष्यं बलं सुखं। आरोग्यं परमं भाग्यं स्वास्थ्यं सर्वार्थसाधनम्॥")
st.markdown("---")
st.header("Balancing Pitta, Guiding Wellness: Your Ayurvedic Companion")
st.image("intro.jpeg")
st.text("Vata is characterized by the mobile nature of Wind (Air) energy.")
st.text("Pitta embodies the transformative nature of Fire energy.")
st.text("And Kapha reflects the binding nature of Water energy.")
st.markdown("---")

data = {
    'Age': None,
    'Gender': None,
    'fluctuation': None,
    'HAIR': None,
    'FINGERS': None,
    'LIPS': None,
    'TEETH': None,
    'High energy level': None,
    'Low energy level': None,
    'Both energy level': None,
    'Low appetite': None,
    'High appetite': None,
    'Moderate appetite': None,
    'Weak digestion': None,
    'Bad digestion': None,
    'Good digestion': None,
    'Deeper sleep': None,
    'Light sleep': None,
    'Moderate sleep': None,
    'Dry skin': None,
    'Oily skin': None,
    'Moderate skin': None,
    'COURAGE': None,
    'ENTHUSIAM': None,
    'LEARN QUICK': None,
    'FORGETQUICK': None,
    'SENTIMENTAL': None,
    'PROTECTIVE': None,
    'Quickly angry': None,
    'Not easily angry': None,
    'No anger': None,
    'ANXIETY': None,
    'RESTLESS': None,
    'MOTIVATED': None,
    'STABLE , CALM': None,
    'COLD HAND': None,
    'COLD FEET': None,
    'CATCHS COLD': None,
    'WARM': None
}

age = st.number_input("Age", value=0)
data['Age'] = age

gender = st.selectbox("Gender", ['M', 'F'])
data['Gender'] = gender

fluctuation = st.selectbox("Fluctuation", ['EASY', 'MEDIUM', 'HARD', None])
data['fluctuation'] = fluctuation


traits = {
    'HAIR': "What is your hair type?",
    'FINGERS': "What is the thickness of your fingers?",
    'LIPS': "What is the condition of your lips?",
    'TEETH': "What is the brightness of your teeth?",
    'High energy level': "Do you have a high energy level?",
    'Low energy level': "Do you have a low energy level?",
    'Both energy level': "Do you have both high and low energy levels?",
    'Low appetite': "Do you have a low appetite?",
    'High appetite': "Do you have a high appetite?",
    'Moderate appetite': "Do you have a moderate appetite?",
    'Weak digestion': "Do you have weak digestion?",
    'Bad digestion': "Do you have bad digestion?",
    'Good digestion': "Do you have good digestion?",
    'Deeper sleep': "Do you experience deep sleep?",
    'Light sleep': "Do you experience light sleep?",
    'Moderate sleep': "Do you experience moderate sleep?",
    'Dry skin': "Do you have dry skin?",
    'Oily skin': "Do you have oily skin?",
    'Moderate skin': "Do you have moderate skin?",
    'COURAGE': "Are you courageous?",
    'ENTHUSIAM': "Are you enthusiastic?",
    'LEARN QUICK': "Do you learn quickly?",
    'FORGETQUICK': "Do you forget quickly?",
    'SENTIMENTAL': "Are you sentimental?",
    'PROTECTIVE': "Are you protective?",
    'Quickly angry': "Do you get angry quickly?",
    'Not easily angry': "Are you not easily angered?",
    'No anger': "Do you not experience anger?",
    'ANXIETY': "Do you experience anxiety?",
    'RESTLESS': "Are you restless?",
    'MOTIVATED': "Are you motivated?",
    'STABLE , CALM': "Are you stable and calm?",
    'COLD HAND': "Do you have cold hands?",
    'COLD FEET': "Do you have cold feet?",
    'CATCHS COLD': "Do you catch cold easily?",
    'WARM': "Are you warm?"
}

for i, (trait, question) in enumerate(traits.items(), start=1):
    st.write(f"{i}. {question}")
    if trait == 'LIPS':
        value_dry = st.checkbox(f"{i}. Dry " + trait)
        value_smooth = st.checkbox(f"{i}. Smooth " + trait)
        value_medium = st.checkbox(f"{i}. Medium " + trait)
        if value_dry:
            data[trait] = "DRY"
        elif value_smooth:
            data[trait] = "SMOOTH"
        elif value_medium:
            data[trait] = "MEDIUM"
        else:
            data[trait] = None
    elif trait == 'TEETH':
        value_bright = st.checkbox(f"{i}. Bright " + trait)
        value_pale = st.checkbox(f"{i}. Pale " + trait)
        value_medium = st.checkbox(f"{i}. Medium " + trait)
        if value_bright:
            data[trait] = "BRIGHT"
        elif value_pale:
            data[trait] = "PALE"
        elif value_medium:
            data[trait] = "MEDIUM"
        else:
            data[trait] = None
    elif trait in ['HAIR', 'FINGERS']:
        value_thin = st.checkbox(f"{i}. Thin " + trait)
        value_medium = st.checkbox(f"{i}. Medium " + trait)
        value_thick = st.checkbox(f"{i}. Thick " + trait)
        if value_thin:
            data[trait] = "THIN "
        elif value_medium:
            data[trait] = "MEDIUM "
        elif value_thick:
            data[trait] = "THICK "
        else:
            data[trait] = None
    else:
        value_yes = st.checkbox(f"{i}. Yes " + trait)
        value_no = st.checkbox(f"{i}. No " + trait)
        if value_yes:
            data[trait] = "Y"
        elif value_no:
            data[trait] = "N"
        else:
            data[trait] = None
            
loaded_model = joblib.load(r'random_forest_model.pkl')

user_data = {}

column_names = [
    'Age', 'Gender_F', 'Gender_M', 'fluctuation_DIFFICULT', 'fluctuation_EASY',
    'fluctuation_HARD', 'HAIR_MEDIUM', 'HAIR_THICK', 'HAIR_THIN', 'FINGERS_MEDIUM',
    'FINGERS_THICK', 'FINGERS_THIN', 'LIPS_DRY', 'LIPS_MEDIUM', 'LIPS_SMOOTH',
    'TEETH_BRIGHT', 'TEETH_MEDIUM', 'TEETH_PALE', 'High energy level_N',
    'High energy level_Y', 'Low energy level_N', 'Low energy level_Y',
    'Both energy level_N', 'Both energy level_Y', 'Low appetite_N', 'Low appetite_Y',
    'High appetite_N', 'High appetite_Y', 'Moderate appetite_N', 'Moderate appetite_Y',
    'Weak digestion_N', 'Weak digestion_Y', 'Bad digestion_N', 'Bad digestion_Y',
    'Good digestion_N', 'Good digestion_Y', 'Deeper sleep_N', 'Deeper sleep_Y',
    'Light sleep_N', 'Light sleep_Y', 'Moderate sleep_N', 'Moderate sleep_Y',
    'Dry skin_N', 'Dry skin_Y', 'Oily skin_N', 'Oily skin_Y', 'Moderate skin_N',
    'Moderate skin_Y', 'COURAGE_N', 'COURAGE_Y', 'ENTHUSIAM_N', 'ENTHUSIAM_Y',
    'LEARN QUICK_N', 'LEARN QUICK_Y', 'FORGETQUICK_N', 'FORGETQUICK_Y',
    'SENTIMENTAL_N', 'SENTIMENTAL_Y', 'PROTECTIVE_N', 'PROTECTIVE_Y',
    'Quickly angry_N', 'Quickly angry_Y', 'Not easily angry_N', 'Not easily angry_Y',
    'No anger_N', 'No anger_Y', 'ANXIETY_N', 'ANXIETY_Y', 'RESTLESS_N', 'RESTLESS_Y',
    'MOTIVATED_N', 'MOTIVATED_Y', 'STABLE , CALM_N', 'STABLE , CALM_Y',
    'COLD HAND_N', 'COLD HAND_Y', 'COLD FEET_N', 'COLD FEET_Y',
    'CATCHS COLD_N', 'CATCHS COLD_Y', 'WARM_N', 'WARM_Y'
]

for column_name in column_names:
    if column_name == 'Age':
        user_data[column_name] = data.get(column_name, 0)
    else:
        key = column_name.split('_')[0]
        value = 1 if data.get(key, None) == column_name.split('_')[1] else 0
        user_data[column_name] = value

sample_data_df = pd.DataFrame([user_data])

prediction = loaded_model.predict(sample_data_df)


# st.write("User data:")
# st.write(data)


st.markdown("---")

st.write("\nAnalysis : ")

if prediction[0][0]=='Y':
        st.write("It seem that you have VATA")
if prediction[0][1]=='Y':
        st.write("It seem that you have PITTA")
if prediction[0][2]=='Y':
        st.write("It seem that you have KAPHA")
        


st.markdown("---")


st.image("image.jpg")

st.text('''-If you have vata dosha
        Your build is likely to be thin and lanky, and your mind is very active. 
        You enjoy trying out anything new, whether it’s an unusual recipe or an undiscovered holiday destination. 
        When imbalanced, you tend to get anxious and shy away from commitment.
        Insomnia and low immunity tend to crop up as common problems too.
        It’s important to restore balance within your sleep cycle and eating habits, which tend to fluctuate because of the influence of the element of air.
        Add a pinch of Arqa Katuki herbs to your morning glass of juice to detoxify your liver, or try mixing a bunch of Arqa Ashwagandha in your drinking water to rejuvenate your body.''')
st.text('''-If you have pitta dosha
        You are likely to be described as strong, fiery and intense as you are dominated by the element of fire. 
        You are a born leader, and enjoy a spot of competition. You like being the first person people come to, whether it’s for the latest music recommendations or straightforward advice. 
        Your skin tends to redden in the sun. When imbalanced, acne and rashes are common problems. Try immersing one teaspoon of Arqa Shatavari herbs in milk or water once a day to bring your mind to a calmer state.
        Arqa Yashti Madhu can help increase your vital energy, so chew on a piece or mix a teaspoon with water and drink it once a day.''')
st.text('''-If you have kapha dosha
        You are likely to have an athletic build, and need to exercise regularly to maintain your weight because of your tendency to put on weight.
        The influence of the earth element ensures that you are stable, loyal and compassionate.
        When imbalanced, you might become stubborn, complacent, and resistant to change. Keep your mind open, and decide against that last piece of pizza—your digestive system will thank you for it.
        Try mixing a teaspoon of Arqa Moringa Powder in milk or water to increase your metabolic rate and energy levels.
        You can also add two tablespoons of marigold petals to two cups of water, and boil it down till just one cup remains to benefit from its antiseptic, anti-inflammatory properties.''')
st.markdown("---")
st.image("mudra.jpg")


st.markdown("---")