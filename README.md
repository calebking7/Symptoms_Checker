# Symptom Checker with Drug Info

## Overview
**Symptom Checker** is a basic web-based tool built with Streamlit that enables users to quickly predict minor illnesses based on their selected symptoms. The application leverages a **Decision Tree Classifier** to provide an initial diagnosis, allowing users to gain insights into potential health issues. This tool is a `demo` for a quick self-check.

Check out the live Streamlit App [here](https://symptomschecker.streamlit.app/).

Image from the web:

<img src="https://lh3.googleusercontent.com/pw/AP1GczM16e_4IArohsV0KL6vUvDFab-rbaF6mCduFryDIm9ujVMW2elgKkOVEcWxHZsa5CBROokY-Jr5gRFdLHsMpJmmO9LdGo2CCPrAPivCtRw46oybP0Kl=w2400" alt="alt text" width="800" />

## Features
- **User-friendly Interface:** Easily select symptoms from a list to get a prediction.
- **Accurate Condition Prediction:** Utilizes a trained Decision Tree Classifier model.
- **Drug Information:** Displays related drug options for the predicted condition, sourced from a drug side effects dataset.
- **Responsive Design:** Accessible from any device, whether on mobile or desktop.
- **Error Handling:** Ensures users select symptoms before making a prediction.

## Getting Started

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/kimnguyen2002/Symptoms_Checker.git
   cd Symptoms_Checker
   ```
2. Install the required packages:
  ```bash
  pip install -r requirements.txt
  ```
3. Download the `symptoms_dataset.csv` and `drugs_side_effects.csv` files.
Place these files in the project directory.

### Running the App
Start the Streamlit application by running:
  ```bash
  streamlit run symptoms_checker.py
  ```

## Disclaimer
This project is intended solely for **educational and research purposes**. It is **NOT a substitute for professional medical advice, diagnosis, or treatment**. Results produced by the model should not be used for clinical decision-making or as a definitive diagnostic tool. Always consult a qualified healthcare professional for medical concerns.

## License

This project is licensed under the MIT License.

Feel free to adjust the structure to fit your actual project layout!
