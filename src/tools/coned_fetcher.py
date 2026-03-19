import requests
import pandas as pd

BASE_URL = "https://services.arcgis.com/ciPnsNFi1JLWVjva/arcgis/rest/services/CECONY_Network_Storage_Prod/FeatureServer/0/query"

def fetch_bronx_networks(min_capacity_mw=1.0):
    """Fetch Bronx network zones with available battery storage capacity."""
    
    params = {
        "where": f"GEOGRAPHIC LIKE '%Bronx%' AND PeakN_0_or_PeakN_1 > {min_capacity_mw}",
        "outFields": "GEOGRAPHIC,NetworkName,NetworkCode,PeakN_0_or_PeakN_1,Notes",
        "f": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    features = data.get("features", [])
    records = [f["attributes"] for f in features]
    df = pd.DataFrame(records)
    df = df.rename(columns={"PeakN_0_or_PeakN_1": "Capacity_MW"})
    df = df.sort_values("Capacity_MW", ascending=False)
    
    return df

if __name__ == "__main__":
    df = fetch_bronx_networks(min_capacity_mw=1.0)
    
    # Summarize by network name
    summary = df.groupby("NetworkName")["Capacity_MW"].agg(
        Count="count",
        Total_MW="sum",
        Max_MW="max",
        Avg_MW="mean"
    ).round(2).sort_values("Total_MW", ascending=False)
    
    print("\n=== Bronx Network Summary (>1MW zones) ===\n")
    print(summary.to_string())