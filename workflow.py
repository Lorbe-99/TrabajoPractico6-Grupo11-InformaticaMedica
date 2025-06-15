from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_document
from observation import create_observation
from diagnostic_report import create_diagnostic_report

if __name__ == "__main__":
    # Parámetros del paciente
    family_name = "SANCHEZ"
    given_name = "Camila"
    birth_date = "1990-03-15"
    gender = "female"
    phone = "+5491145678901"
    document_number = "35987654"  # DNI del paciente

    # Crear recurso con DNI
    patient = create_patient_resource(
        family_name=family_name,
        given_name=given_name,
        birth_date=birth_date,
        gender=gender,
        phone=phone,
        document_number=document_number  # Nuevo parámetro
    )
    
    # Enviar a HAPI FHIR
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Leer el recurso creado (Actividad 3.a)
    if patient_id:
        get_resource_from_hapi_fhir(patient_id, 'Patient')

    # Buscar paciente por DNI (Actividad 3.b)
    print("\nBuscando paciente por DNI...")
    found_patient_id = search_patient_by_document(document_number)
    if found_patient_id and found_patient_id == patient_id:
        print("¡El paciente creado coincide con la búsqueda!")


# Actividad 3.c
if __name__ == "__main__":
    # --- Crear Patient ---
    patient = create_patient_resource(
        family_name="SANCHEZ",
        given_name="Camila",
        birth_date="1990-03-15",
        gender="female",
        document_number="35987654"
    )
    patient_id = send_resource_to_hapi_fhir(patient, "Patient")
    
    # --- Crear Observations ---
    observation1 = create_observation(patient_id, code="72166-2", value="Positive")
    observation2 = create_observation(patient_id, code="94531-1", value="Negative")
    
    obs1_id = send_resource_to_hapi_fhir(observation1, "Observation")
    obs2_id = send_resource_to_hapi_fhir(observation2, "Observation")
    
    # --- Crear DiagnosticReport ---
    report = create_diagnostic_report(
        patient_id=patient_id,
        observations_ids=[obs1_id, obs2_id],
        report_type="LAB"
    )
    report_id = send_resource_to_hapi_fhir(report, "DiagnosticReport")
    
    # --- Ver resultados ---
    print(f"\nPatient ID: {patient_id}")
    print(f"Observation IDs: {obs1_id}, {obs2_id}")
    print(f"DiagnosticReport ID: {report_id}")
