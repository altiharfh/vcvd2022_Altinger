import os
import json

import qrcode
# python -m pip install qrcode

from PIL import Image
# python -m pip install pillow

#consts
ICON_SIZE_DEVIDER = 8

json_base_path = os.path.join(os.path.join(os.getcwd(),'examples'),'qrcodedata.json')
with open(json_base_path,'r') as json_file:
    link_base_data = json.load(json_file)

#get image path
image_base_path = os.path.join(os.path.join(os.getcwd(),'examples'),'img')

#creat qr codes
for cur_entry in link_base_data['qrcodedata']:
    
    http_link = cur_entry['link']
    qr_file_name = cur_entry['name']
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(http_link)
    qr.make(fit=True)

    qr_img = qr.make_image( back_color="white").convert('RGB')
    
    icon_path = os.path.join(image_base_path, cur_entry['image'])
    if os.path.exists(icon_path):
        icon_face = Image.open(icon_path)
        icon_face = icon_face.resize((int(round(img.size[1]/ICON_SIZE_DEVIDER)), int(round(qr_img.size[1]/ICON_SIZE_DEVIDER))))
        pos = ((qr_img.size[0] - icon_face.size[0]) // 2, (qr_img.size[1] - icon_face.size[1]) // 2)
        qr_img.paste(icon_face, pos)

    qr_img.save("qr_" + qr_file_name + ".png")
