import os
import shutil
import random
from pathlib import Path

def sample_mura_data(src_dir, dest_dir, body_parts=None, n_patients=3, n_images=2):
    src = Path("/Users/alvarosanchez/Downloads/MURA-v1.1")  
    dest = Path("src/data_sample")
    body_parts = body_parts or ["XR_ELBOW", "XR_WRIST"]
    total_images = 0

    for split in ["train", "valid"]:
        for part in body_parts:
            part_src = src / split / part
            part_dst = dest / split / part
            if not part_src.exists():
                print(f"⚠️ No existe: {part_src}")
                continue

            patients = list(part_src.glob("patient*"))
            selected_patients = random.sample(patients, min(n_patients, len(patients)))
            for patient in selected_patients:
                study_dirs = list(patient.glob("*"))
                for study in study_dirs:
                    study_rel = study.relative_to(src)
                    dst_study = dest / study_rel
                    dst_study.mkdir(parents=True, exist_ok=True)
                    images = list(study.glob("*.png"))
                    selected_imgs = random.sample(images, min(n_images, len(images)))
                    for img in selected_imgs:
                        shutil.copy(img, dst_study / img.name)
                        total_images += 1

    print(f"🎉 Listo: {total_images} imágenes copiadas a `{dest}`.")

# 🧠 Ruta a tu dataset original completo
SOURCE_DIR = "/Users/alvarosanchez/Descargas/MURA-v1.1"  # <-- Cámbialo si está en otro sitio

# 📂 Carpeta donde guardarás la muestra
DEST_DIR = "src/data_sample"

print("✅ Creando muestra reducida de MURA...")
sample_mura_data(
    src_dir=SOURCE_DIR,
    dest_dir=DEST_DIR,
    body_parts=["XR_ELBOW", "XR_WRIST"],
    n_patients=3,
    n_images=2
)
