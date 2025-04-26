## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

En Galaxia Wonder hemos adoptado una serie de herramientas tanto familiares como más recientes para el diseño, desarrollo y despliegue de nuestra solución de software. En la siguiente tabla a continuación, se presentan las principales herramientas a utilizar por el equipo.

<table>
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Propósito de uso en el proyecto</th>
            <th>Enlace de referencia / descarga</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>UXPressia</td>
            <td><strong>UX/UI Design:</strong> Artefactos de UX</td>
            <td><a href="https://uxpressia.com/" target="_blank">UXPressia Web Application</a></td>
        </tr>
        <tr>
            <td>Miro</td>
            <td><strong>UX/UI Design:</strong> As-Is & To-Be Scenario Mapping</td>
            <td><a href="https://miro.com/es/app/" target="_blank">Descargar Miro</a></td>
        </tr>
        <tr>
            <td>Figma</td>
            <td><strong>UX/UI Design:</strong> Wireframes, Mockups & Prototyping</td>
            <td><a href="https://www.figma.com/es-la/downloads/" target="_blank">Descargar Figma</a></td>
        </tr>
        <tr>
            <td>LucidChart</td>
            <td><strong>UX/UI Design:</strong> Wireflows & Userflows</td>
            <td><a href="https://www.lucidchart.com/" target="_blank">LucidChart Web</a></td>
        </tr>
        <tr>
            <td>Vertabelo</td>
            <td><strong>Software Architecture Design:</strong> Database Diagram</td>
            <td><a href="https://vertabelo.com/" target="_blank">Vertabelo Web</a></td>
        </tr>
        <tr>
            <td>PlantUML</td>
            <td><strong>Software Architecture Design:</strong> UML y C4 Model</td>
            <td><a href="https://plantuml.com/es/" target="_blank">PlantUML Web</a></td>
        </tr>
        <tr>
            <td>VSCode</td>
            <td><strong>IDE:</strong> Editor de código ligero y versátil para múltiples lenguajes</td>
            <td><a href="https://code.visualstudio.com/" target="_blank">Descargar VSCode</a></td>
        </tr>
        <tr>
            <td>WebStorm</td>
            <td><strong>IDE:</strong> Desarrollo especializado en JavaScript y frameworks modernos</td>
            <td><a href="https://www.jetbrains.com/webstorm/" target="_blank">WebStorm Web</a></td>
        </tr>
        <tr>
            <td>IntelliJ IDEA</td>
            <td><strong>IDE:</strong> Desarrollo en Java y tecnologías enterprise</td>
            <td><a href="https://www.jetbrains.com/idea/" target="_blank">IntelliJ IDEA Web</a></td>
        </tr>
        <tr>
            <td>Java</td>
            <td><strong>Lenguaje de Programación:</strong> Backend robusto y multiplataforma</td>
            <td><a href="https://www.oracle.com/java/technologies/javase-downloads.html" target="_blank">Descargar Java</a></td>
        </tr>
        <tr>
            <td>Node.js</td>
            <td><strong>Entorno de Ejecución:</strong> JavaScript del lado del servidor</td>
            <td><a href="https://nodejs.org/" target="_blank">Descargar Node.js</a></td>
        </tr>
        <tr>
            <td>npm</td>
            <td><strong>Gestor de Paquetes:</strong> Manejo de dependencias para proyectos JS</td>
            <td><a href="https://www.npmjs.com/" target="_blank">Sitio de npm</a></td>
        </tr>
        <tr>
            <td>Angular</td>
            <td><strong>Framework:</strong> Desarrollo de aplicaciones web SPA con TypeScript</td>
            <td><a href="https://angular.io/" target="_blank">Angular Web</a></td>
        </tr>
        <tr>
            <td>Spring Boot</td>
            <td><strong>Proyecto del Framework Spring:</strong> Desarrollo de APIs RESTful y aplicaciones backend en Java con configuración mínima</td>
            <td><a href="https://spring.io/projects/spring-boot" target="_blank">Spring Boot Web</a></td>
        </tr>
    </tbody>
</table>

### 5.1.2. Source Code Management

En Galaxia Wonder, la gestión del código fuente de las soluciones se realiza a través de Git como sistema de control de versiones y GitHub, como repositorio de alojamiento descentralizado.

Se adjunta a continuación los enlaces de los repositorios de GitHub:
- Landing Page: [https://github.com/GalaxiaWonder-OpenSource/LandingPage](https://github.com/GalaxiaWonder-OpenSource/LandingPage)
- FrontEnd Web Application: [https://github.com/GalaxiaWonder-OpenSource/FrontEnd](https://github.com/GalaxiaWonder-OpenSource/FrontEnd)
- RESTful API: [https://github.com/GalaxiaWonder-OpenSource/API](https://github.com/GalaxiaWonder-OpenSource/API)
- ProP GMS Web Service: [https://github.com/GalaxiaWonder-OpenSource/Platform](https://github.com/GalaxiaWonder-OpenSource/Platform)

Para su gestión interna, se aplicará GitFlow. Se explican a continuación las ramas a crear, así como las convenciones a utilizar para nombrarlas:

**RAMAS PRINCIPALES**

- **main**: Rama principal de producción. Aquí se encuentran las versiones estables del proyecto, listas para ser desplegadas. Toda publicación oficial se hace desde esta rama.

- **develop**: Rama de desarrollo. Aquí se integran las nuevas funcionalidades antes de ser lanzadas a producción. Es la base para las ramas de tipo *feature*, *release* y *bugfix*.

**RAMAS SECUNDARIAS**

- **feature/**: Ramas para el desarrollo de nuevas funcionalidades. Se crean a partir de `develop` y, una vez completadas, se integran de nuevo en `develop`.
  - **Convención de nombres**:  
    `feature/story-id`  
    Ejemplo: `feature/us77`

- **bugfix/**: Ramas para la correción de errores detectados en fase de desarrollo. Se crean a partir de `develop` y, una vez completadas, se integran de nuevo en `develop`.
  - **Convención de nombres**:  
    `bugfix/story-id`  
    Ejemplo: `feature/us77`

- **release/**: Ramas para preparar una nueva versión de producción. Se crean desde `develop` cuando ya se ha alcanzado un conjunto estable de funcionalidades. Sirven para realizar pruebas, ajustes menores y documentación. Al finalizar, se integran en `main` y `develop`.
  - **Convención de nombres**:  
    `release/x.y.z`  
    Ejemplo: `release/1.0.0`

- **hotfix/**: Ramas para corregir errores críticos detectados tardíamente en producción. Se crean desde `main` y se integran tanto en `main` como en `develop` (o en `release`, si hubiere alguna rama de ese tipo activa).
  - **Convención de nombres**:  
    `hotfix/story-id`  
    Ejemplo: `hotfix/swr35`

### 5.1.3. Source Code Style Guide & Coding Conventions

En esta sección se establecen las guías de estilo y convenciones de codificación que el equipo adoptará para mantener la consistencia, legibilidad y calidad del código fuente.

**LENGUAJES DE PROGRAMACIÓN**

Para el desarrollo de la solución, se utlizarán los siguientes lenguajes de programación y marcado:
- HTML  
- CSS  
- JavaScript  
- TypeScript  
- Java

**CONVENCIONES GENERALES**
Para todos los lenguajes de programación y marcado mencionados:
- Se aplicará el uso de nomenclaturas en inglés.
- Se nombraran variables, constantes, elementos y clases de forma explícita.
- Se usará saltos de linea vacíos para separar unidades lógicas diferentes del código.
- Se promoverá la reutilización de código.

**CONVECIONES ESPECÍFICAS**

A continuación, se describen las convenciones principales a aplicar por lenguaje:

**HTML & CSS:** Se aplicaran las recomendaciones del HTML Style Guide and Coding Conventions y el Google HTML/CSS Style Guide, que indican:
- Escribir etiquetas y atributos en minúsculas.
- Utilizar indentación de 2 espacios.
- Utilizar clases con nombres descriptivos y en `kebab-case`.
- Evitar el uso de estilos en línea.
- Separar el contenido (HTML) de la presentación (CSS).

**JavaScript & TypeScript:** Se adoptarán las recomendaciones del Google JavaScript Style Guide y el Google TypeScript Style Guide.
- Usar `camelCase` para variables y funciones.
- Usar `PascalCase` para clases y componentes.
- Definir constantes en `UPPER_SNAKE_CASE`.
- Evitar el uso de `var`, preferir `let` y `const`.
- Usar funciones flecha (`=>`) siempre que sea posible.
- Documentar funciones y clases con comentarios JSDoc.
- Diseñar y codificar orientados al desacoplamiento.
- Aplicar tipado estricto (para typescript).

**Java:** Seguir el Google Java Style Guide.
- Usar `camelCase` para métodos y variables.
- Usar `PascalCase` para clases e interfaces.
- Agrupar paquetes de forma coherente y ordenada (`com.empresa.proyecto.modulo`).
- Usar anotaciones correctamente (`@Override`, `@Autowired`, etc.).
- Seguir prácticas de desarrollo recomendadas por **Spring Boot** como la inyección de dependencias, uso de DTOs, controladores REST, etc.

### 5.1.4 Software Deployment Configuration

**LANDING PAGE DEPLOYMENT**

La landing page del proyecto se desplegará utilizando GitHub Pages, una plataforma gratuita proporcionada por GitHub para alojar sitios web estáticos directamente desde un repositorio. Esta solución permite mostrar públicamente la interfaz sin necesidad de servidores externos o configuraciones complicadas.

1. El despliegue se realiza a partir de la rama principal del repositorio (main), asegurando que las versiones mas estables del equipo de desarrollo estén siempre disponibles para visualización inmediata.

<img src="../../../img/chapter5/Deploy/Gitpages.png">

Enlace para acceder a la landing page: [https://galaxiawonder-opensource.github.io/LandingPage/](https://galaxiawonder-opensource.github.io/LandingPage/)
