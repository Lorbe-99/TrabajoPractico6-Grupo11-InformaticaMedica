import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# Funcion para buscar pacientes por DNI(identifier)
def search_patient_by_document(document_number):
    url = f"http://hapi.fhir.org/baseR4/Patient?identifier=http://www.renaper.gov.ar/dni|{document_number}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        patients = response.json()
        if patients.get('total', 0) > 0:
            print("Paciente encontrado:")
            print(patients['entry'][0]['resource']) 
            return patients['entry'][0]['resource']['id']
        else:
            print("No se encontraron pacientes con ese DNI.")
    else:
        print(f"Error en la búsqueda: {response.status_code}")
    
    return None
