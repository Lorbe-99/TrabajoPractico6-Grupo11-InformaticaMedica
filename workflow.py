from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_document
from observation import crear_observacion
from diagnostic_report import create_diagnostic_report

def main():
    patient_data = {
        "family_name": "SANCHEZ",
        "given_name": "Camila",
        "birth_date": "1990-03-15",
        "gender": "female",
        "phone": "+5491145678901",
        "document_number": "35987654"
    }

    print("\n--- Actividad 3.a: Creación de Paciente ---")
    patient = create_patient_resource(**patient_data)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')
    
    if patient_id:
        print(f"\nPaciente creado con ID: {patient_id}")
        get_resource_from_hapi_fhir(patient_id, 'Patient')

    print("\n--- Actividad 3.b: Búsqueda por DNI ---")
    found_patient_id = search_patient_by_document(patient_data["document_number"])
    if found_patient_id and found_patient_id == patient_id:
        print("El paciente encontrado coincide con el creado.")

    print("\n--- Actividad 3.c: Creación de Informe Diagnóstico ---")
    
    observaciones = [
        {"codigo": "72166-2", "valor": "Positivo", "descripcion": "Consumo de tabaco"},
        {"codigo": "94531-1", "valor": "Negativo", "descripcion": "Prueba COVID-19"}
    ]
    
    ids_observaciones = []
    for obs in observaciones:
        observacion = crear_observacion(
            id_paciente=patient_id,
            codigo=obs["codigo"],
            valor=obs["valor"],
            descripcion=obs["descripcion"]
        )
        id_obs = send_resource_to_hapi_fhir(observacion, "Observation")
        if id_obs:
            ids_observaciones.append(id_obs)
            print(f"🔹 {obs['descripcion']}: {obs['valor']} (ID: {id_obs})")

    if ids_observaciones:
        informe = create_diagnostic_report(
            patient_id=patient_id,
            observations_ids=ids_observaciones,
            report_type="LAB",
            conclusion="Paciente con consumo de tabaco activo pero sin COVID-19."
        )
        id_informe = send_resource_to_hapi_fhir(informe, "DiagnosticReport")
        
        print(f"\n Informe diagnóstico creado correctamente:")
        print(f"   - ID del informe: {id_informe}")
        print(f"   - Paciente: {patient_data['given_name']} {patient_data['family_name']}")
        print(f"   - Enlace: http://hapi.fhir.org/baseR4/DiagnosticReport/{id_informe}")

if __name__ == "__main__":
    main()

