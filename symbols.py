"""
Symbol definitions for Void Dominion
Unicode symbols used as fallbacks when custom icons are not available
"""

# ============= RESOURCE SYMBOLS =============
RESOURCE_SYMBOLS = {
    # Raw Resources
    'raw_voltium': '⚡',           # Lightning bolt - conductive ore
    'raw_nexium': '💨',            # Dash/gas cloud - exotic gas
    'raw_chronite': '🔷',          # Diamond - time crystal
    'raw_titanite': '⬛',          # Black square - heavy metal
    'raw_synthcrystal': '💎',      # Gem - programmable crystal
    'raw_darkwater': '🌊',         # Water wave - void fluid
    'raw_neuralfiber': '🧬',       # DNA - organic computing
    'raw_quantum_dust': '✨',      # Sparkles - quantum particles

    # Refined Resources
    'voltium': '🔋',               # Battery - refined conductive
    'nexium': '🛢️',               # Oil drum - refined fuel
    'chronite': '💠',              # Diamond with dot - processed crystal
    'titanite': '🔩',              # Nut and bolt - alloy material
    'synthcrystal': '💠',          # Diamond with dot - matrix
    'darkwater': '🌀',             # Spiral - stabilized essence
    'neural_fiber': '🧵',          # Thread - fiber mesh
    'quantum_dust': '⭐',          # Star - refined particles
    'plasmic_fuel': '⚗️',          # Alembic - advanced fuel
}

# ============= SHIP CLASS SYMBOLS =============
SHIP_SYMBOLS = {
    'scout': '🔭',                 # Telescope - exploration vessel
    'fighter': '✈️',               # Airplane - combat fighter
    'hauler': '📦',                # Package - cargo ship
    'cruiser': '🚢',               # Ship - medium cruiser
    'destroyer': '⚔️',             # Crossed swords - combat ship
    'battleship': '🏰',            # Castle - heavy battleship
    'carrier': '🎯',               # Target - carrier with fighters
    'refinery': '⚙️',              # Gear - processing ship
    'mothership': '🏛️',            # Classical building - massive command ship
    'corvette': '🚀',              # Rocket - small fast ship
    'frigate': '🛸',               # Flying saucer - medium ship
}

# ============= MODULE TYPE SYMBOLS =============
MODULE_SYMBOLS = {
    # Weapons
    'weapon': '⚔️',                # Sword - weapons
    'pulse_cannon': '🔫',          # Gun - pulse weapon
    'plasma_lance': '🔥',          # Fire - beam weapon
    'void_torpedo': '💣',          # Bomb - explosive
    'railgun': '⚡',               # Lightning - railgun
    'ion_beam': '⚡',              # Lightning - ion weapon

    # Defense
    'shield': '🛡️',               # Shield - defense
    'shield_generator': '🛡️',     # Shield
    'armor': '🔰',                 # Shield with emblem - armor
    'hull_frame': '🔰',            # Shield with emblem

    # Engines & Propulsion
    'engine': '🔥',                # Fire - engine
    'thruster': '🚀',              # Rocket - thruster
    'thruster_array': '🚀',        # Rocket

    # Utility
    'scanner': '📡',               # Satellite - scanner
    'sensor': '📡',                # Satellite
    'sensor_suite': '📡',          # Satellite
    'computer': '💻',              # Computer - processing
    'computer_system': '💻',       # Computer
    'power_core': '⚡',            # Lightning - power
    'mining_laser': '⛏️',          # Pickaxe - mining
    'refining_module': '⚙️',       # Gear - refining
    'manufacturing': '🏭',         # Factory - manufacturing
    'cargo_hold': '📦',            # Package - storage
    'life_support': '💨',          # Dash - air/life support
    'weapon_mount': '🎯',          # Target - weapon mounting
}

# ============= LOCATION TYPE SYMBOLS =============
LOCATION_SYMBOLS = {
    'station': '🏭',               # Factory - space station
    'planet': '🌍',                # Earth - planet
    'asteroid_belt': '☄️',         # Comet - asteroids
    'nebula': '🌌',                # Milky way - nebula
    'outpost': '🏘️',              # Houses - small outpost
    'sector': '📍',                # Pin - space sector
    'expanse': '🌠',               # Shooting star - open space
    'void': '⚫',                  # Black circle - void space
    'gate': '🚪',                  # Door - jump gate
}

# ============= FACTION SYMBOLS =============
FACTION_SYMBOLS = {
    'meridian_collective': '⚖️',   # Balance scales - justice/order
    'technocrat_union': '⚙️',      # Gear - technology
    'void_walkers': '👻',          # Ghost - void dwellers
    'free_traders': '💰',          # Money bag - commerce
    'crimson_fleet': '🏴‍☠️',        # Pirate flag - pirates
    'stellar_guard': '🛡️',         # Shield - military
    'outcasts': '💀',              # Skull - outlaws
}

# ============= UI & STATUS SYMBOLS =============
UI_SYMBOLS = {
    'credits': '💰',               # Money bag
    'fuel': '⛽',                  # Fuel pump
    'cargo': '📦',                 # Package
    'health': '❤️',                # Heart
    'shield_status': '🛡️',        # Shield
    'danger': '⚠️',                # Warning
    'hostile': '☠️',               # Skull and crossbones
    'friendly': '🤝',              # Handshake
    'neutral': '➖',               # Minus/neutral
    'locked': '🔒',                # Locked
    'unlocked': '🔓',              # Unlocked
    'level': '⭐',                 # Star
    'experience': '📊',            # Bar chart
    'skill': '🎯',                 # Target
    'quest': '📜',                 # Scroll
    'contract': '📋',              # Clipboard
    'combat': '⚔️',                # Crossed swords
    'trade': '💱',                 # Currency exchange
    'manufacture': '🏭',           # Factory
    'refine': '⚗️',                # Alembic
    'mine': '⛏️',                  # Pickaxe
    'repair': '🔧',                # Wrench
    'upgrade': '⬆️',               # Up arrow
    'sell': '💸',                  # Money with wings
    'buy': '🛒',                   # Shopping cart
    'inventory': '🎒',             # Backpack
    'map': '🗺️',                   # World map
    'location': '📍',              # Pin
    'travel': '🧭',                # Compass
    'docked': '⚓',                # Anchor
    'undocked': '🚀',              # Rocket
}

# ============= RARITY COLOR CODES =============
# These work with the existing COLORS scheme in gui.py
RARITY_COLORS = {
    'common': '#8b949e',           # Grey (text_dim)
    'uncommon': '#00d9ff',         # Cyan (accent)
    'rare': '#00ff88',             # Green (success)
    'very_rare': '#7b2cbf',        # Purple (secondary)
    'legendary': '#ffaa00',        # Orange/Gold (warning)
}

# ============= HELPER FUNCTIONS =============

def get_symbol(category, item_id):
    """
    Get the symbol for a given item

    Args:
        category: 'resource', 'ship', 'module', 'location', 'faction', 'ui'
        item_id: The item identifier

    Returns:
        Unicode symbol string or default '●'
    """
    symbol_maps = {
        'resource': RESOURCE_SYMBOLS,
        'ship': SHIP_SYMBOLS,
        'module': MODULE_SYMBOLS,
        'location': LOCATION_SYMBOLS,
        'faction': FACTION_SYMBOLS,
        'ui': UI_SYMBOLS,
    }

    symbol_map = symbol_maps.get(category, {})

    # Try exact match first
    if item_id in symbol_map:
        return symbol_map[item_id]

    # Try partial match for modules (e.g., "pulse_cannon_t1" -> "pulse_cannon")
    if category == 'module':
        for key in MODULE_SYMBOLS:
            if item_id.startswith(key) or key in item_id:
                return MODULE_SYMBOLS[key]

    # Default symbol
    return '●'


def get_rarity_color(rarity):
    """Get the color code for a rarity level"""
    return RARITY_COLORS.get(rarity, RARITY_COLORS['common'])


# ============= SYMBOL CATEGORIES FOR QUICK REFERENCE =============
CATEGORY_DEFAULTS = {
    'resource': '📦',
    'ship': '🚀',
    'module': '⚙️',
    'location': '📍',
    'faction': '🏛️',
    'ui': '●',
}
