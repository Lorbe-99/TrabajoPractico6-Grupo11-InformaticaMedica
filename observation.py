from fhir.resources.observation import Observation
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding

def create_observation(patient_id, code="72166-2", value="Positive"):
    """
    Crea una Observation para vincular al DiagnosticReport.
    
    Args:
        patient_id (str): ID del Patient.
        code (str): Código LOINC del análisis (ej: "72166-2" para "Tobacco smoking status").
        value (str): Resultado (ej: "Positive").
    """
    observation = Observation(
        status="final",
        code=CodeableConcept(coding=[Coding(
            system="http://loinc.org",
            code=code,
            display="Tobacco smoking status"
        )]),
        subject=Reference(reference=f"Patient/{patient_id}"),
        valueCodeableConcept=CodeableConcept(text=value)
    )
    return observation
