# Japanese UI text for i18n/build.py. App terms match the iOS app's Localizable.xcstrings.


def data_note(n, m, of, stores, k, auth):
    about = {None: "", "dishes": "日本食の", "products": "日本の食品の"}[of]
    where = "店舗" if stores else "か所"
    note = f"2026年10月時点、ヘルシンキ周辺の{m}{where}における{about}評価{n}件に基づいています"
    if k:
        note += f"（{'本格的さの' if auth else ''}評価が{k}件以上のお店のみ）"
    return (note + "。スコアと本格的さは10点満点の平均値です。ほとんどの料理はまだ評価が1〜2件で、メニューも変わるため、"
            "最新のランキングはアプリで確認してください。このリストに載るべきお店で食べましたか？"
            "Savory Scoresで評価しましょう。")


STRINGS = {
    "skip": "本文へスキップ",
    "icon_alt": "Savory Scoresのアプリアイコン",
    "nav_label": "メインメニュー",
    "nav_screenshots": "スクリーンショット",
    "nav_how": "使い方",
    "nav_guides": "ガイド",
    "nav_faq": "よくある質問",
    "nav_cta": "アプリを入手",
    "languages": "言語",
    "footer_tag": "ヘルシンキの本格的な日本食を、料理ごとに評価するカタログ。",
    "footer_label": "フッター",
    "footer_download": "App Storeでダウンロード",
    "terms": "利用規約",
    "privacy": "プライバシーポリシー",
    "made_in": "ヘルシンキ発",
    "read_guide": "ガイドを読む",

    "home_title": "Savory Scores（セイヴァリースコア）：ヘルシンキの美味しい日本食を見つけよう",
    "home_description": "ヘルシンキの本格的な日本食を料理ごとに探せるアプリ。街中のカツ丼、ラーメン、寿司を比べて、"
                        "ワンタップで評価し、自分だけのランキングを作れます。iPhone向けの無料アプリです。",
    "app_ld_description": "ヘルシンキの本格的な日本食のカタログ。食べ物のカテゴリーで検索し、ひとつの質問"
                          "（また注文したいですか？）で料理を評価。本格的さで並べ替えて、自分のランキングを作れます。",

    "breadcrumb_label": "パンくずリスト",
    "home": "ホーム",
    "article_meta": "Savory Scoresガイド · ヘルシンキ · 2026年10月更新",
    "cta_strong": "ヘルシンキでお気に入りの一皿を見つけよう。",
    "cta_text": "Savory ScoresはiPhone・iPad向けの無料アプリ。料理を検索して街中のお店を比べ、ワンタップで評価できます。",
    "badge_alt": "App StoreからSavory Scoresをダウンロード",
    "related": "関連ガイド",
    "colon": "：",
    "more_guides": "その他のガイド",
    "back_home": "← Savory Scoresホーム",
    "next": "次のガイド：{name} →",

    "cities": {"Helsinki": "ヘルシンキ", "Vantaa": "ヴァンター"},
    "data": {
        "kicker": "Savory Scoresのデータより",
        "Photo": "写真",
        "#": "順位",
        "Dish": "料理",
        "Restaurant": "お店",
        "Store": "お店",
        "Product": "商品",
        "Score": "スコア",
        "Authenticity": "本格的さ",
        "Avg score": "平均スコア",
        "Avg authenticity": "平均本格的さ",
        "Ratings": "評価数",
        "Last rated": "最終評価",
        "date": lambda month, year: f"{year}年{month}月",
        "alt": lambda dish, place, city: f"{place}（{city}）の{dish}。Savory Scoresユーザー撮影",
        "note": data_note,
    },

    "guides": {
        "japanese-restaurants-helsinki": {
            "name": "ヘルシンキの日本食レストラン",
            "desc": "寿司カウンターから食堂まで、本格的なお店の見つけ方。フュージョン系ビュッフェとの見分け方も。",
            "title": "ヘルシンキの日本食レストラン：本格的なお店の見つけ方 | Savory Scores",
            "description": "ヘルシンキで美味しい日本食レストランを探すなら。本格的なお店とフュージョン系の見分け方と、"
                           "料理ごとの評価で街中の日本食を比べる方法を紹介します。",
        },
        "best-ramen-helsinki": {
            "name": "ヘルシンキのラーメン",
            "desc": "豚骨、塩、醤油、ヴィーガン。ヘルシンキで美味しい一杯を見つける方法。",
            "title": "ヘルシンキのラーメン：美味しい一杯の見つけ方 | Savory Scores",
            "description": "ヘルシンキで美味しいラーメンを食べたい方へ。現地のラーメン事情、良い一杯の見分け方、"
                           "実際の評価で街中のラーメンを比べる方法を紹介します。",
        },
        "best-sushi-helsinki": {
            "name": "ヘルシンキの寿司",
            "desc": "寿司カウンター、おまかせ、食べ放題。寿司の質の見極め方と、美味しいお店の探し方。",
            "title": "ヘルシンキの寿司：本格的なお寿司と食べ放題の見分け方 | Savory Scores",
            "description": "ヘルシンキで本格的なお寿司を食べるなら。サーモンばかりの食べ放題と寿司カウンターの違い、"
                           "シャリやネタの見極め方、評価の高い寿司を紹介します。",
        },
        "authentic-japanese-restaurant": {
            "name": "本格的な日本食レストランの見分け方",
            "desc": "メニュー、テーブル、お皿に表れる8つのサイン。席に着く前にチェック。",
            "title": "本格的な日本食レストランの見分け方：8つのサイン | Savory Scores",
            "description": "そのお店は本格的な日本食？それともフュージョン？海外の日本食レストランを見分ける8つのサインと、"
                           "ヘルシンキで本格的さの評価が高いお店を紹介します。",
        },
        "donburi-helsinki": {
            "name": "ヘルシンキのカツ丼・牛丼・丼もの",
            "desc": "ヘルシンキの丼もの事情と、日本の味に近い一杯を街中から探す方法。",
            "title": "ヘルシンキのカツ丼・牛丼・丼もの：評価の高い一杯は？ | Savory Scores",
            "description": "ヘルシンキでカツ丼や牛丼が恋しくなったら。現地の丼もの事情、日本の味に近い一杯の見つけ方、"
                           "評価の高い丼を紹介します。",
        },
        "izakaya-helsinki": {
            "name": "ヘルシンキの居酒屋",
            "desc": "ヘルシンキで居酒屋気分を味わうには。何を頼むか、どう楽しむか。",
            "title": "ヘルシンキの居酒屋：焼き鳥・唐揚げ・たこ焼きを楽しむ | Savory Scores",
            "description": "ヘルシンキで居酒屋のような夜を過ごしたい方へ。焼き鳥、唐揚げ、たこ焼きなどの小皿料理と、"
                           "評価の高い居酒屋メニューを紹介します。",
        },
        "japanese-lunch-helsinki": {
            "name": "ヘルシンキの日本食ランチ",
            "desc": "弁当、定食、ラーメン、丼。フィンランドのランチ文化と日本の定食の出会い。",
            "title": "ヘルシンキの日本食ランチ：定食・弁当・ラーメン | Savory Scores",
            "description": "ヘルシンキで日本食ランチを食べるなら。フィンランドのランチ（lounas）の仕組み、"
                           "おすすめの注文、評価の高いランチメニューを紹介します。",
        },
        "japanese-grocery-helsinki": {
            "name": "ヘルシンキの日本食材店",
            "desc": "日本の食材やお菓子が買えるお店と、また買いたいおにぎりや調味料の見つけ方。",
            "title": "ヘルシンキの日本食材店：日本の食品が買えるお店 | Savory Scores",
            "description": "ヘルシンキで日本の食材を買うなら。日本食材の専門店、アジア系スーパー、基本の食材リスト、"
                           "評価の高い商品を紹介します。",
        },
        "japanese-food-finland": {
            "name": "フィンランドの日本食",
            "desc": "旅行者や移住したばかりの方へ。フィンランドの日本食事情と、最初の一歩。",
            "title": "フィンランドの日本食：旅行者・在住者のためのガイド | Savory Scores",
            "description": "フィンランド旅行や移住で日本食が恋しくなったら。日本食のお店がどこにあるか、"
                           "何を期待できるか、Savory Scoresの使い方を紹介します。",
        },
        "rate-restaurant-dishes": {
            "name": "料理を評価するコツ",
            "desc": "お店ではなく料理を評価する理由と、無理なく続けられる「ひとつの質問」の仕組み。",
            "title": "レストランの料理を評価する方法（もう注文に迷わない） | Savory Scores",
            "description": "どの料理が美味しかったか忘れてしまう方へ。「また注文したいですか？」のひとつの質問で"
                           "続けられる食事記録の方法を紹介します。",
        },
    },
}
