## Patient
Creación del recurso paciente con algunos parámetros. 

## Base 
Lectura y escritura de recursos en el servidor público de HAPI FHIR. 

## Workflow
Desde acá se corre el código. 

## Observation
Contiene la función `crear_observacion()` que:
- Genera un recurso `Observation` FHIR.
- Asocia la observación a un paciente.
- Define un código LOINC y un valor textual (ej. "Positivo").
- Incluye fecha de observación (`effectiveDateTime`).

## diagnostic_report
