import pyodide_http
import requests

pyodide_http.patch_all()
file_url = f"{base_url}/data/tarif_kinesitherapeute.json"

response = requests.get(file_url)
therapists = response.json()

if debug:
    print(therapists[0])