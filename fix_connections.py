#!/usr/bin/env python3
"""
Fix location connections to be bidirectional.
If A connects to B, then B should connect to A.
"""

from data import LOCATIONS

def analyze_and_fix_connections():
    """
    Make all connections bidirectional.
    """
    print("="*60)
    print("FIXING LOCATION CONNECTIONS")
    print("="*60 + "\n")
    
    fixes = []
    
    # For each location
    for loc_id, loc_data in LOCATIONS.items():
        connections = loc_data.get("connections", [])
        
        # For each connection from this location
        for connected_id in connections:
            if connected_id in LOCATIONS:
                # Check if reverse connection exists
                reverse_connections = LOCATIONS[connected_id].get("connections", [])
                
                if loc_id not in reverse_connections:
                    # Need to add bidirectional connection
                    fixes.append((connected_id, loc_id))
    
    print(f"Found {len(fixes)} missing reverse connections\n")
    
    if fixes:
        print("Connections to add:")
        for from_loc, to_loc in fixes:
            from_name = LOCATIONS[from_loc]['name']
            to_name = LOCATIONS[to_loc]['name']
            print(f"  {from_loc} -> {to_loc}")
            print(f"  ({from_name} -> {to_name})")
        
        print("\n" + "="*60)
        print("Python code to add to data.py:")
        print("="*60 + "\n")
        
        # Group by source location
        by_location = {}
        for from_loc, to_loc in fixes:
            if from_loc not in by_location:
                by_location[from_loc] = []
            by_location[from_loc].append(to_loc)
        
        for loc_id in sorted(by_location.keys()):
            connections_to_add = by_location[loc_id]
            print(f"# {LOCATIONS[loc_id]['name']}")
            print(f'LOCATIONS["{loc_id}"]["connections"].extend([')
            for conn in connections_to_add:
                print(f'    "{conn}",')
            print('])\n')

if __name__ == "__main__":
    analyze_and_fix_connections()
