from fhir.resources.observation import Observation
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding

def crear_observacion(id_paciente, codigo, valor, descripcion):
    """
    Crea una Observación médica en español para vincular a un Informe Diagnóstico.
    
    Args:
        id_paciente (str): ID del Patient (ej: "pat-123").
        codigo (str): Código LOINC del análisis (ej: "72166-2").
        valor (str): Resultado (ej: "Positivo").
        descripcion (str): Descripción en español (ej: "Consumo de tabaco").
    """
    # Configurar el código LOINC 
    codigo_loinc = CodeableConcept()
    codigo_loinc.coding = [Coding(
        system="http://loinc.org",
        code=codigo,
        display=descripcion  # Descripción localizada
    )]
    
    # Crear la Observación
    observacion = Observation(
        status="final",
        code=codigo_loinc,
        subject=Reference(reference=f"Patient/{id_paciente}"),
        valueCodeableConcept=CodeableConcept(text=valor)  
    )
    
    return observacion
