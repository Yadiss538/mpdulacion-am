# Modulación de Amplitud (AM) en Python)

Este repositorio contiene un script en Python diseñado para simular y analizar un sistema de **Modulación de Amplitud (AM)**, enfocado en el estudio de señales y sistemas.

## Propósito del Código
El programa implementa de manera práctica los conceptos fundamentales de las comunicaciones analógicas, realizando las siguientes funciones:
* **Generación de señales:** Crea una señal de mensaje cosenoidal de baja frecuencia ($50\text{ Hz}$) y una onda portadora de alta frecuencia ($1000\text{ Hz}$).
* **Modulación AM:** Aplica la fórmula matemática estándar de modulación utilizando un índice controlado.
* **Simulación de canales reales:** Introduce efectos comunes en los sistemas de comunicación, como ruido gaussiano blanco y atenuación de la señal.
* **Análisis gráfico:** Genera representaciones visuales en el dominio del tiempo (comparando la señal original, la modulada y la afectada por ruido) y en el dominio de la frecuencia mediante la Transformada Rápida de Fourier (FFT).

## Requisitos
Para ejecutar este script en tu computadora, necesitas tener instalado Python junto con las siguientes bibliotecas:
* `NumPy`
* `Matplotlib`

## Ejecución
Puedes correr el script desde tu terminal o entorno de desarrollo con el siguiente comando:
```bash
python am_modulacion.py
