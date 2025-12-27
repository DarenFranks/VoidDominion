# Module Management Button Fixes

## Problem
In the Shipyard > Module Management section, action buttons (Install, Remove, ➜ Ship) were being cut off. This happened because:

1. **Scrollable frames not expanding** - Canvas window frames stayed at minimum width
2. **Two-column layout constraints** - Modules displayed in side-by-side columns
3. **Content squeezed** - Buttons and info frames had insufficient space

**Affected Sections:**
- Installed Modules (Remove buttons)
- Available Modules in Inventory (Install buttons)
- Station Storage Modules (➜ Ship buttons)

## Root Cause

### Scrollable Frame Width Issue
```python
# Canvas window created without width binding
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
```

**Problem:**
- Scrollable frame stayed at its natural minimum width
- Didn't expand to fill available canvas width
- Content was compressed, causing button text to be cut off
- Two-column layout further constrained available space

## Solution

### Dynamic Canvas Width Expansion

Make scrollable frames expand to fill the full canvas width using resize event bindings:

```python
# Create canvas window and store reference
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Bind canvas resize to update scrollable frame width
def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)
canvas.bind('<Configure>', on_canvas_configure)
```

### Simple Button Layout

Buttons pack directly on module_frame without containers:

```python
# Button packed FIRST on right side
self.create_button(
    module_frame,
    "Install",
    command,
    width=10,  # 10 characters fits "Install", "Remove", "➜ Ship"
    style='success'
).pack(side=tk.RIGHT, padx=5, pady=5)

# Info frame packed SECOND on left side (fills remaining space)
info_frame = tk.Frame(module_frame, bg=COLORS['bg_light'])
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
```

**Why This Works:**
1. **Canvas width binding** - Scrollable frames expand to full canvas width
2. **More horizontal space** - Content isn't squeezed into minimum width
3. **Simple layout** - Buttons pack directly without fixed containers
4. **Button width=10** - Enough characters for button text
5. **Info frame fills remaining** - Takes up all space after button

## Changes Made

### 1. Installed Modules Canvas - Width Expansion (Lines 3199-3204)
**Added:** Canvas resize binding to expand scrollable frame width

```python
installed_canvas_window = installed_canvas.create_window((0, 0), window=installed_scrollable, anchor="nw")

# Make scrollable frame expand to canvas width
def on_installed_canvas_configure(event):
    installed_canvas.itemconfig(installed_canvas_window, width=event.width)
installed_canvas.bind('<Configure>', on_installed_canvas_configure)
```

### 2. Installed Modules Buttons (Lines 3225-3232)
**Changed:** Simplified button layout, removed fixed containers

```python
# Remove button (right side)
self.create_button(
    module_frame,
    "Remove",
    lambda m=module_id, t=module_type: self.remove_module_action(m, t),
    width=10,
    style='danger'
).pack(side=tk.RIGHT, padx=5, pady=5)
```

### 3. Available Modules Canvas - Width Expansion (Lines 3296-3301)
**Added:** Canvas resize binding to expand scrollable frame width

```python
available_canvas_window = available_canvas.create_window((0, 0), window=available_scrollable, anchor="nw")

# Make scrollable frame expand to canvas width
def on_available_canvas_configure(event):
    available_canvas.itemconfig(available_canvas_window, width=event.width)
available_canvas.bind('<Configure>', on_available_canvas_configure)
```

### 4. Available Modules Buttons (Lines 3325-3342)
**Changed:** Simplified button layout

```python
# Install button (right side)
if can_install:
    self.create_button(
        module_frame,
        "Install",
        lambda m=module_id: self.install_module_action(m),
        width=10,
        style='success'
    ).pack(side=tk.RIGHT, padx=5, pady=5)
else:
    tk.Label(
        module_frame,
        text="No Slots",
        font=('Arial', 8),
        fg=COLORS['danger'],
        bg=COLORS['bg_light'],
        width=10
    ).pack(side=tk.RIGHT, padx=5, pady=5)
```

### 5. Station Storage Canvas - Width Expansion (Lines 3413-3418)
**Added:** Canvas resize binding to expand scrollable frame width

```python
station_canvas_window = station_canvas.create_window((0, 0), window=station_scrollable, anchor="nw")

# Make scrollable frame expand to canvas width
def on_station_canvas_configure(event):
    station_canvas.itemconfig(station_canvas_window, width=event.width)
station_canvas.bind('<Configure>', on_station_canvas_configure)
```

### 6. Station Storage Buttons (Lines 3434-3441)
**Changed:** Simplified button layout

```python
# Transfer to ship button (right side)
self.create_button(
    module_frame,
    "➜ Ship",
    lambda m=module_id: self.transfer_module_to_ship(m),
    width=10,
    style='info'
).pack(side=tk.RIGHT, padx=5, pady=5)
```

## Key Technique: Canvas Width Binding

The critical fix is binding canvas resize events to update scrollable frame width:

```python
# Store canvas window reference
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Bind resize event
def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)
canvas.bind('<Configure>', on_canvas_configure)
```

**What it does:**
- Updates scrollable frame width whenever canvas resizes
- Ensures content expands to fill full available width
- Prevents content from being squeezed into minimum natural width
- Works dynamically with window resizing

**Without this binding:**
- Scrollable frames stay at minimum natural width
- Content gets compressed
- Buttons and text get cut off
- Wasted empty space on the right side

## Testing

### How to Test
1. **Launch game:**
   ```bash
   python3 launch.py
   ```

2. **Navigate to Shipyard:**
   - Go to Shipyard view
   - Expand "⚙️ Module Management" section

3. **Test all three areas:**
   - **Installed Modules** - Verify "Remove" buttons fully visible
   - **Available Modules** - Verify "Install" buttons fully visible
   - **Station Storage** - Verify "➜ Ship" buttons fully visible

4. **Test with varying content:**
   - Modules with long names
   - Modules with many specs
   - Different screen sizes
   - Resize window

### Expected Results
✅ All buttons fully visible
✅ No button cut-off
✅ No overlap with adjacent columns
✅ Content expands to fill available width
✅ Buttons readable with full text

## Technical Details

### Canvas Width Binding
- **Trigger:** Canvas `<Configure>` event
- **Action:** Updates scrollable frame width via `canvas.itemconfig()`
- **Effect:** Scrollable content expands to fill canvas
- **Dynamic:** Responds to window resizing

### Button Specifications
- **Width:** 10 characters (fits "Install", "Remove", "➜ Ship")
- **Packing:** Direct on `module_frame` (no containers)
- **Side:** RIGHT (packed before info frame)
- **Parent:** `module_frame` (the list item container)

### Packing Order
1. **Button** → Right side, width=10
2. **Info frame** → Left side, fills remaining space

This simple order works because scrollable frames now expand properly.

## Benefits

### User Experience
✅ **All buttons visible** - No more cut-off Install/Remove buttons
✅ **Consistent layout** - Buttons always in same position
✅ **Better usability** - Easy to click action buttons
✅ **Professional appearance** - Clean, organized interface

### Technical
✅ **Predictable layout** - Fixed button width prevents layout issues
✅ **Scalable** - Works with varying module name lengths
✅ **Responsive** - Adapts to different window sizes
✅ **Maintainable** - Clear separation of button and info areas

## Files Modified

### gui.py
- **Lines 3199-3204** - Installed modules canvas width binding
- **Lines 3225-3232** - Installed modules button layout
- **Lines 3296-3301** - Available modules canvas width binding
- **Lines 3325-3342** - Available modules button layout
- **Lines 3413-3418** - Station storage canvas width binding
- **Lines 3434-3441** - Station storage button layout

**Total Changes:** 6 sections (3 canvas bindings + 3 button layouts)

## Pattern for Future Use

When creating scrollable canvases with list items:

```python
# ✅ CORRECT - Canvas with width binding
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add width binding for dynamic expansion
def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)
canvas.bind('<Configure>', on_canvas_configure)
```

For list items with action buttons:

```python
# ✅ CORRECT - Button first, simple layout
self.create_button(
    item_frame,
    "Action",
    command,
    width=10
).pack(side=tk.RIGHT, padx=5, pady=5)

info_frame = tk.Frame(item_frame, bg=bg_color)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
# ... info content ...
```

```python
# ❌ WRONG - No canvas width binding
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# Scrollable frame won't expand, content gets squeezed
```

## Summary

Fixed module management button cut-off issues by:
1. **Adding canvas width bindings** - Scrollable frames now expand to fill canvas width
2. **Simplifying button layout** - Buttons pack directly on module_frame (no containers)
3. **Using width=10** - Sufficient character width for button text
4. **Packing buttons first** - Right side placement before info frame

All three module sections now display buttons correctly without cut-off.

---

**Modified:** 2025-12-27
**Sections Fixed:** 6 (3 canvas bindings + 3 button layouts)
**Root Cause:** Scrollable frames not expanding to fill available width
**Solution:** Canvas resize event bindings + simplified button layout
**Impact:** Buttons now fully visible and clickable in all module sections
