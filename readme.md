# Quotes Forever

A beautiful and inspirational web application that delivers curated quotes based on your mood, preferences, and daily needs. Built with Streamlit and SQLite, this application provides a personalized quote experience for every user.

## Features

### 1. Quote of the Day
- Random inspirational quotes from a massive database
- Beautiful, professional display with category badges
- One-click new quote generation
- Add favorites functionality

### 2. Add New Quotes
- Contribute to the community by adding your own quotes
- Categorize quotes for better organization
- Add context and inspiration behind each quote

### 3. Personal Details
- Secure user profile management
- Collect feedback and suggestions
- Personalized help requests

### 4. Mood-Based Quotes
- Intelligent quote matching based on:
  - Current mood (Happy, Sad, Motivated, Stressed, etc.)
  - Age and gender preferences
  - Social and professional life status
  - Personalized recommendations

## Installation

### Step-by-Step Setup

1. **Create Project Directory**
   ```bash
   md quotes-forever
   cd quotes-forever
   ```

2. **Create Project Files**
   Save all the provided Python files in your project directory:
   - `setup.py`
   - `streamlit_app.py`
   - `requirements.txt`

3. **Run the Setup Script**
   ```bash
   python setup.py
   ```
   This will:
   - Create the SQLite database in database folder (`data.db`)
   - Fetch quotes from multiple external APIs
   - Generate comprehensive mood-based quotes
   - Populate the database with hundreds of quotes

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Launch the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

## Project Structure

```
quotes-forever/
│
├── streamlit_app.py          # Main Streamlit application
├── setup.py                  # Database setup and data fetcher
├── requirements.txt          # Python dependencies
├── database/data.db                   # SQLite database (created automatically)
├── Licence
└── README.md                 # Project documentation

```

## Database Schema

### Quotes Table
- `id` - Primary key
- `quote_text` - The inspirational quote
- `author` - Author of the quote
- `category` - Quote category (Motivation, Life, Love, etc.)
- `inspiration` - Context or inspiration behind the quote
- `created_date` - Timestamp of when quote was added

### Users Table
- `id` - Primary key
- `name` - User's full name
- `phone` - Contact number
- `email` - Email address
- `profession` - User's occupation
- `feedback` - User feedback
- `help_request` - Assistance requests
- `created_date` - Registration timestamp

### Mood Quotes Table
- `id` - Primary key
- `quote_text` - The quote text
- `author` - Quote author
- `mood_category` - Associated mood (happy, sad, motivated, etc.)
- `gender_preference` - Target gender (both, girl, boy)
- `min_age` / `max_age` - Age range targeting
- `social_life` - Social life status targeting
- `professional_life` - Professional life status targeting

<!-- ## Technical Details

### Built With
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite
- **APIs Integrated**:
  - ZenQuotes API
  - Quotable API
  - Forismatic API
  - TypeFit API -->

### Key Dependencies
- `streamlit>=1.28.0` - Web application framework
- `requests>=2.31.0` - HTTP library for API calls
- `sqlite3` - Database management
<!-- 
## Usage Guide

### Getting Started
1. Launch the application using `streamlit run streamlit_app.py`
2. The main page displays a random "Quote of the Day"
3. Use the sidebar dropdown to navigate between features

### Navigation Options

#### Quote of the Day
- View a randomly selected inspirational quote
- Click "Generate New Quote" for a fresh inspiration
- Use "Add to Favorites" to save quotes you love
- Expand "Quote Details" for additional context

#### Add Quote
- Contribute to the growing quote database
- Fill in quote text, author, and category
- Add inspirational context for other users
- All fields are validated before submission

#### Personal Details
- Create your user profile
- Provide feedback about the application
- Request specific help or guidance
- Your information is stored securely

#### Mood Wise Quotes
- Answer a few questions about your current state
- Get personalized quotes matching your mood
- System considers age, gender, social, and professional factors
- Fallback to general quotes if no perfect match found
 -->

## Data Sources

The application fetches quotes from multiple reliable sources:

1. **ZenQuotes API** - Wisdom and inspirational quotes
2. **Quotable API** - Categorized quotes with tags
3. **Forismatic API** - Random inspirational quotes
4. **TypeFit API** - Large collection of famous quotes
5. **Fallback Data** - Comprehensive built-in quote library
<!-- 
## Data Statistics

- **200+** general quotes from APIs
- **50+** mood-based quotes with demographic targeting
- **10+** quote categories
- **8** different mood categories
- Continuous database growth through user contributions
 -->
## Customization

### Adding New Quote Categories
Edit the categories list in `streamlit_app.py`:
```python
categories = ["Motivation", "Life", "Love", "Success", "Career", "Dreams", 
             "Perseverance", "Courage", "Opportunity", "Happiness", 
             "Wisdom", "Innovation", "Your New Category"]
```

### Modifying Mood Categories
Update the mood options in the Mood Wise Quotes section:
```python
current_mood = st.selectbox("How are you feeling right now?", 
                           ["Happy", "Sad", "Motivated", "Stressed", 
                            "Love", "Career-focused", "Your New Mood"])
```

## Contributing

We welcome contributions to make Quotes Forever even better:

1. Fork the project
2. Add new features or fix bugs
3. Submit a pull request
4. Or simply add your favorite quotes through the application!

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Use different port
   streamlit run streamlit_app.py --server.port 8502
   ```

2. **Database Errors**
   ```bash
   # Re-run setup
   python setup.py
   ```

3. **Missing Dependencies**
   ```bash
   # Reinstall requirements
   pip install -r requirements.txt
   ```

4. **API Connection Issues**
   - Application will use fallback data
   - No interruption in service

## License

This project is open source and available under the MIT License.

<!-- ## Acknowledgments

- All the quote APIs for providing inspirational content
- Streamlit team for the amazing framework
- Contributors and users who add quotes to the database -->

## Support

If you encounter any issues or have suggestions:
1. Use the "Personal Details" section in the app
2. Submit feedback through the application
3. Or create an issue in the project repository

---

Start your inspirational journey today with Quotes Forever!


## 🤝 Connect & Collaborate

If you find something useful or want to collaborate, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/crashlar/) or contribute to this repo!