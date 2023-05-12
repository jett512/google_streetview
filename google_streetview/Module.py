# Import google_streetview for the api module

import google_streetview.api

# Define parameters for street view api
params = [{
  'size': '1920x1080', # max 640x640 pixels
  'location': '29.84458027616346, -97.96978071621939',
  'heading': '151.78',
  'pitch': '-120',
  'key': 'AIzaSyBs541YgMqil11RKj6jgQxHxNXUukljyxY',
  'fov': '120'
}]

# Create a results object
results = google_streetview.api.results(params)

# Download images to directory 'downloads'
results.download_links('download')
