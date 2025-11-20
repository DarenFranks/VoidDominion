#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check all four originally problematic locations"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from data import LOCATIONS

problem_locations = {
    "outer_belts": "Outer Belt Clusters",
    "garrison_outpost": "Garrison Outpost", 
    "harvest_fields": "Harvest Fields Belt",
    "aurora_reach": "Aurora Reach Station"
}

print("=" * 80)
print("CHECKING ALL FOUR PROBLEM LOCATIONS")
print("=" * 80)

for loc_id, display_name in problem_locations.items():
    print(f"\n[{loc_id}]")
    print(f"Name: {display_name}")
    
    if loc_id not in LOCATIONS:
        print(f"  ERROR: NOT FOUND IN LOCATIONS")
        continue
    
    loc_data = LOCATIONS[loc_id]
    connections = loc_data.get('connections', [])
    
    print(f"Total connections: {len(connections)}")
    
    if not connections:
        print("  *** STUCK HERE - NO DESTINATIONS ***")
    else:
        for conn_id in connections:
            if conn_id in LOCATIONS:
                print(f"  - {LOCATIONS[conn_id]['name']}")
            else:
                print(f"  - ERROR: {conn_id} not found")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

stuck_locations = []
for loc_id, display_name in problem_locations.items():
    if loc_id in LOCATIONS:
        connections = LOCATIONS[loc_id].get('connections', [])
        if not connections:
            stuck_locations.append(display_name)

if stuck_locations:
    print("\nSTUCK AT THESE LOCATIONS:")
    for name in stuck_locations:
        print(f"  - {name}")
else:
    print("\nALL LOCATIONS HAVE DESTINATIONS")
