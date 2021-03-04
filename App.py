from PIL import Image, ImageDraw
import face_recognition

Joao_image = face_recognition.load_image_file('Eu.jpg')
Joao_face_encoding = face_recognition.face_encodings(Joao_image) [0]

known_face_encoding = [
    Joao_face_encoding
]

known_face_names = [
    "João Paes"
]

image = face_recognition.load_image_file('Picture.jpg')

face_locations = face_recognition.face_locations(image)

face_encodings = face_recognition.face_encodings(image, face_locations)

Pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(Pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)

    name = 'Random Person'

    if True in matches:
        firs_match_index = matches.index(True)
        name = known_face_names[firs_match_index]
    
    draw.rectangle(((left, top), (right, bottom)), outline=(0,255,255))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,255), outline=(0,0,255))
    draw.text((left + 10, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw
Pil_image.show()