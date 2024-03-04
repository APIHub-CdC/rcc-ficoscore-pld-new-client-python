"""
Copyright (C) 2024 Círculo de Crédito - All Rights Reserved

Unauthorized use, copy, modification and/or distribution 
of this software via any medium is strictly prohibited.

This software CAN ONLY be used under the terms and conditions 
established by 'Círculo de Crédito' company.

Proprietary software.
"""
import sys
import logging
import uuid
import traceback

sys.path.append('./code')

from api_service import ApiRccFicoScorePldService
from ecc_service import ECDSAService

from nacionality_catalog import Nacionality
from civil_status_catalog import CivilStatus
from gender_catalog import Gender
from mexico_states_catalog import Mexico
from address_catalog import AddressType
from settlement_catalog import SettlementType
from residence_catalog import ResidenceType

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d - %(message)s')
log = logging.getLogger()

class ApiRccFicoScorePld:

    def __init__(self):
        # API cryptographic keys
        self.public_cert_path    = "/your-path/cdc_cert_xxxx.pem"
        self.pkcs12_path         = "/your-path/keystore.p12"
        self.pkcs12_password     = "your-keystore-password"

        # API credentials
        self.api_username    = "your-username"
        self.api_password    = "your-password"
        self.api_key         = "your-api-key"

        # Services
        self.ecdsa_service   = ECDSAService(self.public_cert_path, self.pkcs12_path, self.pkcs12_password, log)
        self.api_service     = ApiRccFicoScorePldService(self.api_username, self.api_password, self.api_key, self.ecdsa_service, log)


    def retrieve_rcc(self):
        try:
            # rcc data
            payload = {
                "apellidoPaterno": "",
                "apellidoMaterno": "",
                "apellidoAdicional": "",
                "primerNombre": "",
                "segundoNombre": "",
                "fechaNacimiento": "yyyy-mm-dd",
                "RFC": "",
                "CURP": "",
                "nacionalidad": Nacionality.MX.value,
                "residencia": ResidenceType.PROPIETARIO.value,
                "estadoCivil": CivilStatus.CASADO.value,
                "sexo": Gender.MASCULINO.value,
                "claveElectorIFE": "",
                "numeroDependientes": 0,
                "fechaDefuncion": "yyyy-mm-dd",
                "domicilio": {
                    "direccion": "",
                    "coloniaPoblacion": "",
                    "delegacionMunicipio": "",
                    "ciudad": "",
                    "estado": Mexico.JALISCO.value,
                    "CP": "47917",
                    "fechaResidencia": "yyyy-mm-dd",
                    "numeroTelefono": "",
                    "tipoDomicilio": AddressType.CASA.value,
                    "tipoAsentamiento": SettlementType.COLONIA.value
                }
            }

            response = self.api_service.retrieve_rcc(payload)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_credits(self):
        try:
            folio = ""

            response = self.api_service.retrieve_credits(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_addresses(self):
        try:
            folio = ""

            response = self.api_service.retrieve_addresses(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_jobs(self):
        try:
            folio = ""

            response = self.api_service.retrieve_jobs(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_queries(self):
        try:
            folio = ""

            response = self.api_service.retrieve_queries(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_scores(self):
        try:
            folio = ""

            response = self.api_service.retrieve_scores(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

    def retrieve_messages(self):
        try:
            folio = ""

            response = self.api_service.retrieve_messages(folio)

            log.info(f"RCC-FICO-Score-PLD API Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to call RCC-FICO-Score-PLD API. Cause: {exception}")
            traceback.print_exc()

api = ApiRccFicoScorePld()
#api.retrieve_rcc()
#api.retrieve_credits()
#api.retrieve_addresses()
#api.retrieve_jobs()
#api.retrieve_queries()
#api.retrieve_scores()
#api.retrieve_messages()