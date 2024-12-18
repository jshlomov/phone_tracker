from app.db.models.interaction import Interaction


def insert_interaction(interaction: Interaction):
    query = """
        MATCH (from:Device {id: $from_device}), (to:Device {id: $to_device})
        MERGE (from)-[r:CONNECTED {
            method: $method,
            bluetooth_version: $bluetooth_version,
            signal_strength_dbm: $signal_strength_dbm,
            distance_meters: $distance_meters,
            duration_seconds: $duration_seconds,
            timestamp: $timestamp
        }]->(to)
        RETURN r
    """
    params = {
        "from_device": interaction.from_device,
        "to_device": interaction.to_device,
        "method": interaction.method,
        "bluetooth_version": interaction.bluetooth_version,
        "signal_strength_dbm": interaction.signal_strength_dbm,
        "distance_meters": interaction.distance_meters,
        "duration_seconds": interaction.duration_seconds,
        "timestamp": interaction.timestamp.isoformat(),
    }
    return query, params
