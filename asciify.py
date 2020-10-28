from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import tkinter
from tkinter import filedialog

def getAsciiChar(h):
    char_arr = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    return char_arr[math.floor(h * (len(char_arr)/256))]

def main():
    print("Welcome to asciify.")
    print("For reasons currently unknown, this script will convert an input image into greyscale ascii on a per pixel basis.")
    print("For best results use a relatively low resolution image.")
    root = tkinter.Tk()
    root.withdraw()

    print("Please select an input image...")
    file_path = filedialog.askopenfilename(title="Select input image to convert", filetypes=[("JPEG", "*.jpg"), ("JPEG", "*.jpeg")], multiple=False)
    image = Image.open(file_path)
    print("Image opened successfully.")

    scale_factor = 0.8
    char_width = 10
    char_height = 18
    width, height = image.size
    
    print("Resizing...")
    image = image.resize((int(scale_factor * width),int(scale_factor * height * (char_width / char_height))), Image.NEAREST)
    width, height = image.size
    pixels = image.load()

    font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
    output_image = Image.new('RGB',(char_width * width, char_height * height), color = (0, 0, 0))
    draw = ImageDraw.Draw(output_image)

    print("Now converting " + file_path + "...")

    for i in range(height):
        for j in range(width):
            r,g,b = pixels[j, i]
            grey = int((r/3 + g/3 + b/3))
            pixels[j, i] = (grey, grey, grey)
            draw.text((j * char_width, i * char_height), getAsciiChar(grey), font = font, fill = (r,g,b))

    print("Conversion complete, please select a save location...")
    output_image.save(filedialog.asksaveasfilename(title="Save converted image", filetypes=[("JPEG", "*.jpg"), ("JPEG", "*.jpeg")], defaultextension=".jpg"))
    print("Done.")


if __name__ == "__main__":
    main()