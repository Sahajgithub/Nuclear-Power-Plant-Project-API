from .service.connection_service import Connect
Connect.connect()
from .service.data_service import DataService


def power_plant_data(country=None, status=None, type=None, limit=10):
    # Default limit on no of records is 10.
    condition = {}
    condition.update({'Country': country})
    condition.update({'Status': status})
    condition.update({'PlantType': type})
    results = DataService.get_power_plants(condition, limit)
    return results
