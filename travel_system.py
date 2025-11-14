"""
Travel System - Distance and Time Calculations
"""

# Distance matrix between locations (in light-seconds)
# Actual travel time depends on vessel speed
# Base formula: travel_time_seconds = distance / vessel_speed

# Default distances if not specified
DEFAULT_DISTANCE = 500  # Light-seconds for connected locations

# Specific distances between key locations
# Format: (location1, location2): distance_in_light_seconds
TRAVEL_DISTANCES = {
    # Neutral Zone connections
    ("nexus_prime", "starlight_waystation"): 150,
    ("nexus_prime", "outer_belts"): 200,
    ("nexus_prime", "meridian_gates"): 300,
    ("nexus_prime", "forge_station"): 250,
    ("nexus_prime", "titan_alpha"): 350,
    ("nexus_prime", "freeport_exchange"): 180,
    
    ("starlight_waystation", "outer_belts"): 100,
    ("starlight_waystation", "tranquil_belt"): 80,
    
    ("tranquil_belt", "harvest_fields"): 120,
    
    ("freeport_exchange", "titan_alpha"): 200,
    ("freeport_exchange", "aurora_reach"): 250,
    
    # Meridian Collective Territory
    ("titan_alpha", "outer_belts"): 180,
    ("titan_alpha", "harvest_fields"): 150,
    ("titan_alpha", "sapphire_fields"): 200,
    ("titan_alpha", "aurora_reach"): 280,
    ("titan_alpha", "eden_prime"): 300,
    
    ("aurora_reach", "sapphire_fields"): 150,
    ("aurora_reach", "merchant_corridor"): 200,
    
    ("merchant_corridor", "prosperity_hub"): 250,
    ("merchant_corridor", "meridian_gates"): 300,
    
    ("prosperity_hub", "eden_prime"): 200,
    ("prosperity_hub", "crystal_gardens"): 350,
    
    ("eden_prime", "verdant_belt"): 120,
    ("eden_prime", "horizon_vista"): 180,
    
    ("crystal_gardens", "explorer_outpost"): 400,
    
    ("explorer_outpost", "uncharted_expanse"): 450,
    ("explorer_outpost", "meridian_gates"): 350,
    
    # Technocrat Union Territory
    ("forge_station", "synthesis_planet"): 200,
    ("forge_station", "ironhold_sectors"): 350,
    ("forge_station", "binary_belt"): 150,
    
    ("synthesis_planet", "neural_network"): 250,
    ("synthesis_planet", "axiom_labs"): 300,
    ("synthesis_planet", "datacore_prime"): 280,
    ("synthesis_planet", "void_forge"): 400,
    
    ("neural_network", "axiom_labs"): 200,
    ("neural_network", "silicon_spire"): 220,
    ("neural_network", "datacore_prime"): 180,
    
    ("datacore_prime", "protocol_labs"): 250,
    ("datacore_prime", "binary_belt"): 150,
    ("datacore_prime", "silicon_spire"): 200,
    
    ("protocol_labs", "axiom_labs"): 180,
    ("protocol_labs", "quantum_drift"): 350,
    ("protocol_labs", "algorithm_expanse"): 280,
    
    ("quantum_drift", "chronos_expanse"): 300,
    ("quantum_drift", "singularity_reach"): 400,
    ("quantum_drift", "recursion_point"): 320,
    
    ("singularity_reach", "void_forge"): 350,
    ("singularity_reach", "axiom_labs"): 300,
    
    ("void_forge", "circuit_fields"): 180,
    ("void_forge", "convergence_nexus"): 250,
    
    ("silicon_spire", "algorithm_expanse"): 200,
    ("silicon_spire", "convergence_nexus"): 280,
    
    # Cipher Dominion Territory  
    ("meridian_gates", "crimson_expanse"): 400,
    ("meridian_gates", "outer_belts"): 250,
    
    ("crimson_expanse", "ironhold_world"): 350,
    ("crimson_expanse", "ironhold_sectors"): 300,
    ("crimson_expanse", "bastion_prime"): 450,
    ("crimson_expanse", "contested_zone"): 400,
    
    ("ironhold_world", "ironhold_sectors"): 200,
    ("ironhold_world", "vanguard_citadel"): 350,
    ("ironhold_world", "forge_station"): 400,
    
    ("ironhold_sectors", "pristine_fields"): 250,
    ("ironhold_sectors", "warforge_belt"): 200,
    ("ironhold_sectors", "iron_expanse"): 280,
    
    ("bastion_prime", "garrison_outpost"): 300,
    ("bastion_prime", "warforge_belt"): 250,
    ("bastion_prime", "dreadnought_yards"): 400,
    ("bastion_prime", "supremacy_throne"): 500,
    
    ("garrison_outpost", "bloodstone_fields"): 280,
    ("garrison_outpost", "contested_zone"): 350,
    
    ("bloodstone_fields", "conquest_reach"): 320,
    
    ("conquest_reach", "vanguard_citadel"): 380,
    ("conquest_reach", "contested_zone"): 300,
    
    ("vanguard_citadel", "sovereign_belt"): 200,
    ("vanguard_citadel", "dreadnought_yards"): 350,
    ("vanguard_citadel", "supremacy_throne"): 400,
    
    ("dreadnought_yards", "iron_expanse"): 250,
    ("dreadnought_yards", "supremacy_throne"): 300,
    
    # Void Corsairs Territory (Far reaches - longest distances)
    ("outer_belts", "shadow_nebula"): 400,
    
    ("shadow_nebula", "dead_zone_asteroids"): 500,
    ("shadow_nebula", "corsair_haven"): 450,
    ("shadow_nebula", "blackmarket_dock"): 400,
    ("shadow_nebula", "phantom_reach"): 550,
    
    ("corsair_haven", "dead_zone_asteroids"): 350,
    ("corsair_haven", "blackmarket_dock"): 200,
    ("corsair_haven", "dread_maw"): 600,
    
    ("phantom_reach", "reaver_belt"): 500,
    ("phantom_reach", "corsair_haven"): 550,
    
    ("reaver_belt", "dead_zone_asteroids"): 400,
    ("reaver_belt", "dread_maw"): 550,
    
    ("dread_maw", "abyss_edge"): 650,
    
    ("abyss_edge", "oblivion_gate"): 700,  # Furthest reach
    
    ("oblivion_gate", "dread_maw"): 600,
    ("oblivion_gate", "shadow_nebula"): 800,
    
    # Research connections
    ("axiom_labs", "chronos_expanse"): 350,
    ("chronos_expanse", "synthesis_planet"): 300,
}


def get_travel_distance(location_a, location_b):
    """
    Get distance between two locations in light-seconds
    Returns distance or DEFAULT_DISTANCE if not specified
    """
    # Check both orders since connections are bidirectional
    key1 = (location_a, location_b)
    key2 = (location_b, location_a)
    
    if key1 in TRAVEL_DISTANCES:
        return TRAVEL_DISTANCES[key1]
    elif key2 in TRAVEL_DISTANCES:
        return TRAVEL_DISTANCES[key2]
    else:
        return DEFAULT_DISTANCE


def calculate_travel_time(distance, vessel_speed):
    """
    Calculate travel time in seconds
    
    Args:
        distance: Distance in light-seconds
        vessel_speed: Vessel speed stat (higher = faster)
    
    Returns:
        Travel time in seconds (integer)
    """
    # Formula: base_time = distance / speed_factor
    # Speed factor = max(vessel_speed / 10, 1) to prevent division issues
    speed_factor = max(vessel_speed / 10.0, 1.0)
    travel_time = int(distance / speed_factor)
    
    # Minimum 2 seconds, maximum 10 seconds
    return max(2, min(travel_time, 10))


def format_travel_time(seconds):
    """Format travel time for display"""
    if seconds < 60:
        return f"{seconds}s"
    else:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        if remaining_seconds > 0:
            return f"{minutes}m {remaining_seconds}s"
        else:
            return f"{minutes}m"
