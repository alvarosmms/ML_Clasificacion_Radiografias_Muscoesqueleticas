# 🩻 Clasificación de Radiografías Musculoesqueléticas con Deep Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/PyTorch-%3E=2.0-orange)](https://pytorch.org/)
[![Status](https://img.shields.io/badge/status-Completado-brightgreen.svg)]()
[![Modelo](https://img.shields.io/badge/modelo-ResNet18-blueviolet)]()



🇬🇧 Looking for the English version? 👉 [README_EN.md](README_EN.md)


Este proyecto aplica técnicas de Deep Learning para clasificar radiografías musculoesqueléticas como **normales** o **anormales**. Está diseñado como una herramienta experimental de apoyo al diagnóstico médico, utilizando un enfoque basado en transfer learning.

---

## 🎯 Problema a resolver

Los profesionales sanitarios se enfrentan diariamente al análisis de miles de radiografías. Este proceso es **lento, repetitivo y propenso a errores humanos**. El objetivo de este proyecto es crear un modelo que, dado el input de una radiografía, sea capaz de predecir si contiene una anomalía estructural o no.

Esto no pretende sustituir al profesional médico, sino actuar como un sistema de **asistencia inicial** que pueda ayudar a priorizar o detectar automáticamente casos potencialmente patológicos.

---

## 🗂️ Dataset utilizado

- **Nombre**: MURA (Musculoskeletal Radiographs)
- **Fuente**: [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/mura/)
- **Tipo**: Dataset **público y gratuito** para investigación
- **Contenido**:
  - Más de 40.000 imágenes radiográficas
  - 7 regiones anatómicas (hombro, codo, muñeca, etc.)
  - Etiquetas por estudio: `positive` (anormal), `negative` (normal)
- **Tratamiento**:
  - Se creó un **dataset personalizado** que ignora la parte del cuerpo y agrupa las imágenes únicamente por su condición (`positive` o `negative`)
  - Se detectó un claro **desbalance de clases** a favor de las imágenes normales

---

## 🧠 Solución adoptada

El enfoque del proyecto combina prácticas modernas de Deep Learning en visión por computador:

- Modelo base: `ResNet18` preentrenado en ImageNet
- Fine-tuning parcial: solo se descongelan las capas más profundas (`layer3`, `layer4`, `fc`)
- Aumentos de datos: rotación, recorte aleatorio, jitter de color, etc.
- Manejo de desbalance:
  - Ponderación de clases en la función de pérdida (`CrossEntropyLoss`)
  - F1-score como métrica principal de evaluación
- Early stopping y reducción automática del learning rate con `ReduceLROnPlateau`
- Visualización de imágenes mal clasificadas para análisis cualitativo
- Guardado del modelo entrenado en formato `.joblib` para futuras predicciones

---

## 📁 Estructura del repositorio

```plaintext
src/
│   ├── data_sample/        # Subconjunto de datos ligeros
│   ├── img/                # Imágenes necesarias para el proyecto o visualizaciones
│   ├── notebooks/          # Notebooks usados para pruebas y desarrollo exploratorio
│   ├── results_notebook/   # Notebook final, limpio y reproducible con el modelo entrenado
│   ├── models/             # Modelos guardados (state_dict en .pt o .joblib)
│   └── utils/              # Funciones auxiliares, módulos personalizados y clases

```

📌 *Nota*: Los archivos con los datos completos no se han subido a GitHub, pero pueden ser encontrados en [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/mura/) .

---

## 🧪 Resultados

El modelo entrenado obtiene buenos resultados en F1-score sobre el conjunto de validación, mostrando buena capacidad para detectar casos positivos pese al desbalance.  
Se incluye una matriz de confusión, reporte de métricas y visualización de los errores cometidos.

---

## 🚀 Ejecución

Para entrenar o evaluar el modelo, asegúrate de:

1. Tener los datos preparados en `src/data_sample/` o tu ruta completa al dataset MURA
2. Ejecutar el notebook dentro de `results_notebook/`
3. Consultar los pesos entrenados dentro de `src/models/`

---

## 👨‍⚕️ Disclaimer

Este proyecto es solo con fines educativos y de investigación. **No debe utilizarse para diagnósticos clínicos reales** sin validación rigurosa por parte de profesionales médicos.

---

## ✍️ Autor

Álvaro Sánchez Martín
