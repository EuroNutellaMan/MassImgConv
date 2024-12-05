# MassImgConv

This repository has been moved to [codeberg](https://codeberg.org/EuroNutellaMan/MassImgConv)

Mass image converter and resizer that uses Pillow and PyQt6 to make images suitable for telegram stickers.

## Installation

0. Clone this repo and cd into it with:

```
git clone https://github.com/EuroNutellaMan/MassImgConv.git && cd MassImgConv
```

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Setup an alias to more easily run the program (optional):

``` .bashrc
alias massimgconv='python3 /path/to/MassImgConv/MassImgConv.py'
```

## Usage

Run the program with the alias or with thee following code:

```
python3 /path/to/MassImgConv/MassImgConv.py
```

Select the image files you want to convert to png and/or resize.

You will be asked if you want to resize the image to a maximum size allowed by Telegram stickers (512x512).

You will be asked if you want to delete the original picture.

After the two prompts the program will convert the file extension from jpg, jpeg or webp to png, if you said yes it will also resize the image and/or delete the original file.

The new pictures will be saved in the same directory as the old one.
