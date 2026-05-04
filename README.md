# drone-solar-analytics

Automated extraction of engineering statistics (slope and aspect) from UAV-derived Digital Surface Models (DSM) for solar energy assessment.

> **Portfolio project** demonstrating a full end-to-end geospatial pipeline — from drone flight to technical report — relevant to photovoltaic (PV) installation planning.

---

## Project Overview

This project analyses a rooftop surface to determine its suitability for a solar panel installation. The workflow covers UAV data acquisition, photogrammetric processing, spatial analysis in GIS, and automated statistics extraction via Python.

**Key results for the analysed roof section:**

| Parameter | Value |
|---|---|
| Mean slope | 29.23° |
| Aspect (azimuth) | 183.03° (South) |
| Roof area | 117.543 m² |
| GSD (resolution) | 1.61 cm/px |

A southern aspect combined with a ~29° slope places this surface close to the optimal tilt angle for PV panels in Poland (typically 30–35°), making it well-suited for photovoltaic installation.

---

## Pipeline

```
UAV Flight  →  WebODM Light  →  QGIS  →  Python (Rasterio / NumPy)  →  PDF Report
```

### 1. UAV Data Acquisition
- Conducted a drone survey of the target building
- Captured overlapping nadir imagery for photogrammetric reconstruction

### 2. Photogrammetric Processing — WebODM Light
- Processed raw imagery into a georeferenced orthophoto and Digital Surface Model (DSM)
- Output: GeoTIFF DSM at 1.61 cm/px GSD

### 3. Spatial Analysis — QGIS
- Derived slope and aspect rasters from the DSM
- Clipped analysis to the roof polygon
- Generated a colour-classified slope map for the technical report

### 4. Automated Statistics — Python
- Extracted zonal statistics (mean slope, dominant aspect) using Rasterio and NumPy
- Script: [`roof_analysis_stats.py`](./roof_analysis_stats.py)

### 5. Report Generation
- Produced a georeferenced technical map with construction parameters
- Output: [`Raport_Techniczny_PV_Igor_Hajducki.pdf`](./Raport_Techniczny_PV_Igor_Hajducki.pdf)

---

## Repository Structure

```
drone-solar-analytics/
├── roof_analysis_stats.py              # Python script — slope & aspect extraction
├── Raport_Techniczny_PV_Igor_Hajducki.pdf  # Technical report (map + parameters)
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| **UAV / Drone** | Data acquisition |
| **WebODM Light** | Photogrammetric processing (DSM, orthophoto) |
| **QGIS** | Slope/aspect analysis, map cartography |
| **Python** | Automated statistics extraction |
| **Rasterio** | GeoTIFF reading and raster operations |
| **NumPy** | Array-based zonal statistics |

---

## Skills Demonstrated

- UAV mission planning and data collection
- Photogrammetric processing (Structure from Motion)
- DSM-based terrain analysis (slope, aspect)
- Geospatial Python scripting (Rasterio, NumPy)
- Technical report generation in QGIS
- End-to-end project delivery: from raw imagery to client-ready output

---

## Author

**Igor Hajducki**  
GIS Analyst  
[GitHub: IgorH-GIS](https://github.com/IgorH-GIS)
