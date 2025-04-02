import qrcode  

# Lista de modelos con sus URLs
modelos = {
    "ObjetoCubo": "https://renzonius.github.io/museo_AR/cubo.html",
    "ObjetoEsfera": "https://renzonius.github.io/museo_AR/esfera.html",
    "ObjetoCono": "https://renzonius.github.io/museo_AR/cono.html"
}

# Generar QR para cada objeto
for nombre, url in modelos.items():
    qr = qrcode.make(url)  
    qr.save(f"{nombre}_qr.png")  
    print(f"QR generado para {nombre}: {url}")
