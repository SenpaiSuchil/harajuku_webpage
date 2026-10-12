from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# ============================================
# DATOS MOCK (después vendrán de la DB)
# ============================================
FEATURED_ARTICLE = {
    "slug": "el-regreso-del-gyaru-en-guadalajara",
    "title": "El regreso del Gyaru en Guadalajara",
    "excerpt": "Del kogal noventero al gyaru moderno: cómo una subcultura que parecía extinta está resurgiendo en la escena local con una nueva generación de entusiastas.",
    "image": "mock/fashion-6.jpg",
    "author": "Yuki Tanaka",
    "date": "15 oct 2026",
    "tag": "Gyaru",
    "is_coord": False,
    # Campos que solo se usan en el detalle:
    "body": """
        <p>Introducción larga sobre el regreso del Gyaru en Guadalajara...</p>
        <h2>Un poco de historia</h2>
        <p>Más texto aquí...</p>
        <blockquote>Una cita de alguien de la escena.</blockquote>
        <p>Y así sigue el artículo...</p>
    """,
    "tags": ["gyaru", "gdl", "otonio", "tendencias"],
    "credits": {
        "fotos": "@fotografo_gdl",
        "modelo": "@yuki_gdl",
        "coord": "@quien_armo_el_coord",
    },
}

FASHION_ARTICLES = [
    {
        "slug": "coord-lolita-clasico-en-el-centro",
        "title": "Coord: Lolita clásico en el centro",
        "excerpt": "Un coord armado con piezas de BTSSB e Innocent World, fotografiado en el centro de Guadalajara.",
        "image": "mock/fashion-1.jpg",
        "author": "Mariana R.",
        "date": "12 oct 2026",
        "tag": "Lolita",
        "is_coord": True,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
    {
        "slug": "Como-empezar-en-Decora-sin-morir-en-el-intento",
        "title": "Cómo empezar en Decora sin morir en el intento",
        "excerpt": "Los básicos: colores, capas, accesorios y dónde conseguir piezas sin arruinarte.",
        "image": "mock/fashion-2.jpg",
        "author": "Diego M.",
        "date": "10 oct 2026",
        "tag": "Guías",
        "is_coord": False,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
    {
        "slug": "Coord-Jira-Kei-para-ir-a-un-concierto",
        "title": "Coord: Jirai Kei para ir a un concierto",
        "excerpt": "Un coord oscuro con toques rosa, pensado para aguantar toda la noche de pie en un live.",
        "image": "mock/fashion-3.jpg",
        "author": "Karin S.",
        "date": "08 oct 2026",
        "tag": "Jirai Kei",
        "is_coord": True,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
    {
        "slug": "Visual-Kei-la-subcultura-que-no-muere",
        "title": "Visual Kei: la subcultura que no muere",
        "excerpt": "De X Japan a las bandas locales: por qué el Visual Kei sigue teniendo un lugar en GDL.",
        "image": "mock/fashion-4.jpg",
        "author": "Andrés K.",
        "date": "05 oct 2026",
        "tag": "Visual Kei",
        "is_coord": False,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
    {
        "slug": "Coverage-Meetup-de-otoño-en-Parque-Agua-Azul",
        "title": "Coverage: Meetup de otoño en Parque Agua Azul",
        "excerpt": "Lo que pasó, quién asistió y las mejores fotos del meetup más grande del año.",
        "image": "mock/fashion-5.jpg",
        "author": "Equipo HPGDL",
        "date": "02 oct 2026",
        "tag": "Eventos",
        "is_coord": False,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
    {
        "slug": "Coord-Sweet-Lolita-para-cumpleaños",
        "title": "Coord: Sweet Lolita para cumpleaños",
        "excerpt": "Pasteles, encaje y mucho rosa: un coord dulce para una ocasión especial.",
        "image": "mock/fashion-6.jpg",
        "author": "Sayuri H.",
        "date": "30 sep 2026",
        "tag": "Lolita",
        "is_coord": True,
        "body": "<p>Este coord fue armado para un meetup de la comunidad lolita en el centro...</p>",
        "tags": ["lolita", "coord", "gdl"],
        "credits": {
            "fotos": "@fotografo_gdl",
            "modelo": "@mariana_r",
        },
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fashion')
def fashion():
    return render_template(
        '1_fashion.html',
        featured=FEATURED_ARTICLE,
        articles=FASHION_ARTICLES,
    )

@app.route('/fashion/<slug>')
def fashion_detail(slug):
    # Busca el artículo en los datos mock (después será en la DB)
    all_articles = [FEATURED_ARTICLE] + FASHION_ARTICLES
    article = next((a for a in all_articles if a["slug"] == slug), None)

    if not article:
        # Si no existe, 404 (por ahora podemos redirigir a la lista)
        return "Artículo no encontrado", 404

    # Artículos relacionados: mismo tag, excepto el actual, máximo 3
    related = [a for a in FASHION_ARTICLES if a["tag"] == article["tag"] and a["slug"] != slug][:3]
    # Si no hay suficientes del mismo tag, rellena con otros
    if len(related) < 3:
        extras = [a for a in FASHION_ARTICLES if a["slug"] != slug and a not in related]
        related += extras[:3 - len(related)]

    return render_template(
        '1_fashion_detail.html',
        article=article,
        related=related,
    )

@app.route('/beauty')
def beauty():
    return render_template('2_beauty.html')

@app.route('/vlog')
def vlog():
    return render_template('3_vlog.html')

@app.route('/snap')
def snap():
    return render_template('4_snap.html')

@app.route('/resources')
def resources():
    return render_template('5_resources.html')

@app.route('/magazine')
def magazine():
    return render_template('6_magazine.html')

@app.route('/models')
def models():
    return render_template('7_models.html')

@app.route('/contact')
def contact():
    return render_template('8_contact.html')

@app.route('/shoplist')
def shoplist():
    return render_template('9_shoplist.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)