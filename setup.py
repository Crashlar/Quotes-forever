import sqlite3
import os
import requests
import json
import random
from datetime import datetime

class QuoteFetcher:
    def __init__(self):
        self.quotes_data = []
        self.mood_quotes_data = []

    def fetch_zenquotes_api(self):
        """Fetch quotes from ZenQuotes API"""
        try:
            print("📡 Fetching quotes from ZenQuotes API...")
            response = requests.get("https://zenquotes.io/api/quotes")
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    self.quotes_data.append({
                        'text': item['q'],
                        'author': item['a'],
                        'category': 'Wisdom',
                        'inspiration': 'ZenQuotes API'
                    })
                print(f"✅ Fetched {len(data)} quotes from ZenQuotes")
            else:
                print("❌ ZenQuotes API unavailable, using fallback data")
        except Exception as e:
            print(f"❌ Error fetching ZenQuotes: {e}")

    # def fetch_quotable_api(self):
    #     """Fetch quotes from Quotable API"""
    #     try:
    #         print("📡 Fetching quotes from Quotable API...")
    #         response = requests.get("https://api.quotable.io/quotes?limit=200")
    #         if response.status_code == 200:
    #             data = response.json()
    #             for item in data['results']:
    #                 self.quotes_data.append({
    #                     'text': item['content'],
    #                     'author': item['author'],
    #                     'category': item.get('tags', ['General'])[0] if item.get('tags') else 'General',
    #                     'inspiration': 'Quotable API'
    #                 })
    #             print(f"✅ Fetched {len(data['results'])} quotes from Quotable")
    #         else:
    #             print("❌ Quotable API unavailable")
    #     except Exception as e:
    #         print(f"❌ Error fetching Quotable: {e}")

    def fetch_forismatic_api(self):
        """Fetch quotes from Forismatic API"""
        try:
            print("📡 Fetching quotes from Forismatic API...")
            # Fetch multiple quotes
            for _ in range(50):
                response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
                if response.status_code == 200:
                    try:
                        data = response.json()
                        self.quotes_data.append({
                            'text': data['quoteText'].strip(),
                            'author': data['quoteAuthor'] if data['quoteAuthor'] else 'Unknown',
                            'category': 'Inspirational',
                            'inspiration': 'Forismatic API'
                        })
                    except:
                        continue
            print(f"✅ Fetched quotes from Forismatic API")
        except Exception as e:
            print(f"❌ Error fetching Forismatic: {e}")

    def fetch_typefit_api(self):
        """Fetch quotes from TypeFit API"""
        try:
            print("📡 Fetching quotes from TypeFit API...")
            response = requests.get("https://type.fit/api/quotes")
            if response.status_code == 200:
                data = response.json()
                for item in data[:100]:  # Take first 100 quotes
                    self.quotes_data.append({
                        'text': item['text'],
                        'author': item['author'] if item['author'] else 'Unknown',
                        'category': 'Motivation',
                        'inspiration': 'TypeFit API'
                    })
                print(f"✅ Fetched {len(data[:100])} quotes from TypeFit")
            else:
                print("❌ TypeFit API unavailable")
        except Exception as e:
            print(f"❌ Error fetching TypeFit: {e}")

    def generate_mood_quotes(self):
        """Generate comprehensive mood-based quotes"""
        print("🎭 Generating mood-based quotes...")
        
        # Happy mood quotes
        happy_quotes = [
            ("The most wasted of days is one without laughter.", "E. E. Cummings", "happy"),
            ("Happiness is not something ready made. It comes from your own actions.", "Dalai Lama", "happy"),
            ("The purpose of our lives is to be happy.", "Dalai Lama", "happy"),
            ("Spread love everywhere you go. Let no one ever come to you without leaving happier.", "Mother Teresa", "happy"),
            ("Be happy for this moment. This moment is your life.", "Omar Khayyam", "happy"),
            ("Happiness is a butterfly, which when pursued, is always just beyond your grasp.", "Nathaniel Hawthorne", "happy"),
            ("The happiness of your life depends upon the quality of your thoughts.", "Marcus Aurelius", "happy"),
            ("Joy is the simplest form of gratitude.", "Karl Barth", "happy"),
            ("Time you enjoy wasting is not wasted time.", "Marthe Troly-Curtin", "happy"),
        ]
        
        # Sad mood quotes
        sad_quotes = [
            ("Tears come from the heart and not from the brain.", "Leonardo da Vinci", "sad"),
            ("The word 'happy' would lose its meaning if it were not balanced by sadness.", "Carl Jung", "sad"),
            ("Every man has his secret sorrows which the world knows not.", "Henry Wadsworth Longfellow", "sad"),
            ("Sadness is but a wall between two gardens.", "Kahlil Gibran", "sad"),
            ("The soul would have no rainbow had the eyes no tears.", "John Vance Cheney", "sad"),
            ("There are moments when I wish I could roll back the clock.", "Nicholas Sparks", "sad"),
            ("The tragedy of life is not that it ends so soon, but that we wait so long to begin it.", "W. M. Lewis", "sad"),
        ]
        
        # Motivated mood quotes
        motivated_quotes = [
            ("Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Roy T. Bennett", "motivated"),
            ("Believe you can and you're halfway there.", "Theodore Roosevelt", "motivated"),
            ("The only limit to our realization of tomorrow will be our doubts of today.", "Franklin D. Roosevelt", "motivated"),
            ("It always seems impossible until it's done.", "Nelson Mandela", "motivated"),
            ("The way to get started is to quit talking and begin doing.", "Walt Disney", "motivated"),
            ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs", "motivated"),
            ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt", "motivated"),
        ]
        
        # Stressed mood quotes
        stressed_quotes = [
            ("You can't calm the storm, so stop trying. What you can do is calm yourself.", "Timber Hawkeye", "stressed"),
            ("It's not the load that breaks you down, it's the way you carry it.", "Lou Holtz", "stressed"),
            ("Stress is caused by being 'here' but wanting to be 'there'.", "Eckhart Tolle", "stressed"),
            ("Every stress leaves an indelible scar, and the organism pays for its survival.", "Hans Selye", "stressed"),
            ("Adopting the right attitude can convert a negative stress into a positive one.", "Hans Selye", "stressed"),
        ]
        
        # Love mood quotes
        love_quotes = [
            ("The best thing to hold onto in life is each other.", "Audrey Hepburn", "love"),
            ("Love is composed of a single soul inhabiting two bodies.", "Aristotle", "love"),
            ("To love and be loved is to feel the sun from both sides.", "David Viscott", "love"),
            ("Love isn't something you find. Love is something that finds you.", "Loretta Young", "love"),
            ("The greatest happiness of life is the conviction that we are loved.", "Victor Hugo", "love"),
        ]
        
        # Career-focused quotes
        career_quotes = [
            ("Your work is going to fill a large part of your life, so make sure it's something you're passionate about.", "Steve Jobs", "career"),
            ("The only way to do great work is to love what you do.", "Steve Jobs", "career"),
            ("Opportunities don't happen. You create them.", "Chris Grosser", "career"),
            ("Don't be afraid to give up the good to go for the great.", "John D. Rockefeller", "career"),
            ("Success is not the key to happiness. Happiness is the key to success.", "Albert Schweitzer", "career"),
        ]
        
        # Angry mood quotes
        angry_quotes = [
            ("Holding onto anger is like drinking poison and expecting the other person to die.", "Buddha", "angry"),
            ("For every minute you remain angry, you give up sixty seconds of peace of mind.", "Ralph Waldo Emerson", "angry"),
            ("Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.", "Mark Twain", "angry"),
        ]
        
        # Confused mood quotes
        confused_quotes = [
            ("The only true wisdom is in knowing you know nothing.", "Socrates", "confused"),
            ("In the middle of difficulty lies opportunity.", "Albert Einstein", "confused"),
            ("When we are no longer able to change a situation, we are challenged to change ourselves.", "Viktor Frankl", "confused"),
        ]
        
        # Combine all mood quotes
        all_mood_quotes = (happy_quotes + sad_quotes + motivated_quotes + 
                          stressed_quotes + love_quotes + career_quotes + 
                          angry_quotes + confused_quotes)
        
        # Convert to database format with additional parameters
        for text, author, mood in all_mood_quotes:
            self.mood_quotes_data.append({
                'text': text,
                'author': author,
                'mood': mood,
                'gender_preference': random.choice(['both', 'both', 'both', 'girl', 'boy']),
                'min_age': random.randint(15, 25),
                'max_age': random.randint(45, 80),
                'social_life': random.choice(['good', 'not good', 'balanced']),
                'professional_life': random.choice(['good', 'struggling', 'balanced'])
            })
        
        print(f"✅ Generated {len(self.mood_quotes_data)} mood-based quotes")

    def add_fallback_data(self):
        """Add comprehensive fallback data if APIs fail"""
        print("📝 Adding comprehensive fallback data...")
        
        fallback_quotes = [
            # Motivational quotes
            ("The only way to do great work is to love what you do.", "Steve Jobs", "Motivation", "Career inspiration"),
            ("Innovation distinguishes between a leader and a follower.", "Steve Jobs", "Innovation", "Leadership qualities"),
            ("Your time is limited, don't waste it living someone else's life.", "Steve Jobs", "Life", "Personal growth"),
            ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt", "Dreams", "Inspirational"),
            ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson", "Perseverance", "Motivation"),
            ("The only impossible journey is the one you never begin.", "Tony Robbins", "Courage", "Starting new things"),
            ("In the middle of difficulty lies opportunity.", "Albert Einstein", "Opportunity", "Problem solving"),
            ("Life is what happens to you while you're busy making other plans.", "John Lennon", "Life", "Mindfulness"),
            ("The way to get started is to quit talking and begin doing.", "Walt Disney", "Action", "Productivity"),
            ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi", "Resilience", "Sports motivation"),
            
            # Wisdom quotes
            ("Be the change that you wish to see in the world.", "Mahatma Gandhi", "Wisdom", "Social change"),
            ("Live as if you were to die tomorrow. Learn as if you were to live forever.", "Mahatma Gandhi", "Wisdom", "Life philosophy"),
            ("The journey of a thousand miles begins with one step.", "Lao Tzu", "Wisdom", "Starting journeys"),
            ("That which does not kill us makes us stronger.", "Friedrich Nietzsche", "Wisdom", "Resilience"),
            ("Be yourself; everyone else is already taken.", "Oscar Wilde", "Wisdom", "Authenticity"),
            
            # Success quotes
            ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill", "Success", "Persistence"),
            ("The only place where success comes before work is in the dictionary.", "Vidal Sassoon", "Success", "Hard work"),
            ("Don't be afraid to give up the good to go for the great.", "John D. Rockefeller", "Success", "Ambition"),
            
            # Love quotes
            ("You know you're in love when you can't fall asleep because reality is finally better than your dreams.", "Dr. Seuss", "Love", "Romance"),
            ("The best thing to hold onto in life is each other.", "Audrey Hepburn", "Love", "Relationships"),
            ("Love is composed of a single soul inhabiting two bodies.", "Aristotle", "Love", "Philosophy"),
            
            # Additional famous quotes
            ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison", "Perseverance", "Innovation process"),
            ("If you can dream it, you can do it.", "Walt Disney", "Dreams", "Achievement"),
            ("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt", "Courage", "Overcoming fear"),
            ("It is during our darkest moments that we must focus to see the light.", "Aristotle", "Hope", "Difficult times"),
            ("Whoever is happy will make others happy too.", "Anne Frank", "Happiness", "Positive impact"),
            ("Do what you can, with what you have, where you are.", "Theodore Roosevelt", "Action", "Resourcefulness"),
            ("The purpose of life is to live it, to taste experience to the utmost.", "Eleanor Roosevelt", "Life", "Experience"),
        ]
        
        for text, author, category, inspiration in fallback_quotes:
            self.quotes_data.append({
                'text': text,
                'author': author,
                'category': category,
                'inspiration': inspiration
            })

def setup_database():
    """Initialize the database with required tables and massive data"""
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    
    # Create quotes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote_text TEXT NOT NULL,
            author TEXT NOT NULL,
            category TEXT NOT NULL,
            inspiration TEXT,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            profession TEXT,
            feedback TEXT,
            help_request TEXT,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create mood_quotes table with categories for different moods
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mood_quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote_text TEXT NOT NULL,
            author TEXT NOT NULL,
            mood_category TEXT NOT NULL,
            gender_preference TEXT,
            min_age INTEGER,
            max_age INTEGER,
            social_life TEXT,
            professional_life TEXT
        )
    ''')
    
    # Fetch data from multiple sources
    fetcher = QuoteFetcher()
    
    print("🚀 Starting data collection from multiple sources...")
    print("=" * 60)
    
    # Fetch from APIs
    fetcher.fetch_zenquotes_api()
    # fetcher.fetch_quotable_api()
    fetcher.fetch_forismatic_api()
    fetcher.fetch_typefit_api()
    
    # Generate mood quotes
    fetcher.generate_mood_quotes()
    
    # Add fallback data if APIs didn't provide enough
    if len(fetcher.quotes_data) < 50:
        fetcher.add_fallback_data()
    
    # Insert quotes into database
    print("\n💾 Inserting quotes into database...")
    for quote in fetcher.quotes_data:
        cursor.execute('''
            INSERT INTO quotes (quote_text, author, category, inspiration)
            VALUES (?, ?, ?, ?)
        ''', (quote['text'], quote['author'], quote['category'], quote['inspiration']))
    
    # Insert mood quotes into database
    for quote in fetcher.mood_quotes_data:
        cursor.execute('''
            INSERT INTO mood_quotes (quote_text, author, mood_category, gender_preference, min_age, max_age, social_life, professional_life)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (quote['text'], quote['author'], quote['mood'], quote['gender_preference'], 
              quote['min_age'], quote['max_age'], quote['social_life'], quote['professional_life']))
    
    conn.commit()
    
    # Count inserted records
    cursor.execute("SELECT COUNT(*) FROM quotes")
    quote_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mood_quotes")
    mood_quote_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print(f"✅ Database setup completed successfully!")
    print(f"📊 Total quotes in database: {quote_count}")
    print(f"🎭 Total mood-based quotes: {mood_quote_count}")
    print(f"💫 Total quotes overall: {quote_count + mood_quote_count}")

def check_requirements():
    """Check if all required packages are installed"""
    required_packages = ['streamlit', 'sqlite3', 'requests']
    print("\n📦 Required packages: streamlit, sqlite3, requests")
    print("💡 Run: pip install streamlit requests")

if __name__ == "__main__":
    print("🚀 Setting up Quotes Forever Project with Massive Data...")
    print("=" * 60)
    
    setup_database()
    check_requirements()
    
    print("\n🎉 Setup completed! You can now run:")
    print("   streamlit run streamlit_app.py")
    print("\n📁 Files created/updated:")
    print("   ✅ data.db (Database with massive quotes collection)")
    print("   ✅ setup.py (Enhanced data fetcher)")
    print("   ✅ requirements.txt (Dependencies)")
    print("   ✅ streamlit_app.py (Main application)")

    
