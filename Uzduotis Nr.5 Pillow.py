from PIL import Image, ImageEnhance

im = Image.open('ktm.jpg')
im = ImageEnhance.Contrast(im)
naujas = im.enhance(2)
naujas.save('ktm_contrast.jpg')






