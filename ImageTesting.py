from PIL import Image

GPIOIMAGE = Image.open('C:\\Users\\Ziggy\\Desktop\\Desktop Maj\\gpio.png')
ALBUMIMAGE = Image.open('C:\\Users\\Ziggy\\Desktop\\Desktop Maj\\weirdalbum.jpg')

bildSamling = {
    "RPI": GPIOIMAGE.show,
    "ALBUM": ALBUMIMAGE.show
}

imageToShow = bildSamling.get("RPI")

imageToShow()

referenceToFunction = print

## Kommer att printa hejsansvejsan i konsollen

referenceToFunction("HEJSANSVEJSAN")
