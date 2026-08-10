# EUCAIM DCAT Application Profile v2.0 — Catalogue

## Overview

This document defines the properties used to describe a `dcat:Catalog` in version 2.0 of the EUCAIM DCAT Application Profile. The specification inherits the Catalogue specification from [HealthDCAT-AP Release 7](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-7/) without modification.

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
| Language | — | `dct:language` | `dct:LinguisticSystem` | `0..n` **R** | A language used in the textual metadata describing titles, descriptions, and other information about the Datasets in the Catalogue. | Values MUST be selected from the [EU Vocabularies Language Named Authority List](http://publications.europa.eu/resource/authority/language). Use this property to indicate the languages of the Dataset content. Multiple values may be provided. | |
| Modification Date | — | `dct:modified` | `rdfs:Literal` | `0..1` **R** | The most recent date on which the Catalogue was modified. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. Example: `"2023-12-10T13:16:10.246Z"^^xsd:dateTime`. |
| Release Date | — | `dct:issued` | `rdfs:Literal` | `0..1` **R** | The date of formal issuance, such as publication, of the Catalogue. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. Example: `"2023-12-10T13:16:10.246Z"^^xsd:dateTime`. |
| Themes | — | `dcat:themeTaxonomy` | `skos:ConceptScheme` | `0..n` **R** | A knowledge organisation system used to classify the resources contained in the Catalogue. | A Catalogue may be associated with multiple theme taxonomies. The [EU Data Theme controlled vocabulary](http://publications.europa.eu/resource/authority/data-theme) MAY be used. |
| Geographical Coverage | — | `dct:spatial` | `dct:Location` | `0..n` **R** | A geographical area covered by the Catalogue. | Values MUST be selected, where available, from the EU Vocabularies authority tables for [continents](http://publications.europa.eu/resource/authority/continent), [countries](http://publications.europa.eu/resource/authority/country), or [places](http://publications.europa.eu/resource/authority/place). When the required location is not available in these authority tables, a [GeoNames](https://www.geonames.org/) URI SHOULD be used. Multiple values may be provided. |
| Licence | — | `dct:license` | `dct:LicenseDocument` | `0..1` **R** | A licence under which the Catalogue can be used or reused. | Provide the licence under which the Catalogue is made available. Use the canonical IRI of a standard licence where applicable. See the [DCAT 3 guidance on licences and rights](https://www.w3.org/TR/vocab-dcat-3/#license-rights). |
| Service | — | `dcat:service` | `dcat:DataService` | `0..n` **R** | A site or endpoint, represented as a Data Service, that is listed in the Catalogue. | Some Datasets may have real-time Data Services, such as a Beacon API for counting individuals. Implementers should define the relationship between the Catalogue and the Data Service using this property. |
| Dataset | — | `dcat:dataset` | `dcat:Dataset` | `0..n` **R** | A Dataset that is part of the Catalogue. | As empty Catalogues are usually indications of problems, this property should be combined with the Service property to implement an empty-Catalogue check. |
| Catalogue | — | `dcat:catalog` | `dcat:Catalog` | `0..n` **O** | A catalogue whose contents are of interest in the context of this Catalogue. | For certain research projects, multiple Catalogues may need to be organised in a nested manner. This property connects the different Catalogues with each other. |
| Has Part | — | `dct:hasPart` | `dcat:Catalog` | `0..n` **O** | A related Catalogue that is part of the described Catalogue. | Use this property to identify another Catalogue included physically or logically in the described Catalogue. |
| Record | — | `dcat:record` | `dcat:CatalogRecord` | `0..n` **O** | A Catalogue Record that is part of the Catalogue. | Link to a `dcat:CatalogRecord` when applicable. |
| Rights | — | `dct:rights` | `dct:RightsStatement` | `0..n` **O** | A statement that specifies rights associated with the Catalogue. | Detail the intellectual-property rights, usage restrictions, and access permissions governing the Catalogue, complementing the licence information. See the [DCAT 3 guidance on licences and rights](https://www.w3.org/TR/vocab-dcat-3/#license-rights). |
| Temporal Coverage | — | `dct:temporal` | `dct:PeriodOfTime` | `0..n` **O** | A temporal period that the Catalogue covers. | The start and end of the interval SHOULD be provided using `dcat:startDate` or `time:hasBeginning`, and `dcat:endDate` or `time:hasEnd`, respectively. |


## Publisher

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Publisher | — | `dct:publisher` | `foaf:Agent` | `1..1` **M** | An entity, such as an organisation, responsible for making the Catalogue available. | If the Publisher exists in the EU Corporate Bodies Named Authority List, the corresponding entry SHOULD be used. |
| Publisher Name | — | `dct:publisher / foaf:name` | `rdfs:Literal` | `1..n` **M** | The name of the organisation responsible for making the Dataset available. | The publisher may be the data holder or another organisation, such as an intermediation entity. |
| Publisher Type | — | `dct:publisher / dct:type` | `skos:Concept` | `0..1` **R** | The nature or category of the Publisher. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable concept SHOULD be used. |
| Publisher Contact Point | — | `dct:publisher / cv:contactPoint` | `cv:ContactPoint` | `1..1` **M** | Contact information that can be used to contact the Publisher. | The Contact Point MUST provide at least one `cv:contactPage` or `cv:email` value. |
| Publisher Contact Page | — | `dct:publisher / cv:contactPoint / cv:contactPage` | `foaf:Document` | `0..n` **C** | A web page that could be used to reach the Publisher Contact Point. | At least one Publisher Contact Page or Publisher Email MUST be provided. When EUCAIM is the Publisher, the contact information MUST include `https://cancerimage.eu/contact-us/`. |
| Publisher Email | — | `dct:publisher / cv:contactPoint / cv:email` | `rdfs:Literal` | `0..n` **C** | An electronic address through which the Publisher Contact Point can be contacted. | At least one Publisher Contact Page or Publisher Email MUST be provided. When EUCAIM is the Publisher, the contact information MUST include `contact@cancerimage.eu`. |
| Publisher Telephone | — | `dct:publisher / cv:contactPoint / cv:telephone` | `rdfs:Literal` | `0..n` **O** | A telephone number through which the Publisher Contact Point can be contacted. | The value SHOULD include the international country code. |
| Publisher Description | — | `dct:publisher / dct:description` | `rdfs:Literal` | `0..n` **R** | A description of the Publisher's activities. | May be repeated for different language versions. |
| Publisher Availability Restriction | — | `dct:publisher / cv:contactPoint / cv:specialOpeningHoursSpecification` | `dct:PeriodOfTime` | `0..n` **O** | The time during which the Contact Point is not available. | When provided, the Temporal Entity MUST have at least one human-readable description. For example, `"Closed on weekends"@en`. |
| Availability Restriction Description | — | `dct:publisher / cv:contactPoint / cv:specialOpeningHoursSpecification / dct:description` | `rdfs:Literal` | `1..n` **C** | A textual representation of the availability restriction. **M** when a Publisher Availability Restriction is provided. May be repeated for different languages. |
| Availability Restriction Frequency | — | `dct:publisher / cv:contactPoint / cv:specialOpeningHoursSpecification / cv:frequency` | `dct:Frequency` | `0..n` **O** | The recurrence of the availability restriction. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). For example, `WEEKLY`. |
| Publisher Opening Hours | — | `dct:publisher / cv:contactPoint / cv:openingHours` | `dct:PeriodOfTime` | `0..n` **O** | The time at which the Contact Point is normally available. | When provided, the Temporal Entity MUST have at least one human-readable description. For example, `"Open Monday to Saturday"@en`. |
| Opening Hours Description | — | `dct:publisher / cv:contactPoint / cv:openingHours / dct:description` | `rdfs:Literal` | `1..n` **C** | A textual representation of the opening hours. **M** when Publisher Opening Hours are provided. May be repeated for different languages. |
| Opening Hours Frequency | — | `dct:publisher / cv:contactPoint / cv:openingHours / cv:frequency` | `dct:Frequency` | `0..n` **O** | The recurrence of the opening-hours period. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). For example, `DAILY`. |

## Creator

The optional `dct:creator` value is an Agent responsible for creating the Catalogue.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Creator | — | `dct:creator` | `foaf:Agent` | `0..1` **O** | An entity responsible for the creation of the Catalogue. | Identify the Agent that played the role of creating the Catalogue. |
| Creator Name | — | `dct:creator / foaf:name` | `rdfs:Literal` | `1..n` **C** | Name of an entity responsible for producing the Catalogue. | MUST be provided for each Creator. The name may be repeated using language-tagged literals for different language versions. |
| Creator Contact Page | — | `dct:creator / foaf:homepage` | `rdfs:Resource` | `0..n` **O** | Contact page or homepage of the Creator. | When a Creator is provided, at least one Creator Contact Page or Creator Email SHOULD also be provided. The contact page SHOULD be a stable webpage or web form through which the Creator can be contacted. |
| Creator Email | — | `dct:creator / foaf:mbox` | `rdfs:Resource` | `0..n` **O** | Email address through which the Creator can be contacted. | Use a `mailto:` URI. |
| Creator Type | — | `dct:creator / dct:type` | `skos:Concept` | `0..1` **O** | Type of the Agent that created the Catalogue. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable Agent type SHOULD be used. |