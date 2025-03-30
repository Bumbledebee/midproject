# Midproject

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Steps](#steps)
- [Findings](#findings)
- [Conclusions](#conclusions)
- [Presentation](#presentation)
- [Streamlit](#streamlit)

## Project Overview
This project is part of the Ironhack curriculum and focuses on trying out machine learning methods on an example data set.

## Features
The example dataset is one from the Titanic passengers and
the dataset includes the following important columns:
- **Pclass**: The class of the ticket purchased (1 = First, 2 = Second, 3 = Third).
- **Name**: The full name of the passenger.
- **Sex**: The gender of the passenger (male or female).
- **Age**: The age of the passenger in years.
- **SibSp**: The number of siblings or spouses aboard the Titanic.
- **Parch**: The number of parents or children aboard the Titanic.
- **Ticket**: The ticket number.
- **Fare**: The fare paid for the ticket.
- **Cabin**: The cabin number (if available).
- **Embarked**: The port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
- **Boat**: The lifeboat number (if the passenger was assigned one).
- **Body**: The body identification number (if applicable).
- **Home.Dest**: The intended home destination of the passenger (if available).

The target column:
- **Survived**: Indicates whether the passenger survived (1) or not (0).

For machine learning a target column is needed. If the target column in categorical - in this case even binary - then we use a classification model.

## Technologies Used
- **Programming Languages**: [Python]
- **Frameworks**: [Streamlit]

## Steps
1. The data has been taken from this website: [OpenML Titanic Dataset](https://www.openml.org/search?type=data&sort=runs&id=40945&status=active)
2. The data got checked and cleaned from empty values, empty strings and duplicated rows.
3. Then I started applying three different classification models with different versions of the dataframe (e.g. more or less columns) and different machine learning data manipulation tactics (e.g. scaling_standard, scaling_minmax, smote, tomek_links). I decided to focus on "accuracy" as my main performance KPI and collect that data in a dataframe.

## Findings
The models work better with less columns (e.g. one hotfix encoding for title or embarked is not worth it, as well mapping the few available cabins to nominal encoding as most cabin information is missing).
Furthermore, logistic regression and GradientBoostingClassifier worked best, KNearestNeighbor did not work too well.

## Conclusions
Mainly this project brought me a step ahead in having functions for EDA (Exploratory Data Analysis), Cleaning and Plotting.
For Machine learning to compare different dataframes and different data manipulations methods there is still more room to create more functions and optimise the process.


## Presentation
Check the presentation folder for my learnings while doing this project.

## Streamlit
The project includes a streamlit webapp. You can run it locally with "streamlit run streamlit.py". The app features a picture of my grandfather who worked in Harland and Wolff in the 1960s.
