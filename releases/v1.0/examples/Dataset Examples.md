# Dataset Examples

This document provides illustrative RDF/Turtle snippets for the properties defined in the **EUCAIM DCAT Application Profile Dataset specification**.

The examples are based on the examples included in EUCAIM Deliverable D5.3. They are intended to demonstrate how individual properties may be represented in RDF and are not, by themselves, a complete Dataset description.

## Prefixes

The snippets below assume the following prefixes:

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcatap: <http://data.europa.eu/r5r/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-pd: <https://w3id.org/dpv/pd#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix eucaim: <https://hyperontology.eucaim.cancerimage.eu/#> .
@prefix ex: <https://example.org/eucaim/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix healthdcatap: <https://w3id.org/healthdcat-ap#> .
@prefix locn: <http://www.w3.org/ns/locn#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

---

# Identification

## Identifier

```turtle
    dct:identifier
        "https://catalogue.eucaim.cancerimage.eu/#/collection/1a1a6653-975a-4a0a-a79b-b2bfc7317119"^^xsd:anyURI .
```

## Other Identifier

```turtle
    adms:identifier [
        a adms:Identifier ;
        skos:notation "https://www.healthinformationportal.eu/health-information-sources/linking-registers-covid-19-vaccine-surveillance"^^xsd:anyURI ;
        adms:schemaAgency "Health Information Portal"
    ] .
```

## Title

```turtle
    dct:title "Open Challenge Prostate Cancer V1"@en .
```

## Description

```turtle
    dct:description
        "This ProCAncer-I project imaging dataset contains a collection of patients with mpMRI examinations (T2ax, DWI and ADC) who have confirmed prostate cancer at biopsy and/or prostatectomy."@en .
```

## Documentation

```turtle
    foaf:page <https://www.procancer-i.eu/> .
```

## Interoperability Tier

```turtle
    eucaim:interoperabilityLevel eucaim:SPEC1000011 .
```

---

# Classification

## Theme

```turtle
    dcat:theme
        <http://publications.europa.eu/resource/authority/data-theme/HEAL> .
```

## Health Category

```turtle
    healthdcatap:healthCategory
        <http://13.81.34.152:1101/resource/authority/healthcategories/EHRS> .
```

## Health Theme

```turtle
    healthdcatap:healthTheme
        <http://13.81.34.152:1101/resource/authority/health-theme/CANCER> .
```

## Type

```turtle
    dct:type
        eucaim:SPEC1000019 ,
        dpv:PseudonymisedData .
```

## Keyword

```turtle
    dcat:keyword
        "Prostate Cancer"@en ,
        "mpMRI"@en .
```

## Language

```turtle
    dct:language
        <http://publications.europa.eu/resource/authority/language/ENG> .
```

---

# Responsible Parties

## Contact Point

```turtle
    dcat:contactPoint [
        a vcard:Organization ;
        vcard:fn "FORTH" ;
        vcard:hasEmail <mailto:access-committee@procancer-i.com>
    ] .
```

## Creator Name, Creator Contact Point

```turtle
    dct:creator ex:ministry-of-health .
    dct:creator [
        a foaf:Agent, foaf:Organization;
        foaf:name "Ministry of Health";
        vcard:hasURL <https://ministry-health.com/>;
        ] .
```

## Publisher Name, Publisher Contact Point, Publisher Note

```turtle
    dct:publisher [ 
        a foaf:Organization;
        dct:description "Research organisation responsible for publishing and maintaining the dataset metadata."@en ;
        locn:address [ a locn:Address;
            foaf:name "FORTH";
            foaf:mbox <mailto:access-commitee@procancer-i.com>;
            foaf:homepage <https://forth.ics.gr>;
        ];
    ];
```

## Publisher Type

```turtle
    healthdcatap:publisherType
        <https://example.org/authority/publisher-type/ResearchInstitute> .
```

## Qualified Attribution Agent Name, Agent Contact Point, Agent Role

```turtle
    prov:qualifiedAttribution [
        a prov:Attribution;
        dcat:hadRole <https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor>;
        prov:agent [ a foaf:Organization;
            locn:address [ a locn:Address;
            locn:adminUnitL1 "Belgium";
            locn:adminUnitL2 "Brussels capital";
            locn:postCode "1050";
            locn:postName "Elsene - Ixelles";
            locn:thoroughfare "Rue Juliette Wytsmanstraat 14"
            ];
            foaf:homepage <https://healthdata.be>;
            foaf:mbox <mailto:healthdata@sciensano.be>;
            foaf:name "healthdata.be (Sciensano)";
            foaf:phone <tel:+3227930142>
        ]
    ] .
```

---

# Access & Rights

## Access Rights

```turtle
    dct:accessRights
        <http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC> .
```

## Applicable Legislation

```turtle
    dcatap:applicableLegislation
        <http://data.europa.eu/eli/reg/2025/327/oj> .
```

## Purpose

```turtle
    dpv:hasPurpose [
        a dpv:Purpose ;
        dct:description
            "The primary objective of this dataset is the detection of prostate cancer with high accuracy in both peripheral and transitional zones, in order to identify men with cancer and those without cancer."@en
    ] .
```

## Legal Basis

```turtle
ex:dataset
    dpv:hasLegalBasis [
        a dpv:LegalBasis ;
        dct:description
            "Personal data were collected following explicit informed consent obtained from study participants under the X project clinical study protocol (Protocol ID: XXX-2025-01)."@en
    ] .
```

## Retention Period

```turtle
    healthdcatap:retentionPeriod [
        a dct:PeriodOfTime ;
        dcat:startDate "2020-03-01"^^xsd:date ;
        dcat:endDate "2034-12-31"^^xsd:date
    ] .
```

## Personal Data

```turtle
    dpv:hasPersonalData
        dpv-pd:BirthDate ,
        dpv-pd:Age ,
        dpv-pd:DateOfBirth .
```

---

# Population

## Number of Unique Individuals

```turtle
    healthdcatap:numberOfUniqueIndividuals 
        "8237"^^xsd:nonNegativeInteger .
```

## Minimum Typical Age

```turtle
    healthdcatap:minTypicalAge
        "18"^^xsd:nonNegativeInteger .
```

## Maximum Typical Age

```turtle
    healthdcatap:maxTypicalAge
        "90"^^xsd:nonNegativeInteger .
```

## Birth Sex

```turtle
    eucaim:hasBirthSex eucaim:COM1001370 .
```

## Population Coverage

```turtle
    healthdcatap:populationCoverage
        "Patients between 35 and 87 years old with prostate cancer treated with prostatectomy in hospitals in France between 2018 and 2023."@en .
```

## Cancer Condition

```turtle
    eucaim:hasCondition eucaim:CLIN1000075 .
```

---

# Imaging

## Number of Imaging Studies

```turtle
    healthdcatap:numberOfRecords
        "8789"^^xsd:nonNegativeInteger .
```

## Image Modality

```turtle
    eucaim:hasImageModality eucaim:IMG1000022 .
```

## Image Equipment Manufacturer

```turtle
    eucaim:hasEquipmentManufacturer eucaim:IMG1000047 .
```

## Image Body Part / Structure

```turtle
    eucaim:hasImageBodyPart eucaim:BP1000233 .
```

---

# Annotation

## Segmentation Label

```turtle
    eucaim:hasAnnotationLabel eucaim:BP1000075 .
```

## Segmentation Method

```turtle
    eucaim:hasAlgorithmType eucaim:COM1000003 .
```

## Number of Segmentations

```turtle
    eucaim:nbrOfSegmentations
        "789"^^xsd:nonNegativeInteger .
```

---

# Coverage

## Collection Method

```turtle
    eucaim:collectionMethod eucaim:SPEC1000003 .
```

## Image Acquisition Period

```turtle
    dct:temporal [
        a dct:PeriodOfTime ;
        dcat:startDate "2021-01-01"^^xsd:date ;
        dcat:endDate "2023-12-31"^^xsd:date
    ] .
```

## Geographical Coverage

```turtle
    dct:spatial
        <http://publications.europa.eu/resource/authority/country/GRC> .
```

## Spatial Resolution

```turtle
    dcat:spatialResolutionInMeters
        "1000.0"^^xsd:decimal .
```

## Temporal Resolution

```turtle
    dcat:temporalResolution
        "P1M"^^xsd:duration .
```

## Frequency

```turtle
    dct:accrualPeriodicity
        <http://publications.europa.eu/resource/authority/frequency/MONTHLY> .
```

---

# Standards & Coding

## Conforms To

```turtle
    dct:conformsTo
        <https://www.wikidata.org/entity/Q19597236> .
```

## Coding System

```turtle
    healthdcatap:hasCodingSystem
        <https://www.wikidata.org/entity/Q9006342> ,
        <https://www.wikidata.org/entity/Q5969475> .
```

## Code Values

```turtle
    healthdcatap:hasCodeValues [ a skos:Concept;
        skos:inScheme [ a skos:ConceptScheme;
            dct:identifier "http://www.wikidata.org/entity/Q45127"^^xsd:anyURI ;
            skos:prefLabel "International Classification of Diseases, 10th Revision (ICD-10)"@en;
            skos:definition "ICD-10 is a medical classification list by the World Health Organization."@en;
            skos:notation "ICD-10";
            owl:versionInfo "Version:2019"
        ];
        dct:identifier "https://icd.who.int/browse10/2019/en#/Y59.0"^^xsd:anyURI ;
        skos:notation "Y59.0";
        skos:prefLabel "Viral vaccines"@en
    ];
    healthdcatap:hasCodeValues [ a skos:Concept;
        skos:inScheme [ a skos:ConceptScheme;
            dct:identifier "http://www.wikidata.org/entity/Q45127"^^xsd:anyURI ;
            skos:prefLabel "International Classification of Diseases, 10th Revision (ICD-10)"@en;
            skos:definition "ICD-10 is a medical classification list by the World Health Organization."@en;
            skos:notation "ICD-10";
            owl:versionInfo "Version:2019"
        ];
        dct:identifier "https://icd.who.int/browse10/2019/en#/U07.1>"^^xsd:anyURI ;
        skos:notation "U07.1";
        skos:prefLabel "COVID-19, virus identified"@en
    ] .
```

---

# Provenance

## Provenance

```turtle
    dct:provenance [
        a dct:ProvenanceStatement ;
        rdfs:label
            "This data is sourced from several existing datasets, including the Duke dataset, Parc Taulí and TCGA datasets."@en
    ] .
```

## Was Generated By

```turtle
    prov:wasGeneratedBy [ a prov:Activity ;
        dct:type <https://example.org/authority/health-activity/RESEARCH_PROJECT> ;
        foaf:page <https://www.procancer-i.eu/> ;
        rdfs:label "ProCAncer-I AI4HI project"@en ;
        prov:startedAtTime "2020-10-01"^^xsd:date .
```

---

# Quality

## Quality Annotation

```turtle
    dqv:hasQualityAnnotation [
        a dqv:QualityCertificate ;
        oa:hasTarget ex:dataset ;
        dqv:inDimension ex:integrity ;
        oa:motivatedBy dqv:qualityAssessment
    ] .

    ex:integrity
        a dqv:Dimension ;
        skos:prefLabel "Integrity"@en ;
        skos:definition
            "Degree to which the dataset's DICOM files remain complete, internally consistent and compliant with the DICOM standard."@en .
```

---

# Relationships

## Landing Page

```turtle
    dcat:landingPage
        <https://fair.healthdata.be/dataset/example> .
```

## Related Resource

```turtle
    dct:relation
        <https://example.org/another-resource> .
```

## Is Referenced By

```turtle
    dct:isReferencedBy
        <https://doi.org/10.1186/s13690-021-00709-x> .
```

## Sample

```turtle
    adms:sample ex:sample-distribution .

    ex:sample-distribution
        a dcat:Distribution ;
        dct:title "Sample distribution containing the DICOM images for the prostate cancer dataset"@en ;
        dcat:accessURL <https://prostatenet.eu/> .
```

## Analytics

```turtle
    healthdcatap:analytics [ a dcat:Distribution ;
        dct:title
            "Technical report on the number of unique study subjects"@en ;
        dcat:accessURL
            <https://fair.healthdata.be/sites/default/files/distribution/example/technical-report.csv> ;
        dct:format
            <http://publications.europa.eu/resource/authority/file-type/CSV> ;
        dcat:mediaType
            <https://www.iana.org/assignments/media-types/text/csv> ] .
```

---

# Dates & Versioning

## Version

```turtle
    dcat:version "20231122" .
```

## Version Notes

```turtle
    adms:versionNotes
        "Updated data collection methodology and extended temporal coverage to include 2023 data. Fixed data quality issues identified in the previous version."@en .
```

## Release Date

```turtle
    dct:issued "2022-09-10"^^xsd:date .
```

## Modification Date

```turtle
    dct:modified "2023-01-15"^^xsd:date .
```
