# Midproject: Cloud & GenAI

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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
The target columns to predict is:
- **Survived**: Indicates whether the passenger survived (1) or not (0).


## Technologies Used
- **Programming Languages**: [Python]
- **Frameworks**: [Streamlit]

## Setup Instructions
1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/midproject.git
  ```
2. Navigate to the project directory:
  ```bash
  cd midproject
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Set up environment variables:
  - Create a `.env` file and add necessary keys (e.g., API keys, cloud credentials).

5. Run the application:
  ```bash
  streamlit run streamlit.py
  ```

## Usage
1. Access the application via your browser at `http://localhost:5000`.
2. Follow the on-screen instructions to interact with the web app.

## Presentation
Check the presentation folder for my learnings while doing this project.

## License
This project is licensed under the [MIT License](LICENSE).
