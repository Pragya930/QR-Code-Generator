import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=5)

features.add_data('https://uuerp.uttaranchaluniversity.ac.in/Account/Cyborg_StudentMenu')
features.make(fit=True)
generate_image = features.make_image(fill_color="blue",back_color="white")

generate_image.save('image8.png')

import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("Pragyaverma10938@gmail.com")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("mail2.png")


