
import pyqrcode

from pyqrcode import QRCode
s="https://www.youtube.com/watch?v=4fRhNd22io0"
qr_code=QRCode.create(s)
qr_code.svg("mytube", scale=8)


