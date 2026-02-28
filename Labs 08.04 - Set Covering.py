import json

def findStations(stations,needed_cities):
    states_needed = set(needed_cities)
    final_stations = []

    while states_needed:
        best_station = None
        states_covered = set()

        for station, cities in stations.items():
            covered = states_needed.intersection(set(cities))

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        if best_station is None:
            break

        states_needed -= states_covered
        final_stations.append(best_station)

        del stations[best_station]

    return sorted(final_stations)

def main():
    needed_cities = json.loads(input())

    num_stations = int(input())
    stations_dict = {}

    for _ in range(num_stations):
        station_data = json.loads(input())
        stations_dict[station_data["Name"]] = station_data["Cities"]
    result = findStations(stations_dict,needed_cities)
    print(result)

main()
