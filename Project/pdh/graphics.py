"""Original line-art icons for the farm-to-plate graphic (black outline, light green tint)."""
from __future__ import annotations

K, TINT, ACC = "#111", "#E3F1E4", "#2E7D32"
S = f'stroke="{K}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"'

SPROUT = f"""<svg viewBox="0 0 96 96" class="icon" aria-hidden="true">
<path d="M20 72 Q48 50 76 72 Z" fill="#F3F3F3" {S}/>
<path d="M48 63 V40" fill="none" {S}/>
<path d="M48 46 C48 33 38 29 29 31 C29 42 38 48 48 46 Z" fill="{TINT}" {S}/>
<path d="M48 41 C48 28 58 22 68 24 C68 37 58 43 48 41 Z" fill="{TINT}" {S}/></svg>"""

BOX = f"""<svg viewBox="0 0 96 96" class="icon" aria-hidden="true">
<rect x="20" y="30" width="56" height="42" rx="4" fill="{TINT}" {S}/>
<path d="M20 43 H76" fill="none" {S}/>
<rect x="32" y="49" width="9" height="9" fill="#fff" {S}/><rect x="55" y="49" width="9" height="9" fill="#fff" {S}/>
<rect x="32" y="61" width="9" height="7" fill="#fff" {S}/>
<rect x="45" y="50" width="4" height="4" fill="{K}"/><rect x="45" y="58" width="4" height="4" fill="{K}"/>
<rect x="55" y="61" width="4" height="4" fill="{K}"/><rect x="60" y="64" width="4" height="4" fill="{K}"/></svg>"""

STALL = f"""<svg viewBox="0 0 96 96" class="icon" aria-hidden="true">
<path d="M18 40 L26 24 H70 L78 40 Z" fill="{TINT}" {S}/>
<path d="M35 24 L32 40 M48 24 V40 M61 24 L64 40" fill="none" {S}/>
<rect x="22" y="40" width="52" height="32" fill="#fff" {S}/>
<rect x="27" y="54" width="12" height="12" fill="{TINT}" {S}/><rect x="42" y="54" width="12" height="12" fill="{TINT}" {S}/>
<rect x="57" y="54" width="12" height="12" fill="{TINT}" {S}/></svg>"""

PLATE = f"""<svg viewBox="0 0 96 96" class="icon" aria-hidden="true">
<circle cx="48" cy="48" r="26" fill="#fff" {S}/><circle cx="48" cy="48" r="17" fill="{TINT}" {S}/>
<circle cx="42" cy="46" r="4" fill="{ACC}" stroke="{K}" stroke-width="2"/><circle cx="53" cy="44" r="3.5" fill="{ACC}" stroke="{K}" stroke-width="2"/>
<circle cx="49" cy="55" r="4" fill="{ACC}" stroke="{K}" stroke-width="2"/>
<path d="M12 28 V42 M9 28 V38 M15 28 V38 M12 42 V68" fill="none" {S}/>
<path d="M86 28 C91 36 91 46 86 52 V68" fill="none" {S}/></svg>"""

ARROW = (f'<svg viewBox="0 0 56 12" class="dash" aria-hidden="true"><line x1="2" y1="6" x2="40" y2="6" stroke="{K}" '
         f'stroke-width="2" stroke-dasharray="5 5"/><path d="M38 1 L52 6 L38 11 Z" fill="{K}"/></svg>')

STEPS = [
    (SPROUT, "", "The farm", "Grows the food. Pays nothing upfront."),
    (BOX, "us", "Us", "One order, one invoice, one cold delivery, and a QR code on every box."),
    (STALL, "", "Grocer or restaurant", "Orders from many farms in one place."),
    (PLATE, "", "Your plate", "Scan the box. Know the farm, the farmer and the day it was picked."),
]


def farm_to_plate_html() -> str:
    parts = []
    for i, (icon, cls, title, body) in enumerate(STEPS):
        arrow = f'<div class="gap-arrow">{ARROW}</div>' if i < len(STEPS) - 1 else ""
        parts.append(f'<div class="f2p-step"><div class="tile {cls}">{icon}</div><h3>{title}</h3><p>{body}</p>{arrow}</div>')
    return f'<div class="f2p">{"".join(parts)}</div>'
