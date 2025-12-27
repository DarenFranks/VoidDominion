#!/usr/bin/env python3
"""
Generate placeholder icons for Void Dominion
Run this script to create all placeholder icon PNG files
"""

import sys

def main():
    print("=" * 60)
    print("  Void Dominion - Icon Generator")
    print("=" * 60)
    print()

    # Check for PIL/Pillow
    try:
        from PIL import Image
        print("✓ Pillow (PIL) is installed")
    except ImportError:
        print("✗ Pillow (PIL) is NOT installed")
        print()
        print("To install Pillow:")
        print("  pip3 install Pillow")
        print()
        sys.exit(1)

    print()
    print("Generating placeholder icons...")
    print()

    # Import and use the icon manager
    from icon_manager import get_icon_manager

    icon_mgr = get_icon_manager()
    icon_mgr.create_placeholder_icons()

    print()
    print("=" * 60)
    print("  Icon generation complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review generated icons in assets/icons/")
    print("  2. Replace placeholders with custom artwork (optional)")
    print("  3. Launch the game to see icons in action")
    print()
    print("Icon format: 32x32 PNG with transparency")
    print("See ICON_GUIDE.md for customization tips")
    print()

if __name__ == "__main__":
    main()
