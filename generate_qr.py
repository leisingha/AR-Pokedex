#!/usr/bin/env python3
"""Generate the shareable QR code that links to the deployed WebAR page.

Usage:
    python3 generate_qr.py https://your-deployed-url.example/

Re-run this with your REAL https URL after deploying (see docs/README.md).
AR needs a secure (https) context, so the URL must be https, not a local IP.
"""
import sys
import segno

DEFAULT_URL = "https://REPLACE-WITH-YOUR-DEPLOYED-URL.netlify.app/"

url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
qr = segno.make(url, error="m")
# PNG for embedding / printing
qr.save("img/qr.png", scale=10, border=3, dark="#14171c", light="#ffffff")
# SVG for crisp scaling in the write-up / slides
qr.save("img/qr.svg", scale=10, border=3, dark="#14171c", light="#ffffff")

print(f"QR code written to img/qr.png and img/qr.svg")
print(f"  -> encodes: {url}")
if url == DEFAULT_URL:
    print("  WARNING: this is the placeholder URL. Re-run with your real deployed URL.")
