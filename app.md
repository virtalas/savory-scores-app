# Savory Scores: App Store listing & keyword research

_Pulled 2026-10-28 from App Store Connect (bundle `savory-scores.SavoryScores`) and the iTunes lookup API._

## Listing facts

| Field | Value |
|---|---|
| App name | Savory Scores |
| App Store ID | 6499091159 |
| Bundle ID | savory-scores.SavoryScores |
| App Store URL | https://apps.apple.com/fi/app/savory-scores/id6499091159 |
| Developer | Lasse Virtanen |
| Category | Food & Drink |
| Price | Free |
| Rating | ★ 5.0 (2 ratings, FI) |
| Age rating | 12+ |
| Requires | iOS 18.0 or later (iPhone & iPad) |
| Size | ~8.2 MB |
| Languages | English, Finnish, Japanese |
| First release | 2025-05-30 |
| Current version | 10 (2025-12-07): "Fix animation for adding a review." |
| Support URL | https://virtalas.github.io/savory-scores-app/ |
| Marketing URL | _(not set; point it at the new landing page once it's live)_ |
| Promotional text | _(not set)_ |

**Audience:** people who eat Japanese food in **Helsinki / Finland**: locals, Japanese expats and residents, students, and visitors planning a trip. The app is useless outside Finland, so every marketing surface should say "Helsinki" or "Finland".

## Metadata per locale

### en-US
- **Subtitle:** Japanese food in Helsinki
- **Keywords (46/100 chars used):** `authentic,asian,cuisine,restaurant,ramen,sushi`

### fi
- **Subtitle:** Japanilainen ruoka Helsingissä
- **Keywords:** `autenttinen,aito,aasialainen,ravintola,ramen,sushi`

### ja
- **Subtitle:** ヘルシンキの日本食を発見して評価しよう
- **Keywords:** `本格的,ラーメン,寿司`

## Description (en-US)

> Let's create a catalog for authentic Japanese food in Helsinki!
>
> **DISCOVER**
> – Search by food category to find the best and most authentic meals.
>
> **GIVE SCORES**
> – To rate a meal, just answer one simple question: Would you have it again? Nope. Maybe? Yeah!
> – After rating a few meals in the same category, you can compare them easily.
> – Build your personal top list for each category.
> – Your past ratings will help you choose what to order next time.
>
> **SAVE FOR LATER**
> – Save meals, restaurants, or even entire food categories for later.
>
> Savory Scores is all about sharing the love for authentic Japanese food. But it can also be used for dishes from other cuisines, and even retail items.

## Features (from the description and screenshots)

1. **Search by Japanese food category.** For example "Katsudon" lists every katsudon in Helsinki ranked by score, with photos, restaurant and average score. Each category has a "Read about Katsudon" explainer.
2. **Rate a meal in one tap.** "Would you have it again?" → Nope… / Maybe? / Yeah!
3. **Fine-tune against your past scores.** A slider (e.g. Yeah! 8/10) shows your previous scores in the same category (e.g. Genki Sushi Ebi tempura 7, Ravintola Kamome Yasai-tempura 8), so ratings stay consistent. Also records portion size (small / medium / big).
4. **Rank by authenticity.** Sort a category by an authenticity score as well as taste.
5. **Restaurants and Stores tabs.** Covers restaurant dishes and retail items from Asian/Japanese grocery stores (e.g. East Asia Mart).
6. **All reviews vs. your reviews**, personal top list per category, and saving meals, restaurants and categories for later.
7. Restaurant entries link to the restaurant website and **Open in Maps**.
8. Dark mode supported.

Restaurants visible in the screenshots: Restaurant Kabuki, Ravintola Domo, Koto, Genki Sushi, Saburo Shokudou Ravintola, Fuji Biyori, Natsu Japanilainen Ravintola, East Asia Mart (store), Ravintola Kamome.

## Assets

Downloaded in full resolution from the App Store listing into `website/assets/raw/`:

| File | What |
|---|---|
| `icon-1024.png` | App icon (white cat with an onigiri thought bubble over a red/orange/green score dial) |
| `iphone-1.jpg` | "Search by Japanese food category" (Katsudon list) |
| `iphone-2.jpg` | "Rate meals easily" (Nope / Maybe / Yeah) |
| `iphone-3.jpg` | "Adjust scores in the same category" (slider + previous scores) |
| `iphone-4.jpg` | "Rank by authenticity" (Gyudon list, dark mode) |
| `ipad-1..4.jpg` | iPad versions of the same four |

The website uses the **raw app screens** (no marketing frame) from `~/Pictures/Grafiikka/SavoryScores/screenshots/AppStore/en/pure screenshots/1–4.jpg`, copied to `website/assets/raw/screen-1..4.jpg`. They're published as `website/assets/shot-1..4.webp` (660px wide) and shown inside a CSS phone frame.

Existing repo art: `title_alpha.png` (the "Savory Scores" script wordmark) and `ten_wide_alpha.png` (transparent mascot).

---

# Keyword research

Two different search engines matter here, and they want different keywords:

- **App Store search (ASO):** short, head-term keywords typed into the App Store. Scores below come from aso-connect's `score_keywords_batch` for the **Finnish storefront** (`country=fi`). Popularity and difficulty are aso-connect's 0–100 estimates from App Store search results, not Apple's real search volume. Use them to compare keywords against each other, not as absolute numbers.
- **Google (website SEO):** longer, intent-heavy phrases ("best ramen in Helsinki"). I have no Google volume data. The web priorities below are judged from search intent and from checking the current results pages, which are dominated by generic listicles (Wanderlog, Falstaff, MyHelsinki) and old reviews. Nobody owns the dish-level long tail yet. **Check them in Google Search Console after launch.**

## App Store keyword scores (FI storefront)

| Keyword | Pop | Diff | Opp | Notes |
|---|---:|---:|---:|---|
| japanese restaurant | 67 | 37 | **42** | Best opportunity. Results are mostly games and single-restaurant apps |
| asian food | 71 | 45 | **39** | High volume. Competitors are delivery apps |
| food diary | 61 | 45 | 34 | Health/calorie intent, a weaker fit |
| food journal | 55 | 43 | 31 | Same as above |
| onigiri | 37 | 21 | 29 | In the icon. Cheap win |
| dish tracker | 44 | 37 | 28 | Strong intent fit (Aftertaste, Dishy compete) |
| food rating | 46 | 42 | 27 | Strong intent fit (Beli, Eaten, Yelp) |
| asian grocery | 44 | 39 | 27 | Matches the Stores tab |
| ravintolat helsinki | 49 | 46 | 26 | Finnish, location intent |
| restaurant reviews | 48 | 46 | 26 | |
| restaurant list | 36 | 31 | 25 | |
| food review | 50 | 50 | 25 | |
| helsinki | 52 | 54 | 24 | Already in subtitle |
| izakaya | 34 | 29 | 24 | |
| authentic japanese | 29 | 18 | 24 | Core positioning |
| matcha | 32 | 25 | 24 | |
| japanese food | 36 | 36 | 23 | In subtitle |
| sushi | 54 | 58 | 23 | Hard, games dominate |
| restaurant rating | 34 | 33 | 23 | |
| ravintola | 54 | 58 | 23 | |
| foodie | 43 | 48 | 22 | |
| best ramen / best sushi | 56 / 43 | 62 / 52 | 21 | Hard |
| tempura | 40 | 47 | 21 | |
| ruokapäiväkirja | 36 | 43 | 21 | |
| sushi ravintola | 33 | 39 | 20 | |
| takoyaki | 26 | 24 | 20 | |
| ramen | 40 | 57 | 17 | Hard, games dominate |
| dish rating | 18 | 11 | 16 | |
| udon / donburi / japanese grocery | 16 | 16–17 | 13 | |
| tonkatsu | 12 | 15 | 10 | |
| helsinki restaurants | 11 | 16 | 9 | |
| japanilainen ravintola / ruoka | 6–7 | 19–21 | 5–6 | Low App Store volume, but good on Google |
| ramen helsinki / sushi helsinki | 3–4 | 14–15 | 3 | **Savory Scores already ranks #1–2** |
| katsudon / gyudon / okonomiyaki | 0–2 | – | ~0 | No App Store volume |

### ASO recommendations (en-US; Apple also indexes en-US in Finland)

Suggested subtitle (≤30): `Rate Japanese food in Helsinki` (adds "rate" while keeping both location and cuisine).

Keep `restaurant`, `ramen` and `sushi`. Apple combines words across fields, so `restaurant` + "Japanese" in the subtitle covers **japanese restaurant**, the best opportunity, and the app already ranks for "ramen helsinki" and "sushi helsinki". Drop `cuisine` (low intent). Add the dish-rating and grocery terms. Suggested keyword field (95/100 chars, no words repeated from name/subtitle):

```
restaurant,ramen,sushi,izakaya,onigiri,review,dish,tracker,diary,asian,grocery,authentic,matcha
``` Fill the empty **promotional text** and set the **marketing URL** to the new landing page.

## Website SEO keyword map

Each guide page targets one primary keyword cluster. The home page targets the head terms.

| Page | Primary keyword | Long-tail / secondary | Intent | Priority |
|---|---|---|---|---|
| `/` (home) | Japanese food Helsinki | Japanese food rating app, authentic Japanese food Helsinki app, Savory Scores | Navigational + commercial | ★★★ |
| `guides/japanese-restaurants-helsinki` | Japanese restaurants in Helsinki | best Japanese restaurant Helsinki, authentic Japanese restaurant Helsinki, japanilainen ravintola Helsinki | Commercial, the biggest head term | ★★★ |
| `guides/best-ramen-helsinki` | best ramen in Helsinki | ramen Helsinki, tonkotsu ramen Helsinki, vegan ramen Helsinki, paras ramen Helsinki | Commercial | ★★★ |
| `guides/best-sushi-helsinki` | best sushi in Helsinki | sushi Helsinki, authentic sushi Helsinki, omakase Helsinki, sushi buffet vs sushi bar | Commercial, high volume | ★★★ |
| `guides/japanese-lunch-helsinki` | Japanese lunch in Helsinki | Japanese lunch Helsinki, bento Helsinki, teishoku Helsinki, japanilainen lounas | Commercial, Finnish lunch culture | ★★☆ |
| `guides/authentic-japanese-restaurant` | how to tell if a Japanese restaurant is authentic | authentic Japanese food signs, real Japanese vs. fusion | Informational, evergreen | ★★☆ |
| `guides/donburi-helsinki` | katsudon / gyudon in Helsinki | donburi Helsinki, what is katsudon, oyakodon, unadon, rice bowl Helsinki | Informational + local, zero competition | ★★☆ |
| `guides/izakaya-helsinki` | izakaya in Helsinki | Japanese bar Helsinki, yakitori Helsinki, what is an izakaya | Commercial + informational | ★★☆ |
| `guides/japanese-grocery-helsinki` | Japanese grocery store Helsinki | Asian supermarket Helsinki, where to buy Japanese food Helsinki, onigiri Helsinki | Transactional, local | ★★☆ |
| `guides/japanese-food-finland` | Japanese food in Finland | Japanese food for visitors to Finland, Japanese restaurants Finland, Japanese expats Finland | Informational, travel | ★☆☆ |
| `guides/rate-restaurant-dishes` | food rating app | rate restaurant dishes, dish tracker app, remember what you ordered, restaurant food diary | Commercial (the app category itself) | ★★☆ |

**Why these:** each one either names Helsinki/Finland (so the visitor can actually use the app) or is a dish-level question the app answers better than a listicle ("which katsudon in Helsinki is best?" is literally screenshot 1). Generic global terms ("ramen recipe", "what is sushi") are skipped on purpose: they'd bring traffic that can't use the app.

**Next SEO steps:** Finnish versions of the top three pages (`japanilainen ravintola helsinki`, `paras ramen helsinki`, `sushi helsinki`) and Japanese versions (`ヘルシンキ 日本食`, `ヘルシンキ ラーメン`). Both audiences are large and the app is already localised for them.
