import streamlit as st
import time
import random

# Page configuration
st.set_page_config(
    page_title="TypeRacer Pro",
    page_icon="⌨️",
    layout="centered"
)

# Professional dark theme CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
    }
    
    .main-header {
        text-align: center;
        color: #ecf0f1;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #bdc3c7;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .game-card {
        background: rgba(236, 240, 241, 0.05);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(189, 195, 199, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .sentence-box {
        background: rgba(44, 62, 80, 0.9);
        color: #ecf0f1;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 1rem 0;
        border: 2px solid #3498db;
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem;
        color: white;
    }
    
    .easy { background: #27ae60; }
    .medium { background: #f39c12; }
    .hard { background: #e74c3c; }
    
    .metric-box {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced sentences
sentences = {
    "Easy": [
        "The cat sat on the mat and took a nap.",
        "I love pizza and ice cream on sunny days.",
        "Dogs are fun pets to have at home.",
        "Books help us learn new things every day.",
        "Music makes me happy when I feel sad.",
        "The sun is bright and warm today."
    ],
    "Medium": [
        "The quick brown fox jumps over the lazy dog while wearing sunglasses.",
        "Pizza is the answer to all of life's problems, especially on Monday morning.",
        "Cats secretly rule the world from their cardboard box headquarters.",
        "I tried to catch some fog earlier, but I mist completely!",
        "Coffee is just bean soup that makes you vibrate with productivity.",
        "My keyboard is fluent in typos and autocorrect disasters."
    ],
    "Hard": [
        "Why do programmers prefer dark mode? Because light attracts bugs & debugging sessions!",
        "The wifi password is 'P@ssw0rd123!' - hidden in the most obvious place, naturally.",
        "Unicorns use Python because it's the most magical programming language (definitely not C++).",
        "Time flies like an arrow; fruit flies like a banana smoothie at 3:14 AM.",
        "My computer has a sense of humor - it laughs at my code errors & syntax mistakes.",
        "Dancing penguins make the best debugging partners, obviously (trust me on this one)."
    ]
}

def calculate_performance_feedback(difficulty, wpm, accuracy):
    """Calculate performance feedback based on difficulty level"""
    if difficulty == "Easy":
        if wpm >= 40 and accuracy >= 95:
            return "Excellent! Ready for medium difficulty?"
        elif wpm >= 25 and accuracy >= 90:
            return "Good job! Keep practicing!"
        else:
            return "Keep practicing to improve your speed and accuracy!"
    elif difficulty == "Medium":
        if wpm >= 35 and accuracy >= 92:
            return "Outstanding! Try hard difficulty for a challenge!"
        elif wpm >= 22 and accuracy >= 87:
            return "Well done! You're getting better!"
        else:
            return "Good effort! Practice makes perfect!"
    else:  # Hard
        if wpm >= 30 and accuracy >= 90:
            return "Master level! You're a typing champion!"
        elif wpm >= 20 and accuracy >= 85:
            return "Impressive! You're handling the complexity well!"
        else:
            return "Challenging level! Keep pushing your limits!"

def main():
    # Header
    st.markdown('<h1 class="main-header">TypeRacer Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Test your typing speed with precision</p>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'sentence' not in st.session_state:
        st.session_state.sentence = ""
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'results' not in st.session_state:
        st.session_state.results = []
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Game Settings")
        
        # Difficulty selection
        difficulty = st.selectbox(
            "Choose Difficulty:",
            ["Easy", "Medium", "Hard"]
        )
        
        # Display difficulty info
        difficulty_info = {
            "Easy": "Simple words, perfect for warming up",
            "Medium": "Punctuation and longer sentences",
            "Hard": "Special characters and complex text"
        }
        st.info(difficulty_info[difficulty])
        
        # Start game button
        start_clicked = st.button("Start New Game", type="primary", use_container_width=True)
        
        # Show stats if available
        if st.session_state.results:
            avg_wpm = sum(r['wpm'] for r in st.session_state.results) / len(st.session_state.results)
            st.markdown("### Your Stats")
            st.metric("Games Played", len(st.session_state.results))
            st.metric("Average WPM", round(avg_wpm, 1))
    
    # Main game area
    if start_clicked:
        st.session_state.sentence = random.choice(sentences[difficulty])
        st.session_state.game_active = True
        st.session_state.start_time = None
        st.session_state.difficulty = difficulty
        st.rerun()
    
    if st.session_state.game_active:
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        
        # Difficulty badge
        badge_class = st.session_state.difficulty.lower()
        st.markdown(f'''
            <div style="text-align: center; margin-bottom: 1rem;">
                <span class="difficulty-badge {badge_class}">
                    {st.session_state.difficulty.upper()} MODE
                </span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Display sentence
        st.markdown(f'''
            <div class="sentence-box">
                TYPE THIS SENTENCE:<br><br>
                {st.session_state.sentence}
            </div>
        ''', unsafe_allow_html=True)
        
        # Text input
        typed_text = st.text_area(
            "Start typing here:",
            placeholder="Click here and start typing! Timer starts automatically...",
            height=100,
            label_visibility="collapsed"
        )
        
        # Start timing
        if typed_text and st.session_state.start_time is None:
            st.session_state.start_time = time.time()
        
        # Real-time feedback
        if typed_text:
            progress = min(len(typed_text) / len(st.session_state.sentence), 1.0)
            st.progress(progress, text=f"Progress: {int(progress * 100)}%")
            
            # Check completion
            if typed_text.strip() == st.session_state.sentence:
                end_time = time.time()
                time_taken = end_time - st.session_state.start_time
                
                # Calculate metrics
                words = len(st.session_state.sentence.split())
                wpm = round(words / (time_taken / 60), 2)
                accuracy = 100.0
                
                # Celebration
                st.balloons()
                st.success("Perfect! You nailed it!")
                
                # Display results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f'''
                        <div class="metric-box">
                            <h3>Time</h3>
                            <h2>{round(time_taken, 2)}s</h2>
                        </div>
                    ''', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'''
                        <div class="metric-box">
                            <h3>WPM</h3>
                            <h2>{wpm}</h2>
                        </div>
                    ''', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'''
                        <div class="metric-box">
                            <h3>Accuracy</h3>
                            <h2>{accuracy}%</h2>
                        </div>
                    ''', unsafe_allow_html=True)
                
                # Feedback
                feedback = calculate_performance_feedback(st.session_state.difficulty, wpm, accuracy)
                st.info(feedback)
                
                # Save results
                result = {
                    "difficulty": st.session_state.difficulty,
                    "time": round(time_taken, 2),
                    "wpm": wpm,
                    "accuracy": accuracy,
                    "sentence": st.session_state.sentence
                }
                st.session_state.results.append(result)
                st.session_state.game_active = False
                
            else:
                # Live feedback
                correct_chars = sum(1 for a, b in zip(typed_text, st.session_state.sentence) if a == b)
                current_accuracy = round((correct_chars / len(st.session_state.sentence)) * 100, 2)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Live Accuracy", f"{current_accuracy}%")
                with col2:
                    if st.session_state.start_time:
                        elapsed = time.time() - st.session_state.start_time
                        st.metric("Time", f"{round(elapsed, 1)}s")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        # Welcome screen
        st.markdown("""
            <div class="game-card" style="text-align: center;">
                <h2 style="color: white; margin-bottom: 2rem;">Ready to Test Your Skills?</h2>
                <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #27ae60;">●</div>
                        <h4 style="color: #27ae60;">Easy</h4>
                        <p style="color: #ccc;">Perfect for beginners</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #f39c12;">●</div>
                        <h4 style="color: #f39c12;">Medium</h4>
                        <p style="color: #ccc;">Step up the challenge</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #e74c3c;">●</div>
                        <h4 style="color: #e74c3c;">Hard</h4>
                        <p style="color: #ccc;">For typing masters</p>
                    </div>
                </div>
                <p style="color: #ccc;">Choose your difficulty and click "Start New Game"!</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Simple results history
    if st.session_state.results:
        st.markdown("---")
        st.markdown("## Recent Games")
        
        # Show last 3 games only to keep it light
        recent_games = st.session_state.results[-3:]
        
        for i, result in enumerate(reversed(recent_games)):
            with st.expander(f"Game {len(st.session_state.results) - i} - {result['difficulty']} - {result['wpm']} WPM"):
                st.write(f"**Sentence:** _{result['sentence']}_")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Time", f"{result['time']}s")
                with col2:
                    st.metric("WPM", result['wpm'])
                with col3:
                    st.metric("Accuracy", f"{result['accuracy']}%")
        
        # Clear history button
        if st.button("Clear History", use_container_width=True):
            st.session_state.results = []
            st.rerun()

if __name__ == "__main__":
    main()
