## Overview
The goal is to predict survival on the Titanic, where `survived` is the target variable indicating if a passenger survived or not. The dataset includes various features related to the passengers.

## Target Variable
- **`survived`**: Indicates if a passenger survived the Titanic disaster.
  - `0` = No, the passenger did not survive.
  - `1` = Yes, the passenger survived.

## Features
The following features are included in the dataset and are used to predict the target variable:

- **`Pclass`**: Ticket class, a proxy for socio-economic status (SES)
  - `1` = 1st Class (Upper)
  - `2` = 2nd Class (Middle)
  - `3` = 3rd Class (Lower)

- **`Name`**: Passenger's name. It includes titles and sometimes family names, which can be used for feature engineering.

- **`Sex`**: Passenger's sex. 
  - `male`
  - `female`

- **`Age`**: Age in years. It is fractional if less than 1 and estimated as xx.5 if it's estimated.

- **`SibSp`**: Number of siblings or spouses aboard the Titanic. Defines family relations in this way:
  - Sibling = brother, sister, stepbrother, stepsister
  - Spouse = husband, wife (mistresses and fiancés were ignored)

- **`Parch`**: Number of parents or children aboard the Titanic. Defines family relations in this way:
  - Parent = mother, father
  - Child = daughter, son, stepdaughter, stepson
  - Some children travelled only with a nanny, therefore Parch=0 for them.

- **`Ticket`**: Ticket number. The format varies, and it might contain letters and numbers.

- **`Fare`**: Passenger fare. It varies depending on class, embarkation point, and sometimes other factors.

- **`Cabin`**: Cabin number. The format varies, and cabins might be shared among passengers.

- **`Embarked`**: Port of Embarkation. Indicates where the passenger boarded the Titanic.
  - `C` = Cherbourg
  - `Q` = Queenstown
  - `S` = Southampton