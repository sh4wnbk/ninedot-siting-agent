# NineDot Siting Agent

An agentic GIS tool that autonomously analyzes urban grid data to identify optimal battery energy storage (BESS) installation sites in NYC.

Built as part of a summer internship application to NineDot Energy, a Brooklyn-based clean energy company focused on urban battery storage.

## The Three Pillars

- Pillar 1 - Grid Reliability: ConEd hosting capacity by network zone (Live)
- Pillar 2 - Environmental Justice: DAC maps and peaker plant proximity (Coming)
- Pillar 3 - Physical Safety: FEMA flood zone filtering (Coming)

A Master Orchestrator will combine all three agents into a unified siting recommendation engine.

## Data Sources

- ConEd Hosting Capacity Tool: Network-level BESS hosting capacity via ArcGIS REST API
- NY DEC Disadvantaged Communities: Environmental justice layer for Pillar 2
- NYC Flood Zones: FEMA 100/500-year floodplains for Pillar 3

## Setup

1. Clone the repo
2. Create and activate a virtual environment named ndot-env
3. Install dependencies: requests, pandas, anthropic, python-dotenv
4. Add your ANTHROPIC_API_KEY to a .env file in the project root

## Usage

Run the Grid Expert Agent from the project root: python src/agents/grid_agent.py

## Tech Stack

- Python 3.11
- Anthropic Claude API for agent reasoning
- ConEd ArcGIS REST API for live grid data
- Pandas for data processing
- GeoPandas for GIS layer (coming)

## Author

Shawn - Environmental Science background, IBM AI Engineering coursework, building at the intersection of clean energy and agentic AI.
