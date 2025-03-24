import os
import shutil
import random
from pathlib import Path

def crear_test_set(data_dir, output_dir, body_parts=None, n_patients_per_class=1, seed=42):
    """
    Crea una partición de test copiando aleatoriamente pacientes desde 'train/' a 'test/'.
    """
    random.seed(seed)
    data_dir = Path("/Users/alvarosanchez/Downloads/MURA-v1.1")
    output_dir = Path("/Users/alvarosanchez/ONLINE_DS_THEBRIDGE_ALVAROSMMS-1/ML_Clasificacion_Radiografias_Muscoesqueleticas/src/data_sample")
    body_parts = body_parts or ["XR_ELBOW", "XR_WRIST"]

    train_root = data_dir / "train"
    test_root = output_dir / "test"
    test_root.mkdir(parents=True, exist_ok=True)

    total_copiados = 0

    for part in body_parts:
        part_dir = train_root / part
        if not part_dir.exists():
            continue

        patients = list(part_dir.glob("patient*"))
        if len(patients) == 0:
            continue

        selected = random.sample(patients, min(n_patients_per_class, len(patients)))
        for patient in selected:
            # Copiar todo el paciente
            destino = test_root / part / patient.name
            shutil.copytree(patient, destino)
            total_copiados += 1

    return total_copiados

# Ejecutamos la función
test_created = crear_test_set(
    data_dir="src/data_sample",
    output_dir="src/data_sample",
    body_parts=["XR_ELBOW", "XR_WRIST"],
    n_patients_per_class=1
)

test_created