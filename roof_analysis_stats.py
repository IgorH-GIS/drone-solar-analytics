import rasterio
import numpy as np

def get_roof_statistics(tif_path):
    """
    Extracts analytics from Slope or Aspect GeoTIFFs.
    
    """
    with rasterio.open(tif_path) as src:
        data = src.read(1)
        # Filter NoData and ground (0-5 degrees/degrees)
        roof_data = data[data > 5]
        
        if roof_data.size == 0:
            print(f"No significant data found in {tif_path}")
            return

        stats = {
            "Mean": np.mean(roof_data),
            "Max": np.max(roof_data),
            "Std Dev": np.std(roof_data)
        }
        
        print(f"\n--- Analysis for: {tif_path} ---")
        for key, val in stats.items():
            print(f"{key}: {val:.2f}")

# RUN ANALYTICS (Update paths if needed)
# RUN ANALYTICS
get_roof_statistics('Fairleigh-Road-1052026-slope.tif')
get_roof_statistics('Fairleigh-Road-1052026-aspect.tif')