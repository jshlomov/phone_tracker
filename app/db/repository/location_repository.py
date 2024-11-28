from app.db.models.location import Location


def insert_location(device_id: str, location: Location):
        query = """
            MATCH (d:Device {id: $device_id})
            MERGE (l:Location {
                latitude: $latitude,
                longitude: $longitude,
                altitude_meters: $altitude_meters,
                accuracy_meters: $accuracy_meters
            })
            MERGE (d)-[:LOCATED_AT]->(l)
            RETURN l
        """
        params = {
            "device_id": device_id,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "altitude_meters": location.altitude_meters,
            "accuracy_meters": location.accuracy_meters,
        }
        return query, params
