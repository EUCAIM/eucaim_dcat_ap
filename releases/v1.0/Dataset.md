
# Dataset

## Overview

The **Dataset** is the core entity of the EUCAIM DCAT Application Profile. It represents a collection of cancer imaging data and associated metadata published through the EUCAIM Catalogue.

The EUCAIM DCAT-AP extends **DCAT-AP v3** and **HealthDCAT-AP Release 5** by introducing additional metadata elements required for the discovery, understanding and reuse of cancer imaging datasets in the context of cancer imaging research.

This specification corresponds to **EUCAIM DCAT-AP v1.0**.

---

## Legend

The **EUCAIM Modification** column identifies structural or conformance-level differences from HealthDCAT-AP.

| Symbol | EUCAIM Modification | Description |
|---|---|---|
| 🟢 | **Added** | Property introduced by the EUCAIM DCAT Application Profile and not defined for the Dataset in HealthDCAT-AP. |
| 🟠 | **Modified** | HealthDCAT-AP property for which EUCAIM changes the property IRI, range, cardinality, or requirement level. |
| — | **Inherited** | Property inherited with the same IRI, range, cardinality, and requirement level. EUCAIM-specific explanations, examples, and implementation guidance may be added to the Usage Notes without changing its inherited status. |


The occurrence notation combines cardinality and requirement level:

| Code | Meaning |
|---|---|
| **M** | Mandatory — the property MUST be provided. |
| **R** | Recommended — the property SHOULD be provided. |
| **C** | Conditional — the property MUST be provided when the condition in its Usage Notes applies; otherwise, it MAY be omitted. |
| **O** | Optional — the property MAY be provided. |


# Identification

The Identification section contains the metadata required to uniquely identify a Dataset and provide the basic information necessary for its discovery.

| Property | EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Identifier** | 🟠 **Modified** | `dct:identifier` | `rdfs:Literal` | `1..1` **M** | A unique identifier for the Dataset, i.e. the URI in the context of the EUCAIM Public Catalogue (in compliance with the findability aspect of the FAIR principles). | For HealthDCAT-AP the identifier is mandatory and must be unique within the originating catalogue. When a Dataset is published through the EUCAIM Catalogue, the original identifier becomes the value of **Other Identifier**, while the EUCAIM Catalogue assigns a new identifier. |
| **Other Identifier** | — | `adms:identifier` | `adms:Identifier` |  `0..n` **O** | A secondary identifier of the Dataset. | Examples include DOI, DataCite, EZID, W3ID or any identifier assigned by the originating repository. This property preserves the original identifier assigned before publication in the EUCAIM Catalogue. |
| **Title** | — | `dct:title` | `rdfs:Literal` |   `1..n` **M** | A clear and concise name given to the Dataset. | The property may be repeated in multiple languages. An English title is mandatory. |
| **Description** | — | `dct:description` | `rdfs:Literal` |   `1..n` **M** | A detailed description of the Dataset, including its content, purpose and scope. | The property may be repeated in multiple languages. An English description is mandatory. |
| **Documentation** | — | `foaf:page` | `foaf:Document` |  `0..n` **R** | A page or document describing the Dataset. | Use this property for user guides, technical documentation, protocols or publications related to the Dataset. |
| **Interoperability Tier** | 🟢 **Added** | `eucaim:interoperabilityLevel` | `eucaim:SPEC1000008` |  `1..1` **M** | The EUCAIM data federation and interoperability tier the specific dataset belongs to. | EUCAIM controlled vocabulary (One of “Tier 1”, “Tier 2”, “Tier 3”, “Tier 1A+”, “Tier 1C+”, “Tier 2A+”,”Tier 2C+”, “Tier 3A+”, “Tier3C+“). |
| **Dataset Distribution** | — | `dcat:distribution` | `dcat:Distribution` |   `1..n` **M** | An available Distribution of the Dataset. | At least one Distribution MUST be provided, independently of the Dataset's access rights. |

---

# Classification

The Classification section describes how the Dataset is categorised using DCAT-AP, HealthDCAT-AP and EUCAIM controlled vocabularies.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Theme** | 🟠 **Modified** | `dcat:theme` | `skos:Concept` |  `1..1` **M** | The thematic category of the Dataset. | Fixed to the Publications Office Data Theme **Health** (`http://publications.europa.eu/resource/authority/data-theme/HEAL`). |
| **Health Category** | —  | `healthdcatap:healthCategory` | `skos:Concept` |   `1..n` **M** | The EHDS category to which the Dataset belongs. | Use the controlled vocabulary defined under Article 51 of the EHDS Regulation. Multiple categories may be assigned where appropriate. |
| **Health Theme** | — | `healthdcatap:healthTheme` | `skos:Concept` |  `0..n` **R**| A health topic associated with the Dataset. | Multiple health themes may be assigned. For EUCAIM the default value is **Cancer**. |
| **Type** | 🟠 **Modified** | `dct:type` | `eucaim:SPEC1000017`, `dpv:Data` |   `1..n` **M** | The type of Dataset. | Use one or more EUCAIM Dataset Types (e.g. Original Dataset, Annotated Dataset, Processed Dataset) together with applicable concepts from the DPV Data taxonomy (e.g. Personal Data, Pseudonymised Data, Synthetic Data). |
| **Keyword** |  —  | `dcat:keyword` | `rdfs:Literal` |   `1..n` **M** | Keywords describing the Dataset. | Include meaningful keywords to improve discoverability. Keywords may be repeated in multiple languages. Example: *Prostate Cancer*, *mpMRI*. |
| **Language** |  —  | `dct:language` | `dct:LinguisticSystem` |  `0..n` **R** | Language(s) used within the Dataset. | Values should be taken from the EU Vocabularies Languages Named Authority List. Repeat this property if multiple languages are represented. |
| **Alternative** | — | `dct:alternative` | `rdfs:Literal` |  `0..n` **O** | An alternative name for the Dataset. | May be repeated for alternative names or parallel language versions. Language-tagged literals SHOULD be used. |

---
# Responsible Parties

The Responsible Parties section describes organisations or individuals involved in creating, publishing or contributing to the Dataset.

## Contact Point

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Contact Point** |  —  | `dcat:contactPoint` | `vcard:Kind` |   `1..n` **M** | Contact point for questions regarding the Dataset. | At least one contact mechanism must be provided, either an email address or a contact webpage. |

## Creator

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Creator** | — | `dct:creator` | `foaf:Agent` |  `0..n` **O** | Organisation or individual responsible for creating the Dataset. | The property may be repeated for multiple creators. |
| **Creator Name** | — | `dct:creator / foaf:name` | `rdfs:Literal` |   `1..n` **C** | Name of the Creator. | Mandatory for each Creator. It may be repeated for multilingual names. |
| **Creator Type** |  —  | `dct:creator / dct:type` | `skos:Concept` | `0..1` **R** | Type of creator. | If the organisation exists in the EU Corporate Bodies Authority List, use the corresponding concept. |

## Publisher

The Publisher section describes the organisation responsible for making the Dataset available and provides the information required to contact that organisation.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| Publisher | 🟠 **Modified**  | `dct:publisher` | `foaf:Agent` | `1..1` **M**| Agent responsible for making the Dataset available. | The Publisher may be the health data holder or another organisation, such as a data intermediation entity. |
| **Publisher Name** | — | `dct:publisher / foaf:name` | `rdfs:Literal` |   `1..n` **M** | The organisation responsible for making the Dataset available. | This is typically the data holder responsible for ensuring that the Dataset can be accessed and reused. Provide the official name of the organisation. |
| **Publisher Contact Point** | — | `dct:publisher / dcat:contactPoint` | `vcard:Kind` |  `1..1` **M** | Contact information for the Publisher. | Provide at least one email address or contact webpage. |
| **Publisher Type** |  —  | `dct:publisher / dct:type` | `skos:Concept` | `0..1` **R** | The type of organisation publishing the Dataset. | Recommended values include: Research Institute, Hospital or Healthcare System Repository, European Project, Cancer Screening Programme, Patient Association, Data Altruism Organisation, ERIC and EDIC. |
| **Publisher Note** |  —  | `dct:publisher / dct:description` | `rdfs:Literal` |  `0..n` **R** | A description of the publisher and its activities. | This property may be repeated for multiple language versions. It should provide information relevant to the publisher in the context of the Dataset. |
| **Publisher Trusted Data Holder** | — | `dct:publisher / healthdcatap:trustedDataHolder` | `xsd:boolean` | `0..1` **O**  | Indicates whether the Publisher is a trusted health data holder. | Use `true` when the Publisher is recognised as a trusted health data holder and `false` when it is not. |

## Health Data Access Body

A Health Data Access Body is represented as an Agent. Its name and contact point describe the competent body responsible for providing access to the Dataset.

| Property | EUCAIM Modification | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| Health Data Access Body | — | `healthdcatap:hdab` | `foaf:Agent` | `1..1` **M**  | Health Data Access Body responsible for providing access to the Dataset. | Identify the competent Health Data Access Body responsible for access to the Dataset under the EHDS. During the EHDS transition period, the value may remain temporarily unpopulated where the competent Health Data Access Body has not yet been formally designated or cannot yet be determined. A placeholder organisation MUST NOT be supplied. EUCAIM may populate or update this value centrally once the relevant national or regional Health Data Access Body has been officially identified. |
| Health Data Access Body Name | — | `healthdcatap:hdab / foaf:name` | `rdfs:Literal` |  `1..n` **M** | Official name of the Health Data Access Body. | Use the official name of the competent Health Data Access Body. It may be repeated for different language versions. |
| Health Data Access Body Type | — | `healthdcatap:hdab / dct:type` | `skos:Concept` | `0..1` **O** | Nature or category of the Health Data Access Body. | When provided, the value MUST be selected from the [HealthDCAT-AP Publisher Type controlled vocabulary](https://hdeu-dcat.acceptance.data.health.europa.eu/resource/authority/publisher-type/). The most specific applicable concept SHOULD be used. |
| Health Data Access Body Contact Point | — | `healthdcatap:hdab / dcat:contactPoint` | `vcard:Kind` | `1..1` **M** | Contact information through which the Health Data Access Body can be reached. | The Contact Point MUST provide at least one contact page or email address. |

## Qualified Attribution

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Qualified Attribution** | — | `prov:qualifiedAttribution` | `prov:Attribution` |  `0..n` **O** | A qualified attribution linking the Dataset to an Agent and its role. | Each Attribution MUST identify an Agent and a role. |
| **Qualified Attribution Agent** | — | `prov:qualifiedAttribution / prov:agent` | `prov:Agent` |  `1..1` **C** | Agent associated with the qualified attribution. | Mandatory for every Attribution. |
| **Qualified Attribution Agent Name** | — | `prov:qualifiedAttribution / prov:agent / foaf:name` | `rdfs:Literal` |   `1..n` **C** | Name of the attributed Agent. | Mandatory for each Agent and repeatable for language versions. |
| **Qualified Attribution Agent Role** | — | `prov:qualifiedAttribution / dcat:hadRole` | `dcat:Role` |  `1..n` **C** | Role of the Agent with respect to the Dataset. | Use an applicable recognised role vocabulary. |



---

# Access & Rights

The Access & Rights section specifies how the Dataset can be accessed, the legal framework governing its use, and the purposes for which it was collected and may be reused.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Access Rights** |  —  | `dct:accessRights` | `dct:RightsStatement` |  `1..1` **M** | Indicates whether the Dataset is publicly accessible, restricted or non-public. | Use one of the Publications Office controlled values: **PUBLIC**, **RESTRICTED** or **NON_PUBLIC**. This property is mandatory in HealthDCAT-AP. |
| **Applicable Legislation** |  —  | `dcatap:applicableLegislation` | `eli:LegalResource` |   `1..n` **M** | The legislation mandating the creation or management of the Dataset. | Include the ELI of the EHDS Regulation (`http://data.europa.eu/eli/reg/2025/327/oj`). Additional legislation may also be provided where applicable. |
| **Purpose** |  —  | `dpv:hasPurpose` | `dpv:Purpose` |  `0..n` **R**  | The primary purpose for which the Dataset was created. | Values should preferably come from the DPV Purpose taxonomy (e.g. `dpv:ResearchAndDevelopment`). Free-text descriptions may also be provided when necessary. |
| **Legal Basis** |  —  | `dpv:hasLegalBasis` | `dpv:LegalBasis` |  `0..n` **R**  | The legal basis used for the collection and processing of the underlying data. | This property describes the legal basis for processing personal data and is distinct from **Applicable Legislation**, which refers to legislation governing publication of the Dataset. The legal basis can be provided as a value from the dpv taxonomy (https://w3c-cg.github.io/dpv/2.0/dpv/modules/legal_basis.html#vocab-legal-basis). Example values include `dpv:Consent`. |
| **Retention Period** |  —  | `healthdcatap:retentionPeriod` | `dct:PeriodOfTime` | `0..1` **R** | The period during which the Dataset is available for secondary use. | The interval may specify a start date, an end date or both. Open intervals are permitted. |
| **Personal Data** |  —  | `dpv:hasPersonalData` | `dpv:PersonalData` |  `0..n` **R** | Types of personal data represented within the Dataset. | Use concepts from the DPV Personal Data taxonomy (e.g. Birth Date, Age, Gender) to describe the underlying data rather than the metadata record. |

---

# Population

The Population section describes the individuals represented in the Dataset and provides summary information about the study population.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Number of Unique Individuals** | 🟠 **Modified**  | `healthdcatap:numberOfUniqueIndividuals` | `xsd:nonNegativeInteger` |  `1..1` **M** | Total number of unique individuals represented in the Dataset. | Provide the exact number whenever possible. If unavailable, a well-founded estimate may be provided. |
| **Birth Sex** | 🟢 **Added** | `eucaim:hasBirthSex` | `eucaim:COM1001396` |   `1..n` **M** | Birth sex represented within the Dataset. | Use the EUCAIM controlled vocabulary based on subclasses of **Sex assigned at birth**. Multiple values may be provided. |
| **Cancer Condition** | 🟢 **Added** | `eucaim:hasCondition` | `eucaim:CLIN1007977` |  `1..1` **M** | Primary cancer condition represented in the Dataset. | Use the EUCAIM controlled vocabulary based on ICD-10 malignant neoplastic diseases. If only metastatic disease is known, provide the appropriate metastatic concept. |
| **Minimum Typical Age** |  —  | `healthdcatap:minTypicalAge` | `xsd:nonNegativeInteger` | `0..1` **R** | Approximate minimum age of individuals represented in the Dataset. | Approximate values are preferred to reduce disclosure risk. |
| **Maximum Typical Age** |  —  | `healthdcatap:maxTypicalAge` | `xsd:nonNegativeInteger` | `0..1` **R** | Approximate maximum age of individuals represented in the Dataset. | Approximate values are preferred to reduce disclosure risk. |
| **Population Coverage** |  —  | `healthdcatap:populationCoverage` | `rdfs:Literal` |  `0..n` **R** | Free-text description of the population represented in the Dataset. | Describe the study population, for example age range, disease, treatment, geographical area and recruitment period. |


---

# Imaging

The Imaging section describes the imaging characteristics of the Dataset, including the modalities, anatomical regions, acquisition equipment and the scale of the imaging collection.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Number of Imaging Studies** | 🟠 **Modified** | `healthdcatap:numberOfRecords` (maps to `eucaim:nbrOfStudies`) | `xsd:nonNegativeInteger` |  `1..1` **M** | Total number of imaging studies contained in the Dataset (e.g. DICOM Studies). | This property provides an indication of the Dataset size. A single individual may contribute multiple imaging studies acquired at different time points (e.g. diagnosis, treatment, follow-up). |
| **Image Modality** | 🟢 **Added** | `eucaim:hasImageModality` | `eucaim:IMG1000009` |   `1..n` **M** | Imaging modality represented in the Dataset. | Use the EUCAIM controlled vocabulary based on **RadLex** subclasses of *Imaging Modality*. Multiple modalities may be specified. |
| **Image Equipment Manufacturer** | 🟢 **Added** | `eucaim:hasEquipmentManufacturer` | `eucaim:IMG1000010` |   `1..n` **M** | Manufacturer of the imaging equipment. | The value corresponds to the DICOM Manufacturer attribute (0008,0070). Use the EUCAIM controlled vocabulary based on **BirnLex** subclasses of *Manufacturer*. |
| **Image Body Part / Structure** | 🟢 **Added** | `eucaim:hasImageBodyPart` | `eucaim:BP1000024` |   `1..n` **M** | Anatomical structures represented in the imaging studies. | Use the EUCAIM controlled vocabulary based on **ICD-O-3** subclasses of *Body Structure*. Multiple anatomical regions may be specified. |

---

# Annotation

The Annotation section describes image annotations, segmentations and the methods used to generate them.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Segmentation Label** | 🟢 **Added** | `eucaim:hasAnnotationLabel` | `eucaim:BodyStructure` |  `0..n` **R**  | Label identifying an annotated anatomical structure or region. | Use the EUCAIM controlled vocabulary. Organ annotations should reference subclasses of **Body Structure**. |
| **Segmentation Method** | 🟢 **Added** | `eucaim:hasAlgorithmType` | `eucaim:COM1001204` |  `0..n` **R** | Method used to generate the segmentation. | Use the EUCAIM controlled vocabulary. Typical values include Manual, Semi-automatic and Automatic segmentation. |
| **Number of Segmentations** | 🟢 **Added** | `eucaim:nbrOfSegmentations` | `xsd:nonNegativeInteger` | `0..1` **R** | Total number of segmented imaging studies available in the Dataset. | Each segmented DICOM study counts as one segmentation. |

---

# Coverage

The Coverage section describes the temporal, geographical and organisational scope of the Dataset.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Collection Method** | 🟢 **Added** | `eucaim:collectionMethod` | `eucaim:SPEC1000002` |   `1..n` **M** | Defines the scope and aggregation strategy of the Dataset. | Use the EUCAIM controlled vocabulary describing how data records are organised and collected. |
| **Image Acquisition Period** |  —  | `dct:temporal` | `dct:PeriodOfTime` |  `0..n` **R** | Temporal period during which the imaging studies were acquired. | This period should correspond to the DICOM Acquisition Date (0008,0022). If acquisition dates are unavailable due to anonymisation, provide the best possible approximation. |
| **Geographical Coverage** |  —  | `dct:spatial` | `dct:Location` |  `0..n` **R** | Geographic region covered by the Dataset. | Use the EU Vocabularies Named Authority Lists for continents, countries and administrative regions. If no suitable concept exists, use GeoNames URIs. |
| **Spatial Resolution** |  —  | `dcat:spatialResolutionInMeters` | `xsd:decimal` | `0..1` **O** | Minimum spatial separation represented in the Dataset. | For imaging datasets this generally corresponds to image spacing or voxel size. |
| **Temporal Resolution** |  —  | `dcat:temporalResolution` | `xsd:duration` | `0..1` **R** | Minimum temporal interval represented in the Dataset. | Express the value using the `xsd:duration` datatype (ISO 8601 duration format). |
| **Frequency** |  —  | `dct:accrualPeriodicity` | `dct:Frequency` | `0..1` **R** | Frequency at which the Dataset is updated. | Use values from the EU Publications Office Frequency Named Authority List (e.g. Daily, Monthly, Yearly, Irregular). |

---

---

# Standards & Coding

The Standards & Coding section describes the standards, terminologies and coding systems used within the Dataset. These properties improve interoperability and help users understand how information is represented.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Conforms To** |  —  | `dct:conformsTo` | `dct:Standard` |  `0..n` **R** | An established standard or specification to which the Dataset conforms. | Use this property to reference recognised standards, specifications, profiles or implementation guides followed by the Dataset. |
| **Coding System** |  —  | `healthdcatap:hasCodingSystem` | `dct:Standard` |  `0..n` **R** | Coding systems used within the Dataset. | Examples include ICD-10, ICD-10-CM, SNOMED CT, DRGs and other recognised terminologies. |
| **Code Values** |  —  | `healthdcatap:hasCodeValues` | `skos:Concept` |  `0..n` **R** | Classification concepts used in the Dataset. | Associate the Dataset with concepts from controlled vocabularies, ontologies or terminologies to improve discoverability and semantic interoperability. |

---

# Provenance

The Provenance section provides information about how the Dataset was created, processed and maintained.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Provenance** |  —  | `dct:provenance` | `dct:ProvenanceStatement` |   `1..n` **M** | Information describing the origin of the Dataset and how it was produced. | Describe the methodologies, protocols, tools and processing steps used during data collection and preparation. |
| **Was Generated By** |  —  | `prov:wasGeneratedBy` | `prov:Activity` |  `0..n` **O** | Activity responsible for generating the Dataset. | Examples include research projects, surveys, clinical studies or data integration activities. Multiple activities may be recorded to describe different stages of Dataset production. |

---

# Quality

The Quality section provides information about the quality, validation and assessment of the Dataset.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Quality Annotation** |  —  | `dqv:hasQualityAnnotation` | `dqv:QualityCertificate` |  `0..n` **R** | Statement describing the quality of the Dataset. | Quality annotations may include quality certificates, ratings or assessment reports. Within EUCAIM, the assessed quality dimension is identified using `dqv:inDimension`, for example integrity or completeness. |

---

# Relationships

The Relationships section describes links between the Dataset and other resources.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Landing Page** |  —  | `dcat:landingPage` | `foaf:Document` |  `0..n` **R** | A web page providing access to the Dataset, its Distributions or additional information. | This should point to the landing page maintained by the original data holder rather than a third-party catalogue. |
| **Related Resource** |  —  | `dct:relation` | `rdfs:Resource` |  `0..n` **R** | A resource related to the Dataset. | Use this property when another Dataset, Distribution, Data Service or document is related but the nature of the relationship cannot be expressed more specifically. |
| **Is Referenced By** |  —  | `dct:isReferencedBy` | `rdfs:Resource` |  `0..n` **R** | A publication or other resource that references the Dataset. | Examples include scientific publications, technical reports, project websites and documentation. |
| **Sample** |  —  | `adms:sample` | `dcat:Distribution` |  `0..n` **R** | Sample Distribution of the Dataset. | Samples may consist of anonymised data, synthetic data or data dictionaries provided for inspection before requesting access. |
| **Analytics** |  —  | `healthdcatap:analytics` | `dcat:Distribution` |  `0..n` **R** | Analytical resources describing the Dataset. | Typical examples include technical reports, quality reports, summary statistics and usability indicators. |
| **Source** | — | `dct:source` | `dcat:Dataset` |  `0..n` **R** | A related Dataset from which the described Dataset is derived. | Use when the described Dataset is wholly or partly derived from another Dataset. The source Dataset SHOULD be identified using a stable URI. Multiple source Datasets MAY be provided. |

---

## Qualified Relation

A Dataset may have zero or more `dcat:qualifiedRelation` values. Each value is a `dcat:Relationship` that identifies one or more related resources and their role with respect to the Dataset.

| Property | EUCAIM Modification | Property Path | Range | Occurrence | Description | Usage Notes |
|---|---|---|---|---|---|---|
| **Qualified Relation** | — | `dcat:qualifiedRelation` | `dcat:Relationship` |  `0..n` **O** | A qualified relationship between the Dataset and another resource. | Use when the relationship requires an explicit role and no more specific DCTERMS or PROV-O relationship property applies. Each Relationship MUST identify at least one related resource and at least one role. |
| **Qualified Relation Resource** | — | `dcat:qualifiedRelation / dct:relation` | `rdfs:Resource` |   `1..n` **C** | A resource related to the Dataset through the qualified relationship. | Mandatory when a Qualified Relation is provided. The related resource SHOULD be identified using a stable URI. Multiple resources MAY be included when they have the same role. |
| **Qualified Relation Role** | — | `dcat:qualifiedRelation / dcat:hadRole` | `dcat:Role` |   `1..n` **C** | Role of the related resource with respect to the Dataset. | Mandatory when a Qualified Relation is provided. Values SHOULD be selected from a recognised relationship-role vocabulary, such as the IANA Link Relation Types, ISO 19115 `DS_AssociationTypeCode`, DataCite relation types, or MARC relators. |

---

# Dates & Versioning

The Dates & Versioning section records the publication history and lifecycle of the Dataset.

| Property |  EUCAIM Modification | Property IRI | Range | Occurrence | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Version** | 🟠 **Modified** | `dcat:version` | `rdfs:Literal` |  `1..1` **M** | The version of the Dataset. | Version identifiers should follow Semantic Versioning (SemVer) or Calendar Versioning (CalVer). |
| **Version Notes** |  —  | `adms:versionNotes` | `rdfs:Literal` |  `0..n` **O** | A description of the changes introduced in this version of the Dataset. | Describe differences compared with previous versions, such as updated methodology, corrected metadata or additional data. |
| **Release Date** |  —  | `dct:issued` | `rdfs:Literal` | `0..1` **O** | Date on which the Dataset was formally published. | Values should be expressed as `xsd:date`, `xsd:dateTime`, `xsd:gYear` or `xsd:gYearMonth`. |
| **Modification Date** |  —  | `dct:modified` | `rdfs:Literal` | `0..1` **O** | Most recent date on which the Dataset was modified. | Use the same XML Schema temporal datatypes as for the Release Date. |
| **In Series** | — | `dcat:inSeries` | `dcat:DatasetSeries` |  `0..n` **O**  | A Dataset Series of which the Dataset is a member. | Use when the Dataset belongs to a collection of related Datasets published separately, such as a longitudinal, periodic, or versioned series. The Dataset Series SHOULD be identified using a stable URI. Multiple series MAY be provided. |
| **Has Version** | — | `dcat:hasVersion` | `dcat:Dataset` |  `0..n` **O**  | A related Dataset that is a version, edition, or adaptation of the described Dataset. | The related Dataset SHOULD be identified using a stable URI. Multiple related versions MAY be provided. |

---