# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline


# app structure
col1, col2, col3 = st.columns([1,2,1])
with col2:  # middle column
    st.image("Titanic_workers.jpg", width=400) # logo
    
# tabs
tabs = st.tabs(["Titanic History", "Titanic Dataset", "Titanic Analysis"])

with tabs[0]:
    st.title("Titanic built by Harland and Wolff")
    st.write("Harland and Wolff shipyard in Belfast, founded in 1861, quickly established itself as a leading shipbuilding entity in the maritime industry. Renowned for its innovative engineering and monumental constructions, the shipyard became globally recognized for its role in crafting the Olympic-class ocean liners for the White Star Line, including the ill-fated RMS Titanic. Here we see a team of workers celebrating the retirement of one of their colleagues in the 60s, a testament to the enduring legacy and community embodied by Harland and Wolff.")
    st.write("Source: [Wikipedia](https://en.wikipedia.org/wiki/RMS_Titanic)")
    st.write("Timeline of Titanic History")
    timeline_data = {
  "title": {
    "text": {
      "headline": "Significant Events in Titanic's History",
      "text": "<p>Key milestones in the construction and history of the RMS Titanic.</p>"
    }
  },
  "events": [
    {
      "start_date": {
        "year": "1909",
        "month": "3",
        "day": "31"
      },
      "text": {
        "headline": "Construction of Titanic Begins",
        "text": "<p>Construction on the RMS Titanic, the largest ship afloat at the time, began at the Harland and Wolff shipyard in Belfast.</p>"
      }
    },
    {
      "start_date": {
        "year": "1911",
        "month": "5",
        "day": "31"
      },
      "text": {
        "headline": "Titanic Launched",
        "text": "<p>The RMS Titanic was launched, marking a significant moment in maritime history.</p>"
      }
    },
    {
      "start_date": {
        "year": "1912",
        "month": "4",
        "day": "2"
      },
      "text": {
        "headline": "Titanic Begins Sea Trials",
        "text": "<p>The Titanic began its sea trials in the Irish Sea before its maiden voyage.</p>"
      }
    },
    {
      "start_date": {
        "year": "1912",
        "month": "4",
        "day": "15"
      },
      "text": {
        "headline": "Titanic Strikes Iceberg and Sinks",
        "text": "<p>The Titanic collided with an iceberg and sank in the North Atlantic Ocean, leading to a tragic loss of life.</p>"
      }
    },
    {
      "start_date": {
        "year": "1985",
        "month": "9",
        "day": "1"
      },
      "text": {
        "headline": "Titanic Wreck Discovered",
        "text": "<p>The wreck of the Titanic was discovered on the ocean floor, more than 70 years after it sank.</p>"
      }
    }
  ]
}
    timeline(timeline_data)
with tabs[1]:
    print("tbd")
with tabs[2]:
    print("tbd")