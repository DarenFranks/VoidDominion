#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simulate exact game logic for showing travel destinations"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from data import LOCATIONS

# Simulate being at Harvest Fields (what the game would do)
simulated_player_location = "harvest_fields"

print("=" * 80)
print("SIMULATING GAME LOGIC FOR TRAVEL VIEW")
print("=" * 80)

print(f"\nSimulated player.location = '{simulated_player_location}'")

# This is exactly what show_travel_view() does:
if simulated_player_location not in LOCATIONS:
    print(f"ERROR: Location '{simulated_player_location}' not found in LOCATIONS!")
    sys.exit(1)

current_loc = LOCATIONS[simulated_player_location]
print(f"Current location: {current_loc['name']}")

# Get connections
connections = current_loc.get('connections', [])
print(f"Number of connections: {len(connections)}")

if not connections:
    print("\n*** THIS IS THE PROBLEM - NO CONNECTIONS! ***")
    print("The game would show EMPTY list of destinations")
else:
    print(f"\nDestinations that would display:")
    for i, conn_id in enumerate(connections, 1):
        if conn_id in LOCATIONS:
            conn_data = LOCATIONS[conn_id]
            print(f"  {i}. {conn_data['name']}")
            print(f"     ID: {conn_id}")
            print(f"     Type: {conn_data['type']}")
            print(f"     Danger: {int(conn_data.get('danger_level', 0) * 100)}%")
        else:
            print(f"  {i}. ERROR - ID '{conn_id}' not found in LOCATIONS!")

print("\n" + "=" * 80)
print("TRYING DIFFERENT LOCATION IDS")
print("=" * 80)

# Maybe the game is using a different location ID?
possible_ids = [
    "harvest_fields",
    "Harvest Fields",
    "harvest_fields_belt",
    "harvest fields",
    "HarvestFieldsBelt",
    "Harvest_Fields_Belt",
]

print("\nSearching for location by name 'Harvest Fields Belt':")
found = False
for loc_id, loc_data in LOCATIONS.items():
    if loc_data.get('name', '').lower() == 'harvest fields belt':
        print(f"  FOUND: ID = '{loc_id}'")
        connections = loc_data.get('connections', [])
        print(f"  Connections: {len(connections)}")
        if connections:
            for conn_id in connections:
                print(f"    - {conn_id}")
        found = True

if not found:
    print("  NOT FOUND by name match")

print("\n" + "=" * 80)
print("DEBUG: ALL LOCATION IDS IN LOCATIONS DICT")
print("=" * 80)

# Show all locations that contain "harvest" or similar
harvest_matches = {k: v['name'] for k, v in LOCATIONS.items() if 'harvest' in k.lower()}
belt_matches = {k: v['name'] for k, v in LOCATIONS.items() if 'field' in k.lower()}

print(f"\nLocations with 'harvest' in ID: {len(harvest_matches)}")
for loc_id, name in harvest_matches.items():
    print(f"  - '{loc_id}' -> {name}")

print(f"\nLocations with 'field' in ID: {len(belt_matches)}")
for loc_id, name in belt_matches.items():
    print(f"  - '{loc_id}' -> {name}")
