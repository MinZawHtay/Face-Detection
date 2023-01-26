import face_recognition
from PIL import Image,ImageDraw

vijay_image= face_recognition.load_image_file('Thalapathy.jpg')
vijay_face_encoding = face_recognition.face_encodings(vijay_image)[0]

dhanush_image= face_recognition.load_image_file('Dhanush.jpg')
dhanush_face_encoding= face_recognition.face_encodings(dhanush_image)[0]

Sathiya = face_recognition.load_image_file('WIN_20230105_10_50_21_Pro.jpg')
Sathiya_face_encoding = face_recognition.face_encodings(Sathiya)[0]

know_face_encoding = [
    vijay_face_encoding,
    dhanush_face_encoding,
    Sathiya_face_encoding
    ]
know_face_names=[
    'vijay',
    'dhanush',
    'Min_Zaw_Htay'
]
unknow_image = face_recognition.load_image_file('thalapathy_vijay.jpg')
face_location= face_recognition.face_locations(unknow_image)
face_encoding=face_recognition.face_encodings(unknow_image,face_location)
pil_image = Image.fromarray(unknow_image)
draw = ImageDraw.Draw(pil_image)
for (top,right,bottom,left),face_encoding in zip(face_location,face_encoding):
    matches=face_recognition.compare_faces(know_face_encoding,face_encoding)

    name = 'Unknown'
    if True in matches:
        first_match_index = matches.index(True)
        name=know_face_names[first_match_index]
        
    draw.rectangle(((left,top),(right,bottom)),outline=(48,63,159))

    text_wight , text_high = draw.textsize(name)
    draw.rectangle(((left,bottom-text_high-10),(right,bottom)),fill=(48,63,159),outline=(48,63,159))
    draw.text((left+6,bottom-text_high-5),name,fill=(255,255,255,0))

del draw
pil_image.show()
