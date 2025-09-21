import os
from PIL import Image
# Pasta que será acessada
input_folder = r"put your folder here"
# Pasta que será criada após o processamento
output_folder = r"put your output folder here"
# Dimensões da imagem – Full HD (9:16)
height, width = 1920, 1080
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".jpg"):
        in_path = os.path.join(input_folder, file)
        out_path = os.path.join(output_folder, file)
        img = Image.open(in_path)
        img_resized = img.resize((width, height))
        img_resized.save(out_path, quality=95)
        print(f"Processando: {file}")

print("Todas as imagens foram redimensionadas com sucesso")