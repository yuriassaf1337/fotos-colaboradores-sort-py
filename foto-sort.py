# path and str sort
from pathlib import Path
import re
import shutil
folder_path = Path.home() / "Desktop" / "Fotos novas colaborador"
folder_destination = Path.home() / "Desktop" / "Fotos Colaboradores Prontas"
folder_destination.mkdir(parents=True, exist_ok=True)

formatted_files = {}

# pil img compress reqs
from PIL import Image
import os
bytes = 1024 * 1024
max_size_mb = 3.01
max_size_bytes = max_size_mb * bytes

def compress_image(path, output_path=None):
    if output_path is None:
        output_path = path

    img = Image.open(path)
    quality = 85
    step = 5

    while True:
        img.save(output_path, format='JPEG', quality=quality)
        size = os.path.getsize(output_path)

        if size <= max_size_bytes or quality <= 10:
            break
        quality -= step

    final_size_mb = size / (bytes)
    return final_size_mb, quality

# main

for file in folder_path.iterdir():
    if file.is_file():
        raw_name = file.stem.strip()

        # Tira tudo depois de um '-'
        cleaned = re.split(r"\s*-\s*", raw_name)[0]

        # Tira todos (1), (2) etc
        cleaned = re.sub(r"\s*\(\d+\)$", "", cleaned)

        # Tira numeros na final da string
        cleaned = re.sub(r"\s+\d+$", "", cleaned)

        # Checar para arquivos que já estão formatados
        # EX: luiz.filho ; output: Luiz.Filho
        if "." in cleaned and len(cleaned.split()) == 1:
            parts = cleaned.split(".")
            if len(parts) == 2:
                first = parts[0].capitalize()
                last = parts[1].capitalize()
                formatted_name = f"{first}.{last}"
            else:
                formatted_name = parts[0].capitalize()
        else:
            # Dividir em partes
            name_parts = cleaned.split()

            if len(name_parts) >= 2:
                first = name_parts[0].capitalize()
                last = name_parts[-1].capitalize()
                formatted_name = f"{first}.{last}"
            elif len(name_parts) == 1:
                print(f"⚠️ PARSE ERROR (LENGTH IS 1): {raw_name}")
                formatted_name = name_parts[0].capitalize()
            else:
                print(f"⚠️ PARSE ERROR: {raw_name}")
                continue

        size_mb = file.stat().st_size / (bytes)

        # Selecionar o menor arquivo
        if (
            formatted_name not in formatted_files
            or size_mb < formatted_files[formatted_name]["size"]
        ):
            formatted_files[formatted_name] = {"size": size_mb, "file": file.name}


print("\n⚠️ Filtrado:")
for name in sorted(formatted_files):
    data = formatted_files[name]
    file_path = folder_path / data["file"]

    # Apos sortear os menores arquivos, alguns ainda excedem a margem de 3.01mb
    # então, usando compress_image() vamos comprimir se necessário.
    if data["size"] > max_size_mb:
        new_size, quality = compress_image(file_path)
        data["size"] = new_size
        print(f"🔧 arquivo {data['file']} comprimido para {new_size:.2f}MB (quality={quality})")

    print(f"{name} - {data['size']:.2f}MB")

    # Pegar arquivo original e copiar para a paste destino com o nome correto.
    original_path = folder_path / data["file"]
    destination_path = folder_destination / f"{name}.jpg"

    shutil.copy2(original_path, destination_path)
    print(f"✅ {name} copiado para {destination_path.name}")
