
import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent / "movies.csv"


def load_movies():
    """Load and validate the movie dataset."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "movies.csv not found. Keep it in the MovieMind folder."
        )

    movies = pd.read_csv(DATA_FILE).fillna("")

    required = [
        "title", "genre", "language", "mood",
        "age_rating", "year", "description"
    ]

    missing = [col for col in required if col not in movies.columns]

    if missing:
        raise ValueError(f"Missing CSV columns: {missing}")

    return movies


def get_recommendations(
    movies,
    genre="Any",
    language="Any",
    mood="Any",
    age_rating="Any",
    limit=10
):
    """
    Rank movies by matching user preferences.
    Exact matches appear first. If no exact matches exist,
    return the closest matches instead of an empty result.
    """

    results = movies.copy()
    results["_score"] = 0

    preferences = {
        "genre": genre,
        "language": language,
        "mood": mood,
        "age_rating": age_rating
    }

    for column, preference in preferences.items():
        if preference != "Any":
            matches = (
                results[column].astype(str).str.casefold()
                == str(preference).casefold()
            )
            results["_score"] += matches.astype(int)

    # Keep only movies with the highest available match score.
    best_score = results["_score"].max()

    if best_score == 0:
        # Nothing matches any selected preference.
        # Show movies from the dataset as fallback suggestions.
        results = results.sample(
            n=min(limit, len(results)),
            random_state=42
        )
    else:
        results = results[results["_score"] == best_score]

        # Show the best matches first, up to the requested limit.
        results = results.sort_values(
            by=["_score", "title"],
            ascending=[False, True]
        ).head(limit)

    results = results.rename(
        columns={"_score": "match_score"}
    )

    return results.reset_index(drop=True)
