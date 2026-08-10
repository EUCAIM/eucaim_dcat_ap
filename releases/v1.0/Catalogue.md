# EUCAIM DCAT Application Profile v1.0 — Catalogue

## Overview

This document defines the properties used to describe a `dcat:Catalog` in version 1.0 of the EUCAIM DCAT Application Profile. The specification inherits the Catalogue specification from [HealthDCAT-AP Release 5](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/) without modification.

The Catalogue contains metadata records describing EUCAIM datasets and their associated distributions. EUCAIM-specific requirements for individual datasets and distributions are defined separately in the [Dataset](Dataset.md) and [Distribution](Distribution.md) specifications.

## Legend

The **EUCAIM Modification** column identifies structural or conformance-level differences from HealthDCAT-AP.

| Symbol | EUCAIM Modification | Description |
|---|---|---|
| 🟢 | **Added** | Property introduced by the EUCAIM DCAT Application Profile and not defined for the Catalogue in HealthDCAT-AP. |
| 🟠 | **Modified** | HealthDCAT-AP property for which EUCAIM changes the property IRI, range, cardinality, or requirement level. |
| — | **Inherited** | Property inherited with the same IRI, range, cardinality, and requirement level. EUCAIM-specific explanations, examples, and implementation guidance may be added to the Usage Notes without changing its inherited status. |

The occurrence notation combines cardinality and requirement level:

| Code | Meaning |
|---|---|
| **M** | Mandatory — the property MUST be provided. |
| **R** | Recommended — the property SHOULD be provided. |
| **C** | Conditional — the property MUST be provided when the condition in its Usage Notes applies; otherwise, it MAY be omitted. |
| **O** | Optional — the property MAY be provided. |

## Catalogue Properties

| Property | EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Title | — | `dct:title` | `rdfs:Literal` | `1..n` **M** | A name given to the Catalogue. | Provide a title for the Catalogue. The property may be repeated in multiple languages. Example: `"ProCAncer-I Dataset Catalogue"@en`. |
| Description | — | `dct:description` | `rdfs:Literal` | `1..n` **M** | A free-text account of the Catalogue. | Briefly describe the Catalogue and what it contains. The property may be repeated in multiple languages. |
| Applicable Legislation | — | `dcatap:applicableLegislation` | `eli:LegalResource` | `1..n` **M** | The legislation that mandates the creation or management of the Catalogue. | The ELI of the EHDS Regulation, published in March 2025, can be used as the applicable legislation where relevant: [`http://data.europa.eu/eli/reg/2025/327/oj`](http://data.europa.eu/eli/reg/2025/327/oj). As multiple legislations may apply to the resource, the maximum cardinality is not limited. |
| Homepage | — | `foaf:homepage` | `foaf:Document` | `0..1` **R** | A web page that acts as the main page for the Catalogue. | Provide the homepage of the Catalogue, if available. |
| Language | — | `dct:language` | `dct:LinguisticSystem` | `0..n` **R** | A language used in the textual metadata describing titles, descriptions, and other information about the Datasets in the Catalogue. | Values MUST be selected from the [EU Vocabularies Language Named Authority List](http://publications.europa.eu/resource/authority/language). Use this property to indicate the languages used in the textual metadata of the Catalogue. Multiple values may be provided. |
| Modification Date | — | `dct:modified` | `rdfs:Literal` | `0..1` **R** | The most recent date on which the Catalogue was modified. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. Example: `"2023-12-10T13:16:10.246Z"^^xsd:dateTime`. |
| Release Date | — | `dct:issued` | `rdfs:Literal` | `0..1` **R** | The date of formal issuance, such as publication, of the Catalogue. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. Example: `"2023-12-10T13:16:10.246Z"^^xsd:dateTime`. |
| Themes | — | `dcat:themeTaxonomy` | `skos:ConceptScheme` | `0..n` **R** | A knowledge organisation system used to classify the resources contained in the Catalogue. | A Catalogue may be associated with multiple theme taxonomies. At least one theme from the [EU Data Theme controlled vocabulary](http://publications.europa.eu/resource/authority/data-theme) SHOULD be used. |
| Geographical Coverage | — | `dct:spatial` | `dct:Location` | `0..n` **R** | A geographical area covered by the Catalogue. | Values MUST be selected, where available, from the EU Vocabularies authority tables for [continents](http://publications.europa.eu/resource/authority/continent), [countries](http://publications.europa.eu/resource/authority/country), or [places](http://publications.europa.eu/resource/authority/place). When the required location is not available in these authority tables, a [GeoNames](https://www.geonames.org/) URI SHOULD be used. Multiple values may be provided. |
| Licence | — | `dct:license` | `dct:LicenseDocument` | `0..1` **R** | A licence under which the Catalogue can be used or reused. | Provide the licence under which the Catalogue is made available. Use the canonical IRI of a standard licence where applicable. See the [DCAT 3 guidance on licences and rights](https://www.w3.org/TR/vocab-dcat-3/#license-rights). |
| Service | — | `dcat:service` | `dcat:DataService` | `0..n` **R** | A site or endpoint, represented as a Data Service, that is listed in the Catalogue. | Some Datasets may have real-time Data Services, such as a Beacon API for counting individuals. Implementers should define the relationship between the Catalogue and the Data Service using this property. |
| Dataset | — | `dcat:dataset` | `dcat:Dataset` | `0..n` **R** | A Dataset that is part of the Catalogue. | Links the Catalogue to the Datasets it contains. A Catalogue SHOULD contain at least one Dataset or Data Service. |
| Catalogue | — | `dcat:catalog` | `dcat:Catalog` | `0..n` **O** | A catalogue whose contents are of interest in the context of this Catalogue. | For certain research projects, multiple Catalogues may need to be organised in a nested manner. This property connects the different Catalogues with each other. |
| Has Part | — | `dct:hasPart` | `dcat:Catalog` | `0..n` **O** | A related Catalogue that is part of the described Catalogue. | Use this property to identify another Catalogue included physically or logically in the described Catalogue. |
| Record | — | `dcat:record` | `dcat:CatalogRecord` | `0..n` **O** | A Catalogue Record that is part of the Catalogue. | Link to a `dcat:CatalogRecord` when applicable. |
| Rights | — | `dct:rights` | `dct:RightsStatement` | `0..n` **O** | A statement that specifies rights associated with the Catalogue. | Use for rights information not fully expressed by the Licence property, such as copyright or other intellectual-property statements. |
| Temporal Coverage | — | `dct:temporal` | `dct:PeriodOfTime` | `0..n` **O** | A temporal period that the Catalogue covers. | The start and end of the interval SHOULD be provided using `dcat:startDate` or `time:hasBeginning`, and `dcat:endDate` or `time:hasEnd`, respectively. |


## Creator

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Creator** | — | `dct:creator` | `foaf:Agent` | `0..1` **O** | Organisation or individual responsible for creating the Catalogue. | The Agent who played the role of the catalogue creation. |
| **Creator Name** | — | `dct:creator / foaf:name` | `rdfs:Literal` | `1..n` **C** | Name of the Creator. | Mandatory for each Creator. It may be repeated for multilingual names. |
| **Creator Type** |  —  | `dct:creator / dct:type` | `skos:Concept` | `0..1` **O**  | Type of creator. | If the organisation exists in the EU Corporate Bodies Authority List, use the corresponding concept. |

## Publisher

The Publisher section describes the organisation responsible for making the Catalogue available and provides the information required to contact that organisation.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| Publisher | 🟠 **Modified**  | `dct:publisher` | `foaf:Agent` | `1..1` **M** | Agent responsible for making the Catalogue available. | The Publisher may be the health data holder or another organisation, such as a data intermediation entity. |
| **Publisher Name** | — | `dct:publisher / foaf:name` | `rdfs:Literal` | `1..n` **M** | The organisation responsible for making the Catalogue available. | This is typically the data holder responsible for ensuring that the Dataset can be accessed and reused. Provide the official name of the organisation. |
| **Publisher Contact Point** | — | `dct:publisher / dcat:contactPoint` | `vcard:Kind` | `1..1` **M**| Contact information for the Publisher. | Provide at least one email address or contact webpage. |
| **Publisher Type** |  —  | `dct:publisher / dct:type` | `skos:Concept` | `0..1` **R** | The type of organisation publishing the Catalogue. | Recommended values include: Research Institute, Hospital or Healthcare System Repository, European Project, Cancer Screening Programme, Patient Association, Data Altruism Organisation, ERIC and EDIC. |
| **Publisher Note** |  —  | `dct:publisher / dct:description` | `rdfs:Literal` | `0..n` **R**| A description of the publisher and its activities. | This property may be repeated for multiple language versions. It should provide information relevant to the publisher in the context of the Catalogue. |
| **Publisher Trusted Data Holder** | — | `dct:publisher / healthdcatap:trustedDataHolder` | `xsd:boolean` | `0..1` **O** | Indicates whether the Publisher is a trusted health data holder. | Use `true` when the Publisher is recognised as a trusted health data holder and `false` when it is not. |