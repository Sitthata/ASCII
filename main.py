import numpy as np
from PIL import Image
import os
import argparse

ASCII_CHARS = ["@%#*+=-:. ", "@%#*+=-:.  ,", "@%#*+=-:.   ;,_", " .-+=*#%@@", " ,-:.+=*#%@@", "_;,   .-+=*#%@@"]


def scale_image(image, new_width=50):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert("L")


def map_pixels_to_ascii_chars(image, style_index=0):
    pixels = np.array(image)
    ascii_str = ''
    ascii_style = ASCII_CHARS[style_index]
    range_width = 256 // len(ASCII_CHARS)
    for row in pixels:
        for pixel_value in row:
            index = pixel_value // range_width
            if index >= len(ASCII_CHARS):
                index = len(ASCII_CHARS) - 1
            ascii_str += ascii_style[index]
        ascii_str += '\n'
    return ascii_str


def image_to_ascii(image_path, scale=50, style_index=0):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Unable to open image file {image_path}.")
        print(e)
        return
    image = convert_to_grayscale(scale_image(image, scale))
    ascii_str = map_pixels_to_ascii_chars(image, style_index)
    return ascii_str


def print_ascii(image_path, style_index=0, scale=50):
    ascii_str = image_to_ascii(image_path, scale, style_index)
    print(ascii_str)


def save_ascii(image_path, output_path):
    ascii_str = image_to_ascii(image_path)
    with open(output_path, 'w') as f:
        f.write(ascii_str)


def main():
    parser = argparse.ArgumentParser(description='Convert images to ASCII art.')
    parser.add_argument('input_file', help='Input image file')
    parser.add_argument('-o', '--output_file', help='Output text file')
    parser.add_argument('-s', '--style', help='Style index (default: 0)', type=int, default=0)
    parser.add_argument('-w', '--width', help='Output width (default: 50)', type=int, default=50)
    args = parser.parse_args()

    if args.output_file:
        save_ascii(args.input_file, args.output_file)
    else:
        print_ascii(args.input_file, args.style, args.width)


if __name__ == "__main__":
    main()

