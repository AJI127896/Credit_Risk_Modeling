import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
#st.set_page_config(page_title="Lauki Finance: Credit Risk Modelling", page_icon="📊")

# Set Page Config
st.set_page_config(page_title="Loan Eligibility Dashboard", page_icon="💰", layout="wide")
st.title("Credit Risk Modelling")

# Apply custom styling
st.markdown(
    """
    <style>
    .big-font { font-size:30px !important; font-weight: bold; color: #4CAF50; }
    .metric-box { text-align: center; background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with an emoji
st.markdown('<p class="big-font">🏦 Loan Eligibility Dashboard</p>', unsafe_allow_html=True)

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["🏠 Basic Info", "📊 Loan Details", "🔎 Credit Profile"])

# **TAB 1: Basic Information**
with tab1:
    st.subheader("👤 Personal Details")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
    with col2:
        income = st.number_input('Annual Income (₹)', min_value=0, value=1200000)

    residence_type = st.radio('Residence Type', ['Owned', 'Rented', 'Mortgage'], horizontal=True)

# **TAB 2: Loan Information**
with tab2:
    st.subheader("💳 Loan Details")
    col1, col2 = st.columns(2)

    with col1:
        loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)
        loan_tenure_months = st.slider('Loan Tenure (Months)', min_value=6, max_value=120, value=36)
    
    with col2:
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

    # Loan-to-Income Ratio Calculation
    loan_to_income_ratio = loan_amount / income if income else 0
    st.metric(label="📊 Loan-to-Income Ratio", value=f"{loan_to_income_ratio:.2f}")

    # Progress Bar for Loan-to-Income Ratio
    st.progress(min(loan_to_income_ratio / 5, 1.0))  # Normalizing it for visual appeal

# **TAB 3: Credit Profile**
with tab3:
    st.subheader("📉 Credit Profile")
    col1, col2 = st.columns(2)

    with col1:
        delinquency_ratio = st.slider('Delinquency Ratio (%)', 0, 100, 30)
        avg_dpd_per_delinquency = st.number_input('Average DPD', min_value=0, value=20)
    
    with col2:
        credit_utilization_ratio = st.slider('Credit Utilization Ratio (%)', 0, 100, 30)
        num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

# **Summary Display**
st.markdown("---")
st.subheader("📜 Summary of Loan Application")

# Displaying summary in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-box">🏠 <br> <b>Residence Type:</b> ' + residence_type + '</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-box">💰 <br> <b>Loan Type:</b> ' + loan_type + '</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-box">📊 <br> <b>Loan Purpose:</b> ' + loan_purpose + '</div>', unsafe_allow_html=True)

# Final Message
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("### 🚀 Thank you for using the Loan Eligibility Dashboard!")
st.success("📌 Your details have been recorded. Now, proceed with the loan evaluation!")



# Button to calculate risk
if st.button('Calculate Risk'):
    # Call the predict function from the helper module
    # print((age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
    #                                             delinquency_ratio, credit_utilization_ratio, num_open_accounts,
    #                                             residence_type, loan_purpose, loan_type))
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    # Display the results
    st.write(f"Deafult Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")

# Footer
# st.markdown('_Project From Codebasics ML Course_')
