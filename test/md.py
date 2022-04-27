import io

from PIL import Image
from httpx import get

param = {"md": "## Hello World\n\nThis is a test."}

res = get("http://127.0.0.1:8080/md/", params=param)

img = get(res.json()["img_url"])

img = Image.open(io.BytesIO(img.content))
img.save("test.png")
