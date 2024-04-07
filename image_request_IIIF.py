import requests
import os
import imageio

def download_images(manifest_url, output_folder):
    response = requests.get(manifest_url)
    manifest_data = response.json()

    canvases = manifest_data['sequences'][0]['canvases']

    # Controlla se la cartella di output esiste, altrimenti creala
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for idx, canvas in enumerate(canvases):
        image_url = canvas['images'][0]['resource']['@id']
        image_filename = f"{idx+1}.jpg" 
        image_path = os.path.join(output_folder, image_filename)

        
        image_response = requests.get(image_url)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_response.content)

        print(f"Download completato: {image_filename}")

       
        image = imageio.imread(image_path)


manifest_url = "https://historica.unibo.it/json/iiif/20.500.14008/78706/267587/manifest"
output_folder = "C:/Users/erica/Documenti/immaginiAldrovandi"

# Chiamata alla funzione per scaricare le immagini
download_images(manifest_url, output_folder)
