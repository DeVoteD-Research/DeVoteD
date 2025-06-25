import os
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import DCTERMS, PROV, XSD, RDF, RDFS, FOAF, SKOS, ORG

# Definizione dei namespace
DCATAPIT = Namespace("http://dati.gov.it/onto/dcatapit/")
DCAT = Namespace("https://www.w3.org/ns/dcat#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
DVD = Namespace("https://github.com/DeVoteD-Research/DeVoteD/")
CC = Namespace("http://creativecommons.org/ns#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")


# Creazione del grafo per il catalogo
metadata_g = Graph()

metadata_g.bind("dcat3", DCAT)
metadata_g.bind("dct", DCTERMS)
metadata_g.bind("adms", ADMS)
metadata_g.bind("xsd", XSD)
metadata_g.bind("dcatapit", DCATAPIT)
metadata_g.bind("cc", CC)
metadata_g.bind("vcard", VCARD)
metadata_g.bind("foaf", FOAF)
metadata_g.bind("org", ORG)
metadata_g.bind("skos", SKOS)

# Lista dei dataset
datasets = [
    {
        "catalog": {
            "url": "https://v-dem.net/about/v-dem-project/",
            "description": "Varieties of Democracy (V-Dem) is a unique approach to conceptualizing and measuring democracy. We provide a multidimensional and disaggregated dataset that reflects the complexity of the concept of democracy as a system of rule that goes beyond the simple presence of elections. The V-Dem project distinguishes between five high-level principles of democracy: electoral, liberal, participatory, deliberative, and egalitarian, and collects data to measure these principles."
        },
        "id": "https://v-dem.net/data/the-v-dem-dataset/country-year-v-dem-core-v15/",
        "title": "Country-Year: V-Dem Core",
        "distribution": "https://v-dem.net/data/the-v-dem-dataset/country-year-v-dem-core-v15/",
        "description": "The five high-level V-Dem democracy indices, 92 sub-indices, and the 167 indicators constituting them.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2014",
        "modified": "2025",
        "license": "",
        "language": "http://lexvo.org/id/iso639-1/en",
        "keywords": "democracy, indeces, indicators, politics, global, international",
        "version": "15",
        "publisher": {"url": "http://viaf.org/viaf/140125343", "label": "Göteborgs Universitet"},
        "temporal coverage": {"label": "19002024", "start": "1900", "end": "2024"},
        "contact": "mailto:contact@v-dem.net"
    },
    {
        "catalog": {
            "url": "https://www.idea.int/data-tools",
            "description": "The International Institute for Democracy and Electoral Assistance (International IDEA) is an intergovernmental organization that supports democracy worldwide."
        },
        "id": "https://www.idea.int/data-tools/data/voter-turnout-database",
        "title": "IDEA Voter Turnout Database",
        "distribution": "https://www.idea.int/data-tools/data/voter-turnout-database",
        "description": "The most comprehensive global collection of voter turnout statistics from presidential and parliamentary elections since 1945.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "1999",
        "modified": "",
        "license": "",
        "language": "http://lexvo.org/id/iso639-1/en",
        "keywords": "democracy, vote, turnout, politics, election, global, international",
        "version": "",
        "publisher": {"url": "http://viaf.org/viaf/129505852", "label": "International Institute for Democracy and Electoral Assistance"},
        "temporal coverage": {"label": "19452024", "start": "1945", "end": "2024"},
        "contact": "tel:+4686983700"
    },
    {
        "catalog": {
            "url": "https://partyfacts.herokuapp.com/documentation/", 
            "description": "Party Facts links datasets on political parties and provides an online platform about parties and their history as recorded in social science datasets."
        },
        "id": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TJINLQ",
        "title": "Party Facts - Version 2023",
        "distribution": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TJINLQ",
        "description": "Party Facts links datasets on political parties.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2019",
        "modified": "2025",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "language": "http://lexvo.org/id/iso639-1/en",
        "keywords": "democracy, parties, social sciences, politics, global, international",
        "version": "1.1",
        "publisher": {"url": "http://viaf.org/viaf/261806653", "label": "Sage Publicatins, Inc."},
        "temporal coverage": {"label": "19452024", "start": "1945", "end": "2024"},
        "contact": "mailto:paul.bederke@uni-konstanz.de"
    },
    {
        "catalog": {
            "url": "https://manifesto-project.wzb.eu/information/documents/information",
            "description": "The Manifesto Corpus is a free, digital, multilingual, and annotated collection of electoral programmes. It is based on the collection of the Manifesto Project, comprising the currently largest collection of annotated electoral programmes."
        },
        "id": "https://manifesto-project.wzb.eu/datasets/MPDS2024a",
        "title": "Manifesto Project Corpus",
        "distribution": "https://manifesto-project.wzb.eu/datasets/MPDS2024a",
        "description": "The Manifesto Corpus is a free, digital, multilingual, and annotated collection of electoral programmes. It is based on the collection of the Manifesto Project, comprising the currently largest collection of annotated electoral programmes.",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "issued": "2015",
        "modified": "2024",
        "license": "",
        "language": "http://lexvo.org/id/iso639-1/en",
        "keywords": "democracy, party, manifesto, politics, global, international",
        "version": "",
        "publisher": {"url": "http://viaf.org/viaf/146283948", "label": "Wissenschaftszentrum Berlin für Sozialforschung"},
        "temporal coverage": {"label": "19452024", "start": "1945", "end": "2024"},
        "contact": "mailto:manifesto-communication@wzb.eu"
    }
]

# Informazioni del catalogo secondo DCAT-3
names = ["Valentino_Castagna", "Romolo_David_d&#39;Alessandro"]
for name in names:
    agent = DVD[name]
    metadata_g.add((agent, RDF.type, FOAF.Agent))
    # Mandatory
    metadata_g.add((agent, FOAF.name, Literal(name.replace("_", " ").replace("&#39;", "'"))))
    # Recommended
    metadata_g.add((agent, RDF.type, FOAF.Person))

catalogs_list = []
for dataset in datasets:
    # Definizione URI
    catalog_uri = URIRef(dataset["catalog"]["url"])
    catalogs_list.append(catalog_uri)
    dataset_uri = URIRef(dataset["id"])
    publisher_uri = URIRef(dataset["publisher"]["url"]) # Il publisher viene usato anche come riferimento per i contatti
    contact_uri = URIRef(dataset["contact"]) if dataset["contact"] else False
    distribution_uri = URIRef(dataset["distribution"])
    period_uri = DVD[dataset["temporal coverage"]["label"]]
    theme_uri = URIRef(dataset["theme"])
    language_uri = URIRef(dataset["language"])
    license_uri = URIRef(dataset["license"]) if dataset["license"] else False

    # Proprietà per theme_uri
    metadata_g.add((theme_uri, RDF.type, SKOS.Concept))
    metadata_g.add((theme_uri, SKOS.prefLabel, Literal(dataset["theme"])))

    # Proprietà per period_uri
    metadata_g.add((period_uri, RDF.type, DCTERMS.PeriodOfTime))
    metadata_g.add((period_uri, DCAT.startDate, Literal(dataset["temporal coverage"]["start"], datatype=XSD.gYear)))
    metadata_g.add((period_uri, DCAT.endDate, Literal(dataset["temporal coverage"]["end"], datatype=XSD.gYear)))

    # Proprietà per resource_uri
    metadata_g.add((distribution_uri, RDF.type, DCAT.Distribution))
    metadata_g.add((distribution_uri, DCAT.accessURL, Literal(dataset["distribution"])))  

    # Proprietà per publisher_uri
    metadata_g.add((publisher_uri, RDF.type, VCARD.Group))
    metadata_g.add((publisher_uri, RDF.type, FOAF.Organization))
    metadata_g.add((publisher_uri, SKOS.prefLabel, Literal(dataset["publisher"]["label"])))
    if contact_uri:
        if dataset["contact"].startswith("tel"):
            metadata_g.add((publisher_uri, VCARD.hasTelephone, contact_uri))
        else:
            metadata_g.add((publisher_uri, VCARD.hasEmail, contact_uri))
        metadata_g.add((dataset_uri, DCAT.contactPoint, publisher_uri))
    
    # Proprietà per dataset_uri
    metadata_g.add((dataset_uri, RDF.type, DCAT.Dataset))
    ## Mandatory properties
    metadata_g.add((dataset_uri, DCTERMS.description, Literal(dataset["description"])))
    metadata_g.add((dataset_uri, DCTERMS.title, Literal(dataset["title"])))    
    ## Recommended properties
    metadata_g.add((dataset_uri, DCAT.distribution, distribution_uri))
    for keyword in dataset["keywords"].split(', '):
        metadata_g.add((dataset_uri, DCAT.keyword, Literal(keyword)))
    metadata_g.add((dataset_uri, DCTERMS.temporal, period_uri))
    metadata_g.add((dataset_uri, DCAT.theme, theme_uri))
    # Optional properties
    if dataset["version"]:
        metadata_g.add((dataset_uri, DCAT.version, Literal(dataset["version"])))


    # Proprietà per catalog_uri
    metadata_g.add((catalog_uri, RDF.type, DCAT.Catalog))
    ## Mandatory properties
    metadata_g.add((catalog_uri, DCTERMS.description, Literal(dataset["catalog"]["description"])))
    metadata_g.add((catalog_uri, DCTERMS.publisher, publisher_uri))
    metadata_g.add((catalog_uri, DCTERMS.title, Literal(dataset["publisher"]["label"])))
    ## Recommended properties
    metadata_g.add((catalog_uri, DCAT.dataset, dataset_uri))
    metadata_g.add((catalog_uri, DCTERMS.language, language_uri))
    if license_uri:
        metadata_g.add((catalog_uri, DCTERMS.license, license_uri))
    if dataset["modified"]:
        metadata_g.add((catalog_uri, DCTERMS.modified, Literal(dataset["modified"], datatype=XSD.gYear)))
    if dataset["issued"]:
        metadata_g.add((catalog_uri, DCTERMS.issued, Literal(dataset["issued"], datatype=XSD.gYear)))

# Metadati relativi al catalogo del progetto DeVoteD
temporal_coverage = {"label": "19452019", "start": "1945", "end": "2019"}
# Definizione URI
devoted_uri = URIRef("https://github.com/DeVoteD-Research/DeVoteD")
devoted_catalog_uri = URIRef("https://github.com/DeVoteD-Research/DeVoteD/tree/main/data")
language_uri = URIRef("http://lexvo.org/id/iso639-1/en")
license_uri = URIRef("https://creativecommons.org/licenses/by/4.0/")
legalcode_uri = URIRef("https://creativecommons.org/licenses/by/4.0/legalcode")
theme_uri = URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")
period_uri = URIRef(temporal_coverage["label"])

# Proprietà per period_uri
metadata_g.add((period_uri, RDF.type, DCTERMS.PeriodOfTime))
metadata_g.add((period_uri, DCAT.startDate, Literal(temporal_coverage["start"], datatype=XSD.gYear)))
metadata_g.add((period_uri, DCAT.endDate, Literal(temporal_coverage["end"], datatype=XSD.gYear)))

metadata_g.add((devoted_catalog_uri, RDF.type, DCAT.Catalog))
# Mandatory
metadata_g.add((devoted_catalog_uri, DCTERMS.title, Literal("DeVoteD - Datasets Catalog", lang="en")))
metadata_g.add((devoted_catalog_uri, DCTERMS.description,
               Literal("Catalog containing the datasets for the DeVoteD project", lang="en")))
metadata_g.add((devoted_catalog_uri, DCTERMS.publisher, devoted_uri))
# Recommended
metadata_g.add((devoted_catalog_uri, DCTERMS.issued, Literal("2025", datatype=XSD.date)))
metadata_g.add((devoted_catalog_uri, DCTERMS.modified, Literal("2025", datatype=XSD.date)))
metadata_g.add((devoted_catalog_uri, DCTERMS.license, license_uri))
metadata_g.add((devoted_catalog_uri, DCTERMS.language,  language_uri))
metadata_g.add((devoted_catalog_uri, DCTERMS.modified, Literal("2025", datatype=XSD.gYear)))
metadata_g.add((devoted_catalog_uri, DCTERMS.issued, Literal("2025", datatype=XSD.gYear)))
metadata_g.add((devoted_catalog_uri, DCAT.theme, theme_uri))
for keyword in ["democracy", "party", "vote", "turnout", "politics", "indeces", "global"]:
    metadata_g.add((devoted_catalog_uri, DCAT.keyword, Literal(keyword)))
metadata_g.add((devoted_catalog_uri, DCTERMS.temporal, period_uri))
metadata_g.add((devoted_catalog_uri, DCAT.distribution, devoted_catalog_uri))
# Optional
metadata_g.add((devoted_catalog_uri, PROV.wasAttributedTo, devoted_uri))
metadata_g.add((devoted_catalog_uri, ADMS.identifier,  Literal("DeVoteD-Catalog", datatype=XSD.string)))
for catalog in catalogs_list:
    metadata_g.add((devoted_catalog_uri, DCAT.catalog, catalog))
metadata_g.add((dataset_uri, DCAT.version, Literal("1.0")))

# Creazione grafo per la licenza del progetto
license_g = Graph()
license_g.bind("cc", CC)

license_g.add((license_uri, RDF.type, CC.License))
license_g.add((license_uri, CC.legalcode, legalcode_uri))
license_g.add((license_uri, CC.permits, CC.Reproduction))
license_g.add((license_uri, CC.permits, CC.Distribution))
license_g.add((license_uri, CC.permits, CC.DerivativeWorks))
license_g.add((license_uri, CC.requires, CC.Notice))
license_g.add((license_uri, CC.requires, CC.Attribution))
license_g.add((license_uri, RDFS.label, Literal("Creative Commons CC-BY 4.0", lang="en")))


# Creazione della directory serialisations se non esiste
output_dir = "serialization/"

# Salvataggio del file nella directory
metadata_file = os.path.join(output_dir, "metadata.ttl")
license_file = os.path.join(output_dir, "license.ttl")

with open(metadata_file, "w", encoding="utf-8") as f:
    f.write(metadata_g.serialize(format="turtle"))
with open(license_file, "w", encoding="utf-8") as f:
    f.write(license_g.serialize(format="turtle"))

print(f"Serializzazione completata! File salvati:\n{metadata_file}\n{license_file}.")