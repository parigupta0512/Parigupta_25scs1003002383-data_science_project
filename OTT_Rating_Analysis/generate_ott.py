import csv
import random

random.seed(42)

platforms = ['Netflix', 'Amazon Prime', 'Disney+', 'Hulu', 'HBO Max', 'Apple TV+', 'Peacock', 'Paramount+']
genres = ['Drama', 'Comedy', 'Action', 'Thriller', 'Horror', 'Romance', 'Sci-Fi', 'Documentary', 'Animation', 'Crime', 'Fantasy', 'Biography']
content_types = ['Movie', 'Series', 'Mini-Series', 'Documentary', 'Stand-Up Special']
languages = ['English', 'Spanish', 'French', 'Hindi', 'Korean', 'Japanese', 'German', 'Italian', 'Portuguese', 'Mandarin']
countries = ['United States', 'United Kingdom', 'India', 'South Korea', 'Japan', 'France', 'Germany', 'Spain', 'Brazil', 'Canada', 'Australia', 'Mexico']
age_ratings = ['G', 'PG', 'PG-13', 'R', 'TV-MA', 'TV-14', 'TV-PG', 'TV-G']
devices = ['Smart TV', 'Mobile', 'Tablet', 'Laptop', 'Desktop', 'Gaming Console']
subscription_plans = ['Basic', 'Standard', 'Premium']
resolutions = ['SD', 'HD', 'Full HD', '4K']

titles = [
    'The Last Kingdom', 'Midnight Sun', 'Dark Waters', 'Neon City', 'The Forgotten',
    'Crimson Tide', 'Blue Horizon', 'Shadow Protocol', 'The Inheritance', 'Lost Signal',
    'Parallel Lives', 'The Outsider', 'Broken Wings', 'Silent Storm', 'The Reckoning',
    'Ember Falls', 'Cold Case Files', 'The Uprising', 'Vanishing Point', 'Iron Will',
    'The Divide', 'Starfall', 'Echoes of War', 'The Prodigy', 'Burning Bridges',
    'The Awakening', 'Fractured', 'Wildfire', 'The Covenant', 'Phantom Signal',
    'Crossroads', 'The Verdict', 'Shattered Glass', 'Rising Tide', 'The Confession',
    'Darkroom', 'The Heist', 'Frozen in Time', 'The Witness', 'Afterglow',
    'The Conspiracy', 'Borderline', 'The Escape', 'Nightfall', 'The Informant',
    'Deadlock', 'The Pursuit', 'Hollow Ground', 'The Renegade', 'Flashpoint',
    'Neon Lights', 'The Wanderer', 'Broken Chains', 'Silent Echo', 'Iron Fist',
    'Crossfire', 'Shattered', 'Rising Sun', 'Darkroom Files', 'The Heist Plan',
    'The Conspiracy Files', 'Borderline Cases', 'The Great Escape', 'Nightfall City',
    'Deadlock City', 'The Pursuit of Truth', 'Hollow Ground Zero', 'Flashpoint City',
    'Undertow', 'Freefall', 'The Relic', 'Stormfront', 'Endgame',
    'Firestorm', 'Deadfall', 'Shockwave', 'Blowback', 'Meltdown',
    'Fallout', 'Countdown', 'Uprising', 'Backlash', 'Breakdown',
    'Blackout', 'Flashback', 'Burnout', 'Lockdown', 'Standoff',
    'Gridlock', 'Overload', 'Shutdown', 'Reboot', 'Override',
    'Catalyst', 'Threshold', 'Nexus', 'Apex', 'Zenith',
    'Nadir', 'Vertex', 'Axis', 'Orbit', 'Pulse',
    'Signal', 'Frequency', 'Wavelength', 'Spectrum', 'Horizon'
]

rows = []
for i in range(1, 1001):
    base_title = random.choice(titles)
    suffix = f' {random.randint(2, 5)}' if random.random() < 0.2 else ''
    title = base_title + suffix

    platform = random.choice(platforms)
    content_type = random.choice(content_types)
    genre = random.choice(genres)
    language = random.choice(languages)
    country = random.choice(countries)
    age_rating = random.choice(age_ratings)
    release_year = random.randint(2015, 2024)
    release_month = random.randint(1, 12)

    if content_type in ('Movie', 'Stand-Up Special'):
        seasons = ''
        episodes = ''
        runtime_min = random.randint(75, 180)
    elif content_type == 'Mini-Series':
        seasons = 1
        episodes = random.randint(3, 8)
        runtime_min = random.randint(30, 60)
    elif content_type == 'Documentary':
        seasons = random.choice([1, ''])
        episodes = random.randint(1, 10) if seasons == 1 else ''
        runtime_min = random.randint(45, 120)
    else:
        seasons = random.randint(1, 8)
        episodes = seasons * random.randint(6, 24)
        runtime_min = random.randint(22, 60)

    imdb_score = round(random.uniform(4.0, 9.5), 1)
    rotten_tomatoes = random.randint(20, 99)
    audience_score = random.randint(30, 99)

    monthly_views_m = round(random.uniform(0.1, 95.0), 2)
    avg_watch_time_min = round(random.uniform(15, runtime_min), 1)
    completion_rate_pct = round(random.uniform(20, 98), 1)
    rewatches = random.randint(0, 5)

    subscribers_gained = random.randint(0, 500000)
    subscribers_lost = random.randint(0, 100000)
    revenue_usd_m = round(random.uniform(0.05, 50.0), 2)
    production_cost_usd_m = round(random.uniform(0.5, 200.0), 2)

    primary_device = random.choice(devices)
    subscription_plan = random.choice(subscription_plans)
    resolution = random.choice(resolutions)

    user_reviews = random.randint(50, 500000)
    likes = random.randint(100, 2000000)
    shares = random.randint(10, 500000)

    available_in_countries = random.randint(5, 190)
    subtitles_available = random.randint(1, 40)
    dubbed_languages = random.randint(0, 15)

    is_original = random.choice(['Yes', 'No'])
    is_award_winning = random.choice(['Yes', 'No'])
    is_trending = random.choice(['Yes', 'No'])

    rows.append([
        i, title, platform, content_type, genre, language, country,
        age_rating, release_year, release_month,
        seasons, episodes, runtime_min,
        imdb_score, rotten_tomatoes, audience_score,
        monthly_views_m, avg_watch_time_min, completion_rate_pct, rewatches,
        subscribers_gained, subscribers_lost, revenue_usd_m, production_cost_usd_m,
        primary_device, subscription_plan, resolution,
        user_reviews, likes, shares,
        available_in_countries, subtitles_available, dubbed_languages,
        is_original, is_award_winning, is_trending
    ])

headers = [
    'content_id', 'title', 'platform', 'content_type', 'genre', 'language', 'country',
    'age_rating', 'release_year', 'release_month',
    'seasons', 'episodes', 'runtime_min',
    'imdb_score', 'rotten_tomatoes_pct', 'audience_score_pct',
    'monthly_views_millions', 'avg_watch_time_min', 'completion_rate_pct', 'rewatches',
    'subscribers_gained', 'subscribers_lost', 'revenue_usd_millions', 'production_cost_usd_millions',
    'primary_device', 'subscription_plan', 'resolution',
    'user_reviews', 'likes', 'shares',
    'available_in_countries', 'subtitles_available', 'dubbed_languages',
    'is_original', 'is_award_winning', 'is_trending'
]

path = r'c:\Users\anant\OneDrive\Desktop\MovieratingAnalysis\ott_platform_data.csv'
with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print('Done. Rows:', len(rows), '| Columns:', len(headers))
