# KBC ZipMap

**Live tool:** [https://gc-bcsa.github.io/zip_map/](https://gc-bcsa.github.io/zip_map/)

A browser-based US zip code mapping tool. Plot up to 10 series of zip codes (200 zips each) on an interactive map with full pan and zoom. No installation required — open the URL and go.

---

## Quick Start

1. Click **+ ADD SERIES** in the sidebar
2. Paste zip codes into the text area (comma, space, or newline separated)
3. Click **PLOT ZIPS**
4. Zoom and pan the map to your area of interest
5. Click **EXPORT PNG** to download a high-resolution image

---

## Header Controls

All header controls are uniform width and height. From left to right:

<table>
<tr>
<td><kbd style="background:#1A204C;color:#fff;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:none;display:inline-block">US 48+AK/HI</kbd></td>
<td>Map view showing the contiguous 48 states with Alaska and Hawaii insets. Projection is fixed to Albers USA.</td>
</tr>
<tr>
<td><kbd style="background:transparent;color:#fff;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid rgba(255,255,255,0.3);display:inline-block;background:#1A204C">LOWER 48</kbd></td>
<td>Contiguous 48 states only. Alaska and Hawaii are excluded. Projection is selectable.</td>
</tr>
<tr>
<td><kbd style="background:#1A204C;color:rgba(255,255,255,0.6);padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid rgba(255,255,255,0.3);display:inline-block">WORLD</kbd></td>
<td>World view with country borders and US state overlays. Projection is selectable.</td>
</tr>
<tr>
<td><kbd style="background:#21409A;color:#fff;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:none;display:inline-block">PLOT ZIPS</kbd></td>
<td>Resolves all entered zip codes to lat/lon coordinates and renders pins on the map. Run this after entering or changing zip codes.</td>
</tr>
<tr>
<td><kbd style="background:rgba(255,255,255,0.1);color:#fff;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid rgba(255,255,255,0.25);display:inline-block">&#9635; WATER</kbd></td>
<td>Checkbox toggle. When checked, the ocean/water background is visible on the map and included in exports. Uncheck for a transparent background in the exported PNG.</td>
</tr>
<tr>
<td><kbd style="background:rgba(255,255,255,0.1);color:#fff;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid rgba(255,255,255,0.25);display:inline-block">RESET</kbd></td>
<td>Resets pan and zoom back to the default fitted view for the current map selection.</td>
</tr>
<tr>
<td><kbd style="background:rgba(52,211,153,0.1);color:#34d399;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid #34d399;display:inline-block">EXPORT PNG</kbd></td>
<td>Exports the current map view as a PNG. The shortest side is always 2000px. The current pan/zoom position is captured as-is.</td>
</tr>
</table>

---

## Map Views

| View | Projection | Description |
|---|---|---|
| US 48+AK/HI | Albers USA (fixed) | All 50 states. Alaska and Hawaii rendered as insets in the lower left. |
| Lower 48 | Selectable | Contiguous states only. Zoom in without the AK/HI insets. |
| World | Selectable | Full world with country borders and US state detail overlaid. |

**Pan:** click and drag anywhere on the map.  
**Zoom:** scroll wheel. Scale range is 0.5&times; to 200&times;.  
**Reset:** click RESET in the header to return to the default fit.

---

## Projections

Available projections vary by map view. The dropdown appears in the sidebar below the series list when Lower 48 or World is active. It is hidden for US 48+AK/HI, which is always Albers USA.

| Projection | Available For |
|---|---|
| Albers USA | US 48+AK/HI only |
| Albers | Lower 48 |
| Lambert Conformal | Lower 48, World |
| Conic Equidistant | Lower 48, World |
| Mercator | Lower 48, World |
| Transverse Mercator | Lower 48, World |
| Equal Earth | Lower 48, World |
| Natural Earth | Lower 48, World |
| Azimuthal Equal-Area | Lower 48, World |
| Orthographic | Lower 48, World |
| Stereographic | Lower 48, World |
| Mollweide | World |
| Winkel Tripel | World |
| Robinson | World |

---

## Series Panel

Up to **10 series**, **200 zip codes each**. Each series is always fully expanded in the sidebar. Scroll the sidebar to see all series.

### Series Card

<table style="border:1px solid #c8ccd4;border-radius:8px;background:#e8eaed;padding:0;width:280px;border-spacing:0;font-family:Arial,sans-serif;overflow:hidden">
<tr style="background:#eaecf0;border-bottom:1px solid #c8ccd4">
  <td style="padding:8px 10px;display:flex;align-items:center;gap:8px">
    <span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#005B82;border:2px solid rgba(0,0,0,0.15)"></span>
    <strong style="color:#1A204C;font-size:13px">Series 1</strong>
    <span style="margin-left:auto;font-size:10px;color:#6b7280;font-family:monospace">3/3</span>
  </td>
</tr>
<tr><td style="padding:6px 10px">
  <table style="width:100%;border-spacing:0">
    <tr>
      <td style="font-size:10px;color:#21409A;font-family:monospace;width:48px">COLOR</td>
      <td>
        <span style="display:inline-block;width:20px;height:20px;background:#005B82;border-radius:3px;vertical-align:middle;margin-right:4px;border:1px solid #c8ccd4"></span>
        <code style="font-size:11px;background:#fff;border:1px solid #c8ccd4;padding:2px 6px;border-radius:3px">#005B82</code>
      </td>
    </tr>
    <tr><td colspan="2" style="padding:4px 0">
      <span style="font-size:10px;color:#21409A;font-family:monospace">SHAPE&nbsp;&nbsp;</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:4px;background:#21409A;text-align:center;line-height:24px;color:#fff;font-size:12px">●</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:4px;border:1px solid #c8ccd4;text-align:center;line-height:24px;font-size:12px">■</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:4px;border:1px solid #c8ccd4;text-align:center;line-height:24px;font-size:12px">◆</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:4px;border:1px solid #c8ccd4;text-align:center;line-height:24px;font-size:12px">▲</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:4px;border:1px solid #c8ccd4;text-align:center;line-height:24px;font-size:12px">★</span>
    </td></tr>
    <tr>
      <td style="font-size:10px;color:#21409A;font-family:monospace">SIZE</td>
      <td><input type="range" min="3" max="18" value="6" disabled style="width:140px;accent-color:#21409A"> <code style="font-size:10px">6</code></td>
    </tr>
    <tr>
      <td style="font-size:10px;color:#21409A;font-family:monospace">BORDER</td>
      <td><input type="checkbox" checked disabled> <span style="font-size:10px;font-family:monospace">ON</span></td>
    </tr>
    <tr><td colspan="2" style="padding-top:6px">
      <textarea disabled rows="3" style="width:100%;font-family:monospace;font-size:11px;background:#fff;border:1px solid #c8ccd4;border-radius:4px;padding:4px;resize:none;color:#1A204C">26105, 62260, 40508</textarea>
    </td></tr>
    <tr><td colspan="2" style="padding-top:6px;display:flex;gap:6px">
      <kbd style="background:#e8eaed;border:1px solid #c8ccd4;border-radius:4px;padding:3px 10px;font-family:monospace;font-size:10px;color:#1A204C">HIDE</kbd>
      <kbd style="background:#e8eaed;border:1px solid #c0392b;border-radius:4px;padding:3px 10px;font-family:monospace;font-size:10px;color:#c0392b">DEL</kbd>
    </td></tr>
    <tr><td colspan="2" style="padding-top:4px;font-family:monospace;font-size:10px;color:#059669">3 plotted, 0 failed</td></tr>
  </table>
</td></tr>
</table>

&nbsp;

### Series Card Fields

| Field | Description |
|---|---|
| **Name** | Editable text at the top of the card. Click to rename. |
| **Color** | Color picker and hex input. Defaults cycle through the 10-color brand palette. Both the swatch and hex field are synced. |
| **Shape** | Pin shape: circle, square, diamond, triangle, or star. |
| **Size** | Pin radius in pixels, range 3–18. |
| **Border** | Toggles the dark outline stroke on pins on or off. |
| **Zip codes** | Paste or type zip codes. Accepts comma, space, or newline delimiters. Maximum 200 per series. |
| **HIDE / SHOW** | Toggles visibility of the series pins on the map without deleting the data. |
| **DEL** | Permanently removes the series. |
| **Status** | Shows resolved/failed counts after PLOT ZIPS is run. |

---

## Sidebar Footer

<table style="border-spacing:6px">
<tr>
  <td><kbd style="background:#21409A;color:#fff;padding:6px 20px;border-radius:5px;font-family:monospace;font-size:12px;border:none;display:inline-block">+ ADD SERIES</kbd></td>
  <td>Adds a new series card. Maximum 10 series total.</td>
</tr>
<tr>
  <td><kbd style="background:transparent;color:#c0392b;padding:6px 16px;border-radius:5px;font-family:monospace;font-size:12px;border:1px solid #c0392b;display:inline-block">CLEAR ALL</kbd></td>
  <td>Removes all series after confirmation. Cannot be undone.</td>
</tr>
</table>

---

## Export

Clicking **EXPORT PNG** captures the current map viewport — including the current pan/zoom position — and saves it as a PNG file. The shorter dimension is always scaled to **2000px**, so a landscape viewport exports at roughly 2000&times;1200px or wider depending on window proportions.

The **WATER** checkbox controls whether the ocean background color is included in the export. Unchecked produces a transparent/white background suitable for overlaying on other documents.

---

## Color Palette

Default series colors follow the brand palette:

<table>
<tr>
  <td><span style="display:inline-block;width:20px;height:20px;background:#005B82;border-radius:3px;border:1px solid #ccc"></span></td><td>Cobalt <code>#005B82</code></td>
  <td><span style="display:inline-block;width:20px;height:20px;background:#00A9E0;border-radius:3px;border:1px solid #ccc"></span></td><td>Volt <code>#00A9E0</code></td>
</tr>
<tr>
  <td><span style="display:inline-block;width:20px;height:20px;background:#E37222;border-radius:3px;border:1px solid #ccc"></span></td><td>Clay <code>#E37222</code></td>
  <td><span style="display:inline-block;width:20px;height:20px;background:#FECB00;border-radius:3px;border:1px solid #ccc"></span></td><td>Solar <code>#FECB00</code></td>
</tr>
<tr>
  <td><span style="display:inline-block;width:20px;height:20px;background:#5A6A71;border-radius:3px;border:1px solid #ccc"></span></td><td>Slate <code>#5A6A71</code></td>
  <td><span style="display:inline-block;width:20px;height:20px;background:#0F6636;border-radius:3px;border:1px solid #ccc"></span></td><td>Meadow <code>#0F6636</code></td>
</tr>
<tr>
  <td><span style="display:inline-block;width:20px;height:20px;background:#69BE28;border-radius:3px;border:1px solid #ccc"></span></td><td>Leaf <code>#69BE28</code></td>
  <td><span style="display:inline-block;width:20px;height:20px;background:#C3C8C8;border-radius:3px;border:1px solid #ccc"></span></td><td>Cloud <code>#C3C8C8</code></td>
</tr>
<tr>
  <td><span style="display:inline-block;width:20px;height:20px;background:#21409A;border-radius:3px;border:1px solid #ccc"></span></td><td>Clear Blue <code>#21409A</code></td>
  <td><span style="display:inline-block;width:20px;height:20px;background:#1A204C;border-radius:3px;border:1px solid #ccc"></span></td><td>Cadet Blue <code>#1A204C</code></td>
</tr>
</table>

Any series color can be overridden via the color picker or hex input in the series card.

---

## Technical Notes

- All data processing happens in the browser. No data is sent to any server.
- Zip code coordinates are resolved from the [`us-zips`](https://www.npmjs.com/package/us-zips) package via jsDelivr CDN.
- Map geometry uses [`world-atlas`](https://github.com/topojson/world-atlas) and [`us-atlas`](https://github.com/topojson/us-atlas) via jsDelivr CDN.
- Rendering uses [D3.js v7](https://d3js.org/) and [TopoJSON](https://github.com/topojson/topojson).
- The tool is a single self-contained HTML file with no build step required.
