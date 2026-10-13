
import streamlit as st
from recommender import load_movies, get_recommendations

st.set_page_config(
    page_title="MovieMind | Movie Discovery",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PROFESSIONAL UI ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #211637 0%, transparent 35%),
        #0b0d14;
    color: #f5f6fb;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background: #111522;
    border-right: 1px solid #292d3c;
}

.block-container {
    max-width: 1300px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(115deg, #26183f, #171d31 65%, #172238);
    border: 1px solid #40315d;
    border-radius: 24px;
    padding: 35px;
    margin-bottom: 25px;
}

.hero-label {
    color: #c4b5fd;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.hero h1 {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(34px, 4vw, 52px);
    line-height: 1.15;
    font-weight: 800;
    color: white;
    margin: 0 0 14px 0;
}

.hero p {
    color: #c4cada;
    font-size: 16px;
    line-height: 1.7;
    max-width: 680px;
    margin-bottom: 0;
}

.section-heading {
    font-family: 'Manrope', sans-serif;
    color: #f5f6fb;
    font-size: 24px;
    font-weight: 750;
    margin: 25px 0 5px;
}

.section-subtitle {
    color: #9ca5ba;
    font-size: 14px;
    margin-bottom: 18px;
}

.metric-box {
    background: linear-gradient(145deg, #191e2e, #121622);
    border: 1px solid #2b3040;
    border-radius: 16px;
    padding: 20px;
    min-height: 100px;
}

.metric-label {
    color: #a8b0c3;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.metric-number {
    color: white;
    font-family: 'Manrope', sans-serif;
    font-size: 32px;
    font-weight: 800;
    margin-top: 8px;
}

.movie-card {
    background: linear-gradient(145deg, #191e2e, #121622);
    border: 1px solid #2b3040;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 14px;
    min-height: 250px;
}

.movie-card:hover {
    border-color: #8b5cf6;
}

.movie-title {
    font-family: 'Manrope', sans-serif;
    font-size: 20px;
    font-weight: 750;
    color: #ffffff;
    margin-bottom: 7px;
}

.movie-meta {
    color: #c4b5fd;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 12px;
}

.movie-description {
    color: #bdc5d5;
    font-size: 14px;
    line-height: 1.65;
    margin: 12px 0;
}

.tag {
    display: inline-block;
    background: #29203f;
    border: 1px solid #493467;
    color: #ddd6fe;
    padding: 5px 9px;
    border-radius: 7px;
    font-size: 12px;
    margin: 2px 4px 2px 0;
}

.score {
    display: inline-block;
    color: #86efac;
    background: #142c24;
    border: 1px solid #28533e;
    padding: 6px 10px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    margin-top: 5px;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #7c3aed, #6d28d9);
    color: white;
    border: 1px solid #8b5cf6;
    border-radius: 10px;
    font-weight: 700;
    min-height: 43px;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #8b5cf6;
    color: white;
    border-color: #c4b5fd;
}

div[data-baseweb="select"] > div {
    background: #191e2e;
    border-color: #353b4d;
    border-radius: 9px;
}

[data-testid="stMetric"] {
    background: #191e2e;
    border: 1px solid #2b3040;
    border-radius: 14px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #a8b0c3;
}

[data-testid="stMetricValue"] {
    color: white;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    color: #788196;
    text-align: center;
    font-size: 12px;
    padding: 30px 0 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD DATA ----------------
try:
    movies = load_movies()
except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.stop()


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown(
        "<h2 style='color:white;font-family:Manrope'>🎬 MovieMind</h2>",
        unsafe_allow_html=True
    )
    st.caption("YOUR PERSONAL MOVIE DISCOVERY")

    st.markdown("---")
    st.subheader("🎯 Your Preferences")
    st.caption("Customize your movie recommendations.")

    genre = st.selectbox(
        "Preferred genre",
        ["Any"] + sorted(movies["genre"].unique().tolist())
    )

    language = st.selectbox(
        "Preferred language",
        ["Any"] + sorted(movies["language"].unique().tolist())
    )

    mood = st.selectbox(
        "Current mood",
        ["Any"] + sorted(movies["mood"].unique().tolist())
    )

    age_rating = st.selectbox(
        "Age suitability",
        ["Any"] + sorted(movies["age_rating"].unique().tolist())
    )

    recommend_button = st.button(
        "✨ Find My Movies",
        use_container_width=True
    )

    st.markdown("---")
    st.markdown("**How it works**")
    st.caption(
        "MovieMind compares your selected preferences "
        "with the movie dataset and ranks matching movies."
    )

    st.markdown(
        f"<p style='color:#c4b5fd;font-size:13px'>"
        f"● {len(movies)} movies available</p>",
        unsafe_allow_html=True
    )


# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="hero-label">YOUR PERSONAL MOVIE ASSISTANT</div>
    <h1>Find your next<br>favourite movie.</h1>
    <p>
        Less scrolling, more watching. Discover movies that match
        your genre, language, mood, and age suitability.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- DASHBOARD METRICS ----------------
metrics = st.columns(3)

metric_data = [
    ("MOVIES IN COLLECTION", len(movies)),
    ("GENRES TO EXPLORE", movies["genre"].nunique()),
    ("LANGUAGES AVAILABLE", movies["language"].nunique())
]

for column, (label, value) in zip(metrics, metric_data):
    with column:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-label">{label}</div>
                <div class="metric-number">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)


# ---------------- WELCOME SECTION ----------------
if not recommend_button and "recommendations" not in st.session_state:
    st.markdown(
        '<div class="section-heading">Start Exploring</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Your next movie is just a few clicks away.</div>',
        unsafe_allow_html=True
    )

    intro_columns = st.columns(3)

    cards = [
        (
            "🎭 Choose Your Genre",
            "Select a genre that matches your interests and mood."
        ),
        (
            "🧩 Personalize Results",
            "Choose your preferred language and age suitability."
        ),
        (
            "🍿 Discover Movies",
            "Explore recommendations and download your shortlist."
        )
    ]

    for column, (title, description) in zip(intro_columns, cards):
        with column:
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">{title}</div>
                    <div class="movie-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-heading">Explore by Genre</div>',
        unsafe_allow_html=True
    )
    genres = sorted(movies["genre"].astype(str).unique().tolist())
    st.write("  ·  ".join(genres))


# ---------------- RECOMMENDATION LOGIC ----------------
if recommend_button:
    results = get_recommendations(
        movies=movies,
        genre=genre,
        language=language,
        mood=mood,
        age_rating=age_rating
    )

    st.session_state["recommendations"] = results
    st.session_state["selected_preferences"] = {
        "Genre": genre,
        "Language": language,
        "Mood": mood,
        "Age suitability": age_rating
    }


# ---------------- RECOMMENDATION RESULTS ----------------
if "recommendations" in st.session_state:
    results = st.session_state["recommendations"]
    preferences = st.session_state["selected_preferences"]

    st.markdown(
        '<div class="section-heading">🍿 Recommended for You</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-subtitle">'
        'Your personalized movie shortlist.</div>',
        unsafe_allow_html=True
    )

    active_preferences = [
        f"{key}: {value}"
        for key, value in preferences.items()
        if value != "Any"
    ]

    if active_preferences:
        tags = "".join(
            f'<span class="tag">{item}</span>'
            for item in active_preferences
        )
        st.markdown(tags, unsafe_allow_html=True)
    else:
        st.caption("No filters selected. Showing general suggestions.")

    if results.empty:
        st.warning("No movies are available in the dataset.")

    else:
        best_score = int(results["match_score"].max())
        selected_count = sum(
            value != "Any" for value in preferences.values()
        )

        result_metrics = st.columns(3)
        result_metrics[0].metric(
            "Recommendations",
            len(results)
        )
        result_metrics[1].metric(
            "Best match",
            f"{best_score} / 4"
        )
        result_metrics[2].metric(
            "Preferences selected",
            f"{selected_count} / 4"
        )

        if best_score == 4:
            st.success("Excellent! These movies match all four preferences.")
        elif best_score > 0:
            st.info(
                "No exact combination was available. "
                "Showing movies with the highest match score."
            )
        else:
            st.info(
                "No selected preference matched. "
                "Showing general movie suggestions."
            )

        st.markdown("<br>", unsafe_allow_html=True)

        for start in range(0, len(results), 2):
            columns = st.columns(2)

            for offset, column in enumerate(columns):
                index = start + offset

                if index >= len(results):
                    continue

                movie = results.iloc[index]

                with column:
                    st.markdown(
                        f"""
                        <div class="movie-card">
                            <div class="movie-title">
                                🎬 {movie["title"]}
                            </div>
                            <div class="movie-meta">
                                {movie["year"]} &nbsp; • &nbsp; {movie["genre"]}
                            </div>
                            <span class="tag">{movie["language"]}</span>
                            <span class="tag">{movie["mood"]}</span>
                            <span class="tag">Age: {movie["age_rating"]}</span>
                            <div class="movie-description">
                                {movie["description"]}
                            </div>
                            <span class="score">
                                ✓ {int(movie["match_score"])} of 4 preferences matched
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        download_data = results.drop(
            columns=["match_score"]
        ).to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download Recommendations (CSV)",
            data=download_data,
            file_name="movie_recommendations.csv",
            mime="text/csv"
        )


# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class="footer">
        MOVIEMIND · Rule-Based Movie Recommendations<br>
        Built with Python, Pandas and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
