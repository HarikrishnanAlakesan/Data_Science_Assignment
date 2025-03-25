# **Heart Disease Prediction Using Machine Learning**  

## **Overview**  
This project aims to predict the presence of heart disease using machine learning techniques. The model is built using a dataset containing patient health records, and it classifies individuals as having heart disease or not based on various medical parameters.  

## **Dataset**  
- The dataset contains attributes like **Age, Sex, Cholesterol, Resting Blood Pressure, Max Heart Rate, Exercise Angina, ST Slope**, and more.  
- It is sourced from a publicly available heart disease dataset.  

## **Implementation Steps**  
1. **Data Preprocessing:**  
   - Encoding categorical variables  
   - Standardizing numerical features  
   - Handling missing values (if any)  
2. **Model Training:**  
   - Used **Random Forest Classifier** due to its efficiency in classification tasks.  
   - Split data into **80% training and 20% testing**.  
3. **Evaluation:**  
   - Achieved an **accuracy of 88.04%**.  
   - Visualized feature correlations using **Matplotlib**.  
4. **User Interface:**  
   - Built a **Tkinter-based GUI** for users to input health parameters and get real-time predictions.  

## **Technologies Used**  
- **Programming Language:** Python  
- **Libraries:**  
  - Pandas (Data Processing)  
  - Scikit-learn (Machine Learning)  
  - Matplotlib (Visualization)  
  - Tkinter (GUI)  

## **How to Run the Project**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/HarikrishnanAlakesan/Data_Science_Assignment.git  
   ```
2. Navigate to the project directory:  
   ```sh
   cd Data_Science_Assignment  
   ```
3. Install dependencies:  
   ```sh
   pip install -r requirements.txt  
   ```
4. Run the application:  
   ```sh
   python heart_disease_prediction.py  
   ```
5. Enter the required details in the **Tkinter GUI** to get a prediction.  

## **Results**  
- **Model Accuracy:** 88.04%  
- **Key Insights:**  
  - Age, Cholesterol, and Maximum Heart Rate play a major role in prediction.  
  - Feature importance was analyzed using visualization techniques.  

## **Contributors**  
- **Harikrishnan Alakesan** ([@HarikrishnanAlakesan](https://github.com/HarikrishnanAlakesan))  

## **GitHub Repository**  
🔗 [**Click Here to Access the Repository**](https://github.com/HarikrishnanAlakesan/Data_Science_Assignment)  

## **Screen Recording**  
🎥 https://drive.google.com/drive/folders/1zKgeLb-H6tSEPiva5f19NmkJ1u-fjgfG?usp=sharing
