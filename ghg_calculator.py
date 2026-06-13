import pandas as pd

# Emission factors (tonnes CO2 per unit)
emission_factors = {
    "Power":     {"Scope1": 0.82, "Scope2": 0.45},
    "Transport": {"Scope1": 2.10, "Scope2": 0.30},
    "Industry":  {"Scope1": 1.50, "Scope2": 0.60},
    "Buildings": {"Scope1": 0.45, "Scope2": 0.80}
}

print("=" * 50)
print("  GHG EMISSIONS CALCULATOR — INDIA")
print("=" * 50)

# Get user input
print("\nAvailable Sectors: Power, Transport, Industry, Buildings")
sector = input("Enter sector: ").strip().title()

if sector not in emission_factors:
    print("Invalid sector!")
else:
    units = float(input(f"Enter activity units for {sector}: "))
    
    # Calculate emissions
    scope1 = units * emission_factors[sector]["Scope1"]
    scope2 = units * emission_factors[sector]["Scope2"]
    total  = scope1 + scope2
    
    print("\n" + "=" * 50)
    print(f"  EMISSIONS REPORT — {sector.upper()}")
    print("=" * 50)
    print(f"  Scope 1 Emissions: {scope1:.2f} tonnes CO2")
    print(f"  Scope 2 Emissions: {scope2:.2f} tonnes CO2")
    print(f"  Total Emissions:   {total:.2f} tonnes CO2")
    
    # Save to Excel
    df = pd.DataFrame({
        "Sector": [sector],
        "Activity Units": [units],
        "Scope 1 (tCO2)": [scope1],
        "Scope 2 (tCO2)": [scope2],
        "Total (tCO2)": [total]
    })
    df.to_excel("ghg_results.xlsx", index=False)
    print(f"\n  Results saved to ghg_results.xlsx!")
    print("=" * 50)