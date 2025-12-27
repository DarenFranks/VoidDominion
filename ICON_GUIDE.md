# Icon System Guide for Void Dominion

## Overview

Void Dominion now features a comprehensive icon system that enhances the visual experience while maintaining the game's distinctive aesthetic. The system uses custom PNG icons with automatic fallback to Unicode symbols.

## Icon Specifications

### Technical Requirements
- **Format:** PNG with transparency (RGBA)
- **Size:** 32x32 pixels (base size)
- **Color Scheme:** Match the game's sci-fi theme
  - Primary accent: `#00d9ff` (Cyan)
  - Success/Positive: `#00ff88` (Green)
  - Warning: `#ffaa00` (Orange)
  - Danger: `#ff3366` (Red)
  - Background: `#1a2332` (Dark Blue-Grey)

### Icon Categories

Icons are organized in the following directories:

```
assets/icons/
├── resources/     # Raw and refined resources (91 generated)
├── ships/         # Ship classes (scout, fighter, hauler, etc.)
├── modules/       # Ship modules (weapons, shields, engines, etc.)
├── locations/     # Location types (station, planet, asteroid, nebula)
├── factions/      # Faction symbols
└── ui/            # UI elements (credits, fuel, cargo, etc.)
```

## How the System Works

### 1. Icon Loading Priority
1. **Custom PNG** - Loads from `assets/icons/{category}/{item_id}.png`
2. **Generated Symbol** - Falls back to Unicode symbol if PNG not found
3. **Rarity Tinting** - Automatically applies color based on item rarity

### 2. Size Variants
Icons are automatically scaled to different sizes:
- **Tiny:** 12px (compact displays)
- **Small:** 16px (inventory, storage lists)
- **Medium:** 24px (market listings, locations)
- **Large:** 32px (shipyard, important items)
- **Huge:** 48px (headers, special displays)

### 3. Rarity Colors
Items are color-coded by rarity:
- **Common:** `#8b949e` (Grey)
- **Uncommon:** `#00d9ff` (Cyan)
- **Rare:** `#00ff88` (Green)
- **Very Rare:** `#7b2cbf` (Purple)
- **Legendary:** `#ffaa00` (Gold/Orange)

## Customizing Icons

### Option 1: Edit Existing Placeholders

The generated placeholder icons can be edited:

1. Open icon in image editor (GIMP, Photoshop, Aseprite, etc.)
2. Keep 32x32 size and transparent background
3. Design your icon using the color scheme
4. Save as PNG with transparency
5. Replace the file in `assets/icons/{category}/`

### Option 2: Create New Icons from Scratch

**Recommended Tools:**
- **Aseprite** - Pixel art editor (perfect for 32x32 icons)
- **GIMP** - Free image editor
- **Photoshop** - Professional image editor
- **Krita** - Free painting program
- **Pixaki** - iOS pixel art app

**Creation Steps:**
1. Create new 32x32 canvas with transparent background
2. Design using 2-3 colors from the game palette
3. Keep designs simple and recognizable
4. Add subtle shading or glow effects (optional)
5. Export as PNG with transparency
6. Save to appropriate category folder

### Option 3: Use Icon Packs

You can use existing icon packs if they match the theme:

**Free Resources:**
- [Game-icons.net](https://game-icons.net/) - Thousands of game icons
- [Itch.io](https://itch.io/game-assets/free/tag-icons) - Free game assets
- [OpenGameArt.org](https://opengameart.org/) - Open source game art

**License Note:** Ensure icons are free for use or properly licensed.

## Icon Naming Convention

Icons must match the exact item ID from `data.py`:

### Resources
```
raw_voltium.png
raw_nexium.png
voltium.png
nexium.png
chronite.png
titanite.png
```

### Ships
```
scout.png
fighter.png
hauler.png
cruiser.png
destroyer.png
battleship.png
carrier.png
refinery.png
mothership.png
```

### Modules
```
pulse_cannon.png
plasma_lance.png
shield_generator.png
mining_laser.png
```

### Locations
```
station.png
planet.png
asteroid_belt.png
nebula.png
```

## Symbol Fallbacks

When PNG icons aren't available, the system uses Unicode symbols:

| Category | Symbol | Item |
|----------|--------|------|
| Resources | ⚡ | Voltium (conductive) |
| Resources | 💎 | Synthcrystal (rare) |
| Resources | 🌊 | Darkwater (void fluid) |
| Ships | 🚀 | Scout/Light ships |
| Ships | 🏰 | Battleship (heavy) |
| Ships | 🎯 | Carrier |
| Modules | ⚔️ | Weapons |
| Modules | 🛡️ | Shields |
| Modules | ⛏️ | Mining laser |
| Locations | 🏭 | Space station |
| Locations | 🌍 | Planet |
| Locations | ☄️ | Asteroid belt |

Full symbol list in `symbols.py`

## Testing Your Icons

1. Replace an icon PNG in `assets/icons/`
2. Launch the game: `python3 launch.py`
3. Navigate to where that item appears
4. The icon should display automatically
5. If not showing, check:
   - Filename matches item ID exactly
   - File is PNG format with transparency
   - File is in correct category folder

## Clearing Icon Cache

If icons don't update after replacement:

```python
# Add to your code or create a utility script
from icon_manager import get_icon_manager
icon_mgr = get_icon_manager()
icon_mgr.clear_cache()
```

Or simply restart the game - cache is memory-only.

## Advanced Customization

### Creating Animated Icons (Future Enhancement)

The system supports static PNGs currently. For future animation:
- Use sprite sheets (32x32 frames)
- Modify `icon_manager.py` to load and cycle frames
- Ideal for: engines (flames), shields (shimmer), resources (glow)

### Batch Icon Generation

Use the provided generator:

```bash
python3 generate_icons.py
```

This creates placeholder icons for all game items.

### Custom Color Schemes

Edit `symbols.py` `RARITY_COLORS` to change rarity colors:

```python
RARITY_COLORS = {
    'common': '#your_color_here',
    'uncommon': '#your_color_here',
    # ... etc
}
```

## Icon Style Guide

### Design Principles

1. **Simplicity** - Icons should be recognizable at 16px
2. **Consistency** - Use similar style across all icons
3. **Contrast** - Ensure icons stand out against dark backgrounds
4. **Symbolism** - Use universal symbols when possible
5. **Color Coding** - Leverage rarity colors for quick identification

### Example Icon Themes

**Option A: Minimalist Line Art**
- Simple outlines
- 1-2 pixel strokes
- High contrast
- Clean and modern

**Option B: Pixel Art Sprites**
- Retro pixel art style
- 8-bit or 16-bit aesthetic
- Chunky, readable pixels
- Nostalgic feel

**Option C: Glowing Neon**
- Neon outlines
- Glow effects
- Cyberpunk aesthetic
- Matches existing UI theme

## Community Contributions

Want to share your icon pack?
1. Create a complete set for a category
2. Package as ZIP with proper folder structure
3. Share on game's GitHub or forums
4. Credit yourself in a README

## Troubleshooting

### Icons Not Showing
- Check file extension is `.png` (lowercase)
- Verify filename matches item ID from `data.py`
- Ensure file is in correct category folder
- Check file permissions (should be readable)

### Icons Look Blurry
- Verify source is exactly 32x32 pixels
- Don't upscale smaller images
- Use crisp pixel art or vector-based designs

### Colors Don't Match
- Use eyedropper tool to sample colors from `gui.py` COLORS
- Apply color overlay instead of replacing
- Test against dark backgrounds

## Quick Start Checklist

- [x] Icons system installed and working
- [x] Placeholder icons generated (91 icons)
- [x] Icon manager integrated into GUI
- [ ] (Optional) Customize resource icons
- [ ] (Optional) Customize ship icons
- [ ] (Optional) Customize module icons
- [ ] (Optional) Customize location icons

## Resources

- **Icon Manager:** `icon_manager.py`
- **Symbol Definitions:** `symbols.py`
- **Generation Script:** `generate_icons.py`
- **Assets Folder:** `assets/icons/`
- **Game Data:** `data.py` (for item IDs)

---

**Happy icon designing!** Your customizations will make Void Dominion even more visually distinctive.
