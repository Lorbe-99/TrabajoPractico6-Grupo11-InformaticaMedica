from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from datetime import datetime

def create_diagnostic_report(patient_id, observations_ids, status="final", report_type="LAB", conclusion=None):
    """
    Crea un informe diagnóstico con relaciones a Patient y Observations.

    A continuacion se enumera como se explican las variables:
        patient_id (str): ID del Patient.
        observations_ids (list): IDs de Observations (ej: ["obs-1", "obs-2"]).
        status (str): "final"|"partial"|"corrected".
        report_type (str): Tipo de informe ("LAB", "RAD", etc.).
        conclusion (str): Interpretación clínica (opcional).
    """
    # Configurar el tipo de informe (LOINC)
    report_code = CodeableConcept(coding=[Coding(
        system="http://loinc.org",
        code="58448-4" if report_type == "LAB" else "60591-5",  # Códigos LOINC
        display="Laboratory Report" if report_type == "LAB" else "Radiology Report"
    )])
    
    # Crear el informe
    report = DiagnosticReport(
        status=status,
        code=report_code,
        subject=Reference(reference=f"Patient/{patient_id}"),
        result=[Reference(reference=f"Observation/{obs_id}") for obs_id in observations_ids],
        effectiveDateTime=datetime.now().isoformat(),
        conclusion=conclusion  # Campo añadido para diagnóstico textual
    )
    return report
