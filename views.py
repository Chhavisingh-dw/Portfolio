
from django.shortcuts import render

emission_factors = {
    "Power":     {"Scope1": 0.82, "Scope2": 0.45},
    "Transport": {"Scope1": 2.10, "Scope2": 0.30},
    "Industry":  {"Scope1": 1.50, "Scope2": 0.60},
    "Buildings": {"Scope1": 0.45, "Scope2": 0.80}
}

def calculator(request):
    result = None
    if request.method == "POST":
        sector = request.POST.get("sector")
        units = float(request.POST.get("units"))
        scope1 = units * emission_factors[sector]["Scope1"]
        scope2 = units * emission_factors[sector]["Scope2"]
        total = scope1 + scope2
        result = {
            "sector": sector,
            "units": units,
            "scope1": round(scope1, 2),
            "scope2": round(scope2, 2),
            "total": round(total, 2)
        }
    return render(request, "calculator.html", {"result": result})
# Create your views here.
