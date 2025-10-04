import streamlit as st
import sqlite3
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Quotes Forever",
    page_icon="💫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database/data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize session state for quote tracking
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = None
if 'quote_history' not in st.session_state:
    st.session_state.quote_history = []

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Quote of the Day"

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    .quote-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 3rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        color: white;
        position: relative;
    }
    .category-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
    }
    .quote-text {
        font-size: 1.8rem;
        line-height: 1.6;
        margin: 1.5rem 0;
        font-weight: 300;
        font-style: italic;
        text-align: center;
    }
    .author-text {
        text-align: center;
        font-size: 1.2rem;
        margin-top: 2rem;
        opacity: 0.9;
        font-weight: 400;
    }
    .action-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    .sidebar-title {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 400;
    }
    .dropdown-container {
        margin: 1rem 0;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-title">Quotes Forever</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Dropdown navigation
    st.markdown('<div class="dropdown-container">', unsafe_allow_html=True)
    
    page_options = {
        "Quote of the Day": "quote_of_day",
        "Add Quote": "add_quote", 
        "Personal Details": "personal_details",
        "Mood Wise Quotes": "mood_quotes"
    }
    
    selected_page = st.selectbox(
        "Navigate to:",
        list(page_options.keys()),
        index=list(page_options.keys()).index(st.session_state.current_page) if st.session_state.current_page in page_options else 0,
        key="page_navigation"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Update current page in session state
    st.session_state.current_page = selected_page

# Main content based on selected page
if selected_page == "Quote of the Day":
    st.markdown('<div class="main-header">Quote of the Day</div>', unsafe_allow_html=True)
    
    def get_random_quote():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
        quote = cursor.fetchone()
        conn.close()
        return quote
    
    # Display current quote in the professional template
    if st.session_state.current_quote is None:
        st.session_state.current_quote = get_random_quote()
    
    if st.session_state.current_quote:
        quote = st.session_state.current_quote
        
        # Main quote display template
        st.markdown(f"""
        <div class="quote-container">
            <div class="category-badge">{quote['category']}</div>
            <div class="quote-text">"{quote['quote_text']}"</div>
            <div class="author-text">- {quote['author']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
        
        with col2:
            if st.button("Generate New Quote", use_container_width=True, type="primary"):
                st.session_state.current_quote = get_random_quote()
                st.rerun()
        
        with col3:
            if st.button("Add to Favorites", use_container_width=True):
                st.success("Quote added to favorites!")
        
        # Additional information in an expander
        with st.expander("Quote Details"):
            st.write(f"**Category:** {quote['category']}")
            st.write(f"**Inspiration:** {quote['inspiration']}")
            if 'created_date' in quote:
                st.write(f"**Added on:** {quote['created_date']}")

elif selected_page == "Add Quote":
    st.markdown('<div class="main-header">Add New Quote</div>', unsafe_allow_html=True)
    
    with st.form("add_quote_form"):
        quote_text = st.text_area("Quote Text*", placeholder="Enter the inspirational quote here...", height=120)
        author_name = st.text_input("Author Name*", placeholder="Who said this?")
        
        categories = ["Motivation", "Life", "Love", "Success", "Career", "Dreams", "Perseverance", 
                     "Courage", "Opportunity", "Happiness", "Wisdom", "Innovation", "Inspiration"]
        category = st.selectbox("Category*", categories)
        
        inspiration = st.text_area("Inspiration/Context", placeholder="What makes this quote special? When should someone read this?")
        
        submitted = st.form_submit_button("Save Quote", use_container_width=True)
        
        if submitted:
            if quote_text and author_name and category:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO quotes (quote_text, author, category, inspiration)
                    VALUES (?, ?, ?, ?)
                ''', (quote_text, author_name, category, inspiration))
                conn.commit()
                conn.close()
                st.success("Quote added successfully to the database!")
            else:
                st.error("Please fill in all required fields (Quote Text, Author Name, Category)")

elif selected_page == "Personal Details":
    st.markdown('<div class="main-header">Your Personal Details</div>', unsafe_allow_html=True)
    
    with st.form("personal_details_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name*")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email Address*")
        
        with col2:
            profession = st.text_input("Profession")
            feedback = st.text_area("Feedback/Suggestions", placeholder="What do you think about Quotes Forever?")
        
        help_request = st.text_area("How can I help you?", placeholder="Any specific help or guidance you're looking for?")
        
        submitted = st.form_submit_button("Save Details", use_container_width=True)
        
        if submitted:
            if name and email:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, phone, email, profession, feedback, help_request)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, phone, email, profession, feedback, help_request))
                conn.commit()
                conn.close()
                st.success("Your details have been saved successfully! Thank you for sharing.")
            else:
                st.error("Please fill at least Name and Email fields")

elif selected_page == "Mood Wise Quotes":
    st.markdown('<div class="main-header">Get Quotes Based on Your Mood</div>', unsafe_allow_html=True)
    
    with st.form("mood_form"):
        st.subheader("Tell us about your current state:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.radio("You are:", ["Girl", "Boy", "Prefer not to say"])
            age = st.slider("Your Age", 15, 80, 25)
        
        with col2:
            social_life = st.radio("How's your social life going?", ["Good", "Not Good", "Balanced"])
            professional_life = st.radio("How's your professional life?", ["Good", "Struggling", "Balanced"])
        
        current_mood = st.selectbox("How are you feeling right now?", 
                                   ["Happy", "Sad", "Motivated", "Stressed", "Love", "Career-focused"])
        
        submitted = st.form_submit_button("Get Personalized Quote", use_container_width=True)
        
        if submitted:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Convert mood to lowercase for database matching
            mood_lower = current_mood.lower()
            gender_lower = gender.lower() if gender != "Prefer not to say" else "both"
            
            # Query for matching quotes based on user's profile
            cursor.execute('''
                SELECT * FROM mood_quotes 
                WHERE mood_category = ? 
                AND (gender_preference = ? OR gender_preference = 'both')
                AND min_age <= ? AND max_age >= ?
                AND (social_life = ? OR social_life = 'balanced')
                AND (professional_life = ? OR professional_life = 'balanced')
                ORDER BY RANDOM() LIMIT 1
            ''', (mood_lower, gender_lower, age, age, social_life.lower(), professional_life.lower()))
            
            quote = cursor.fetchone()
            conn.close()
            
            if quote:
                st.markdown(f"""
                <div class="quote-container">
                    <div class="category-badge">{current_mood} Mood</div>
                    <div class="quote-text">"{quote['quote_text']}"</div>
                    <div class="author-text">- {quote['author']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Show matching criteria
                st.info(f"Selected for your profile: {current_mood} mood | Age: {age} | Social Life: {social_life} | Professional: {professional_life}")
            else:
                st.warning("No perfect match found. Here's a general inspirational quote:")
                # Fallback to general quote
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
                fallback_quote = cursor.fetchone()
                conn.close()
                
                if fallback_quote:
                    st.markdown(f"""
                    <div class="quote-container">
                        <div class="category-badge">{fallback_quote['category']}</div>
                        <div class="quote-text">"{fallback_quote['quote_text']}"</div>
                        <div class="author-text">- {fallback_quote['author']}</div>
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div class="footer">Made by crashlar | Quotes Forever </div>', unsafe_allow_html=True)