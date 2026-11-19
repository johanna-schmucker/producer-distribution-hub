"""Maps. Coordinates are approximate and the Montréal areas are examples, not confirmed delivery zones."""
from __future__ import annotations

import pandas as pd
import pydeck as pdk
import streamlit as st

MONTEREGIE_TOWNS = {
    "Saint-Hyacinthe": (45.630, -72.957), "Granby": (45.400, -72.733),
    "Saint-Jean-sur-Richelieu": (45.307, -73.262), "Salaberry-de-Valleyfield": (45.256, -74.131),
    "Longueuil": (45.531, -73.518), "Châteauguay": (45.380, -73.750), "Vaudreuil-Dorion": (45.400, -74.033),
    "Sorel-Tracy": (46.040, -73.113), "Cowansville": (45.201, -72.746), "Chambly": (45.450, -73.287),
    "Beloeil": (45.567, -73.200), "Saint-Rémi": (45.267, -73.617), "Farnham": (45.284, -72.985),
}
MONTREAL_AREAS = {
    "Plateau-Mont-Royal": (45.523, -73.582), "Rosemont": (45.547, -73.573), "Villeray": (45.545, -73.620),
    "Verdun": (45.459, -73.571), "Notre-Dame-de-Grâce": (45.470, -73.620),
    "Sud-Ouest": (45.483, -73.565), "Hochelaga": (45.545, -73.545), "Westmount": (45.487, -73.600),
    "Ahuntsic": (45.560, -73.650),
}


# Chemin de la Côte-Sainte-Catherine: 5.5 km, main street of the former village of Outremont.
# Coordinates (45.5022, -73.6242) from Wikipedia. Not claimed to be a grocery street.
MAIN_STREET = {"Côte-Sainte-Catherine": (45.5022, -73.6242)}


def area_map(points: dict, center: tuple, zoom: float, region_radius: int = 0, selected: str | None = None,
             highlight: tuple = ()) -> None:
    marked = {selected, *highlight}
    df = pd.DataFrame([{"name": n, "lat": lat, "lon": lon} for n, (lat, lon) in points.items()])
    df["color"] = [[46, 125, 50, 255] if n in marked else [17, 17, 17, 200] for n in df["name"]]
    base = max(region_radius // 14, 400)
    df["size"] = [int(base * 1.6) if n in marked else base for n in df["name"]]
    layers = []
    if region_radius:
        region = pd.DataFrame([{"lat": center[0], "lon": center[1]}])
        layers.append(pdk.Layer("ScatterplotLayer", region, get_position="[lon, lat]", get_radius=region_radius,
                                get_fill_color=[46, 125, 50, 25], get_line_color=[46, 125, 50, 180], stroked=True,
                                line_width_min_pixels=2))
    layers += [
        pdk.Layer("ScatterplotLayer", df, get_position="[lon, lat]", get_radius="size", get_fill_color="color",
                  radius_min_pixels=5, pickable=True),
        pdk.Layer("TextLayer", df, get_position="[lon, lat]", get_text="name", get_size=13, get_color=[17, 17, 17, 255],
                  get_pixel_offset=[0, -16], get_alignment_baseline="'bottom'", font_weight=600, outline_width=3,
                  outline_color=[255, 255, 255, 255], font_settings={"sdf": True}),
    ]
    deck = pdk.Deck(map_style="light", layers=layers, tooltip={"text": "{name}"},
                    initial_view_state=pdk.ViewState(latitude=center[0], longitude=center[1], zoom=zoom))
    st.pydeck_chart(deck, height=460)


def circle_map(center: tuple, zoom: float, radius: int) -> None:
    """Just the launch area as a shaded circle: no towns, no labels."""
    region = pd.DataFrame([{"lat": center[0], "lon": center[1]}])
    layer = pdk.Layer("ScatterplotLayer", region, get_position="[lon, lat]", get_radius=radius,
                      get_fill_color=[46, 125, 50, 40], get_line_color=[46, 125, 50, 220], stroked=True,
                      line_width_min_pixels=2)
    deck = pdk.Deck(map_style="light", layers=[layer],
                    initial_view_state=pdk.ViewState(latitude=center[0], longitude=center[1], zoom=zoom))
    st.pydeck_chart(deck, height=460)
