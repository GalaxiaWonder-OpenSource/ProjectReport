# Registro de Versiones del Informe

<style>
    .version-table {
        border-collapse: collapse;
        width: 100%;
        text-align: left;
        font-family: monospace;
    }

    .version-table th, .version-table td {
        border: 1px solid black;
        padding: 8px;
    }

    .version-table th {
        font-weight: bold;
    }

    .version-table th:nth-child(1), 
    .version-table th:nth-child(2), 
    .version-table th:nth-child(3) {
        text-align: center;
    }

    .version-table td:nth-child(1), .version-table td:nth-child(2), .version-table td:nth-child(3) {
        text-align: center;
        vertical-align: middle;
    }

    .version-table td:nth-child(1), .version-table td:nth-child(2) {
        width: 10%;
    }

    .version-table td:nth-child(4) {
        width: 60%;
    }

    .indent-0, .indent-1, .indent-2, .indent-3, .indent-4 {
        text-indent: 0px; 
        display: block;
        margin: 2px 0;
        line-height: 0.1;
    }

    .indent-0 { text-indent: 0px; font-weight: bold; }

    .indent-1 { text-indent: 10px; }

    .indent-2 { text-indent: 20px; }

    .indent-3 { text-indent: 30px; }

    .indent-4 { text-indent: 40px; }
</style>

<table class="version-table">
    <thead>
        <tr>
            <th>Versión</th>
            <th>Fecha</th>
            <th>Autor</th>
            <th>Descripción de modificación</th>
        </tr>
    </thead>
    <tbody>
        <!-- Cada versión nueva, copiar y pegar el <tr> con 4 <td> dentro
        Molde 
        <tr>
            <td>[N]</td>
            <td>[XX/XX/25]</td>
            <td>[Autor]</td>
            <td>
                <strong>[Adición/Corrección] de secciones:</strong><br>
                <span class="indent-0">
                    &nbsp;&nbsp;&nbsp;
                    [Nombre de sección principal NO numerada]
                </span><br>
                <span class="indent-1">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    [Nombre de subsección NO numerada]
                </span><br>
                <span class="indent-0">[N.] [Nombre de sección principal numerada]</span><br>
                <span class="indent-1">[N.n.] [Nombre de subsección numerada]</span><br>
                <span class="indent-2">[N.n.n.] [Nombre de sub-subsección numerada]</span><br>
                <span class="indent-3">[N.n.n.n.] [Nombre de tercera subsección numerada]</span><br>
            </td>
        </tr>
        -->
    </tbody>
</table>