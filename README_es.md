# Project Report Markdown Manager

## Descripción del proyecto 📝

Este proyecto facilita la creación de informes de ingeniería de software según la estructura académica utilizada en los cursos de Aplicaciones Web y Desarrollo de Aplicaciones Open Source. Su objetivo es permitir que los estudiantes trabajen más fácilmente en secciones individuales de un informe al usar branches, manteniendo un formato estándar y asegurando la correcta integración del contenido en un único documento final al realizar three-way merging.

El programa toma secciones individuales escritas en Markdown, las organiza en un orden predefinido y las combina en un archivo final llamado **informe_final.md**. Además, ajusta automáticamente las rutas de imágenes para evitar problemas de visualización tanto en el markdown como el .pdf generado a partir de él.

## Objetivo 🎯

- Facilitar la escritura colaborativa en documentos largos.
- Permitir trabajar en secciones individuales sin preocuparse por la estructura final.
- Automatizar la combinación de secciones en un solo archivo Markdown.
- Ajustar automáticamente las rutas de imágenes para evitar errores de visualización.

## Estructura del proyecto 📌

```sh
/ Project Report MDM
│
├── main.py                         # Script principal del proyecto
├── informe_final.md                # Archivo combinado final en Markdown
├── README_es.md                    # Documentación del proyecto (Español)
├── README.md                       # Documentación del proyecton (Inglés)
│
├── img/                            # Carpeta de imágenes usadas en el informe
│   └── ...                         # Total libertad para organizar el contenido dentro de esta carpeta
│
├── utils/                          # Módulos auxiliares del proyecto
│   ├── constants.py                # Definición de constantes y estructura de los markdown fusionados
│   ├── functions.py                # Funciones de procesamiento y formateo de Markdown
│   └── models.py                   # Definición de clases
│
└── report_sections/                # Secciones individuales del informe en Markdown
    ├── Carátula.md                 # Presentación del informe
    ├── Contenido.md                # Índice del contenido del informe con hipervínculos
    └── chapter_sections/           # Subdivisiones de capítulos más complejos
        ├── chapter1/               # Carpeta con subsecciones del capítulo I
        │   ├── Startup Profile.md  # Subsección Startup Profile
        │   └── ...                 # Otras subsecciones
        └── ...                     # Otras carpetas con subsecciones de otros capítulos
```

## Instrucciones de uso 📝

1️⃣ **Clona este proyecto** dentro de tu organización de GitHub para el desarrollo del informe.
```bash
    git clone https://github.com/L1LZ4Z/ProjectReportMDM.git
    cd nombre-del-proyecto
```

2️⃣ **Crea branches** para organizar y dividir el trabajo en el desarrollo del informe.
```bash
    git checkout -b nombre-de-la-seccion
```

3️⃣ **Trabaja localmente** en la branch correspondiente editando directamente los archivos .md dentro de la carpeta `report_sections/`.

4️⃣ **Visualiza los cambios** en tu editor favorito con la vista previa Markdown para asegurarte de que el formato es correcto. Se recomienda usar **Visual Studio Code con Markdown Preview Enhanced**.

5️⃣ **Asegúrate de que las imágenes referenciadas en los .md usen la ruta relativa correcta**. Estas rutas se ajustarán automáticamente al correr el script principal del programa.
```bash
    # Para .md en la carpeta report_sections/ 
    [Texto alternativo de imagen](../img/imagen.png)
    <img src="../img/imagen.png">
    # Para .md en la carpeta chapterN/
    [Texto alternativo de imagen](../../../img/imagen.png)
    <img src="../../../img/imagen.png">
```
6️⃣ **Ejecuta el script principal** (`main.py`) para combinar todas las secciones en informe_final.md.
```bash
    python ./main.py
```
7️⃣ **Utiliza una herramienta de conversión** para convertir el markdown combinado en un archivo del tipo .pdf. 

## ADVERTENCIA ⚠️
Ten en cuenta que diferentes herramientas interpretan markdown de manera diferente.

- **Usar HTML puro en markdown** podría no ser compatible con algunas herramientas, las cuales lo interpretarían como texto plano.
- Para mayor compatibilidad, si usas HTML dentro de markdown, asegura de probar la conversión con **Pandoc** o usar estilos CSS dentro del documento.