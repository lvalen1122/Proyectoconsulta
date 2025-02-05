import requests
import pandas as pd


def fetch_clinical_trials(query="GLP-1", max_results=100):
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "query.term": query,
        "pageSize": max_results,
        "format": "json"
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        print("Response text:", response.text)
        return []

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: No se pudo decodificar la respuesta JSON. Respuesta recibida:")
        print(response.text)
        return []

    trials = data.get("studies", [])
    return trials


def process_trials(trials):
    records = []
    for trial in trials:
        records.append({
            "NCTId": trial.get("nctId", None),
            "Title": trial.get("title", None),
            "Condition": ", ".join(trial.get("conditions", [])),
            "Intervention": ", ".join(trial.get("interventions", [])),
            "Primary Outcome": ", ".join(trial.get("primaryOutcomeMeasures", [])),
            "Status": trial.get("overallStatus", None),
            "Type": trial.get("studyType", None),
            "Phase": trial.get("phase", None),
            "Start Date": trial.get("startDate", None),
            "Completion Date": trial.get("completionDate", None),
            "Location": ", ".join(trial.get("locations", [])),
        })
    return pd.DataFrame(records)


def main():
    query = "GLP-1"
    trials = fetch_clinical_trials(query)

    if not trials:
        print("No se encontraron ensayos clínicos para la consulta.")
        return

    df = process_trials(trials)
    df.to_csv("clinical_trials_glp1.csv", index=False)
    print("Datos guardados en clinical_trials_glp1.csv")


if __name__ == "__main__":
    main()
