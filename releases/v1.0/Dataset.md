
# Dataset

## Overview

The **Dataset** is the core entity of the EUCAIM DCAT Application Profile. It represents a collection of cancer imaging data and associated metadata published through the EUCAIM Catalogue.

The EUCAIM DCAT-AP extends **DCAT-AP v3** and **HealthDCAT-AP Release 5** by introducing additional metadata elements required for the discovery, understanding and reuse of cancer imaging datasets in the context of cancer imaging research.

This specification corresponds to **EUCAIM DCAT-AP v1.0**.

---

# Identification

The Identification section contains the metadata required to uniquely identify a Dataset and provide the basic information necessary for its discovery.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Identifier** | EUCAIM DCAT-AP | `dct:identifier` | `rdfs:Literal` | **1..1** | A unique identifier for the Dataset, i.e. the URI in the context of the EUCAIM Public Catalogue (in compliance with the findability aspect of the FAIR principles). | For HealthDCAT-AP the identifier is mandatory and must be unique within the originating catalogue. When a Dataset is published through the EUCAIM Catalogue, the original identifier becomes the value of **Other Identifier**, while the EUCAIM Catalogue assigns a new identifier. |
| **Other Identifier** | DCAT-AP v3 | `adms:identifier` | `adms:Identifier` | **0..n** | A secondary identifier of the Dataset. | Examples include DOI, DataCite, EZID, W3ID or any identifier assigned by the originating repository. This property preserves the original identifier assigned before publication in the EUCAIM Catalogue. |
| **Title** | DCAT-AP v3 | `dct:title` | `rdfs:Literal` | **1..n** | A clear and concise name given to the Dataset. | The property may be repeated in multiple languages. An English title is mandatory. |
| **Description** | DCAT-AP v3 | `dct:description` | `rdfs:Literal` | **1..n** | A detailed description of the Dataset, including its content, purpose and scope. | The property may be repeated in multiple languages. An English description is mandatory. |
| **Documentation** | DCAT-AP v3 | `foaf:page` | `foaf:Document` | **0..n** | A page or document describing the Dataset. | Use this property for user guides, technical documentation, protocols or publications related to the Dataset. |
| **Interoperability Tier** | EUCAIM DCAT-AP | `adms:interoperabilityLevel` | `eucaim:SPEC1000008` | **1..1** | The EUCAIM data federation and interoperability tier the specific dataset belongs to. | EUCAIM controlled vocabulary (One of “Tier 1”, “Tier 2”, “Tier 3”, “Tier 1A+”, “Tier 1C+”, “Tier 2A+”,”Tier 2C+”, “Tier 3A+”, “Tier3C+“). |

---

# Classification

The Classification section describes how the Dataset is categorised using DCAT-AP, HealthDCAT-AP and EUCAIM controlled vocabularies.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Theme** | HealthDCAT-AP | `dcat:theme` | `skos:Concept` | **1..1** | The thematic category of the Dataset. | Fixed to the Publications Office Data Theme **Health** (`http://publications.europa.eu/resource/authority/data-theme/HEAL`). |
| **Health Category** | HealthDCAT-AP | `healthdcatap:healthCategory` | `skos:Concept` | **1..n** | The EHDS category to which the Dataset belongs. | Use the controlled vocabulary defined under Article 51 of the EHDS Regulation. Multiple categories may be assigned where appropriate. |
| **Health Theme** | HealthDCAT-AP | `healthdcatap:healthTheme` | `skos:Concept` | **1..n** | A health topic associated with the Dataset. | Multiple health themes may be assigned. For EUCAIM the default value is **Cancer**. |
| **Type** | EUCAIM DCAT-AP | `dct:type` | `eucaim:DatasetType`, `dpv:Data` | **1..n** | The type of Dataset. | Use one or more EUCAIM Dataset Types (e.g. Original Dataset, Annotated Dataset, Processed Dataset) together with applicable concepts from the DPV Data taxonomy (e.g. Personal Data, Pseudonymised Data, Synthetic Data). |
| **Keyword** | DCAT-AP v3 | `dcat:keyword` | `rdfs:Literal` | **1..n** | Keywords describing the Dataset. | Include meaningful keywords to improve discoverability. Keywords may be repeated in multiple languages. Example: *Prostate Cancer*, *mpMRI*. |
| **Language** | DCAT-AP v3 | `dct:language` | `dct:LinguisticSystem` | **0..n** | Language(s) used within the Dataset. | Values should be taken from the EU Vocabularies Languages Named Authority List. Repeat this property if multiple languages are represented. |

---
# Responsible Parties

The Responsible Parties section describes organisations or individuals involved in creating, publishing or contributing to the Dataset.

## Contact Point

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Contact Point** | DCAT-AP v3 | `dcat:contactPoint` | `vcard:Kind` | **1..n** | Contact point for questions regarding the Dataset. | At least one contact mechanism must be provided, either an email address or a contact webpage. |

## Creator

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Creator Name** | DCAT-AP v3 | `dct:creator` | `foaf:Agent` | **0..n** | Organisation or individual responsible for creating the Dataset. | The property may be repeated for multiple creators and multilingual names. |
| **Creator Contact Point** | DCAT-AP v3 | *(part of `foaf:Agent`)* | `vcard:Kind` | **0..1** | Contact information for the creator. | Provide an email address or webpage through which the creator can be contacted. |
| **Creator Type** | DCAT-AP v3 | `dct:type` | `skos:Concept` | **0..1** | Type of creator. | If the organisation exists in the EU Corporate Bodies Authority List, use the corresponding concept. |
| **Creator Note** | DCAT-AP v3 | `dct:description` | `rdfs:Literal` | **0..1** | Description of the creator and its activities. | Free-text description of the creator's role. |

## Publisher

The Publisher section describes the organisation responsible for making the Dataset available and provides the information required to contact that organisation.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Publisher Name** | EUCAIM DCAT-AP | `dct:publisher` | `foaf:Organization` `(foaf:name)` | **1..1** | The organisation responsible for making the Dataset available. | This is typically the data holder responsible for ensuring that the Dataset can be accessed and reused. Provide the official name of the organisation. |
| **Publisher Contact Point** | EUCAIM DCAT-AP | `dct:publisher` | `foaf:Organization` `(foaf:mbox,foaf:homepage)` | **1..1** | Contact information for the publisher. | Provide either a contact email address or a webpage (e.g. web form) through which the organisation can be contacted. |
| **Publisher Type** | HealthDCAT-AP | `healthdcatap:publisherType` | `skos:Concept` | **0..1** | The type of organisation publishing the Dataset. | Recommended values include: Research Institute, Hospital or Healthcare System Repository, European Project, Cancer Screening Programme, Patient Association, Data Altruism Organisation, ERIC and EDIC. |
| **Publisher Note** | HealthDCAT-AP | `dct:description` | `rdfs:Literal` | **0..1** | A description of the publisher and its activities. | This property may be repeated for multiple language versions. It should provide information relevant to the publisher in the context of the Dataset. |

## Qualified Attribution

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Qualified Attribution Agent Name** | DCAT-AP v3 | `prov:qualifiedAttribution` | `prov:Attribution` | **0..n** | Agent having a specific role with respect to the Dataset. | Use when the relationship between an Agent and the Dataset cannot be represented using standard DCAT properties such as Creator or Publisher. |
| **Qualified Attribution Agent Contact Point** | DCAT-AP v3 | *(part of `prov:Attribution`)* | `vcard:Kind` | **0..1** | Contact information for the attributed Agent. | Provide an email address or webpage where appropriate. |
| **Qualified Attribution Agent Role** | DCAT-AP v3 | `dcat:hadRole` | `skos:Concept` | **1..1** | Function or responsibility of the attributed Agent. | Use values from recognised controlled vocabularies such as ISO 19115 CI_RoleCode. |



---

# Access & Rights

The Access & Rights section specifies how the Dataset can be accessed, the legal framework governing its use, and the purposes for which it was collected and may be reused.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Access Rights** | HealthDCAT-AP | `dct:accessRights` | `dct:RightsStatement` | **1..1** | Indicates whether the Dataset is publicly accessible, restricted or non-public. | Use one of the Publications Office controlled values: **PUBLIC**, **RESTRICTED** or **NON_PUBLIC**. This property is mandatory in HealthDCAT-AP. |
| **Applicable Legislation** | DCAT-AP v3 | `dcatap:applicableLegislation` | `rdfs:Resource` | **1..n** | The legislation mandating the creation or management of the Dataset. | Include the ELI of the EHDS Regulation (`http://data.europa.eu/eli/reg/2025/327/oj`). Additional legislation may also be provided where applicable. |
| **Purpose** | HealthDCAT-AP | `dpv:hasPurpose` | `dpv:Purpose` | **0..n** | The primary purpose for which the Dataset was created. | Values should preferably come from the DPV Purpose taxonomy (e.g. `dpv:ResearchAndDevelopment`). Free-text descriptions may also be provided when necessary. |
| **Legal Basis** | HealthDCAT-AP | `dpv:hasLegalBasis` | `dpv:LegalBasis` | **0..n** | The legal basis used for the collection and processing of the underlying data. | This property describes the legal basis for processing personal data and is distinct from **Applicable Legislation**, which refers to legislation governing publication of the Dataset. The legal basis can be provided as a value from the dpv taxonomy (https://w3c-cg.github.io/dpv/2.0/dpv/modules/legal_basis.html#vocab-legal-basis). Example values include `dpv:Consent`. |
| **Retention Period** | HealthDCAT-AP | `healthdcatap:retentionPeriod` | `xsd:duration` | **0..1** | The period during which the Dataset is available for secondary use. | The interval may specify a start date, an end date or both. Open intervals are permitted. |
| **Personal Data** | HealthDCAT-AP | `dpv:hasPersonalData` | `dpv:PersonalData` | **0..n** | Types of personal data represented within the Dataset. | Use concepts from the DPV Personal Data taxonomy (e.g. Birth Date, Age, Gender) to describe the underlying data rather than the metadata record. |

---

# Population

The Population section describes the individuals represented in the Dataset and provides summary information about the study population.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Number of Unique Individuals** | EUCAIM DCAT-AP | `healthdcatap:numberOfUniqueIndividuals` | `xsd:nonNegativeInteger` | **1..1** | Total number of unique individuals represented in the Dataset. | Provide the exact number whenever possible. If unavailable, a well-founded estimate may be provided. |
| **Minimum Typical Age** | HealthDCAT-AP | `healthdcatap:minTypicalAge` | `xsd:nonNegativeInteger` | **0..1** | Approximate minimum age of individuals represented in the Dataset. | Approximate values are preferred to reduce disclosure risk. |
| **Maximum Typical Age** | HealthDCAT-AP | `healthdcatap:maxTypicalAge` | `xsd:nonNegativeInteger` | **0..1** | Approximate maximum age of individuals represented in the Dataset. | Approximate values are preferred to reduce disclosure risk. |
| **Birth Sex** | EUCAIM DCAT-AP | `eucaim:hasBirthSex` | `eucaim:COM1001396` | **1..n** | Birth sex represented within the Dataset. | Use the EUCAIM controlled vocabulary based on subclasses of **Sex assigned at birth**. Multiple values may be provided. |
| **Population Coverage** | HealthDCAT-AP | `healthdcatap:populationCoverage` | `rdfs:Literal` | **0..n** | Free-text description of the population represented in the Dataset. | Describe the study population, for example age range, disease, treatment, geographical area and recruitment period. |
| **Cancer Condition** | EUCAIM DCAT-AP | `eucaim:hasCondition` | `eucaim:MalignantNeoplasticDisease` | **1..1** | Primary cancer condition represented in the Dataset. | Use the EUCAIM controlled vocabulary based on ICD-10 malignant neoplastic diseases. If only metastatic disease is known, provide the appropriate metastatic concept. |

---

---

# Imaging

The Imaging section describes the imaging characteristics of the Dataset, including the modalities, anatomical regions, acquisition equipment and the scale of the imaging collection.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Number of Imaging Studies** | EUCAIM DCAT-AP | `healthdcatap:numberOfRecords` (maps to `eucaim:nbrOfStudies`) | `xsd:nonNegativeInteger` | **1..1** | Total number of imaging studies contained in the Dataset (e.g. DICOM Studies). | This property provides an indication of the Dataset size. A single individual may contribute multiple imaging studies acquired at different time points (e.g. diagnosis, treatment, follow-up). |
| **Image Modality** | EUCAIM DCAT-AP | `eucaim:hasImageModality` | `eucaim:ImagingModality` | **1..n** | Imaging modality represented in the Dataset. | Use the EUCAIM controlled vocabulary based on **RadLex** subclasses of *Imaging Modality*. Multiple modalities may be specified. |
| **Image Equipment Manufacturer** | EUCAIM DCAT-AP | `eucaim:hasEquipmentManufacturer` | `eucaim:Manufacturer` | **1..n** | Manufacturer of the imaging equipment. | The value corresponds to the DICOM Manufacturer attribute (0008,0070). Use the EUCAIM controlled vocabulary based on **BirnLex** subclasses of *Manufacturer*. |
| **Image Body Part / Structure** | EUCAIM DCAT-AP | `eucaim:hasImageBodyPart` | `eucaim:BodyStructure` | **1..n** | Anatomical structures represented in the imaging studies. | Use the EUCAIM controlled vocabulary based on **ICD-O-3** subclasses of *Body Structure*. Multiple anatomical regions may be specified. |

---

# Annotation

The Annotation section describes image annotations, segmentations and the methods used to generate them.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Segmentation Label** | EUCAIM DCAT-AP | `eucaim:hasAnnotationLabel` | `eucaim:BodyStructure` | **0..n** | Label identifying an annotated anatomical structure or region. | Use the EUCAIM controlled vocabulary. Organ annotations should reference subclasses of **Body Structure**. |
| **Segmentation Method** | EUCAIM DCAT-AP | `eucaim:hasAlgorithmType` | `eucaim:SegmentationMethod` | **0..n** | Method used to generate the segmentation. | Use the EUCAIM controlled vocabulary. Typical values include Manual, Semi-automatic and Automatic segmentation. |
| **Number of Segmentations** | EUCAIM DCAT-AP | `eucaim:nbrOfSegmentations` | `rdfs:Integer` | **0..1** | Total number of segmented imaging studies available in the Dataset. | Each segmented DICOM study counts as one segmentation. |

---

# Coverage

The Coverage section describes the temporal, geographical and organisational scope of the Dataset.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Collection Method** | EUCAIM DCAT-AP | `eucaim:collectionMethod` | `eucaim:SPEC1000002` | **1..n** | Defines the scope and aggregation strategy of the Dataset. | Use the EUCAIM controlled vocabulary describing how data records are organised and collected. |
| **Image Acquisition Period** | DCAT-AP v3 | `dct:temporal` | `dct:PeriodOfTime` | **0..n** | Temporal period during which the imaging studies were acquired. | This period should correspond to the DICOM Acquisition Date (0008,0022). If acquisition dates are unavailable due to anonymisation, provide the best possible approximation. |
| **Geographical Coverage** | DCAT-AP v3 | `dct:spatial` | `dct:Location` | **1..n** | Geographic region covered by the Dataset. | Use the EU Vocabularies Named Authority Lists for continents, countries and administrative regions. If no suitable concept exists, use GeoNames URIs. |
| **Spatial Resolution** | DCAT-AP v3 | `dcat:spatialResolutionInMeters` | `xsd:decimal` | **0..1** | Minimum spatial separation represented in the Dataset. | For imaging datasets this generally corresponds to image spacing or voxel size. |
| **Temporal Resolution** | DCAT-AP v3 | `dcat:temporalResolution` | `xsd:duration` | **0..1** | Minimum temporal interval represented in the Dataset. | Express the value using the `xsd:duration` datatype (ISO 8601 duration format). |
| **Frequency** | DCAT-AP v3 | `dct:accrualPeriodicity` | `dct:Frequency` | **0..1** | Frequency at which the Dataset is updated. | Use values from the EU Publications Office Frequency Named Authority List (e.g. Daily, Monthly, Yearly, Irregular). |

---

---

# Standards & Coding

The Standards & Coding section describes the standards, terminologies and coding systems used within the Dataset. These properties improve interoperability and help users understand how information is represented.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Conforms To** | DCAT-AP v3 | `dct:conformsTo` | `dct:Standard` | **0..n** | An established standard or specification to which the Dataset conforms. | Use this property to reference recognised standards, specifications, profiles or implementation guides followed by the Dataset. |
| **Coding System** | HealthDCAT-AP | `healthdcatap:hasCodingSystem` | `dct:Standard` | **0..n** | Coding systems used within the Dataset. | Examples include ICD-10, ICD-10-CM, SNOMED CT, DRGs and other recognised terminologies. |
| **Code Values** | HealthDCAT-AP | `healthdcatap:hasCodeValues` | `skos:Concept` | **0..n** | Classification concepts used in the Dataset. | Associate the Dataset with concepts from controlled vocabularies, ontologies or terminologies to improve discoverability and semantic interoperability. |

---

# Provenance

The Provenance section provides information about how the Dataset was created, processed and maintained.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Provenance** | DCAT-AP v3 | `dct:provenance` | `dct:ProvenanceStatement` | **1..n** | Information describing the origin of the Dataset and how it was produced. | Describe the methodologies, protocols, tools and processing steps used during data collection and preparation. |
| **Was Generated By** | DCAT-AP v3 | `prov:wasGeneratedBy` | `prov:Activity` | **0..n** | Activity responsible for generating the Dataset. | Examples include research projects, surveys, clinical studies or data integration activities. Multiple activities may be recorded to describe different stages of Dataset production. |

---

# Quality

The Quality section provides information about the quality, validation and assessment of the Dataset.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Quality Annotation** | HealthDCAT-AP | `dqv:hasQualityAnnotation` | `dqv:QualityCertificate` | **0..n** | Statement describing the quality of the Dataset. | Quality annotations may include quality certificates, ratings or assessment reports. Within EUCAIM, the assessed quality dimension is identified using `dqv:inDimension`, for example integrity or completeness. |

---

# Relationships

The Relationships section describes links between the Dataset and other resources.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Landing Page** | DCAT-AP v3 | `dcat:landingPage` | `foaf:Document` | **0..n** | A web page providing access to the Dataset, its Distributions or additional information. | This should point to the landing page maintained by the original data holder rather than a third-party catalogue. |
| **Related Resource** | DCAT-AP v3 | `dct:relation` | `rdfs:Resource` | **0..n** | A resource related to the Dataset. | Use this property when another Dataset, Distribution, Data Service or document is related but the nature of the relationship cannot be expressed more specifically. |
| **Is Referenced By** | DCAT-AP v3 | `dct:isReferencedBy` | `rdfs:Resource` | **0..n** | A publication or other resource that references the Dataset. | Examples include scientific publications, technical reports, project websites and documentation. |
| **Sample** | HealthDCAT-AP | `adms:sample` | `dcat:Distribution` | **0..n** | Sample Distribution of the Dataset. | Samples may consist of anonymised data, synthetic data or data dictionaries provided for inspection before requesting access. |
| **Analytics** | HealthDCAT-AP | `healthdcatap:analytics` | `dcat:Distribution` | **0..n** | Analytical resources describing the Dataset. | Typical examples include technical reports, quality reports, summary statistics and usability indicators. |

---


# Dates & Versioning

The Dates & Versioning section records the publication history and lifecycle of the Dataset.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Version** | EUCAIM DCAT-AP | `dcat:version` | `rdfs:Literal` | **1..1** | The version of the Dataset. | Version identifiers should follow Semantic Versioning (SemVer) or Calendar Versioning (CalVer). |
| **Version Notes** | DCAT-AP v3 | `adms:versionNotes` | `rdfs:Literal` | **0..n** | A description of the changes introduced in this version of the Dataset. | Describe differences compared with previous versions, such as updated methodology, corrected metadata or additional data. |
| **Release Date** | DCAT-AP v3 | `dct:issued` | `rdfs:TemporalLiteral` | **0..1** | Date on which the Dataset was formally published. | Values should be expressed as `xsd:date`, `xsd:dateTime`, `xsd:gYear` or `xsd:gYearMonth`. |
| **Modification Date** | DCAT-AP v3 | `dct:modified` | `rdfs:TemporalLiteral` | **0..1** | Most recent date on which the Dataset was modified. | Use the same XML Schema temporal datatypes as for the Release Date. |

---