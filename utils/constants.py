import os
from utils.models import OutputFile, HeaderOutputFile

page_break = '\n\n<div style="page-break-before: always;"></div>\n\n'
report_source_dir = "report_sections"
chapters_source_dir = os.path.join(report_source_dir, "chapter_sections", "chapter")

FINAL_REPORT = OutputFile(
    source_dir = report_source_dir, 
    output_file_name="README.md",
    order = [
        "Carátula.md",
        "Registro de Versiones del Informe.md",
        "Project Report Collaboration Insights.md",
        "Contenido.md",
        "Student Outcome.md",
        "Introducción.md",
        "Requirements Elicitation & Analysis.md",
        "Requirements Specification.md",
        "Product Design.md",
        "Product Implementation, Validation & Deployment.md",
        "Conclusiones.md",
        "Bibliografía.md",
        "Anexos.md"
    ]
)

CHAPTER_1 = HeaderOutputFile(
    header= "# Capítulo I: Introducción",
    source_dir= chapters_source_dir + "1",
    output_file_name= os.path.join("report_sections", "Introducción.md"),
    order=[
        "Startup Profile.md",
        "Solution Profile.md",
        "Segmentos Objetivo.md",
    ]
)

CHAPTER_2 = HeaderOutputFile(
    header="# Capítulo II: Requirements Elicitation & Analysis",
    source_dir=chapters_source_dir + "2",
    output_file_name=os.path.join("report_sections", "Requirements Elicitation & Analysis.md"),
    order=[
        "Competidores.md",
        "Entrevistas.md",
        "Needfinding.md",
        "Ubiquitous Language.md",
    ]
)

CHAPTER_3 = HeaderOutputFile(
    header="# Capítulo III: Requirements Specification",
    source_dir=chapters_source_dir + "3",
    output_file_name=os.path.join("report_sections", "Requirements Specification.md"),
    order=[
        "To-Be Scenario Mapping.md",
        "User Stories.md",
        "Impact Mapping.md",
        "Product Backlog.md",
    ]
)

CHAPTER_4 = HeaderOutputFile(
    header="# Capítulo IV: Product Design",
    source_dir=chapters_source_dir + "4",
    output_file_name=os.path.join("report_sections", "Product Design.md"),
    order=[
        "Style Guidelines.md",
        "Information Architecture.md",
        "Landing Page UI Design.md",
        "Web Applications UX_UI Design.md",
        "Web Applications Prototyping.md",
        "Domain-Driven Software Architecture.md",
        "Software Object-Oriented Design.md",
        "Database Design.md",
    ]
)

IMPLEMENTATION = HeaderOutputFile(
    header="## 5.2. Landing Page, Services & Applications Implementation",
    source_dir=os.path.join(chapters_source_dir + "5", "implementation_sections"),
    output_file_name=os.path.join("report_sections", "chapter_sections", "chapter5", "Landing Page, Services & Applications Implementation.md"),
    order=[
        #"1.md", "2.md", "3.md", "4.md"
    ]
)

CHAPTER_5 = HeaderOutputFile(
    header="# Capítulo V: Product Implementation, Validation & Deployment",
    source_dir=chapters_source_dir + "5",
    output_file_name=os.path.join("report_sections", "Product Implementation, Validation & Deployment.md"),
    order=[
        "Software Configuration Management.md",
        "Landing Page, Services & Applications Implementation.md"
        #,"Validation Interviews.md", "Video About-the-Product.md"
    ]
)