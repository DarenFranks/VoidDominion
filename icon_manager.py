"""
Icon Manager for Void Dominion
Handles loading, caching, and generating icons with symbol fallbacks
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from symbols import get_symbol, get_rarity_color, RARITY_COLORS

# Optional tkinter imports (only needed for GUI display)
try:
    import tkinter as tk
    from tkinter import PhotoImage
    from PIL import ImageTk
    HAS_TK = True
except ImportError:
    HAS_TK = False
    ImageTk = None


class IconManager:
    """Manages game icons with caching and fallback to symbols"""

    def __init__(self, assets_dir="assets/icons"):
        """
        Initialize the icon manager

        Args:
            assets_dir: Path to the icons directory
        """
        self.assets_dir = Path(assets_dir)
        self.icon_cache = {}  # Cache for PhotoImage objects
        self.symbol_cache = {}  # Cache for symbol-based icons

        # Create assets directory if it doesn't exist
        self.assets_dir.mkdir(parents=True, exist_ok=True)

        # Default sizes
        self.default_size = 16
        self.sizes = {
            'tiny': 12,
            'small': 16,
            'medium': 24,
            'large': 32,
            'huge': 48,
        }

        # Color scheme (matches gui.py)
        self.colors = {
            'bg': '#1a2332',
            'text': '#e6edf3',
            'accent': '#00d9ff',
            'border': '#30363d',
        }

    def get_icon(self, category, item_id, size='small', rarity=None):
        """
        Get an icon for an item, loading from file or generating from symbol

        Args:
            category: Icon category ('resource', 'ship', 'module', 'location', 'faction', 'ui')
            item_id: Item identifier
            size: Size name ('tiny', 'small', 'medium', 'large', 'huge') or pixel size
            rarity: Optional rarity for color coding ('common', 'uncommon', 'rare', 'very_rare', 'legendary')

        Returns:
            PhotoImage object ready for tkinter display
        """
        # Convert size name to pixels
        if isinstance(size, str):
            pixel_size = self.sizes.get(size, self.default_size)
        else:
            pixel_size = size

        # Create cache key
        cache_key = f"{category}_{item_id}_{pixel_size}_{rarity}"

        # Check cache first
        if cache_key in self.icon_cache:
            return self.icon_cache[cache_key]

        # Try to load from file
        icon_path = self.assets_dir / category / f"{item_id}.png"
        if icon_path.exists():
            icon = self._load_icon_from_file(icon_path, pixel_size, rarity)
        else:
            # Fallback to generated symbol icon
            icon = self._generate_symbol_icon(category, item_id, pixel_size, rarity)

        # Cache and return
        self.icon_cache[cache_key] = icon
        return icon

    def _load_icon_from_file(self, path, size, rarity=None):
        """Load and resize an icon from a PNG file"""
        if not HAS_TK:
            return None

        try:
            img = Image.open(path)
            img = img.resize((size, size), Image.Resampling.LANCZOS)

            # Apply rarity tint if specified
            if rarity:
                img = self._apply_rarity_tint(img, rarity)

            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Warning: Failed to load icon from {path}: {e}")
            # Fallback to symbol
            return None

    def _apply_rarity_tint(self, img, rarity):
        """Apply a subtle color tint based on rarity"""
        if rarity not in RARITY_COLORS:
            return img

        # Convert to RGBA if necessary
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Create a colored overlay
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        color = self._hex_to_rgb(RARITY_COLORS[rarity])

        # Draw a subtle tint
        draw = ImageDraw.Draw(overlay)
        draw.rectangle([0, 0, img.size[0], img.size[1]], fill=(*color, 30))

        # Composite the overlay onto the image
        img = Image.alpha_composite(img, overlay)
        return img

    def _generate_symbol_icon(self, category, item_id, size, rarity=None):
        """Generate an icon from a unicode symbol"""
        if not HAS_TK:
            return None

        symbol = get_symbol(category, item_id)

        # Create cache key for symbol
        symbol_cache_key = f"symbol_{symbol}_{size}_{rarity}"
        if symbol_cache_key in self.symbol_cache:
            return self.symbol_cache[symbol_cache_key]

        # Create an image with the symbol
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Determine font size (about 75% of image size for good fit)
        font_size = int(size * 0.75)

        try:
            # Try to use a nice font
            # On most systems, we can use DejaVu or similar
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except:
            try:
                # Fallback to another common font
                font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)
            except:
                # Use default font
                font = ImageFont.load_default()

        # Determine color based on rarity
        if rarity:
            color = RARITY_COLORS.get(rarity, self.colors['text'])
        else:
            color = self.colors['text']

        # Calculate text position to center it
        bbox = draw.textbbox((0, 0), symbol, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size - text_width) // 2 - bbox[0]
        y = (size - text_height) // 2 - bbox[1]

        # Draw the symbol
        draw.text((x, y), symbol, font=font, fill=color, embedded_color=True)

        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(img)

        # Cache the symbol icon
        self.symbol_cache[symbol_cache_key] = photo
        return photo

    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def create_placeholder_icons(self):
        """
        Generate placeholder PNG icons for all categories
        This creates simple colored squares with symbols that can be replaced later
        """
        from data import RAW_RESOURCES, REFINED_RESOURCES, VESSEL_CLASSES, MODULES, LOCATIONS, FACTIONS

        print("Generating placeholder icons...")

        # Resources
        for resource_id in list(RAW_RESOURCES.keys()) + list(REFINED_RESOURCES.keys()):
            self._create_placeholder_png('resources', resource_id, get_symbol('resource', resource_id))

        # Ships (vessel classes)
        ship_types = ['scout', 'fighter', 'hauler', 'cruiser', 'destroyer', 'battleship', 'carrier', 'refinery', 'mothership', 'corvette', 'frigate']
        for ship_type in ship_types:
            self._create_placeholder_png('ships', ship_type, get_symbol('ship', ship_type))

        # Module types (create generic icons for each module type)
        module_types = ['weapon', 'shield', 'engine', 'scanner', 'computer', 'power_core',
                       'mining_laser', 'cargo_hold', 'armor', 'hull_frame', 'thruster',
                       'pulse_cannon', 'plasma_lance', 'void_torpedo', 'railgun', 'ion_beam']
        for module_type in module_types:
            self._create_placeholder_png('modules', module_type, get_symbol('module', module_type))

        # Locations
        location_types = ['station', 'planet', 'asteroid_belt', 'nebula', 'outpost', 'sector', 'expanse', 'void', 'gate']
        for loc_type in location_types:
            self._create_placeholder_png('locations', loc_type, get_symbol('location', loc_type))

        # Factions
        faction_ids = ['meridian_collective', 'technocrat_union', 'void_walkers', 'free_traders',
                      'crimson_fleet', 'stellar_guard', 'outcasts']
        for faction_id in faction_ids:
            self._create_placeholder_png('factions', faction_id, get_symbol('faction', faction_id))

        # UI icons
        ui_icons = ['credits', 'fuel', 'cargo', 'health', 'shield_status', 'danger', 'hostile',
                   'friendly', 'neutral', 'locked', 'unlocked', 'level', 'experience', 'skill',
                   'quest', 'contract', 'combat', 'trade', 'manufacture', 'refine', 'mine',
                   'repair', 'upgrade', 'sell', 'buy', 'inventory', 'map', 'location', 'travel',
                   'docked', 'undocked']
        for ui_icon in ui_icons:
            self._create_placeholder_png('ui', ui_icon, get_symbol('ui', ui_icon))

        print(f"✓ Placeholder icons generated in {self.assets_dir}")

    def _create_placeholder_png(self, category, item_id, symbol, size=32):
        """Create a placeholder PNG icon with a symbol"""
        output_path = self.assets_dir / category / f"{item_id}.png"

        # Skip if already exists
        if output_path.exists():
            return

        # Create image with background
        img = Image.new('RGBA', (size, size), (26, 35, 50, 255))  # bg_light color
        draw = ImageDraw.Draw(img)

        # Add a subtle border
        draw.rectangle([0, 0, size-1, size-1], outline=(48, 54, 61, 255), width=1)  # border color

        # Font size
        font_size = int(size * 0.6)

        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)
            except:
                font = ImageFont.load_default()

        # Center the symbol
        bbox = draw.textbbox((0, 0), symbol, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size - text_width) // 2 - bbox[0]
        y = (size - text_height) // 2 - bbox[1]

        # Draw symbol in accent color
        draw.text((x, y), symbol, font=font, fill=(0, 217, 255, 255), embedded_color=True)  # accent color

        # Save the icon
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, 'PNG')

    def clear_cache(self):
        """Clear the icon cache (useful if icons are updated)"""
        self.icon_cache.clear()
        self.symbol_cache.clear()

    def preload_common_icons(self, size='small'):
        """Preload commonly used icons into cache"""
        common_ui = ['credits', 'fuel', 'cargo', 'shield_status', 'health']
        for icon_id in common_ui:
            self.get_icon('ui', icon_id, size)


# Singleton instance
_icon_manager = None


def get_icon_manager():
    """Get the global IconManager instance"""
    global _icon_manager
    if _icon_manager is None:
        _icon_manager = IconManager()
    return _icon_manager
