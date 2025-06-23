import os
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import DCTERMS, PROV, XSD, RDF, RDFS

# Definizione dei namespace
DCATAPIT = Namespace("http://dati.gov.it/onto/dcatapit/")
DCAT = Namespace("https://www.w3.org/ns/dcat#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
DVD = Namespace("https://github.com/DeVoteD-Research/DeVoteD")
CC = Namespace("http://creativecommons.org/ns#")

# Creazione del grafo
g = Graph()
catalog_g = Graph()
g.bind("dcat3", DCAT)
g.bind("dct", DCTERMS)
g.bind("prov", PROV)
g.bind("adms", ADMS)
g.bind("xsd", XSD)
g.bind("dcatapit", DCATAPIT)
g.bind("dvd", DVD)
g.bind("cc", CC)

catalog_g.bind("dcat3", DCAT)
catalog_g.bind("dct", DCTERMS)
catalog_g.bind("adms", ADMS)
catalog_g.bind("xsd", XSD)
catalog_g.bind("dcatapit", DCATAPIT)
catalog_g.bind("cc", CC)

# Lista dei dataset
datasets = [
    {
        "id": "V-Dem_Core",
        "title": "Country-Year: V-Dem Core",
        "distribution": "STATA, CSV, R, SPSS",
        "description": "The five high-level V-Dem democracy indices, 92 sub-indices, and the 167 indicators constituting them.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2014",
        "modified": "2025",
        "license": "n/a",
        "language": "English",
        "keywords": "democracy, indeces, indicators, politics",
        "version": "15",
        "publisher": "http://viaf.org/viaf/140125343",
        "spatial coverage": "global",
        "temporal coverage": "1900-2024"

    },
    {
        "id": "IDEA_Voter_Turnout",
        "title": "IDEA Voter Turnout Database",
        "distribution": "XLS, API",
        "description": "The most comprehensive global collection of voter turnout statistics from presidential and parliamentary elections since 1945.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "n/a",
        "modified": "n/a",
        "license": "n/a",
        "language": "English",
        "keywords": "democracy, vote, turnout, politics, election",
        "version": "n/a",
        "publisher": "http://viaf.org/viaf/129505852",
        "spatial coverage": "global",
        "temporal coverage": "1945-2024"

    },
    {
        "id": "Party_Facts",
        "title": "Party Facts - Version 2023",
        "distribution": "CSV, TAB",
        "description": "Party Facts links datasets on political parties.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2019",
        "modified": "2023",
        "license": "https://creativecommons.org/licenses/by/1.0/",
        "language": "English",
        "keywords": "democracy, parties, social sciences, politics",
        "version": "1.1",
        "publisher": "http://viaf.org/viaf/261806653",
        "spatial coverage": "global",
        "temporal coverage": "1945-2024"
    },
    {
        "id": "DeVoteD",
        "title": "DeVoteD",
        "distribution": "",
        "description": "",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2025",
        "modified": "2025",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "language": "English",
        "keywords": "democracy, party, vote, turnout, politics, indeces, ",
        "version": "1.0",
        "publisher": "n/a",
        "spatial coverage": "global",
        "temporal coverage": "1945-2024"

    },
]

# Creazione dei dataset
for dataset in datasets: 
    dataset_uri = DVD[dataset["id"]]
    catalog_g.add((URIRef("https://github.com/DeVoteD-Research/DeVoteD/tree/main/data"),
                   DCAT.dataset, Literal(dataset["id"])))
    g.add((dataset_uri, DCAT.title, Literal(dataset["title"], lang="en")))
    g.add((dataset_uri, RDF.type, DCAT.Dataset))
    g.add((dataset_uri, RDF.type, PROV.Entity))
    g.add((dataset_uri, DCTERMS.description, Literal(dataset["description"], lang="en")))
    g.add((dataset_uri, DCAT.theme, URIRef(dataset["theme"])))
    g.add((dataset_uri, DCAT.releaseDate, Literal(dataset["issued"], datatype=XSD.year)))
    g.add((dataset_uri, DCAT.releaseDate, Literal(dataset["modified"], datatype=XSD.year)))
    g.add((dataset_uri, DCAT.license, URIRef(dataset["license"])))
    for el in dataset["distribution"].split(", "):
        g.add((dataset_uri, DCAT.distribution, Literal(el)))
    g.add((dataset_uri, DCAT.language,  Literal("en", datatype=XSD.language)))

    if isinstance(dataset["publisher"], list):
        for publisher in dataset["publisher"]:
            g.add((dataset_uri, PROV.wasAttributedTo, URIRef(publisher)))
    else:
        # For a single publisher
        g.add((dataset_uri, PROV.wasAttributedTo, URIRef(dataset["publisher"])))


# Aggiungi informazioni al catalogo
catalog_uri = URIRef("https://github.com/Asemica-me/OADE_OpenVoices/tree/main/data")
catalog_g.add((catalog_uri, RDF.type, DCAT.Catalog))
catalog_g.add((catalog_uri, DCTERMS.title, Literal("Open Voices OADE Project - Datasets Catalog", lang="en")))
catalog_g.add((catalog_uri, DCTERMS.description,
               Literal("Catalog containing the datasets for the Open Voices project", lang="en")))
catalog_g.add((catalog_uri, PROV.wasAttributedTo, URIRef("https://github.com/Asemica-me/OADE_OpenVoices")))
catalog_g.add((catalog_uri, DCTERMS.issued, Literal("2025-01-01", datatype=XSD.date)))
catalog_g.add((catalog_uri, DCTERMS.modified, Literal("2025-01-01", datatype=XSD.date)))
catalog_g.add((catalog_uri, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
catalog_g.add((catalog_uri, DCAT.language,  Literal("en", datatype=XSD.language)))
catalog_g.add((catalog_uri, ADMS.identifier,  Literal("OV-Catalog", datatype=XSD.string)))

# License
license_uri = URIRef("https://creativecommons.org/licenses/by/4.0/")
catalog_g.add((catalog_uri, DCTERMS.license, license_uri))

catalog_g.add((license_uri, RDF.type, CC.License))
catalog_g.add((license_uri, CC.legalcode, URIRef("http://creativecommons.org/licenses/by/4.0/")))
catalog_g.add((license_uri, CC.permits, CC.Reproduction))
catalog_g.add((license_uri, CC.permits, CC.Distribution))
catalog_g.add((license_uri, CC.permits, CC.DerivativeWorks))
catalog_g.add((license_uri, CC.requires, CC.Notice))
catalog_g.add((license_uri, CC.requires, CC.Attribution))
catalog_g.add((license_uri, RDFS.label, Literal("Creative Commons CC-BY 4.0", lang="en")))



# Creazione della directory serialisations se non esiste
output_dir = "serialization"

# Salvataggio del file nella directory
datasets_file = os.path.join(output_dir, "serial_datasets.ttl")
catalog_file = os.path.join(output_dir, "serial_catalog.ttl")

with open(datasets_file, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

with open(catalog_file, "w", encoding="utf-8") as f:
    f.write(catalog_g.serialize(format="turtle"))

print(f"Serializzazione completata! File salvati come {datasets_file} e {catalog_file}.")