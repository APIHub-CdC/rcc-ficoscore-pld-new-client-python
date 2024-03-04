from enum import Enum

class AddressType(Enum):
    NEGOCIO                 = 'N'
    DOMICILIO_DEL_OTORGANTE = 'O'
    CASA                    = 'C'
    APARTADO_POSTAL         = 'P'
    EMPLEO                  = 'E'