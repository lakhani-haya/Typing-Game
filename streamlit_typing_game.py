import streamlit as st
import time
import random
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="TypeRacer Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Beautiful enhanced pastel theme CSS with vib colors
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #e8f5e8 25%, #e3f2fd 50%, #fff3e0 75%, #f3e5f5 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main-header {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: linear-gradient(45deg, #ff6b9d, #4ecdc4, #96ceb4, #ffeaa7, #dda0dd, #87ceeb, #ffa07a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 400% 400%;
        animation: textGradient 8s ease infinite;
    }
    
    @keyframes textGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .subtitle {
        text-align: center;
        color: #8b7fb8;
        font-size: 1.5rem;
        margin-top: -10px;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(139, 127, 184, 0.3);
    }
    
    .game-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 249, 255, 0.95) 50%, rgba(255, 248, 250, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 3rem;
        margin: 2rem 0;
        border: 3px solid transparent;
        background-clip: padding-box;
        position: relative;
        box-shadow: 0 20px 50px rgba(183, 148, 246, 0.2);
    }
    
    .game-container::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, #ff6b9d, #4ecdc4, #96ceb4, #ffeaa7, #dda0dd);
        border-radius: 33px;
        z-index: -1;
        background-size: 300% 300%;
        animation: borderGradient 8s ease infinite;
    }
    
    @keyframes borderGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .sentence-display {
        background: linear-gradient(135deg, #ffffff 0%, #f8f4ff 25%, #fff8f0 50%, #f0fff4 75%, #fff0f5 100%);
        color: #2d3748;
        padding: 2.5rem;
        border-radius: 25px;
        font-size: 1.3rem;
        font-family: 'Courier New', monospace;
        line-height: 1.6;
        text-align: center;
        margin: 2rem 0;
        border: 3px solid transparent;
        background-clip: padding-box;
        position: relative;
        box-shadow: 0 15px 40px rgba(183, 148, 246, 0.2);
        transition: all 0.3s ease;
    }
    
    .sentence-display::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, #ff9a9e, #4ecdc4, #a8e6cf, #ffd3a5, #dda0dd);
        border-radius: 28px;
        z-index: -1;
        background-size: 300% 300%;
        animation: borderGradient 6s ease infinite;
    }
    
    .sentence-display:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 60px rgba(183, 148, 246, 0.3);
    }
    
    .typing-input {
        font-size: 1.3rem !important;
        font-family: 'Courier New', monospace !important;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 50%, #fff5f8 100%) !important;
        border-radius: 20px !important;
        border: 3px solid transparent !important;
        padding: 1.5rem !important;
        box-shadow: 0 8px 30px rgba(195, 217, 255, 0.3) !important;
        transition: all 0.3s ease !important;
        background-clip: padding-box !important;
    }
    
    .typing-input:focus {
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4) !important;
        outline: none !important;
        transform: translateY(-3px) !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #e0f2ff 0%, #d6efff 25%, #cce7ff 50%, #c3d9ff 75%, #bbd1ff 100%);
        padding: 2rem;
        border-radius: 25px;
        text-align: center;
        color: #2d5a87;
        margin: 1rem;
        box-shadow: 0 12px 35px rgba(173, 216, 255, 0.35);
        border: 2px solid rgba(173, 216, 255, 0.5);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent);
        transition: left 0.6s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 50px rgba(173, 216, 255, 0.5);
        border-color: rgba(102, 126, 234, 0.8);
    }
    
    .metric-card h3 {
        color: #4a90e2;
        margin-bottom: 0.8rem;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    .metric-card h2 {
        color: #2d5a87;
        margin: 0;
        font-size: 2.8rem;
        font-weight: 700;
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 1rem 2.5rem;
        border-radius: 35px;
        font-weight: bold;
        margin: 1rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        border: 3px solid rgba(255,255,255,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .difficulty-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        transition: left 0.5s;
    }
    
    .difficulty-badge:hover::before {
        left: 100%;
    }
    
    .difficulty-badge:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }
    
    .easy { 
        background: linear-gradient(135deg, #a8e6cf 0%, #7fcdcd 33%, #88d8a3 66%, #98fb98 100%);
        color: #2d5a3d;
        box-shadow: 0 8px 25px rgba(168, 230, 207, 0.5);
    }
    .medium { 
        background: linear-gradient(135deg, #ffd3a5 0%, #fd9853 33%, #ffb347 66%, #ffa500 100%);
        color: #8b4513;
        box-shadow: 0 8px 25px rgba(255, 211, 165, 0.5);
    }
    .hard { 
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 33%, #fbb6ce 66%, #ff69b4 100%);
        color: #8b2635;
        box-shadow: 0 8px 25px rgba(255, 154, 158, 0.5);
    }
    
    /* Enhanced Streamlit component styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #ff6b9d 75%, #4ecdc4 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 1rem 3rem;
        font-weight: 700;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        background-size: 200% 200%;
        animation: buttonGradient 4s ease infinite;
    }
    
    @keyframes buttonGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.08);
        box-shadow: 0 15px 45px rgba(102, 126, 234, 0.6);
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #ff6b9d 0%, #4ecdc4 20%, #96ceb4 40%, #ffeaa7 60%, #dda0dd 80%, #87ceeb 100%);
        border-radius: 20px;
        height: 15px;
        background-size: 300% 300%;
        animation: progressGradient 3s ease infinite;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    @keyframes progressGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .stSelectbox > div > div > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 50%, #fff0f5 100%);
        border: 3px solid rgba(183, 148, 246, 0.5);
        border-radius: 15px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(183, 148, 246, 0.2);
    }
    
    .stSelectbox > div > div > div:hover {
        border-color: rgba(102, 126, 234, 0.8);
        box-shadow: 0 8px 25px rgba(183, 148, 246, 0.3);
        transform: translateY(-2px);
    }
    
    /* Custom animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 12px 35px rgba(183, 148, 246, 0.3); }
        50% { box-shadow: 0 20px 50px rgba(183, 148, 246, 0.6); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    .glow {
        animation: glow 2s ease-in-out infinite;
    }
    
    /* Additional enhancements */
    .stInfo {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border-left: 5px solid #4ecdc4;
        border-radius: 10px;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #e8f5e8 0%, #f0fff4 100%);
        border-left: 5px solid #96ceb4;
        border-radius: 10px;
    }
    
    .stError {
        background: linear-gradient(135deg, #fce4ec 0%, #fff0f5 100%);
        border-left: 5px solid #ff9a9e;
        border-radius: 10px;
    }
</style>""", unsafe_allow_html=True)

# Enhanced sentences with more variety
sentences = {
    "Easy": [
        "The cat sat on the mat and took a nap.",
        "I love pizza and ice cream on sunny days.",
        "Dogs are fun pets to have at home.",
        "Books help us learn new things every day.",
        "Music makes me happy when I feel sad.",
        "The sun is bright and warm today.",
        "We went to the park to play games.",
        "My friend has a red bike and a blue car.",
        "Rain drops fall from the gray clouds above."
    ],
    "Medium": [
        "The quick brown fox jumps over the lazy dog while wearing sunglasses.",
        "Pizza is the answer to all of life's problems, especially on Monday morning.",
        "Cats secretly rule the world from their cardboard box headquarters.",
        "I tried to catch some fog earlier, but I mist completely!",
        "Coffee is just bean soup that makes you vibrate with productivity.",
        "My keyboard is fluent in typos and autocorrect disasters.",
        "The early bird might get the worm, but the second mouse gets the cheese.",
        "Programming is like writing a book... except if you miss a single comma, the story fails.",
        "Why don't scientists trust atoms? Because they make up everything!"
    ],
    "Hard": [
        "Why do programmers prefer dark mode? Because light attracts bugs & debugging sessions!",
        "The wifi password is 'P@ssw0rd123!' - hidden in the most obvious place, naturally.",
        "Unicorns use Python because it's the most magical programming language (definitely not C++).",
        "Time flies like an arrow; fruit flies like a banana smoothie at 3:14 AM.",
        "My computer has a sense of humor - it laughs at my code errors & syntax mistakes.",
        "Dancing penguins make the best debugging partners, obviously (trust me on this one).",
        "I told my wife she was drawing her eyebrows too high... She looked surprised! 😮",
        "The difference between 'help' and 'hlep' is that one will fix your problem & the other is a typo.",
        "Life is like JavaScript: full of unexpected behavior, but somehow it still works! 🤷‍♂️"
    ]
}

def calculate_performance_feedback(difficulty, wpm, accuracy):
    """Calculate performance feedback based on difficulty level"""
    if difficulty == "Easy":
        if wpm >= 40 and accuracy >= 95:
            return "🌟 Excellent! Ready for medium difficulty?"
        elif wpm >= 25 and accuracy >= 90:
            return "👍 Good job! Keep practicing!"
        else:
            return "💪 Keep practicing to improve your speed and accuracy!"
    elif difficulty == "Medium":
        if wpm >= 35 and accuracy >= 92:
            return "🔥 Outstanding! Try hard difficulty for a challenge!"
        elif wpm >= 22 and accuracy >= 87:
            return "✨ Well done! You're getting better!"
        else:
            return "📈 Good effort! Practice makes perfect!"
    else:  # Hard
        if wpm >= 30 and accuracy >= 90:
            return "🏆 Master level! You're a typing champion!"
        elif wpm >= 20 and accuracy >= 85:
            return "⭐ Impressive! You're handling the complexity well!"
        else:
            return "🎯 Challenging level! Keep pushing your limits!"

def main():
    # Cool animated header
    st.markdown('<h1 class="main-header">⚡ TypeRacer Pro ⚡</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🚀 Test your typing speed with style! 🚀</p>', unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize session state
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'sentence' not in st.session_state:
        st.session_state.sentence = ""
    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0.0
    if 'results' not in st.session_state:
        st.session_state.results = []
    if 'high_score' not in st.session_state:
        st.session_state.high_score = {'wpm': 0, 'accuracy': 0}
    if 'timer_active' not in st.session_state:
        st.session_state.timer_active = False
    
    # Cool sidebar
    with st.sidebar:
        st.markdown("### 🎮 Game Control Center")
        
        # Difficulty selection with cool badges
        st.markdown("#### 🎯 Select Difficulty")
        difficulty = st.radio(
            "Choose your challenge:",
            ["Easy", "Medium", "Hard"],
            format_func=lambda x: f"{'🟢' if x == 'Easy' else '🟡' if x == 'Medium' else '🔴'} {x}",
            horizontal=True
        )
        
        # Display difficulty info with styled badges
        difficulty_info = {
            "Easy": ("🟢 Beginner friendly", "Simple words, perfect for warming up"),
            "Medium": ("🟡 Getting serious", "Punctuation and longer sentences"),
            "Hard": ("🔴 Expert mode", "Special characters and complex text")
        }
        
        badge_class = difficulty.lower()
        st.markdown(f'<div class="difficulty-badge {badge_class}">{difficulty_info[difficulty][0]}</div>', 
                   unsafe_allow_html=True)
        st.caption(difficulty_info[difficulty][1])
        
        # Start game button with animation
        start_clicked = st.button("🚀 Launch Game", type="primary", use_container_width=True)
        
        # Display high scores in sidebar
        if st.session_state.high_score['wpm'] > 0:
            st.markdown("### 🏆 Personal Best")
            st.metric("Best WPM", st.session_state.high_score['wpm'])
            st.metric("Best Accuracy", f"{st.session_state.high_score['accuracy']}%")
    
    # Start new game
    if start_clicked:
        st.session_state.sentence = random.choice(sentences[difficulty])
        st.session_state.game_active = True
        st.session_state.start_time = 0.0
        st.session_state.difficulty = difficulty
        st.rerun()
    
    # Main game area
    if st.session_state.game_active:
        # Game container with glass effect
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Display difficulty badge
        badge_class = st.session_state.difficulty.lower()
        st.markdown(f'''
            <div style="text-align: center; margin-bottom: 1rem;">
                <span class="difficulty-badge {badge_class} pulse">
                    🎮 {st.session_state.difficulty.upper()} MODE
                </span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Display the sentence with cool styling
        st.markdown(f'''
            <div class="sentence-display glow">
                <div style="margin-bottom: 0.5rem; color: #4ecdc4; font-size: 1rem;">
                    📝 TYPE THIS SENTENCE:
                </div>
                {st.session_state.sentence}
            </div>
        ''', unsafe_allow_html=True)
        
        # Text input for typing with custom styling
        typed_text = st.text_area(
            "Start typing here:",
            key="typing_input",
            placeholder="🎯 Click here and start typing! Your timer starts automatically...",
            height=100,
            label_visibility="collapsed"
        )
        
        # Start timing when user begins typing
        if typed_text and st.session_state.start_time == 0.0:
            st.session_state.start_time = time.time()
        
        # Real-time feedback with cool progress bar
        if typed_text:
            # Calculate progress
            progress = min(len(typed_text) / len(st.session_state.sentence), 1.0)
            
            # Custom progress bar
            progress_html = f"""
                <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 5px; margin: 1rem 0;">
                    <div style="background: linear-gradient(90deg, #4ecdc4, #44a08d); height: 20px; 
                                border-radius: 7px; width: {progress*100}%; transition: width 0.3s ease;
                                display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                        {int(progress * 100)}% Complete
                    </div>
                </div>
            """
            st.markdown(progress_html, unsafe_allow_html=True)
            
            # Check if completed
            if typed_text.strip() == st.session_state.sentence:
                end_time = time.time()
                time_taken = end_time - st.session_state.start_time
                
                # Calculate metrics
                words = len(st.session_state.sentence.split())
                wpm = round(words / (time_taken / 60), 2)
                accuracy = 100.0  # Perfect match
                
                # Update high scores
                if wpm > st.session_state.high_score['wpm']:
                    st.session_state.high_score['wpm'] = wpm
                if accuracy > st.session_state.high_score['accuracy']:
                    st.session_state.high_score['accuracy'] = accuracy
                
                # Celebration animation
                st.balloons()
                st.success("🎉 PERFECT! You nailed it! 🎉")
                
                # Display results with cool metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f'''
                        <div class="metric-card">
                            <h3>⏱️</h3>
                            <h2>{round(time_taken, 2)}s</h2>
                            <p>Time Taken</p>
                        </div>
                    ''', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'''
                        <div class="metric-card">
                            <h3>💨</h3>
                            <h2>{wpm}</h2>
                            <p>Words/Min</p>
                        </div>
                    ''', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'''
                        <div class="metric-card">
                            <h3>🎯</h3>
                            <h2>{accuracy}%</h2>
                            <p>Accuracy</p>
                        </div>
                    ''', unsafe_allow_html=True)
                with col4:
                    st.markdown(f'''
                        <div class="metric-card">
                            <h3>📊</h3>
                            <h2>{len(st.session_state.sentence.split())}</h2>
                            <p>Words</p>
                        </div>
                    ''', unsafe_allow_html=True)
                
                # Performance feedback with emojis
                feedback = calculate_performance_feedback(st.session_state.difficulty, wpm, accuracy)
                st.info(f"💬 {feedback}")
                
                # Save results
                result = {
                    "difficulty": st.session_state.difficulty,
                    "time": round(time_taken, 2),
                    "wpm": wpm,
                    "accuracy": accuracy,
                    "sentence": st.session_state.sentence,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.results.append(result)
                st.session_state.game_active = False
                
            else:
                # Show live accuracy and visual feedback
                correct_chars = sum(1 for a, b in zip(typed_text, st.session_state.sentence) if a == b)
                current_accuracy = round((correct_chars / len(st.session_state.sentence)) * 100, 2)
                
                # Live stats
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("⚡ Live Accuracy", f"{current_accuracy}%")
                with col2:
                    if st.session_state.start_time > 0:
                        elapsed = time.time() - st.session_state.start_time
                        st.metric("⏱️ Elapsed Time", f"{round(elapsed, 1)}s")
                    else:
                        st.metric("⏱️ Elapsed Time", "0.0s")
                
                # Visual typing feedback
                display_html = "<div style='font-family: monospace; font-size: 1.1rem; padding: 1rem; background: rgba(0,0,0,0.7); border-radius: 10px; margin: 1rem 0;'>"
                
                for i, char in enumerate(typed_text):
                    if i < len(st.session_state.sentence):
                        if char == st.session_state.sentence[i]:
                            display_html += f"<span style='color: #4ecdc4; background: rgba(78, 205, 196, 0.2);'>{char}</span>"
                        else:
                            display_html += f"<span style='color: #ff6b6b; background: rgba(255, 107, 107, 0.2);'>{char}</span>"
                    else:
                        display_html += f"<span style='color: #ffa500; background: rgba(255, 165, 0, 0.2);'>{char}</span>"
                
                # Show remaining characters in gray
                if len(typed_text) < len(st.session_state.sentence):
                    remaining = st.session_state.sentence[len(typed_text):]
                    display_html += f"<span style='color: #666;'>{remaining}</span>"
                
                display_html += "</div>"
                st.markdown("**Live Preview:**", help="Green = correct, Red = wrong, Orange = extra")
                st.markdown(display_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        # Welcome screen when no game is active
        st.markdown("""
            <div class="game-container" style="text-align: center;">
                <h2 style="color: white; margin-bottom: 2rem;">🎮 Ready to Test Your Typing Skills? 🎮</h2>
                <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
                    <div style="text-align: center;">
                        <div style="font-size: 3rem;">🟢</div>
                        <h4 style="color: #4CAF50;">Easy Mode</h4>
                        <p style="color: #ccc;">Perfect for beginners</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 3rem;">🟡</div>
                        <h4 style="color: #FF9800;">Medium Mode</h4>
                        <p style="color: #ccc;">Step up the challenge</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 3rem;">🔴</div>
                        <h4 style="color: #F44336;">Hard Mode</h4>
                        <p style="color: #ccc;">For typing masters</p>
                    </div>
                </div>
                <p style="color: #ccc; font-size: 1.1rem;">Choose your difficulty and click "Launch Game" to begin!</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Results history with cool charts
    if st.session_state.results:
        st.markdown("---")
        st.markdown('<div class="stats-container">', unsafe_allow_html=True)
        st.markdown("## 📊 Your Performance Dashboard")
        
        # Create performance charts
        col1, col2 = st.columns(2)
        
        with col1:
            # WPM over time chart
            if len(st.session_state.results) > 1:
                wpm_data = [r['wpm'] for r in st.session_state.results]
                fig_wpm = go.Figure()
                fig_wpm.add_trace(go.Scatter(
                    y=wpm_data,
                    mode='lines+markers',
                    line=dict(color='#4ecdc4', width=3),
                    marker=dict(size=8, color='#4ecdc4'),
                    name='WPM'
                ))
                fig_wpm.update_layout(
                    title="💨 WPM Progress",
                    yaxis_title="Words Per Minute",
                    xaxis_title="Game Number",
                    template="plotly_dark",
                    height=300
                )
                st.plotly_chart(fig_wpm, use_container_width=True)
        
        with col2:
            # Difficulty distribution pie chart
            difficulty_counts = {}
            for result in st.session_state.results:
                diff = result['difficulty']
                difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
            
            if difficulty_counts:
                fig_pie = go.Figure(data=[go.Pie(
                    labels=list(difficulty_counts.keys()),
                    values=list(difficulty_counts.values()),
                    hole=0.4,
                    marker_colors=['#4CAF50', '#FF9800', '#F44336']
                )])
                fig_pie.update_layout(
                    title="🎯 Difficulty Distribution",
                    template="plotly_dark",
                    height=300
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        # Summary statistics
        avg_wpm = sum(r['wpm'] for r in st.session_state.results) / len(st.session_state.results)
        avg_accuracy = sum(r['accuracy'] for r in st.session_state.results) / len(st.session_state.results)
        total_games = len(st.session_state.results)
        best_wpm = max(r['wpm'] for r in st.session_state.results)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'''
                <div class="metric-card">
                    <h3>🎮</h3>
                    <h2>{total_games}</h2>
                    <p>Games Played</p>
                </div>
            ''', unsafe_allow_html=True)
        with col2:
            st.markdown(f'''
                <div class="metric-card">
                    <h3>⚡</h3>
                    <h2>{round(avg_wpm, 1)}</h2>
                    <p>Avg WPM</p>
                </div>
            ''', unsafe_allow_html=True)
        with col3:
            st.markdown(f'''
                <div class="metric-card">
                    <h3>🎯</h3>
                    <h2>{round(avg_accuracy, 1)}%</h2>
                    <p>Avg Accuracy</p>
                </div>
            ''', unsafe_allow_html=True)
        with col4:
            st.markdown(f'''
                <div class="metric-card">
                    <h3>🏆</h3>
                    <h2>{best_wpm}</h2>
                    <p>Best WPM</p>
                </div>
            ''', unsafe_allow_html=True)
        
        # Recent games table
        st.markdown("### 📈 Recent Games")
        recent_games = st.session_state.results[-5:]
        
        for i, result in enumerate(reversed(recent_games)):
            with st.expander(f"🎮 Game {len(st.session_state.results) - i} - {result['difficulty']} - {result['wpm']} WPM - {result['timestamp']}"):
                st.markdown(f"**📝 Sentence:** _{result['sentence']}_")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("⏱️ Time", f"{result['time']}s")
                with col2:
                    st.metric("💨 WPM", result['wpm'])
                with col3:
                    st.metric("🎯 Accuracy", f"{result['accuracy']}%")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear All History", type="secondary", use_container_width=True):
                st.session_state.results = []
                st.session_state.high_score = {'wpm': 0, 'accuracy': 0}
                st.rerun()
        with col2:
            if st.button("📊 Export Results", type="secondary", use_container_width=True):
                import json
                results_json = json.dumps(st.session_state.results, indent=2)
                st.download_button(
                    "💾 Download JSON",
                    results_json,
                    "typing_results.json",
                    "application/json"
                )
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
