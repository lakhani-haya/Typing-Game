import streamlit as st
import time
import random

# Page configuration
st.set_page_config(
    page_title="TypeRacer Pro",
    page_icon="⌨️",
    layout="centered"
)

#  pastel theme CSS
st.markdown("""
<style>
    .stApp {
        background: #f8f4ff;
    }
    
    .main-header {
        text-align: center;
        color: #6366f1;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(99, 102, 241, 0.2);
    }
    
    .subtitle {
        text-align: center;
        color: #8b7fb8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    .sentence-box {
        background: #ffffff;
        color: #2d3748;
        padding: 2rem;
        border-radius: 20px;
        font-size: 1.2rem;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 1.5rem 0;
        border: 3px solid #c7d2fe;
        box-shadow: 0 8px 25px rgba(199, 210, 254, 0.3);
        transition: all 0.3s ease;
    }
    
    .sentence-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(199, 210, 254, 0.4);
        border-color: #a5b4fc;
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 0.8rem 1.8rem;
        border-radius: 25px;
        font-weight: bold;
        margin: 0.8rem;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    .easy { 
        background: #86efac;
        color: #166534;
        box-shadow: 0 6px 20px rgba(134, 239, 172, 0.4);
    }
    .medium { 
        background: #fbbf24;
        color: #92400e;
        box-shadow: 0 6px 20px rgba(251, 191, 36, 0.4);
    }
    .hard { 
        background: #f87171;
        color: #991b1b;
        box-shadow: 0 6px 20px rgba(248, 113, 113, 0.4);
    }
    
    .metric-box {
        background: #dbeafe;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: #1e40af;
        margin: 0.5rem;
        box-shadow: 0 8px 25px rgba(219, 234, 254, 0.4);
        border: 2px solid #bfdbfe;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(219, 234, 254, 0.6);
        border-color: #93c5fd;
        background: #bfdbfe;
    }
    
    .metric-box h3 {
        color: #3b82f6;
        margin-bottom: 0.5rem;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .metric-box h2 {
        color: #1e40af;
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Streamlit component styling */
    .stButton > button {
        background: #8b5cf6;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
        transition: all 0.3s ease;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 35px rgba(139, 92, 246, 0.6);
        background: #7c3aed;
    }
    
    .stTextInput > div > div > input {
        background: #ffffff;
        border: 3px solid #e0e7ff;
        border-radius: 15px;
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        padding: 1.2rem;
        box-shadow: 0 6px 20px rgba(224, 231, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4);
        outline: none;
        transform: translateY(-2px);
    }
    
    .stProgress > div > div > div {
        background: #a78bfa;
        border-radius: 15px;
        height: 12px;
    }
    
    .stSelectbox > div > div > div {
        background: #ffffff;
        border: 2px solid #e0e7ff;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div > div:hover {
        border-color: #8b5cf6;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.2);
    }
    
    /* Welcome screen enhancements */
    .welcome-container {
        background: #ffffff;
        border-radius: 25px;
        padding: 3rem;
        margin: 2rem 0;
        border: 2px solid #e0e7ff;
        box-shadow: 0 20px 50px rgba(224, 231, 255, 0.3);
        text-align: center;
    }
    
    /* Custom animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Message styling */
    .stInfo {
        background: #dbeafe;
        border-left: 4px solid #60a5fa;
        border-radius: 10px;
    }
    
    .stSuccess {
        background: #dcfce7;
        border-left: 4px solid #4ade80;
        border-radius: 10px;
    }
    
    .stError {
        background: #fee2e2;
        border-left: 4px solid #f87171;
        border-radius: 10px;
    }
    
    .stWarning {
        background: #fef3c7;
        border-left: 4px solid #fbbf24;
        border-radius: 10px;
    }
</style>""", unsafe_allow_html=True)

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
    # Heade
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
            # Text input for active game - using key to track changes
            typed_text = st.text_input(
                "Type here (press Enter to submit):",
                placeholder="Click here and start typing! Press Enter when done...",
                key="typing_input"
            )
            
            # Start timer on first character typed
            if typed_text and not st.session_state.timer_active:
                st.session_state.start_time = time.time()
                st.session_state.timer_active = True
                st.success("⏱️ Timer started!")
            
            # Store current input for reference
            st.session_state.current_input = typed_text
            
            # Debug information (remove after testing)
            if st.checkbox("Show Debug Info", value=False):
                st.write(f"**Debug Info:**")
                st.write(f"- Timer Active: {st.session_state.timer_active}")
                st.write(f"- Start Time: {st.session_state.start_time}")
                st.write(f"- Current Time: {time.time()}")
                st.write(f"- Typed Text Length: {len(typed_text) if typed_text else 0}")
                if st.session_state.timer_active and st.session_state.start_time > 0:
                    elapsed = time.time() - st.session_state.start_time
                    st.write(f"- Calculated Elapsed: {round(elapsed, 2)}s")
            
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
                            # Only show elapsed time if meaningful (more than 0.1 seconds)
                            if elapsed >= 0.1:
                                st.metric("Elapsed Time", f"{round(elapsed, 1)}s")
                            else:
                                st.metric("Elapsed Time", "0.0s")
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
