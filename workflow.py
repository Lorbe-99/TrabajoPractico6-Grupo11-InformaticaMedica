from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # Parámetros del paciente
    family_name = "SANCHEZ"
    given_name = "Camila"
    birth_date = "1990-03-15"
    gender = "female"
    phone = "+5491145678901"
    document_number = "35987654"  # DNI del paciente utilizado en las actividades 1 y 2

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

