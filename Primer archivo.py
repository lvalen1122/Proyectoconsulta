
import requests
from bs4 import BeautifulSoup


def buscar_pubmed(medicamento, max_resultados=10):
    """Busca artículos en PubMed relacionados con un medicamento y devuelve títulos y enlaces."""

    # Construir la URL de búsqueda en PubMed
    base_url = "https://pubmed.ncbi.nlm.nih.gov/"
    search_url = f"{base_url}?term={medicamento.replace(' ', '+')}"

    # Hacer la solicitud a PubMed
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.ge

    if response.status_code != 200:
        print("Error al acceder a PubMed")
        return []

        # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar los artículos en la página de búsqueda
    articles = soup.find_all("article", class_="full-docsum"),
    resultados = []

    for article in articles[:max_resultados]:
        try:
            titulo = article.find("a", class_="docsum-title").get_text(strip=True)
            enlace = base_url + article.find("a", class_="docsum-title")["href"]
            resultados.append((titulo, enlace))
        except AttributeError:
            continue  # Saltar artículos sin título

    return resultados


# Ejemplo de búsqueda para "metformin"
medicamento = "metformin"
articulos = buscar_pubmed(medicamento, max_resultados=5)

# Imprimir resultados
for i, (titulo, enlace) in enumerate(articulos, 1):
    print(f"{i}. {titulo}\n   {enlace}\n")


