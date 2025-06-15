from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier

def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_number=None):
    patient = Patient()
    
    # Agregar identificador (DNI)
    if document_number:
        identifier = Identifier()
        identifier.system = "http://www.renaper.gov.ar/dni"  # Sistema de identificación argentino utilizado para la actividad 1 y 2
        identifier.value = str(document_number)
        patient.identifier = [identifier]
    
    
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    if birth_date:
        patient.birthDate = birth_date

    if gender:
        patient.gender = gender

    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    return patient
