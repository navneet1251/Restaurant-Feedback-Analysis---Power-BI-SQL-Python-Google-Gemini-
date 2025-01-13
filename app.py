import streamlit as st
import google.generativeai as genai
import pymysql
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables
load_dotenv()

# configure Gemini API
genai.configure(
    api_key=os.getenv('GEMINI_API_KEY')
)

# Function to classify feedback using Gemini 
def classify_feedback(feedback):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""Classify the following restaurant feedback into one of these categories: 
    Food Quality, Service(Food Service(serving and waiting time)), Ambience(Lighting), Value for money, hygiene(not proper cleaning), or Overall Experience.
    Only return the classification word.

    Feedback: {feedback}"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to insert data into Sql server
def insert_data(name, phone, rating, feedback, category):
    try:
        conn = pymysql.connect(
            host='127.0.0.1',  # Use your MySQL server IP or hostname
            user='root',        # Your MySQL username
            password='Chunnu@1',  # Your MySQL password
            database='feedback_db'  # Your database name'
        )
        cursor = conn.cursor()
        today = date.today().isoformat()
        cursor.execute(f"""INSERT INTO RestaurantFeedback
                        (Name, PhoneNumber, Rating, Feedback, Category, Date)
                        VALUES ('{name}', '{phone}', '{rating}', '{feedback}', '{category}', '{today}')""")
        conn.commit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        conn.close()

# streamlit app
def main():
    st.title("Jalwa - Customer Feedback")

    st.write(''' 
            Dear Valued Guest,

            Thank you for dining at Jalwa! We hope you enjoyed your experience with us.
            We would love to hear your thoughts to help us serve you better in the future.
            ''')
        
        # get user input
    name = st.text_input("Name (Optional):")
    phone = st.text_input("Phone Number (Optional):")
    rating = st.slider("How would you rate your overall experience?", 1, 5,3)
    feedback = st.text_area("Please share your thoughts about your dining experience:")

    if st.button("Submit Feedback"):
            if feedback:
                #clasify feedback
                category = classify_feedback(feedback)
                
                # insert data into sql 
                insert_data(name if name else "Anonymous",
                             phone if phone else "Not Provided",
                               rating, feedback, category)
                
                st.success("Thank you for your feedback! We appreciate your time.")

                if rating <=2:
                    st.info("We're sorry to hear that you had a bad experience. ")
            else:
                st.warning("Please provide your feedback before submitting.")

if __name__ == '__main__':
    main()
