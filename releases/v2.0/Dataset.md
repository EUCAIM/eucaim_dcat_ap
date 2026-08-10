# EUCAIM DCAT Application Profile v2.0 — Dataset

## Overview

This document defines the properties used to describe a `dcat:Dataset` in version 2.0 of the EUCAIM DCAT Application Profile. It is aligned with DCAT-AP v3 and HealthDCAT-AP release 7 and extends them with metadata required for the discovery and reuse of cancer imaging datasets in EUCAIM.

## Legend

The **EUCAIM Change** column identifies structural or conformance-level differences from HealthDCAT-AP.

| Symbol | EUCAIM Change | Description |
|---|---|---|
| 🟢 | **Added** | Property introduced by the EUCAIM DCAT Application Profile and not defined for the Dataset in HealthDCAT-AP. |
| 🟠 | **Modified** | HealthDCAT-AP property for which EUCAIM changes the property IRI, range, cardinality, or requirement level. |
| — | **Inherited** | Property inherited with the same IRI, range, cardinality, and requirement level. EUCAIM-specific explanations, examples, and implementation guidance may be added to the Usage Notes without changing its inherited status. |

### Occurrence notation

The **Occurrence** column combines cardinality and requirement level.

| Code | Requirement |
|---|---|
| **M** | Mandatory — the property MUST be provided. |
| **R** | Recommended — the property SHOULD be provided when applicable or available. |
| **C** | Conditional — the property MUST be provided when the condition in its Usage Notes applies; otherwise, it MAY be omitted. |
| **O** | Optional — the property MAY be provided. |

Examples:

- `1..n` **M** — one or more values are mandatory.
- `0..1` **R** — zero or one value; providing it is recommended.
- `1..1` **C** — exactly one value is required when the stated condition applies.
- `0..n` **O** — zero or more values may be provided.

## Processing Conformance

This specification defines the properties that EUCAIM catalogue implementations are required to accept and process.

- **Accept** means that the harvester MUST ingest the property without producing an error.
- **Process** means that the harvester MUST preserve the value and map it to the corresponding catalogue field or internal representation.
- Properties not explicitly listed in this specification MAY be present in the RDF. Harvesters SHOULD preserve such properties where technically possible but are not required to interpret, index, or display them.
- An unlisted property MUST NOT be interpreted as an alternative to a listed Mandatory property.
- The cardinalities in the Dataset property tables apply to each Dataset.
- Where a property path traverses a structured resource, such as `foaf:Agent`, `cv:ContactPoint`, `prov:Attribution`, or `dcat:Relationship`, the cardinalities in the corresponding section apply to each instance of that resource.

## Identification

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Identifier | 🟠  | `dct:identifier` | `rdfs:Literal` | `1..1` **M** | A unique identifier for the dataset, corresponding to its URI in the EUCAIM Public Catalogue. | The value MUST be unique. Example: `https://cancerimage.eu/datasets/ds-001`. |
| Title | — | `dct:title` | `rdfs:Literal` | `1..n` **M** | A clear and concise name given to the Dataset. | An English title is mandatory. The property may be repeated for other languages. |
| Alternative | — | `dct:alternative` | `rdfs:Literal` | `0..n` **O** | An alternative name for the Dataset. | May be repeated for alternative names or parallel language versions. |
| Description | — | `dct:description` | `rdfs:Literal` | `1..n` **M** | A free-text account of the Dataset. | An English description is mandatory. The property may be repeated for other languages. |
| Version | 🟠 | `dcat:version` | `rdfs:Literal` | `1..1` **M** | The version of the Dataset. | Use Semantic Versioning or Calendar Versioning, e.g. `1.0.0` or `2026.08.1`. |
| Interoperability Tier | 🟢 | `eucaim:interoperabilityLevel` | `eucaim:SPEC1000008` | `1..1` **M** | The EUCAIM data-federation and interoperability tier to which the Dataset belongs. | Values MUST be selected from the subclasses of [`eucaim:SPEC1000008` — Interoperability level](https://hyperontology.eucaim.cancerimage.eu/#SPEC1000008). |
| Dataset Distribution | — | `dcat:distribution` | `dcat:Distribution` | `1..n` **M** | An available Distribution of the Dataset. | At least one Distribution MUST be provided, independently of the Dataset's access rights. |
| In Series | — | `dcat:inSeries` | `dcat:DatasetSeries` | `0..n` **O** | A Dataset Series of which the Dataset is a member. | Use when the Dataset belongs to a collection of related Datasets published separately, such as a longitudinal, periodic, or versioned series. The Dataset Series SHOULD be identified using a stable URI. Multiple series MAY be provided. |
| Dataset Contact Point | — | `dcat:contactPoint` | `vcard:Kind` | `1..n` **M** | Contact information that can be used to submit enquiries or comments about the Dataset. | At least one Contact Page or Email MUST be supplied. |
| Dataset Contact Point — Contact Page | — | `dcat:contactPoint / vcard:hasURL` | `rdfs:Resource` | `0..1` **C** | A webpage or form through which comments or enquiries about the Dataset can be submitted. | At least one contact page or contact email MUST be provided for each contact point. |
| Dataset Contact Point — Email | — | `dcat:contactPoint / vcard:hasEmail` | `rdfs:Resource` | `0..1` **C** | An email address through which comments or enquiries about the Dataset can be submitted. | Use a `mailto:` URI. At least one contact page or contact email MUST be provided. |
| Documentation | — | `foaf:page` | `foaf:Document` | `0..n` **R** | A page or document about the Dataset. | Any additional source of information about the Dataset. |

## Classification

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Theme | — | `dcat:theme` | `skos:Concept` | `1..1` **M** | A category of the Dataset. | Fixed value: [`HEAL` — Health](http://publications.europa.eu/resource/authority/data-theme/HEAL) from the EU Data Theme Named Authority List. |
| Health Category | — | `healthdcatap:healthCategory` | `skos:Concept` | `1..n` **M** | The health category to which the Dataset belongs, based on Article 51 of the EHDS Regulation. | Values MUST be selected from the [Health Categories controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/healthcategories/), which defines the categories of electronic health data listed in Article 51 of the EHDS Regulation. Multiple values may be provided. |
| Health Theme | — | `healthdcatap:healthTheme` | `skos:Concept` | `0..n` **R** | A category or tag describing the health subject of the Dataset. | Values MUST be selected from the [Health Themes controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/health-theme). For EUCAIM datasets, the value SHOULD be [`CANCER_DISEASE` — Cancer](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/health-theme/CANCER_DISEASE). Multiple values may be provided. |
| Type | 🟠 | `dct:type` | `eucaim:SPEC1000017` and/or `dpv:Data` | `1..n` **M** | A type of the Dataset. | Values MUST be selected from the subclasses of [`eucaim:SPEC1000017` — Dataset Type](https://hyperontology.eucaim.cancerimage.eu/#SPEC1000017) and/or [`dpv:Data`](https://w3id.org/dpv#Data). Multiple values may be provided. |

## Access and Rights

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Access Rights | — | `dct:accessRights` | `dct:RightsStatement` | `1..1` **M** | Information indicating whether the Dataset is publicly accessible, restricted, or non-public. | The value MUST be one of [`PUBLIC`](http://publications.europa.eu/resource/authority/access-right/PUBLIC), [`RESTRICTED`](http://publications.europa.eu/resource/authority/access-right/RESTRICTED), or [`NON_PUBLIC`](http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC) from the [EU Access Right Authority Table](https://publications.europa.eu/resource/authority/access-right). |
| Applicable Legislation | — | `dcatap:applicableLegislation` | `eli:LegalResource` | `1..n` **M** | Legislation that mandates the creation or management of the Dataset. | Where applicable, the value MUST include the ELI URI of the [European Health Data Space Regulation (EU) 2025/327](http://data.europa.eu/eli/reg/2025/327/oj). Additional applicable EU or national legislation SHOULD also be provided, preferably using an official persistent URI such as an ELI. |
| Legal Basis | — | `dpv:hasLegalBasis` | `dpv:LegalBasis` | `0..n` **R** | Legal basis used to justify the processing of data or use of technology under applicable law. | Values MUST be selected from the subclasses of [`dpv:LegalBasis`](https://w3id.org/dpv#LegalBasis). The most specific legally applicable concept SHOULD be used. |
| Purpose | — | `dpv:hasPurpose` | `dpv:Purpose` | `0..n` **R** | The purpose for which the data or personal data is processed. | The purpose SHOULD be represented using a concept from the subclasses of [`dpv:Purpose`](https://w3id.org/dpv#Purpose). A language-tagged `dct:description` MAY additionally be provided to describe the specific purpose in greater detail. When no suitable DPV concept is available, a generic `dpv:Purpose` resource with a language-tagged `dct:description` MAY be used. Multiple purposes may be provided. |
| Personal Data | — | `dpv:hasPersonalData` | `dpv:PersonalData` | `0..n` **R** | Types of personal data contained in the Dataset. | Values MUST be selected from the subclasses of [`dpv:PersonalData`](https://w3id.org/dpv#PersonalData), including the categories defined in the [DPV Personal Data taxonomy](https://w3id.org/dpv/pd). The most specific applicable concepts SHOULD be used. Multiple values may be provided. This property describes the types of personal data contained in the Dataset, not personal data contained in the catalogue metadata record. |
| Retention Period | — | `healthdcatap:retentionPeriod` | `dct:PeriodOfTime` | `0..1` **R** | A temporal period for which the Dataset is available for secondary use. | Describe the interval using `dcat:startDate` and/or `dcat:endDate`. The interval may be open-ended. |

## Publisher

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Publisher | 🟠  | `dct:publisher` | `foaf:Agent` | `1..1` **M** | Agent responsible for making the Dataset available. | The Publisher may be the health data holder or another organisation, such as a data intermediation entity. |
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

## Subjects and Population

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Structured Data | — | `healthdcatap:hasStructuredData` | `xsd:boolean` | `1..1` **M** | Indicates whether the Dataset contains structured data for which a machine-readable description of the variables can be provided. | If `true`, at least one `healthdcatap:hasVariables` value MUST be provided. |
| Variables | — | `healthdcatap:hasVariables` | `csvw:TableGroup` | `0..n` **C** | Links the Dataset to a CSVW Table Group describing its variables, columns, or fields. **M** when `healthdcatap:hasStructuredData` is `true`. |
| Number of Unique Individuals | 🟠 | `healthdcatap:numberOfUniqueIndividuals` | `xsd:nonNegativeInteger` | `1..1` **M** | Total count of unique individuals represented in the Dataset. | An approximate count may be supplied when an exact count is unavailable. |
| Number of Imaging Studies | 🟠 | `healthdcatap:numberOfRecords` | `xsd:nonNegativeInteger` | `1..1` **M** | Total count of imaging studies, such as DICOM Studies, represented in the Dataset. | Each imaging study is counted once; an individual may have multiple studies. |
| Birth Sex | 🟢 | `eucaim:hasBirthSex` | `eucaim:COM1001396` | `1..n` **M** | Sex assigned at birth of the individuals represented in the Dataset. | Values MUST be selected from the subclasses of [`eucaim:COM1001396` — Sex assigned at birth](https://hyperontology.eucaim.cancerimage.eu/#COM1001396). Multiple values may be provided. |
| Minimum Typical Age | — | `healthdcatap:minTypicalAge` | `xsd:nonNegativeInteger` | `0..1` **R** | Approximate minimum age of individuals represented in the Dataset. | Expressed in years. Approximation protects potentially sensitive information. |
| Maximum Typical Age | — | `healthdcatap:maxTypicalAge` | `xsd:nonNegativeInteger` | `0..1` **R** | Approximate maximum age of individuals represented in the Dataset. | Expressed in years. Approximation protects potentially sensitive information. |
| Cancer Condition | 🟢 | `eucaim:hasCondition` | `eucaim:CLIN1007977` | `1..1` **M** | The primary cancer condition represented in the Dataset. | The value MUST be selected from the subclasses of [`eucaim:CLIN1007977` — Malignant neoplastic disease](https://hyperontology.eucaim.cancerimage.eu/#CLIN1007977). If the Dataset contains individuals with metastatic cancer and the primary cancer condition is unknown, the appropriate subclass of [`Secondary Cancer Condition`](https://hyperontology.eucaim.cancerimage.eu/#CLIN1007989) SHOULD be used. |
| Population Coverage | — | `healthdcatap:populationCoverage` | `rdfs:Literal` | `0..n` **R** | A free-text definition of the population represented in the Dataset. | May describe age, disease, treatment, geography, and collection period and may be repeated for different languages. |
| Collection Method | 🟢 | `eucaim:collectionMethod` | `eucaim:SPEC1000002` | `1..n` **M** | Scope and method of data aggregation used to create the Dataset. | Values MUST be selected from the subclasses of [`eucaim:SPEC1000002` — Collection method](https://hyperontology.eucaim.cancerimage.eu/#SPEC1000002). Multiple values may be provided when more than one collection method applies to the Dataset. |
| Geographical Coverage | — | `dct:spatial` | `dct:Location` | `0..n` **O** | A geographic region covered by the Dataset. | Values MUST be selected, where available, from the EU Vocabularies authority tables for [continents](http://publications.europa.eu/resource/authority/continent), [countries](http://publications.europa.eu/resource/authority/country), or [places](http://publications.europa.eu/resource/authority/place). When the required location is not available in these authority tables, a [GeoNames](https://www.geonames.org/) URI SHOULD be used. Multiple values may be provided. |

## Imaging Properties

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Image Modality | 🟢 | `eucaim:hasImageModality` | `eucaim:IMG1000009` | `1..n` **M** | Imaging modalities represented in the Dataset. | Values MUST be selected from the subclasses of [`eucaim:IMG1000009` — Imaging modality](https://hyperontology.eucaim.cancerimage.eu/#IMG1000009). The most specific applicable modality SHOULD be used. Multiple values may be provided. |
| Image Equipment Manufacturer | 🟢 | `eucaim:hasEquipmentManufacturer` | `eucaim:IMG1000010` | `1..n` **M** | Manufacturer of the imaging device, corresponding to DICOM attribute (0008,0070). | Values MUST be selected from the subclasses of [`eucaim:IMG1000010` — Manufacturer](https://hyperontology.eucaim.cancerimage.eu/#IMG1000010). The values SHOULD correspond to the imaging-equipment manufacturers recorded in DICOM attribute (0008,0070) — Manufacturer. Multiple values may be provided. |
| Image Body Part / Structure | 🟢 | `eucaim:hasImageBodyPart` | `eucaim:BP1000024` | `1..n` **M** | Anatomical areas captured in the images. | Values MUST be selected from the subclasses of [`eucaim:BP1000024` — Body structure](https://hyperontology.eucaim.cancerimage.eu/#BP1000024). The most specific applicable body structure SHOULD be used. Multiple values may be provided. |
| Image Acquisition Period | — | `dct:temporal` | `dct:PeriodOfTime` | `0..n` **R** | Temporal period covered by image acquisition dates in the Dataset. | Describe the interval using `dcat:startDate` and/or `dcat:endDate`. Approximate dates may be used when exact dates are unavailable after anonymisation. |

## Annotations

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Segmentation Label | 🟢 | `eucaim:hasAnnotationLabel` | `rdfs:Resource` | `0..n` **O** | An ontology-defined entity represented by a segmentation, such as an anatomical structure, pathological structure, lesion, clinical finding, imaging-derived region, or other segmentation target. | Values MUST be selected from the [EUCAIM Segmentation Label value set](../controlled-vocabularies/segmentation-labels.csv). The value set contains approved anatomical, clinical, pathological, and imaging-related concepts from the EUCAIM Hyper-Ontology. Values MUST be supplied as canonical ontology IRIs. The most specific applicable concept SHOULD be used. Multiple values may be provided. |
| Segmentation Method | 🟢 | `eucaim:hasAlgorithmType` | `eucaim:COM1001204` | `0..n` **O** | Method used to generate a segmentation, such as manual, automatic, or semi-automatic. | Values MUST be selected from the subclasses of [`eucaim:COM1001204` — Segmentation Method](https://hyperontology.eucaim.cancerimage.eu/#COM1001204). Multiple values may be provided when the Dataset contains segmentations produced using different methods. |
| Number of Segmentations | 🟢 | `eucaim:nbrOfSegmentations` | `xsd:nonNegativeInteger` | `0..1` **O** | Total number of annotated imaging studies in the Dataset. | Each segmented DICOM Study is counted once. |

## Keywords, Provenance, Standards, and Coding

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Keyword | — | `dcat:keyword` | `rdfs:Literal` | `1..n` **M** | A keyword or tag describing the Dataset. | One or more keywords MUST be provided to support Dataset discovery, such as the cancer type, imaging modality, body structure, or annotation type. Each keyword SHOULD be provided as a language-tagged literal. Keywords may be repeated in multiple languages. |
| Provenance | — | `dct:provenance` | `dct:ProvenanceStatement` | `1..n` **M** | Information about how the Dataset was collected, created, or processed. | Provide one or more provenance statements describing how the Dataset was collected, created, derived, curated, or processed, including relevant methodologies, tools, protocols, source datasets, and processing steps. Textual statements SHOULD be language-tagged. |
| Coding System | — | `healthdcatap:hasCodingSystem` | `dct:Standard` | `0..n` **R** | A coding system used in the Dataset. | When provided, values MUST be selected from the [HealthDCAT-AP Coding System controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/coding-system/). Only coding systems actually used in the Dataset SHOULD be specified. Multiple values may be provided. |
| Code Values | — | `healthdcatap:hasCodeValues` | `rdfs:Literal` | `0..n` **R** | Free-text description of relevant code values used in the Dataset. | May be used to list or describe code values represented in the Dataset, for example `ICD-10: C61`. No controlled vocabulary is required for this property. Each code value SHOULD be accompanied by its coding-system identifier when this is not otherwise clear. Multiple values may be provided. |
| Was Generated By | — | `prov:wasGeneratedBy` | `prov:Activity` | `0..n` **O** | An activity that generated, or provides the business context for the creation of, the Dataset. | When provided, the Activity MUST be typed using the Health Activity controlled vocabulary. Multiple Activities may be provided. |
| Activity Type | — | `prov:wasGeneratedBy / dct:type` | `skos:Concept` | `1..1` **C** | Type of Activity that generated the Dataset. **M** when a `prov:wasGeneratedBy` Activity is provided. The value MUST be selected from the [Health Activity controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/health-activity). |
| Conforms To | — | `dct:conformsTo` | `dct:Standard` | `0..n` **O** | An established standard or specification to which the Dataset conforms. | When provided, values MUST be selected from the [HealthDCAT-AP Standard controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/standard/). Use this property only when the Dataset itself conforms to the referenced standard or specification. Standards that apply only to a particular Distribution, file format, metadata record, software implementation, or conceptual mapping SHOULD NOT be specified at Dataset level. Multiple standards may be provided when the Dataset conforms to each of them. |

## Custodian

The optional `geodcatap:custodian` value is an Agent that accepts accountability for the care and maintenance of the Dataset. The custodian may differ from the publisher.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Custodian | — | `geodcatap:custodian` | `foaf:Agent` | `0..1` **R** | Party that accepts accountability and responsibility for the Dataset. | In the EHDS context, the Custodian may represent the legally defined health data holder. The Custodian may differ from the Publisher. |
| Custodian Name | — | `geodcatap:custodian / foaf:name` | `rdfs:Literal` | `1..n` **C** | Name of the Custodian. **M** when a Custodian is provided. May be repeated for different languages. |
| Custodian Type | — | `geodcatap:custodian / dct:type` | `skos:Concept` | `0..1` **O** | Type of the Custodian Agent. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable Agent type SHOULD be used. |
| Custodian Contact Point | — | `geodcatap:custodian / cv:contactPoint` | `cv:ContactPoint` | `1..1` **C** | Contact information for the Custodian. **M** when a Custodian is provided. At least one contact page or email MUST be supplied. |
| Custodian Contact Page | — | `geodcatap:custodian / cv:contactPoint / cv:contactPage` | `foaf:Document` | `0..n` **C** | A web page through which the Custodian can be contacted. | At least one Custodian Contact Page or Custodian Email MUST be provided. |
| Custodian Email | — | `geodcatap:custodian / cv:contactPoint / cv:email` | `rdfs:Literal` | `0..n` **C** | An electronic address through which the Custodian can be contacted. | At least one Custodian Contact Page or Custodian Email MUST be provided. |
| Custodian Telephone | — | `geodcatap:custodian / cv:contactPoint / cv:telephone` | `rdfs:Literal` | `0..n` **O** | Telephone number through which the Custodian can be contacted. | The value SHOULD include the international country code. |
| Custodian Availability Restriction | — | `geodcatap:custodian / cv:contactPoint / cv:specialOpeningHoursSpecification` | `dct:PeriodOfTime` | `0..n` **O** | The time during which the Contact Point is not available. | When provided, the Temporal Entity MUST have at least one human-readable description. For example, `"Closed on weekends"@en`. |
| Availability Restriction Description | — | `geodcatap:custodian / cv:contactPoint / cv:specialOpeningHoursSpecification / dct:description` | `rdfs:Literal` | `1..n` **C** | A textual representation of the availability restriction. **M** when a Custodian Availability Restriction is provided. May be repeated for different languages. |
| Availability Restriction Frequency | — | `geodcatap:custodian / cv:contactPoint / cv:specialOpeningHoursSpecification / cv:frequency` | `dct:Frequency` | `0..n` **O** | The recurrence of an instant or period. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). For example, `WEEKLY`. |
| Custodian Opening Hours | — | `geodcatap:custodian / cv:contactPoint / cv:openingHours` | `dct:PeriodOfTime` | `0..n` **O** | The time at which the Contact Point is normally available. | When provided, the Temporal Entity MUST have at least one human-readable description. For example, `"Open Monday to Saturday"@en`. |
| Opening Hours Description | — | `geodcatap:custodian / cv:contactPoint / cv:openingHours / dct:description` | `rdfs:Literal` | `1..n` **C** | A textual representation of the opening hours. **M** when Custodian Opening Hours are provided. May be repeated for different languages. |
| Opening Hours Frequency | — | `geodcatap:custodian / cv:contactPoint / cv:openingHours / cv:frequency` | `dct:Frequency` | `0..n` **O** | The recurrence of an instant or period. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). For example, `DAILY`. |

## Health Data Access Body

A Health Data Access Body is represented as an Agent. Its name and contact point describe the competent body responsible for providing access to the Dataset.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Health Data Access Body | — | `healthdcatap:hdab` | `foaf:Agent` | `1..1` **M** | Health Data Access Body responsible for providing access to the Dataset. | Identify the competent Health Data Access Body responsible for access to the Dataset under the EHDS. During the EHDS transition period, the value may remain temporarily unpopulated where the competent Health Data Access Body has not yet been formally designated or cannot yet be determined. A placeholder organisation MUST NOT be supplied. EUCAIM may populate or update this value centrally once the relevant national or regional Health Data Access Body has been officially identified. |
| Health Data Access Body Name | — | `healthdcatap:hdab / foaf:name` | `rdfs:Literal` | `1..n` **M** | Official name of the Health Data Access Body. | Use the official name of the competent Health Data Access Body. It may be repeated for different language versions. |
| Health Data Access Body Type | — | `healthdcatap:hdab / dct:type` | `skos:Concept` | `0..1` **O** | Nature or category of the Health Data Access Body. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable concept SHOULD be used. |
| Health Data Access Body Contact Point | — | `healthdcatap:hdab / cv:contactPoint` | `cv:ContactPoint` | `1..1` **M** | Contact information through which the Health Data Access Body can be reached. | The Contact Point MUST provide at least one contact page or email address. |
| Health Data Access Body Contact Page | — | `healthdcatap:hdab / cv:contactPoint / cv:contactPage` | `foaf:Document` | `0..n` **C** | Webpage through which the Health Data Access Body can be contacted. | A Contact Page or Email MUST be provided. Prefer the official webpage, access-application portal, helpdesk, or contact form of the Health Data Access Body. |
| Health Data Access Body Email | — | `healthdcatap:hdab / cv:contactPoint / cv:email` | `rdfs:Literal` | `0..n` **C** | Email address through which the Health Data Access Body can be contacted. | A Contact Page or Email MUST be provided. Supply the official functional email address of the Health Data Access Body. |
| Health Data Access Body Telephone | — | `healthdcatap:hdab / cv:contactPoint / cv:telephone` | `rdfs:Literal` | `0..n` **O** | Telephone number through which the Health Data Access Body can be contacted. | Include the international country code where applicable. |
| Health Data Access Body Availability Restriction | — | `healthdcatap:hdab / cv:contactPoint / cv:specialOpeningHoursSpecification` | `dct:PeriodOfTime` | `0..n` **O** | Time during which the Contact Point is not available. | When provided, the Temporal Entity MUST have at least one human-readable description, for example `"Closed on public holidays"@en`. |
| Availability Restriction Description | — | `healthdcatap:hdab / cv:contactPoint / cv:specialOpeningHoursSpecification / dct:description` | `rdfs:Literal` | `1..n` **C** | Human-readable description of the availability restriction. | MUST be provided when a Health Data Access Body Availability Restriction is supplied. It may be repeated for different languages. |
| Availability Restriction Frequency | — | `healthdcatap:hdab / cv:contactPoint / cv:specialOpeningHoursSpecification / cv:frequency` | `dct:Frequency` | `0..n` **O** | Recurrence of the availability restriction. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). |
| Health Data Access Body Opening Hours | — | `healthdcatap:hdab / cv:contactPoint / cv:openingHours` | `dct:PeriodOfTime` | `0..n` **O** | Time during which the Contact Point is normally available. | When provided, the Temporal Entity MUST have at least one human-readable description, for example `"Monday to Friday, 09:00–17:00"@en`. |
| Opening Hours Description | — | `healthdcatap:hdab / cv:contactPoint / cv:openingHours / dct:description` | `rdfs:Literal` | `1..n` **C** | Human-readable description of the opening hours. | MUST be provided when Health Data Access Body Opening Hours are supplied. It may be repeated for different languages. |
| Opening Hours Frequency | — | `healthdcatap:hdab / cv:contactPoint / cv:openingHours / cv:frequency` | `dct:Frequency` | `0..n` **O** | Recurrence of the opening-hours period. | When provided, the value MUST be selected from the [EU Frequency authority table](http://publications.europa.eu/resource/authority/frequency). |

> [!NOTE]
> The Health Data Access Body is a mandatory HealthDCAT-AP property. However, during the EHDS transition period, the competent body may not yet have been formally designated or made publicly identifiable. EUCAIM may therefore accept a Dataset record with this value temporarily unpopulated during onboarding. Such a record does not fully satisfy this HealthDCAT-AP requirement until the competent Health Data Access Body has been added.

## Creator

The optional `dct:creator` value is an Agent responsible for producing the Dataset.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Creator | — | `dct:creator` | `foaf:Agent` | `0..n` **O** | Agent responsible for producing the Dataset. | Multiple Creators may be supplied. |
| Creator Name | — | `dct:creator / foaf:name` | `rdfs:Literal` | `1..n` **C** | Name of an entity responsible for producing the Dataset. | MUST be provided for each Creator. The name may be repeated using language-tagged literals for different language versions. |
| Creator Contact Page | — | `dct:creator / foaf:homepage` | `rdfs:Resource` | `0..n` **O** | Contact page or homepage of the Creator. | When a Creator is provided, at least one Creator Contact Page or Creator Email SHOULD also be provided. The contact page SHOULD be a stable webpage or web form through which the Creator can be contacted. |
| Creator Email | — | `dct:creator / foaf:mbox` | `rdfs:Resource` | `0..n` **O** | Email address through which the Creator can be contacted. | Use a `mailto:` URI. |
| Creator Type | — | `dct:creator / dct:type` | `skos:Concept` | `0..1` **O** | Type of the Agent that produced the Dataset. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable Agent type SHOULD be used. |

## Dates and Versioning

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Release Date | — | `dct:issued` | `rdfs:Literal` | `0..1` **O** | Date of formal issuance or publication of the Dataset. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. The most precise datatype supported by the available information SHOULD be used. This property represents the Dataset’s formal issuance or publication date, not the data-collection or image-acquisition period. |
| Has Version | — | `dcat:hasVersion` | `dcat:Dataset` | `0..n` **O** | A related Dataset that is a version, edition, or adaptation of the described Dataset. | Use to link the described Dataset to another Dataset that is a version, edition, or adaptation of it. The related Dataset MUST be identified using a stable URI. Multiple related versions may be provided. |
| Modification Date | — | `dct:modified` | `rdfs:Literal` | `0..1` **O** | Most recent date on which the Dataset was changed. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. The most precise datatype supported by the available information SHOULD be used. This property records the most recent date on which the Dataset was changed. |
| Version Notes | — | `adms:versionNotes` | `rdfs:Literal` | `0..n` **O** | Description of differences between this version and a previous version. | Provide a concise, human-readable summary of the changes made since the previous Dataset version. The value SHOULD be language-tagged and MAY be repeated for different language versions. |
| Other Identifier | — | `adms:identifier` | `adms:Identifier` | `0..n` **O** | A secondary identifier of the Dataset. | May be used to provide a secondary identifier, such as a DOI, EZID, W3ID, or the original source-system identifier. The identifier value and its issuing or schema agency SHOULD be specified. Multiple identifiers may be provided. |

## Other and Optional Properties

| Property | EUCAIM Change | Property IRI | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Language | — | `dct:language` | `dct:LinguisticSystem` | `0..n` **R** | A language of the Dataset. | Values MUST be selected from the [EU Vocabularies Language Named Authority List](http://publications.europa.eu/resource/authority/language). Use this property to indicate the languages of the Dataset content. Multiple values may be provided. |
| Frequency | — | `dct:accrualPeriodicity` | `dct:Frequency` | `0..1` **R** | Frequency at which the Dataset is updated. | When provided, the value MUST be selected from the [EU Vocabularies Frequency Authority Table](http://publications.europa.eu/resource/authority/frequency). The value indicates how often the Dataset is updated. |
| Landing Page | — | `dcat:landingPage` | `foaf:Document` | `0..n` **R** | A webpage providing access to the Dataset, its Distributions, or additional information. | The value SHOULD identify a landing page maintained by the original data provider that provides access to the Dataset, its Distributions, and/or additional information. It SHOULD NOT be used for a direct file-download URL. Multiple landing pages may be provided. |
| Source | — | `dct:source` | `dcat:Dataset` | `0..n` **O** | A related Dataset from which the described Dataset is derived. | Use to identify a Dataset from which the described Dataset was derived. The source Dataset SHOULD be identified using a stable URI. Multiple source Datasets may be provided. |
| Is Referenced By | — | `dct:isReferencedBy` | `rdfs:Resource` | `0..n` **O** | A resource, such as a publication, that references or cites the Dataset. | Use to identify a resource that references, cites, or otherwise points to the Dataset. The resource SHOULD be identified using a stable URI; a DOI URI SHOULD be used for scholarly publications when available. Multiple referencing resources may be provided. |
| Sample | — | `adms:sample` | `dcat:Distribution` | `0..n` **R** | A sample Distribution of the Dataset. | Use to link the Dataset to a sample Distribution. The sample MAY contain anonymised or synthetic data. When provided, the sample MUST be described according to the EUCAIM Sample Distribution specification. Multiple sample Distributions may be provided. |
| Analytics | — | `healthdcatap:analytics` | `dcat:Distribution` | `0..n` **R** | An analytics Distribution associated with the Dataset. | Use to link the Dataset to an analytics Distribution containing or providing access to associated resources, such as technical reports, quality measurements, usability indicators, or analytical results. When provided, the analytics resource MUST be described as a `dcat:Distribution`. Multiple analytics Distributions may be provided. |
| Spatial Resolution | — | `dcat:spatialResolutionInMeters` | `xsd:decimal` | `0..1` **O** | Minimum spatial separation resolvable in the Dataset, measured in metres. | The value SHOULD represent the smallest spatial sampling interval present in the medical images and MUST be expressed in metres. It SHOULD be derived from the relevant DICOM pixel or voxel spacing metadata. When spatial spacing varies across studies, series, images, or dimensions, the smallest value SHOULD be reported. This property provides a discovery-level Dataset summary and does not replace detailed in-plane and through-plane spacing information in the DICOM metadata. |
| Temporal Resolution | — | `dcat:temporalResolution` | `xsd:duration` | `0..1` **O** | Minimum time period resolvable in the Dataset. | The value MUST use the `xsd:duration` lexical format and SHOULD represent the shortest temporal interval distinguishable in the Dataset, such as the interval between image frames, acquisitions, or longitudinal observations. Examples include `PT1S` for one second and `P1D` for one day. This property provides a discovery-level Dataset summary and does not replace detailed temporal information in the DICOM metadata. |
| Related Resource | — | `dct:relation` | `rdfs:Resource` | `0..n` **O** | A related resource. | Use to link the Dataset to a related resource only when no more specific relationship property applies. More specific properties, such as `dct:source`, `dct:conformsTo`, `dct:isReferencedBy`, or `dcat:hasVersion`, SHOULD be preferred when applicable. The related resource SHOULD be identified using a stable URI. Multiple related resources may be provided. |
| Quality Annotation | — | `dqv:hasQualityAnnotation` | `dqv:QualityCertificate` | `0..n` **R** | A quality annotation associating the Dataset with a resource that certifies its quality. | Use `dqv:inDimension` to identify the quality dimension assessed by the certificate. EUCAIM quality certificates and associated quality dimensions are not yet formally defined and remain work in progress. |

## Qualified Attribution

A Dataset may have zero or more qualified attributions. Each attribution links the Dataset to an Agent and identifies the Agent's role with respect to the Dataset.

Qualified attribution SHOULD be used when the relationship does not correspond to a more specific property such as `dct:creator`, `dct:publisher`, or the EUCAIM custodian property.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Qualified Attribution | — | `prov:qualifiedAttribution` | `prov:Attribution` | `0..n` **O** | An attribution describing an Agent having responsibility for the Dataset. | Each Attribution MUST identify an Agent using `prov:agent` and MUST identify the Agent's role using `dcat:hadRole`. |
| Qualified Attribution Agent | — | `prov:qualifiedAttribution / prov:agent` | `prov:Agent` | `1..1` **C** | Agent having responsibility for the Dataset within the qualified attribution. | MUST be provided when a Qualified Attribution is supplied. The Agent SHOULD be identified using a stable URI where available. |
| Qualified Attribution Agent Name | — | `prov:qualifiedAttribution / prov:agent / foaf:name` | `rdfs:Literal` | `1..n` **C** | Name of the Agent. | MUST be provided when a Qualified Attribution Agent is described. It may be repeated for different language versions. |
| Qualified Attribution Agent Description | — | `prov:qualifiedAttribution / prov:agent / dct:description` | `rdfs:Literal` | `0..n` **O** | Description of the Agent. | The description MAY be repeated for different languages. |
| Qualified Attribution Agent Type | — | `prov:qualifiedAttribution / prov:agent / dct:type` | `skos:Concept` | `0..1` **O** | Type of the Agent. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). |
| Qualified Attribution Agent Email | — | `prov:qualifiedAttribution / prov:agent / foaf:mbox` | `rdfs:Resource` | `0..1` **O** | Contact email address of the Agent. | The value MUST be expressed as a `mailto:` URI. |
| Qualified Attribution Agent Homepage | — | `prov:qualifiedAttribution / prov:agent / foaf:homepage` | `foaf:Document` | `0..1` **O** | Homepage or contact page of the Agent. | Provide a stable URI maintained by or on behalf of the Agent. |
| Qualified Attribution Agent Role | — | `prov:qualifiedAttribution / dcat:hadRole` | `dcat:Role` | `1..n` **C** | Function or role of the Agent with respect to the Dataset. | When a Qualified Attribution is provided, at least one role MUST be selected from the [ISO 19115 `CI_RoleCode` controlled vocabulary](https://schemas.isotc211.org/resources/codelists/ISO19115-1.1.cit.CI-RoleCode/). Multiple roles MAY be provided where applicable. A more specific relationship property, such as `dct:creator` or `dct:publisher`, SHOULD be used when available. |

## Qualified Relation

A Dataset may have zero or more qualified relations. Each qualified relation identifies one or more related resources and describes their role with respect to the Dataset.

Qualified relation SHOULD be used when the nature of the relationship is known but does not correspond to a more specific DCTERMS or PROV-O property.

| Property | EUCAIM Change | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Qualified Relation | — | `dcat:qualifiedRelation` | `dcat:Relationship` | `0..n` **O** | Description of a qualified relationship between the Dataset and another resource. | Use only when no more specific DCTERMS or PROV-O relationship property applies. |
| Qualified Relation Resource | — | `dcat:qualifiedRelation / dct:relation` | `rdfs:Resource` | `1..n` **C** | Resource related to the Dataset through the qualified relationship. **M** when a Qualified Relation is provided. The related resource SHOULD be identified using a stable URI. Multiple related resources MAY be included when they have the same role with respect to the Dataset. |
| Qualified Relation Role | — | `dcat:qualifiedRelation / dcat:hadRole` | `dcat:Role` | `1..n` **C** | Role of the related resource with respect to the Dataset. **M** when a Qualified Relation is provided. Values SHOULD be selected from a recognised controlled vocabulary of relationship roles, such as the [IANA Link Relation Types](https://www.iana.org/assignments/link-relations/link-relations.xhtml), ISO 19115 `DS_AssociationTypeCode`, the DataCite relation types, or MARC relators. |

