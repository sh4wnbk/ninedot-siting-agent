import anthropic
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.coned_fetcher import fetch_bronx_networks

client = anthropic.Anthropic()

def run_grid_agent(borough="Bronx", min_capacity_mw=1.0):
    """Grid Expert Agent - analyzes ConEd hosting capacity and returns a recommendation."""
    
    # Step 1: Fetch the data
    print(f"Fetching ConEd grid data for {borough}...")
    df = fetch_bronx_networks(min_capacity_mw=min_capacity_mw)
    
    summary = df.groupby("NetworkName")["Capacity_MW"].agg(
        Zone_Count="count",
        Total_MW="sum",
        Max_MW="max",
        Avg_MW="mean"
    ).round(2).sort_values("Total_MW", ascending=False)
    
    data_str = summary.to_string()
    
    # Step 2: Send to Claude for reasoning
    print("Agent is reasoning about the data...\n")
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""You are the NineDot Grid Analyst. Your job is to identify 
the best locations in the {borough} for urban battery energy storage (BESS) installations.

Here is the current ConEd hosting capacity data for {borough} networks 
(zones with >{min_capacity_mw}MW available capacity):

{data_str}

Based on this data, answer one specific question:

Which single zone in the Bronx represents the best first installation 
for NineDot? Consider: highest capacity, network reliability, and 
strategic value as a flagship project.

Give a specific recommendation with your reasoning. Use the numbers."""
            }
        ]
    )
    
    return message.content[0].text

if __name__ == "__main__":
    report = run_grid_agent()
    print("=== GRID EXPERT AGENT REPORT ===\n")
    print(report)