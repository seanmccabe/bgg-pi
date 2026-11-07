"""Constants for bgg-pi."""

BGG_URL = "https://boardgamegeek.com"
BASE_URL = f"{BGG_URL}/xmlapi2"
DEFAULT_USER_AGENT = "bgg-pi/0.1.2 (+https://github.com/seanmccabe/bgg-pi)"
API_HEADERS = {
    "User-Agent": DEFAULT_USER_AGENT,
    "Accept": "application/xml",
}
