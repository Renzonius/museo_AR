import qrcode  # type: ignore # Importa la librería para generar códigos QR

url = "https://tusitio.com/modelo3d"  # Enlace al modelo 3D
qr = qrcode.make(url)  # Crea el código QR con la URL
qr.save("modelo3d_qr.png")  # Guarda la imagen del código QR
