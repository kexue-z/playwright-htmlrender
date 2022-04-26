from PIL import Image
from httpx import get

param = {"md": "## Hello World\n\nThis is a test."}

res = get("http://127.0.0.1:8080/md/", params=param)

im = Image.open(res.content)
im.save("test.png")
