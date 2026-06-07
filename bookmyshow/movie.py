from dataclasses import dataclass


@dataclass
class Movie:
    movie_id: str
    title: str
    duration_minutes: int
