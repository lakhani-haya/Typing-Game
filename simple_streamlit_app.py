import streamlit as st
import time
import random

# Page configuration
st.set_page_config(
    page_title="TypeRacer Pro",
    page_icon="⌨️",
    layout="centered"
)

# Beautiful pastel theme CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffeef2 0%, #f0f4ff 50%, #f0fff4 100%);
    }
    
    .main-header {
        text-align: center;
        color: #5a4fcf;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(90, 79, 207, 0.1);
        background: linear-gradient(45deg, #5a4fcf, #ff6b9d, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        text-align: center;
        color: #8b7fb8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    .sentence-box {
        background: linear-gradient(135deg, #ffffff 0%, #fafbff 100%);
        color: #2d3748;
        padding: 2rem;
        border-radius: 20px;
        font-size: 1.2rem;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 1.5rem 0;
        border: 2px solid #b794f6;
        box-shadow: 0 8px 25px rgba(183, 148, 246, 0.15);
        transition: all 0.3s ease;
    }
    
    .sentence-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(183, 148, 246, 0.2);
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 0.7rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        margin: 0.5rem;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .easy { 
        background: linear-gradient(135deg, #a8e6cf 0%, #7fcdcd 100%);
        color: #2d5a3d;
    }
    .medium { 
        background: linear-gradient(135deg, #ffd3a5 0%, #fd9853 100%);
        color: #8b4513;
    }
    .hard { 
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        color: #8b2635;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #e0f2ff 0%, #d6efff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: #2d5a87;
        margin: 0.5rem;
        box-shadow: 0 6px 20px rgba(173, 216, 255, 0.25);
        border: 1px solid rgba(173, 216, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(173, 216, 255, 0.35);
    }
    
    .metric-box h3 {
        color: #4a90e2;
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    .metric-box h2 {
        color: #2d5a87;
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Streamlit component styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .stTextInput > div > div > input {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        border: 2px solid #c3d9ff;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(195, 217, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        outline: none;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    .stSelectbox > div > div > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        border: 2px solid #c3d9ff;
        border-radius: 12px;
    }
    
    /* Custom animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
</style>""", unsafe_allow_html=True)
        background: #ffffff !important;
        border: 2px solid #007bff !important;
        border-radius: 8px !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1.1rem !important;
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
        st.session_state.start_time = 0.0
    if 'results' not in st.session_state:
        st.session_state.results = []
    if 'game_completed' not in st.session_state:
        st.session_state.game_completed = False
    if 'final_time' not in st.session_state:
        st.session_state.final_time = 0.0
    if 'current_input' not in st.session_state:
        st.session_state.current_input = ""
    if 'timer_active' not in st.session_state:
        st.session_state.timer_active = False
    
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
        st.session_state.start_time = 0.0
        st.session_state.difficulty = difficulty
        st.session_state.game_completed = False
        st.session_state.final_time = 0.0
        st.session_state.current_input = ""
        st.session_state.timer_active = False
        st.rerun()
    
    if st.session_state.game_active:
        
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
        
        # Check if game was just completed
        if st.session_state.game_completed:
            # Show results from completed game
            time_taken = st.session_state.final_time
            
            # Debug info - remove this later if needed
            if time_taken <= 0:
                st.error("Timer error detected! Please start a new game.")
                time_taken = 1.0  # Fallback to prevent division by zero
            
            words = len(st.session_state.sentence.split())
            wpm = round(words / (time_taken / 60), 2) if time_taken > 0 else 0
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
            
            # Save results only once
            if not any(r.get('just_added') for r in st.session_state.results):
                result = {
                    "difficulty": st.session_state.difficulty,
                    "time": round(time_taken, 2),
                    "wpm": wpm,
                    "accuracy": accuracy,
                    "sentence": st.session_state.sentence,
                    "just_added": True
                }
                st.session_state.results.append(result)
            
            # Button to start new game
            if st.button("Start New Game", type="primary"):
                st.session_state.game_active = False
                st.session_state.game_completed = False
                st.session_state.current_input = ""
                st.session_state.timer_active = False
                # Clean up the just_added flag
                for result in st.session_state.results:
                    if 'just_added' in result:
                        del result['just_added']
                st.rerun()
        
        else:
            # Text input for active game
            typed_text = st.text_input(
                "Type here (press Enter to submit):",
                placeholder="Click here and start typing! Press Enter when done...",
                key="typing_input",
                value=st.session_state.current_input
            )
            
            # Check if user started typing and start timer
            if typed_text and not st.session_state.timer_active:
                st.session_state.start_time = time.time()
                st.session_state.timer_active = True
                st.session_state.current_input = typed_text
                st.success("⏱️ Timer started!")
            
            # Update current input if changed
            if typed_text != st.session_state.current_input:
                st.session_state.current_input = typed_text
            
            # Real-time feedback
            if typed_text:
                progress = min(len(typed_text) / len(st.session_state.sentence), 1.0)
                st.progress(progress, text=f"Progress: {int(progress * 100)}%")
                
                # Check for exact completion
                if typed_text == st.session_state.sentence and st.session_state.timer_active:
                    end_time = time.time()
                    time_taken = end_time - st.session_state.start_time
                    st.session_state.final_time = time_taken
                    st.session_state.game_completed = True
                    st.session_state.timer_active = False
                
                else:
                    # Live feedback
                    correct_chars = sum(1 for a, b in zip(typed_text, st.session_state.sentence) if a == b)
                    current_accuracy = round((correct_chars / len(st.session_state.sentence)) * 100, 2)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Live Accuracy", f"{current_accuracy}%")
                    with col2:
                        if st.session_state.timer_active and st.session_state.start_time > 0:
                            elapsed = time.time() - st.session_state.start_time
                            st.metric("Elapsed Time", f"{round(elapsed, 1)}s")
                        else:
                            st.metric("Elapsed Time", "0.0s")
                            
            # Show instructions if user hasn't started typing
            else:
                st.info("💡 Start typing to begin the timer!")
    
    else:
        # Welcome screen
        st.markdown("""
            <div class="game-card" style="text-align: center;">
                <h2 style="color: #343a40; margin-bottom: 2rem;">Ready to Test Your Skills?</h2>
                <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #28a745;">●</div>
                        <h4 style="color: #28a745;">Easy</h4>
                        <p style="color: #6c757d;">Perfect for beginners</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #ffc107;">●</div>
                        <h4 style="color: #ffc107;">Medium</h4>
                        <p style="color: #6c757d;">Step up the challenge</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 2rem; color: #dc3545;">●</div>
                        <h4 style="color: #dc3545;">Hard</h4>
                        <p style="color: #6c757d;">For typing masters</p>
                    </div>
                </div>
                <p style="color: #6c757d;">Choose your difficulty and click "Start New Game"!</p>
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
