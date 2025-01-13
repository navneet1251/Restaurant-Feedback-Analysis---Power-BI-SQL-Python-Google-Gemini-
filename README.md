# Jalwa - Restaurant Feedback Analysis 

## 📋 Project Overview
The **Jalwa - Restaurant Feedback System** is a web-based application designed to collect, classify, and store customer feedback for a restaurant. The system uses AI to categorize feedback into predefined categories such as Food Quality, Service, Ambience, Value for Money, Hygiene, and Overall Experience. The collected feedback is stored in a MySQL database, and the insights are visualized using a Power BI dashboard.

---

## 🛠️ Tech Stack
- **Streamlit**: For building the web application interface
- **Google Gemini API**: For AI-driven feedback classification
- **MySQL**: For storing feedback data
- **Power BI**: For creating interactive dashboards to showcase insights
- **pymysql**: For connecting Streamlit with MySQL
- **dotenv**: For managing environment variables

---

## ⚙️ Features
- **User-Friendly Interface**: Allows customers to easily submit feedback
- **AI-Powered Feedback Classification**: Uses Google Gemini API to categorize feedback into predefined categories
- **Secure Data Storage**: Stores feedback in a MySQL database
- **Data Visualization**: Power BI dashboard for displaying feedback trends and insights

---

## 🧩 Project Structure
```
jalwa-feedback-system
├── app.py                # Main Streamlit app file
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables file
└── README.md             # Project documentation
```

---

## 🚀 How to Set Up the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/jalwa-feedback-system.git
cd jalwa-feedback-system
```

### 2️⃣ Create a Virtual Environment
```bash
# For Windows
python -m venv env
env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📊 Power BI Dashboard
The collected feedback is visualized using a Power BI dashboard, providing stakeholders with actionable insights into customer experiences. The dashboard includes:
- **Feedback Category Distribution**
- **Average Ratings Over Time**
- **Sentiment Analysis**
- **Category-Wise Feedback Trends**

---

## 📈 Results & Impact
- **Improved Customer Experience**: Identified key areas of improvement based on customer feedback.
- **Data-Driven Decision Making**: Enabled the restaurant to make informed decisions to enhance service quality.
- **Efficient Feedback Management**: Reduced manual efforts in categorizing and analyzing feedback.

---




