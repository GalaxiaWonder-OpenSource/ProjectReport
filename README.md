# Project Report Markdown Manager

## Project Description 📝

This project facilitates the creation of software engineering reports following the academic structure used in Web Applications and Open Source Application Development courses. Its goal is to allow students to work more easily on individual report sections using branches, maintaining a standard format and ensuring proper content integration into a single final document through three-way merging.

The program takes individually written Markdown sections, organizes them in a predefined order, and combines them into a final file called `informe_final.md`. Additionally, it automatically adjusts image paths to prevent visualization issues in both the Markdown file and the generated .pdf.

## Objective 🎯

- Facilitate collaborative writing in long documents.
- Allow work on individual sections without worrying about the final structure.
- Automate the merging of sections into a single Markdown file.
- Automatically adjust image paths to prevent visualization errors.

## Project Structure 📌

```sh
/ Project Report MDM
│
├── main.py                         # Main script of the project
├── informe_final.md                # Final combined file in Markdown
├── README_es.md                    # Project documentation (Spanish)
├── README.md                       # Project documentation (English)
│
├── img/                            # Folder containing images used in the report
│   └── ...                         # Full freedom to organize content within this folder
│
├── utils/                          # Auxiliary modules of the project
│   ├── constants.py                # Definition of constants and structure of merged markdown files
│   ├── functions.py                # Functions for processing and formatting Markdown
│   └── models.py                   # Definition of classes
│
└── report_sections/                # Individual report sections in Markdown
    ├── Cover.md                    # Report cover page
    ├── Table_of_Contents.md        # Report content index with hyperlinks
    └── chapter_sections/           # Subdivisions of more complex chapters
        ├── chapter1/               # Folder containing chapter I subsections
        │   ├── Startup_Profile.md  # Subsection Startup Profile
        │   └── ...                 # Other subsections
        └── ...                     # Other folders with subsections of other chapters
```

## Usage Instructions 📝

1️⃣ **Fork this project** into your GitHub organization for report development. Then, clone it into your local machine using:
```bash
    git clone https://github.com/your-org-name/fork-name.git
    cd project-name
```

2️⃣ **Create branches** to organize and divide the work for report development.
```bash
    git checkout -b section-name
```

3️⃣ **Work locally** on the corresponding branch by directly editing the .md files within the `report_sections/` folder.

4️⃣ **Preview changes** in your favorite editor with Markdown preview to ensure correct formatting. It is recommended to use **Visual Studio Code with Markdown Preview Enhanced**.

5️⃣ **Ensure referenced images in the .md files use the correct relative path.**
These paths will be automatically adjusted when running the main script.
```bash
    # For .md files in the report_sections/ folder
    ![Alt text](../img/image.png)
    <img src="../img/image.png">

    # For .md files in the chapterN/ folder
    ![Alt text](../../../img/image.png)
    <img src="../../../img/image.png">
```

6️⃣ **Run the main script** (`main.py`) to combine all sections into `informe_final.md`.
```bash
    python main.py
```

7️⃣ **Use a conversion tool** to convert the combined markdown into a .pdf format file.


## ⚠️ WARNING

Keep in mind that different tools interpret Markdown content differently.

- **Using raw HTML within Markdown** may not be compatible with some tools, which might interpret it as plain text.
- For better compatibility, if you use HTML within Markdown, ensure testing the conversion with **Pandoc** or use CSS styles within the document.

