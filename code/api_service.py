"""
Copyright (C) 2024 Círculo de Crédito - All Rights Reserved

Unauthorized use, copy, modification and/or distribution 
of this software via any medium is strictly prohibited.

This software CAN ONLY be used under the terms and conditions 
established by 'Círculo de Crédito' company.

Proprietary software.
"""
import requests
import json
import logging
import traceback

from ecc_service import ECDSAService

class ApiRccFicoScorePldService:
    """
    Class service to call the RCC-FICO-SCORE-PLD API of 'Círculo de Crédito'.

    :Author: Ricardo Rubio
    :Copyright: 2024 Círculo de Crédito
    """

    API_URL = "https://services.circulodecredito.com.mx/v1/rcc-ficoscore-pld"
    
    HEADER_USERNAME        = "username"
    HEADER_PASSWORD        = "password"
    HEADER_X_API_KEY       = "x-api-key"
    HEADER_X_SIGNATURE     = "x-signature"

    def __init__(self, api_username, api_password, api_key, ecdsa_service, log):
        """
        Constructor.

        :param api_username: The assigned username for the consumption of the 'Círculo de Crédito' APIs.
        :type api_username: str

        :param api_password: The assigned password for the consumption of the 'Círculo de Crédito' APIs.
        :type api_password: str

        :param api_key: The assigned key for the consumption of the 'Círculo de Crédito' APIs.
        :type api_key: str

        :param ecdsa_service: A service object to perform cryptographic functionality.
        :type ecdsa_service: ECDSAService

        :param log: A logger object to print logs.
        :type log: logging
        """
        
        self.api_username   = api_username
        self.api_password   = api_password
        self.api_key        = api_key
        self.ecdsa_service  = ecdsa_service
        self.log            = log

    def retrieve_rcc(self, payload):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param payload: The request body that will be send when calling the RCC-FICO-Score-PLD API.
        :type payload: dict

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """
        
        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(json.dumps(payload))

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info("Calling RCC-FICO-Score-PLD API - Query RCC")

        response = requests.post(self.API_URL, headers=headers, json=payload)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_credits(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/creditos'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_addresses(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/domicilios'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_jobs(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/empleos'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_queries(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/consultas'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_scores(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/scores'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

    def retrieve_messages(self, folio):
        """
        Call the RCC-FICO-Score-PLD API to retrieve an existing RCC report.

        :param folio: The RCC folio required to call the RCC-FICO-Score-PLD API.
        :type payload: str

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """

        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(folio)

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.HEADER_USERNAME: self.api_username,
            self.HEADER_PASSWORD: self.api_password,
            self.HEADER_X_API_KEY: self.api_key,
            self.HEADER_X_SIGNATURE: signature.hex()
        }

        self.log.info(f"Calling RCC-FICO-Score-PLD API - Query RCC")

        url =  f'{self.API_URL}/{folio}/mensajes'

        response = requests.get(url, headers=headers)

        self.log.info(f"RCC-FICO-Score-PLD API Response Status: {response.reason} {response.status_code}")

        return response

