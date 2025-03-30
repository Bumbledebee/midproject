# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
import pickle
import pandas as pd


# app structure
col1, col2 = st.columns([1,1])
with col1:  
    st.image("images/titanic_main.jpg", width=600)
with col2:
    st.write("The Titanic's tragic sinking on April 15, 1912, resulted in the loss of over 1,500 lives. The ship was equipped with only enough lifeboats for about half of its passengers, a reflection of the era's maritime safety standards. The disaster prompted significant changes in maritime laws and regulations, leading to improved safety measures and protocols to ensure the protection of passengers at sea.")

# tabs
tabs = st.tabs(["Survivability", "Titanic History", "Titanic Today"])

with tabs[0]:
    st.subheader("Survivability Prediction")
    st.write("In this web app you would be able to predict if you would or not survive the sinking of the Titanic")

    # Load the logistic regression model
    model = pickle.load(open('data/logreg_model.pkl', 'rb'))

    st.write("Please adjust the values of the features and the predicted survivability will be displayed.")
    # Collect user input features 
    Gender_input = st.selectbox("Gender", ["Male", "Female"])
    Class_input = st.selectbox("Class", ["First", "Second", "Third"])
    Age_input = st.number_input('Age in Years', min_value=0, max_value=100, value=30)
    Fare_input = st.number_input('Fare in USD', min_value=0, max_value=512, value=15)
    SibSp_input = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, max_value=8, value=0)
    Parch_input = st.number_input('Number of Parents/Children Aboard', min_value=0, max_value=9, value=0)

    # Encode categorical inputs
    Gender_encoded = 1 if Gender_input == "Male" else 0
    if Class_input == "First":
      Class_encoded = 1
    elif Class_input == "Second":
      Class_encoded = 2
    elif Class_input == "Third":
      Class_encoded = 3


    # Prepare input data
    input_data = pd.DataFrame([[Class_encoded,Gender_encoded, Age_input, SibSp_input, Parch_input, Fare_input]], 
                                        columns=['pclass','sex','age', 'sibsp',	'parch','fare'])


    # Predict the output

    if st.button("Predict"):
        prediction = model.predict(input_data)
        print(prediction[0])
        if prediction[0] == "1":
            st.success("Congrats!! You survived!")
        else:
            st.error("You did not survive..... but hey is just a model")

with tabs[1]:
    st.subheader("Titanic Timeline")
    timeline_data = {
  "title": {
    "text": {
      "headline": "History of the Titanic and Harland & Wolff",
      "text": "<p>Explore the pivotal events in the journey of the RMS Titanic and the Harland & Wolff shipyard.</p>"
    }
  },
  "events": [
    {
      "start_date": {
        "year": "1861"
      },
      "text": {
        "headline": "Founding of Harland & Wolff Shipyard",
        "text": "<p>Harland & Wolff was established in 1861 in Belfast, Northern Ireland, and became one of the largest shipbuilders in the world.</p>"
      }
    },
    {
      "start_date": {
        "year": "1909"
      },
      "text": {
        "headline": "Construction of Titanic Begins",
        "text": "<p>Construction of the RMS Titanic began in 1909 at the Harland & Wolff shipyard, alongside its sister ship, the RMS Olympic.</p>"
      }
    },
    {
      "start_date": {
        "year": "1912",
        "month": "4",
        "day": "10"
      },
      "text": {
        "headline": "Titanic Sets Sail",
        "text": "<p>The RMS Titanic set sail from Southampton, UK, embarking on its maiden voyage across the Atlantic to New York City.</p>"
      }
    },
    {
      "start_date": {
        "year": "1912",
        "month": "4",
        "day": "15"
      },
      "text": {
        "headline": "Sinking of the Titanic",
        "text": "<p>RMS Titanic, on its maiden voyage, sinks after hitting an iceberg, causing the deaths of over 1,500 passengers and crew.</p>"
      }
    },
    {
      "start_date": {
        "year": "1912",
        "month": "9",
        "day": "1"
      },
      "text": {
        "headline": "Titanic Inquiry Conclusion",
        "text": "<p>The British inquiry into the Titanic disaster, led by Lord Mersey, concludes, emphasizing recommendations for improved maritime safety.</p>"
      }
    },
    {
      "start_date": {
        "year": "1938",
        "month": "3",
        "day": "17"
      },
      "text": {
        "headline": "Launch of HMS Belfast",
        "text": "<p>Harland & Wolff launches HMS Belfast, which would become one of the most famous Royal Navy ships, now a museum ship in London.</p>"
      }
    },
    {
      "start_date": {
        "year": "1960",
        "month": "5",
        "day": "31"
      },
      "text": {
        "headline": "Launch of MV Arlanza",
        "text": "<p>Harland & Wolff launches the MV Arlanza, signifying the shipyard's continued prominence in shipbuilding post-WWII.</p>"
      }
    },
    {
      "start_date": {
        "year": "2022",
        "month": "1",
        "day": "31"
      },
      "text": {
        "headline": "Museum Opening",
        "text": "<p>The Titanic Belfast museum, opened in 2012, is a state-of-the-art visitor attraction located in the heart of Belfast, Northern Ireland</p>"
      }
    }
  ]
}
    timeline(timeline_data)
with tabs[2]:
    st.subheader("Titanic Aftermath")
    st.write("Despite the tragic incident of the Titanic, the ship's legacy lives on...")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:  # left column
        st.image("images/titanic_workers.jpg", width=400)
        st.write("Harland and Wolff, the Belfast-based shipyard, did indeed continue its operations successfully after the loss of the RMS Titanic. Although the Titanic disaster was a significant tragedy, Harland and Wolff managed to overcome the challenges and maintain its position as a prominent shipbuilder. Here we see a team of workers celebrating the retirement of one of their colleagues in the 60s. The worker on the left is my grandfather.") 
    with col2:  # middle column
        st.image("images/titanic_underwater.jpg", width=400)
        st.write("The wreckage of the Titanic was discovered in 1985, lying about 12,500 feet below the surface of the North Atlantic Ocean. Since then, numerous expeditions have been launched to explore and document the site, revealing artifacts and remnants of the ship's grandeur. Today, the Titanic serves as a poignant reminder of the importance of maritime safety and the human stories intertwined with its history.")
    with col3:  # right column
        st.image("images/titanic_museum.jpg", width=400)
        st.write("The Titanic Belfast museum, opened in 2012, is a state-of-the-art visitor attraction located in the heart of Belfast, Northern Ireland. It tells the story of the Titanic and its place in history, showcasing the ship's construction, its tragic sinking, and its legacy. The museum features interactive exhibits, artifacts, and immersive experiences that allow visitors to learn about the Titanic's story in a modern and engaging way.")