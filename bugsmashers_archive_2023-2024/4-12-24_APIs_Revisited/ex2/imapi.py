# to run: py imapi.py
# dependencies: flask, perlin_noise, cv2, numpy

from flask import Flask, send_file
from perlin_noise import PerlinNoise
import cv2
import io
import numpy as np

app = Flask(__name__)

# generate a perlin noise image with defined size and color bands
# then, send file as jpg back to user
# octaves is the number of octaves to use in the perlin noise generation
# higher octaves = noisier image
@app.route('/', defaults={'bands': '3', 'size': '128', 'octaves': '3'})
@app.route('/<bands>', defaults={'size': '128', 'octaves': '3'})
@app.route('/<bands>/<size>', defaults={'octaves': '3'})
@app.route('/<bands>/<size>/<octaves>')
def perlin(size, bands, octaves):
    # restrict input values to valid ranges
    if not size.isdigit():
        size = '128'

    if not bands.isdigit():
        bands = '3'

    if not octaves.isnumeric():
        octaves = '3'

    bands = min(max(int(bands), 1), 3)
    if bands == 2: bands = 3
    size = min(max(int(size), 1), 1024) 
    octaves = min(max(float(octaves), 1), 10)

    # create perlin noise image in np array
    matrix = generate_perlin(size, bands, octaves)

    # send image as jpg back to user
    img = cv2.imencode('.jpg', matrix)[1].tobytes()
    return send_file(io.BytesIO(img), mimetype='image/jpeg')

def generate_perlin(size, bands, octaves):
    # create a new instance of noise for randomness on each query
    noise = PerlinNoise(octaves=octaves)

    matrix = np.zeros((size, size, bands), dtype=np.float32)
    # iterate over each pixel in each color band
    for i in range(size):
        for j in range(size):
            for band in range(bands):
                coord = [i / size, j / size, band / bands]
                matrix[i, j, band] = abs(noise(coord))

    # set color from 0-1 to 0-255
    return (matrix * 255).astype(np.uint8)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
