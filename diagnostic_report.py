from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from datetime import datetime

def create_diagnostic_report(patient_id, observations_ids, status="final", report_type="LAB"):
    report = DiagnosticReport(
        status=status,
        code=CodeableConcept(coding=[Coding(
            system="http://loinc.org",
            code="58448-4",
            display="Diagnostic Report"
        )]),
        subject=Reference(reference=f"Patient/{patient_id}"),
        result=[Reference(reference=f"Observation/{obs_id}") for obs_id in observations_ids],
        effectiveDateTime=datetime.now().isoformat()
    )
    return report
