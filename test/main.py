from PIL import Image

image = Image.open("cat.jpg")
exifdata = image.getexif()
print(exifdata)
for tag_id, data in exifdata.items():
  print(tag_id, data)
