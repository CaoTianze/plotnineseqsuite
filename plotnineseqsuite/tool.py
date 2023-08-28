from typing import List
import matplotlib.pyplot as plt
from PIL import Image
from plotnine import ggplot
import os
from tempfile import TemporaryDirectory
import random

def extract(data: List[str], start: int = None, end: int = None) -> List[str]:
    complete_len = len(data[0])
    if start is None:
        start = 0
    if end is None:
        end = complete_len
    return list(map(lambda x: x[start:end], data))


def arrange(gg1: ggplot, gg2: ggplot, direction: str = 'horizontal', filename: str = None, display: bool = True):
    if direction not in {'vertical', 'horizontal'}:
        raise Exception('"direction" must be vertical or horizontal!')
    if filename is not None and not filename.endswith('.png'):
        raise Exception('"filename" must end with png!')
    with TemporaryDirectory(prefix='p9SeqSuite_') as temp_dir:
        random_num = random.randint(1111,9999)
        gg1.save("%s%s%d%s" % (temp_dir, os.sep, random_num, 'gg1.png'))
        gg2.save("%s%s%d%s" % (temp_dir, os.sep, random_num, 'gg2.png'))
        with Image.open("%s%s%d%s" % (temp_dir, os.sep, random_num, 'gg1.png')) as img1, Image.open(
                "%s%s%d%s" % (temp_dir, os.sep, random_num, 'gg2.png')) as img2:
            if direction == 'horizontal':
                dst_width = img1.width + img2.width
                dst_height = max(img1.height, img2.height)
                coordinate = [(0, 0), (img1.width, 0)]
            else:
                dst_width = max(img1.width, img2.width)
                dst_height = img1.height + img2.height
                coordinate = [(0, 0), (0, img1.height)]
            with Image.new('RGB', (dst_width, dst_height), color='white') as dst:
                dst.paste(img1, coordinate[0])
                dst.paste(img2, coordinate[1])
                if filename is not None:
                    dst.save(filename)
                if display:
                    fig, ax = plt.subplots()
                    ax.set_axis_off()
                    fig.set_size_inches(dst_width / fig.dpi, dst_height / fig.dpi)
                    ax.imshow(dst)