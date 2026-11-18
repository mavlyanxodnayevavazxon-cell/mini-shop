from flask import Flask, abort, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Futbolka", "price": 10000, "description": "Paxta"},
    {"id": 2, "name": "Shorty", "price": 15000, "description": "Yengil"},
    {"id": 3, "name": "Krassovka", "price": 20000, "description": "Sport"},
    {"id": 4, "name": "Pamada", "price": 11000, "description": "Beauty"},
    {"id": 5, "name": "Jinsi shim", "price": 180000, "description": "Klassik ko'k jinsi"},
    {"id": 6, "name": "Xudi (Hoodie)", "price": 150000, "description": "Issiq va qulay"},
    {"id": 7, "name": "Kepka", "price": 45000, "description": "Yozgi quyoshdan himoya"},
    {"id": 8, "name": "Ryukzak", "price": 130000, "description": "O'qish va sayohat uchun"},
    {"id": 9, "name": "Soat", "price": 220000, "description": "Zamonaviy qo'l soati"},
    {"id": 10, "name": "Ko'zoynak", "price": 60000, "description": "Quyoshdan saqlovchi"},
    {"id": 11, "name": "Kurtka", "price": 320000, "description": "Kuzgi-qishki yomg'irga chidamli"},
    {"id": 12, "name": "Paypoq (3 juft)", "price": 25000, "description": "100% tabiiy paxta"},
    {"id": 13, "name": "Kamar", "price": 75000, "description": "Charm klassik kamar"},
    {"id": 14, "name": "Atir (Parfyum)", "price": 190000, "description": "Yoqimli va uzoq turuvchi hid"}
]

def find_product(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)

@app.template_filter("money")
def money(value):
    """120000 -> 120 000 sum"""
    return f"{value:,}".replace(",", " ") + " sum"

@app.route("/")
def home():
    q = request.args.get("q", "").strip()
    if q:
        filtered = [p for p in PRODUCTS if q.lower() in p["name"].lower() or q.lower() in p["description"].lower()]
    else:
        filtered = PRODUCTS[:3]
    return render_template("index.html", featured=filtered, q=q)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    q = request.args.get("q", "").strip()
    if q:
        filtered = [p for p in PRODUCTS if q.lower() in p["name"].lower() or q.lower() in p["description"].lower()]
    else:
        filtered = PRODUCTS
    return render_template("products.html", products=filtered, q=q)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = find_product(product_id)
    if not product:
        abort(404)
    return render_template("product_detail.html", product=product)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)

    


 
 
