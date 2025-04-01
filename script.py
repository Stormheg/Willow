#!/bin/env python3
from io import BytesIO

from willow.image import (
    PNGImageFile,
)
from willow.plugins.wand import WandImage

with open("tests/images/transparent.png", "rb") as f:
    image = WandImage.open(PNGImageFile(f))

    webp_buffer = BytesIO()
    avif_buffer = BytesIO()

    import ipdb; ipdb.set_trace()
    image.save_as_webp(webp_buffer)
    image.save_as_avif(avif_buffer)
    webp_buffer.seek(0)
