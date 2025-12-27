# GUI Layout Fixes - Full Screen Column Expansion

## Problem
When running the game in full screen mode, single-column views were not expanding properly to use all available screen space. This caused:
- Text being cut off at fixed widths
- Action buttons being hidden or cut off
- Wasted empty space on the right side of the screen
- Poor use of screen real estate

## Root Causes

### 1. Fixed-Width Scrollable Frames
The scrollable canvas windows were not configured to expand to fill the parent canvas width. They were created with default width which didn't adapt to screen size.

**Original Code Pattern:**
```python
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
```

### 2. Fixed wraplength Values
Text labels used fixed `wraplength` values (like 700 pixels) that didn't adapt to different screen sizes.

**Example:**
```python
wraplength=700  # Fixed width - doesn't adapt to screen
```

### 3. Missing Expansion Hints
Single-column panels weren't given proper padding and expansion parameters.

## Solutions Implemented

### 1. Created `create_scrollable_frame()` Helper Method

Added a new helper method at `gui.py:773` that properly creates scrollable frames that automatically expand to fill available width:

```python
def create_scrollable_frame(self, parent, bg_color=None):
    """
    Create a scrollable frame that expands to fill available width
    Returns: (canvas, scrollbar, scrollable_frame)
    """
    canvas = tk.Canvas(parent, bg=bg_color, highlightthickness=0)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=bg_color)

    # Update scroll region when content changes
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=(0, 0, canvas.winfo_width(), scrollable_frame.winfo_reqheight()))
    )

    # Create window and make it expand to canvas width
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Bind canvas width changes to update scrollable frame width
    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)
    canvas.bind('<Configure>', on_canvas_configure)

    canvas.configure(yscrollcommand=scrollbar.set)
    self.bind_mousewheel(canvas, scrollable_frame)

    return canvas, scrollbar, scrollable_frame
```

**Key Innovation:**
- Binds canvas resize events to update the scrollable frame width
- Uses `canvas.itemconfig()` to dynamically set window width
- Ensures content always fills available horizontal space

### 2. Fixed Contracts View (`show_contracts_view`)

**Changes:**
- Added padding to panel: `panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)`
- Replaced manual scrollable frame creation with helper method
- Made description text wraplength dynamic based on available width

**Before:**
```python
wraplength=700  # Fixed
```

**After:**
```python
# Dynamic wraplength
def update_wraplength(event, label=desc_label):
    label.configure(wraplength=event.width - 30)
contract_frame.bind('<Configure>', update_wraplength)
```

### 3. Fixed Skills View (`show_skills_view`)

**Changes:**
- Added padding to panel: `panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)`
- Updated scrollable frame to use new helper method with width expansion

### 4. Fixed Market View (`show_market_view`)

**Changes:**
- Replaced manual scrollable frame creation with one-liner:

**Before:**
```python
canvas = tk.Canvas(market_content, bg=COLORS['bg_medium'], highlightthickness=0)
scrollbar = tk.Scrollbar(market_content, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=COLORS['bg_medium'])
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(...))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
self.bind_mousewheel(canvas, scrollable_frame)
```

**After:**
```python
canvas, scrollbar, scrollable_frame = self.create_scrollable_frame(market_content)
```

## Files Modified

### gui.py
- **Line 773-802**: Added `create_scrollable_frame()` helper method
- **Line 1863**: Updated market view scrollable frame
- **Line 2324**: Added padding to contracts panel
- **Line 2336-2344**: Updated contracts scrollable frame with width expansion
- **Line 2374-2387**: Made contract description wraplength dynamic
- **Line 2436**: Added padding to skills panel
- **Line 2531-2539**: Updated skills scrollable frame with width expansion

## Testing

### To Verify Fixes:
1. Launch game in full screen or maximize window
2. Navigate to:
   - **Contracts** - Verify description text wraps properly, buttons visible
   - **Skills** - Verify all content expands to fill width
   - **Market** - Verify listings expand to fill width
3. Resize window - content should adapt dynamically
4. Check all action buttons are fully visible

### Expected Behavior:
- ✅ Single-column views fill entire content area width
- ✅ Text wraps dynamically based on available space
- ✅ No buttons cut off or hidden
- ✅ Consistent spacing and padding
- ✅ Responsive to window resizing

## Future Improvements

### Apply Helper to All Views
The `create_scrollable_frame()` helper should be adopted by all scrollable views for consistency:

**Views to Update:**
- Travel view (`show_travel_view` - line ~1669)
- Vessel view (if needed)
- Shipyard view (nested scrollable frames - lines ~3515, ~3758)
- Components view (line ~4256)
- Storage view (line ~4678)
- Modules view (line ~4861)
- Manufacturing view (line ~5440)

**Pattern to Replace:**
```python
# OLD PATTERN (11 lines)
canvas = tk.Canvas(parent, bg=COLORS['bg_medium'], highlightthickness=0)
scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=COLORS['bg_medium'])
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=(0, 0, canvas.winfo_width(), scrollable_frame.winfo_reqheight()))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
self.bind_mousewheel(canvas, scrollable_frame)

# NEW PATTERN (1 line)
canvas, scrollbar, scrollable_frame = self.create_scrollable_frame(parent)
```

**Benefits:**
- Reduces code duplication (11 lines → 1 line)
- Ensures consistent behavior across all views
- Automatically includes width expansion fix
- Easier to maintain and update

### Remove Fixed Width Labels
Future optimization: Audit all `width=` parameters on labels to see if they can be removed or made dynamic.

**Current Fixed Widths:**
- Lines with `width=20`, `width=30`, `width=12` on labels
- Consider using `anchor='w'` with `fill=tk.X` instead

## Summary

These fixes ensure that single-column views in the GUI properly expand to use all available screen space, especially important for full-screen or large monitor users. The content now dynamically adapts to any window size, with text wrapping appropriately and all UI elements remaining visible and accessible.

**Impact:**
- ✅ Better UX on full-screen mode
- ✅ Better UX on large monitors (1440p, 4K)
- ✅ Responsive design that adapts to window resizing
- ✅ No more hidden or cut-off buttons
- ✅ Optimal use of screen real estate

---

**Modified:** 2025-12-27
**Affected Views:** Contracts, Skills, Market (with helper method for future use)
