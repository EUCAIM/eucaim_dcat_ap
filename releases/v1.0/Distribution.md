# Distribution

## Overview

A **Distribution** represents a specific representation of a Dataset that can be accessed, shared or reused.

Within the EUCAIM DCAT Application Profile, a Distribution describes the technical characteristics, access mechanisms, formats, licensing conditions and availability of the Dataset.

This specification corresponds to **EUCAIM DCAT-AP v1.0**, aligned with **HealthDCAT-AP Release 5**.


---

# Description

The Description section provides human-readable information describing the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Title** | DCAT-AP v3 | `dct:title` | `rdfs:Literal` | **0..n** | Name of the Distribution. | Use a descriptive title distinguishing this Distribution from other representations of the same Dataset. |
| **Description** | DCAT-AP v3 | `dct:description` | `rdfs:Literal` | **0..n** | Description of the Distribution. | Describe the content, intended use, technical characteristics and any health-data-specific considerations. |
| **Documentation** | DCAT-AP v3 | `foaf:page` | `foaf:Document` | **0..n** | Documentation describing the Distribution. | Include user guides, data dictionaries, schema documentation or technical manuals where appropriate. |

---



# Access

The Access section describes how users can discover and obtain access to the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Access URL** | DCAT-AP v3 | `dcat:accessURL` | `rdfs:Resource` | **1..n** | URL providing access to the Distribution. | In EUCAIM this corresponds to the URL of the Negotiator Service for the Dataset. The URL may provide a landing page, API endpoint or access request mechanism rather than direct download. |
| **Access Service** | DCAT-AP v3 | `dcat:accessService` | `dcat:DataService` | **1..1** | Data Service through which the Distribution can be accessed. | Reference the service providing programmatic access to the Distribution. |
| **Download URL** | DCAT-AP v3 | `dcat:downloadURL` | `rdfs:Resource` | **0..n** | Direct URL to download the Distribution. | Use only when direct download is available. |
| **Availability** | DCAT-AP v3 | `dcatap:availability` | `skos:Concept` | **0..1** | Planned availability of the Distribution. | Use the Publications Office Planned Availability Authority List. |



---

# Technical Characteristics

The Technical Characteristics section describes the physical representation and technical properties of the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Format** | DCAT-AP v3 | `dct:format` | `dct:MediaTypeOrExtent` | **0..1** | Technical format of the Distribution. | Examples include DICOM, NIfTI, CSV, JSON, XML or Parquet. Different data types should be represented as separate Distributions. |
| **Media Type** | DCAT-AP v3 | `dcat:mediaType` | `dct:MediaType` | **0..1** | Internet media type. | Use official IANA Media Types whenever possible. |
| **Compression Format** | DCAT-AP v3 | `dcat:compressFormat` | `dct:MediaType` | **0..1** | Compression format used by the Distribution. | Examples include ZIP, GZIP and BZIP2. |
| **Packaging Format** | DCAT-AP v3 | `dcat:packageFormat` | `dct:MediaType` | **0..1** | Packaging format grouping multiple files. | Use official IANA media types where available. |
| **Image Size** | EUCAIM DCAT-AP | `dcat:byteSize` | `xsd:decimal` | **0..1** | Size of the Distribution. | Provide the file size in bytes. If unknown, an estimate may be provided. |
| **Checksum** | EUCAIM DCAT-AP | `spdx:checksumValue` | `xsd:hexBinary` | **0..1** | Checksum used to verify file integrity. | The checksum corresponds to the Download URL. |
| **Checksum Algorithm** | EUCAIM DCAT-AP | `spdx:algorithm` | `spdx:ChecksumAlgorithm` | **1..1** | Algorithm used to compute the checksum. | Examples include SHA-256 and MD5. |
| **Spatial Resolution** | DCAT-AP v3 | `dcat:spatialResolutionInMeters` | `xsd:decimal` | **0..1** | Minimum spatial separation represented in the Distribution. | Applicable to imaging data where relevant. |
| **Temporal Resolution** | DCAT-AP v3 | `dct:temporal` | `xsd:duration` | **0..1** | Minimum temporal interval represented in the Distribution. | Express using ISO 8601 duration format. |

---

# Standards

The Standards section specifies the technical standards and schemas followed by the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Linked Schemas** | DCAT-AP v3 | `dct:conformsTo` | `dct:Standard` | **0..n** | Schema or technical specification implemented by the Distribution. | Examples include HL7 FHIR, OMOP CDM or other machine-readable specifications. |
| **Language** | DCAT-AP v3 | `dct:language` | `dct:LinguisticSystem` | **0..n** | Language used within the Distribution. | Use values from the EU Languages Authority List. |

---

# Rights & Policies

The Rights & Policies section describes the legal framework governing access and reuse of the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Applicable Legislation** | DCAT-AP v3 | `dcatap:applicableLegislation` | `rdfs:Resource` | **1..n** | Legislation governing the Distribution. | Include the ELI of the EHDS Regulation. Multiple legislative references may be provided. |
| **License** | DCAT-AP v3 | `dct:license` | `dct:LicenseDocument` | **0..1** | Licence governing reuse of the Distribution. | Use canonical IRIs whenever possible (e.g. Creative Commons licences). |
| **Rights** | DCAT-AP v3 | `dct:rights` | `dct:RightsStatement` | **0..1** | Rights statement associated with the Distribution. | Describe access restrictions and intellectual property rights. |
| **Has Policy** | DCAT-AP v3 | `odrl:hasPolicy` | `odrl:Policy` | **0..1** | Machine-readable usage policy. | Use ODRL to express permissions, prohibitions and obligations. |
| **Access Conditions** | EUCAIM DCAT-AP | `dct:rights` | `eucaim:DatasetAccessCondition` | **1..1** | Conditions under which access to the Distribution is granted. | One of the predefined EUCAIM access conditions: download, in-situ processing, or remote processing without direct data access. |

---

# Lifecycle

The Lifecycle section records the publication history and maturity of the Distribution.

| Property | Origin | Property IRI | Range | Cardinality | Description | Usage Notes |
|----------|--------|--------------|-------|-------------|-------------|-------------|
| **Status** | DCAT-AP v3 | `adms:status` | `skos:Concept` | **0..1** | Maturity status of the Distribution. | Use one of: Completed, Under Development, Deprecated or Withdrawn. |
| **Release Date** | DCAT-AP v3 | `dct:issued` | `rdfs:TemporalLiteral` | **0..1** | Date on which the Distribution was first published. | Use XML Schema temporal datatypes. |
| **Modification Date** | DCAT-AP v3 | `dct:modified` | `rdfs:TemporalLiteral` | **0..1** | Most recent modification date. | Indicates when the Distribution was last updated. |

---