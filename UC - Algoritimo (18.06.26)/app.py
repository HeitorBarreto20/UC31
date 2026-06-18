from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "segredo123"

pratos = [
    {"id": 1, "nome": "Filé mignon ao vinho", "preco": 99.99, "img": "https://www.comidaereceitas.com.br/wp-content/uploads/2012/05/bife-com-crosta-de-pimenta-servido-com-um-molho-de-reducao-de-vinho-vermelho-780x520.jpg"},
    {"id": 2, "nome": "Salmão grelhado", "preco": 149.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2FMhOMJI6yQ9wK6RQzvnNl0_k08n1NxanCg&s"},
    {"id": 3, "nome": "Risoto de camarão", "preco": 199.99, "img": "https://static.itdg.com.br/images/640-400/50d611c5a317e666dc8f9899efaa693b/shutterstock-2018302928-1-1-.jpg"},
    {"id": 4, "nome": "Lagosta Thermidor", "preco": 249.99, "img": "https://festivaisceagesp.com.br/wp-content/webp-express/webp-images/uploads/2020/02/Lagosta-Sapateira-ao-Thermidor-Foto-divulgacao-_MG_5386er.jpg.webp"},
    {"id": 5, "nome": "Tiramisù", "preco": 89.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJSZckj9KR0tGLs81Z7eSzvDf0EwFQOk4zYQ&s"},
    {"id": 6, "nome": "Espresso Martini", "preco": 29.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDM86uut6zd-KN2fL6BBXNXip12iV3Yki8mA&s"},
    {"id": 7, "nome": "Mojito", "preco": 39.99, "img": "https://assets.tmecosys.com/image/upload/t_web_rdp_recipe_584x480_1_5x/img/recipe/ras/Assets/3279978A-FC6C-4231-A42C-DF759994C99C/Derivates/4278FB29-8E6B-4986-BF60-231C91231A01.jpg"},
    {"id": 8, "nome": "Margarita", "preco": 14.99, "img": "https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/tk%2Fphoto%2F2025%2F06-2025%2F2025-06-WC-whipped-margarita%2FWC-whipped-margarita-107"},
    {"id": 9, "nome": "Spritz de limão", "preco": 19.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOlBuOZJh4p8uIjIt2VnxbD2l-XRMDOEabGw&s"},
    {"id": 10, "nome": "Água com limão", "preco": 9.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR-bJJRhIczlYf-vi-4UmeCZHc4b2eO58v5g&s"},
    {"id": 11, "nome": "Tiramisù clássico", "preco": 49.99, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnA3v9vegPxi9aYTEcH0f4Xgglw7siHWL2lw&s"},
    {"id": 12, "nome": "Crème brûlée", "preco": 69.99, "img": "https://www.allrecipes.com/thmb/y-S61IJkYyCUjTMGYqkaoJGwBrY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-228515-simple-creme-brulee-dessert-dmfs-4x3-821623e7a86548eeb89370ac23d5f251.jpg"},
    {"id": 13, "nome": "Panna cotta", "preco": 89.99, "img": "https://www.allrecipes.com/thmb/NlP50cO2BjJdN4uGvl5JhW0Rx2A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-72567-Panna-cotta-ddmfs-4x3-14ae724a2a8e4ca3a79c5e27b2b61994.jpg"},
    {"id": 14, "nome": "Mousse de chocolate", "preco": 149.99, "img": "https://www.receitasnestle.com.br/sites/default/files/srh_recipes/369562012750bd46ceaeef5d59a23229.jpg"},
    {"id": 15, "nome": "Cheesecake", "preco": 99.99, "img": "https://www.seriouseats.com/thmb/VAuEFUAePPa4QXEP3dhBHA4RvJA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20250904-SEA-WhiteChocolateCheesecake-LorenaMasso-HERO-206c88529afb4abbb2ca8f114b1d0f2b.jpg"},
]

def get_session(key):
    return session.get(key, [])

def get_pratos_por_ids(ids):
    return [p for p in pratos if p["id"] in ids]

@app.route("/")
def home():
    return redirect(url_for("cardapio"))

@app.route("/cardapio")
def cardapio():
    return render_template(
        "cardapio.html",
        pratos=pratos,
        favoritos=get_session("favoritos"),
        carrinho=get_session("carrinho")
    )

@app.route("/favoritar/<int:id>")
def favoritar(id):
    favoritos = get_session("favoritos")

    if id in favoritos:
        favoritos.remove(id)
    else:
        favoritos.append(id)

    session["favoritos"] = favoritos
    return redirect(url_for("cardapio"))

@app.route("/carrinho/add/<int:id>")
def add_carrinho(id):
    carrinho = get_session("carrinho")
    carrinho.append(id)
    session["carrinho"] = carrinho
    return redirect(url_for("cardapio"))

@app.route("/carrinho/remover/<int:id>")
def remover_carrinho(id):
    carrinho = get_session("carrinho")

    if id in carrinho:
        carrinho.remove(id)

    session["carrinho"] = carrinho
    return redirect(url_for("carrinho"))

@app.route("/carrinho")
def carrinho():
    ids = get_session("carrinho")
    itens = get_pratos_por_ids(ids)

    total = sum(p["preco"] for p in itens)

    return render_template("carrinho.html", itens=itens, total=total)

@app.route("/favoritos")
def favoritos():
    ids = get_session("favoritos")
    itens = get_pratos_por_ids(ids)

    return render_template("favoritos.html", pratos=itens)

if __name__ == "__main__":
    app.run(debug=True)