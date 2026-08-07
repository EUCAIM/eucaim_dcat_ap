# EUCAIM DCAT Application Profile v2.0 — Distribution

## Overview

This document defines the properties used to describe a `dcat:Distribution` in version 2.0 of the EUCAIM DCAT Application Profile. It is aligned with DCAT-AP v3 and HealthDCAT-AP Release 7 and extends them with metadata required for accessing and reusing cancer imaging datasets in EUCAIM.

A Distribution represents a specific representation of a Dataset that can be accessed, shared, or reused. It describes the representation's access mechanisms, technical characteristics, formats, legal conditions, policies, and availability.

The specification uses the following requirement levels:

| Requirement | Definition |
|---|---|
| **Mandatory** | The property MUST be provided for every Distribution. |
| **Recommended** | The property SHOULD be provided when applicable or available. |
| **Conditional** | The property MUST be provided when the condition specified in its Usage Notes applies; otherwise, it MAY be omitted. |
| **Optional** | The property MAY be provided. |

## Legend

The **EUCAIM Modification** column identifies structural or conformance-level differences from HealthDCAT-AP Release 7.

| Symbol | EUCAIM Modification | Description |
|---|---|---|
| 🟢 | **Added** | Property introduced by the EUCAIM DCAT Application Profile and not defined for the Distribution in HealthDCAT-AP. |
| 🟠 | **Modified** | HealthDCAT-AP property for which EUCAIM changes the property IRI, range, cardinality, or requirement level. |
| — | **Inherited** | Property inherited with the same IRI, range, cardinality, and requirement level. EUCAIM-specific explanations, examples, and implementation guidance may be added to the Usage Notes without changing its inherited status. |

## Processing Conformance

This specification defines the properties that EUCAIM catalogue implementations are required to accept and process.

- **Accept** means that the harvester MUST ingest the property without producing an error.
- **Process** means that the harvester MUST preserve the value and map it to the corresponding catalogue field or internal representation.
- Properties not explicitly listed in this specification MAY be present in the RDF. Harvesters SHOULD preserve such properties where technically possible but are not required to interpret, index, or display them.
- An unlisted property MUST NOT be interpreted as an alternative to a listed Mandatory property.
- The cardinalities in the Distribution property tables apply to each Distribution.
- Where a property path traverses a structured resource, such as `spdx:Checksum` or `odrl:Policy`, the cardinalities in the corresponding section apply to each instance of that resource.

## Description

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Title | — | `dct:title` | `rdfs:Literal` | `0..n` | Optional | A name given to the Distribution. | The property MAY be repeated for parallel language versions. Language-tagged literals SHOULD be used. Use a title that distinguishes this Distribution from other representations of the same Dataset. |
| Description | — | `dct:description` | `rdfs:Literal` | `0..n` | Recommended | A free-text account of the Distribution. | Describe the content, intended use, technical characteristics, and any health-data-specific considerations. The property MAY be repeated for different languages. |
| Documentation | — | `foaf:page` | `foaf:Document` | `0..n` | Optional | A page or document about the Distribution. | May link to user guides, data dictionaries, schema documentation, technical manuals, or other information supporting use of the Distribution. |

## Access

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Access URL | — | `dcat:accessURL` | `rdfs:Resource` | `1..n` | Mandatory | A URL that gives access to the Distribution. | In EUCAIM, this SHOULD identify the Negotiator Service URL for the Dataset where access is mediated. The URL may identify a landing page, API endpoint, or access-request mechanism rather than a directly downloadable file. Multiple access URLs MAY be provided. |
| Access Service | — | `dcat:accessService` | `dcat:DataService` | `0..n` | Optional | A Data Service that gives access to the Distribution. | Use when the Distribution is accessible through a described Data Service, such as an API or federated-query service. Multiple services MAY be provided. |
| Download URL | — | `dcat:downloadURL` | `rdfs:Resource` | `0..n` | Optional | A URL that is a direct link to a downloadable file in a given format. | Use only when the Distribution can be downloaded directly. It SHOULD NOT be used for an access-request page or other indirect access mechanism. |
| Availability | — | `dcatap:availability` | `skos:Concept` | `0..1` | Recommended | An indication of how long the Distribution is planned to remain available. | The [EU Planned Availability authority table](http://publications.europa.eu/resource/authority/planned-availability) MUST be used. |

## Technical Characteristics

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Format | — | `dct:format` | `dct:MediaTypeOrExtent` | `0..1` | Recommended | The file format of the Distribution. | The [EU File Type authority table](http://publications.europa.eu/resource/authority/file-type) MUST be used. Different representations or formats SHOULD be described as separate Distributions. |
| Media Type | — | `dcat:mediaType` | `dct:MediaType` | `0..1` | Optional | The media type of the Distribution as defined in the official IANA register. | The [IANA Media Types registry](https://www.iana.org/assignments/media-types/) SHOULD be used where applicable, for example `application/dicom`. |
| Compression Format | — | `dcat:compressFormat` | `dct:MediaType` | `0..1` | Optional | The format in which the Distribution's data is compressed. | The [IANA Media Types registry](https://www.iana.org/assignments/media-types/) SHOULD be used where applicable. Use this property for compression applied to an individual data file. |
| Packaging Format | — | `dcat:packageFormat` | `dct:MediaType` | `0..1` | Optional | The format in which one or more files are grouped together for distribution. | The [IANA Media Types registry](https://www.iana.org/assignments/media-types/) SHOULD be used where applicable. Use this property for a container or package that groups multiple files. |
| Byte Size | — | `dcat:byteSize` | `xsd:nonNegativeInteger` | `0..1` | Optional | The size of the Distribution in bytes. | Provide the size as a non-negative integer expressed in bytes. |
| Checksum | — | `spdx:checksum` | `spdx:Checksum` | `0..1` | Optional | A mechanism that can be used to verify that the contents of the Distribution have not changed. | When supplied, the Checksum MUST contain exactly one checksum value and exactly one algorithm. The checksum SHOULD correspond to the resource identified by `dcat:downloadURL`. |
| Spatial Resolution | — | `dcat:spatialResolutionInMeters` | `xsd:decimal` | `0..1` | Optional | The minimum spatial separation resolvable in the Distribution, measured in metres. | For medical images, the value SHOULD represent the smallest spatial sampling interval present in the Distribution and MUST be expressed in metres. Detailed in-plane and through-plane spacing remains available in the DICOM metadata. |
| Temporal Resolution | — | `dcat:temporalResolution` | `xsd:duration` | `0..1` | Optional | The minimum time period resolvable in the Distribution. | The value MUST use the `xsd:duration` lexical format, for example `PT1S` or `P1D`. For medical images, it may represent the interval between frames, acquisitions, or longitudinal observations. |

## Checksum

A `spdx:Checksum` supplied through `spdx:checksum` contains the checksum value and the algorithm used to calculate it.

| Property | EUCAIM Modification | Property Path | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Checksum Value | — | `spdx:checksum / spdx:checksumValue` | `xsd:hexBinary` | `1..1` | Conditional | Lowercase hexadecimal checksum value. | MUST be provided when a Checksum is supplied. The lexical value MUST be compatible with the selected checksum algorithm. |
| Checksum Algorithm | — | `spdx:checksum / spdx:algorithm` | `spdx:ChecksumAlgorithm` | `1..1` | Conditional | Algorithm used to calculate the checksum. | MUST be provided when a Checksum is supplied. Use an SPDX checksum algorithm IRI, such as `spdx:checksumAlgorithm_sha256`. |

## Standards and Language

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Linked Schemas | — | `dct:conformsTo` | `dct:Standard` | `0..n` | Optional | An established schema to which the Distribution conforms. | Use only for standards, schemas, profiles, or implementation guides with which the Distribution itself conforms. Examples may include DICOM, HL7 FHIR, or OMOP CDM where applicable. Multiple standards MAY be provided. |
| Language | — | `dct:language` | `dct:LinguisticSystem` | `0..n` | Optional | A language used in the Distribution. | Values MUST be selected from the [EU Languages authority table](http://publications.europa.eu/resource/authority/language). The property MAY be repeated when the Distribution contains content in multiple languages. |

## Rights and Policies

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Applicable Legislation | — | `dcatap:applicableLegislation` | `eli:LegalResource` | `1..n` | Mandatory | Legislation that mandates the creation or management of the Distribution. | Where applicable, include the ELI URI of the [European Health Data Space Regulation (EU) 2025/327](http://data.europa.eu/eli/reg/2025/327/oj). Additional applicable EU or national legislation SHOULD be provided, preferably using an official persistent URI such as an ELI. |
| Licence | — | `dct:license` | `dct:LicenseDocument` | `0..1` | Recommended | A licence under which the Distribution is made available. | Provide licence and rights information at Distribution level. Use the canonical IRI of a standard licence where applicable. See the [DCAT 3 guidance on licences and rights](https://www.w3.org/TR/vocab-dcat-3/#license-rights). |
| Rights | 🟠 | `dct:rights` | `dct:RightsStatement` | `0..n` | Recommended  | A statement that specifies rights, access conditions, or data-use conditions associated with the Distribution. | At least one value MUST be selected from the [EUCAIM Access Conditions controlled vocabulary](https://eucaim.github.io/eucaim_dcat_ap/releases/controlled-vocabularies/access-conditions/). These concepts describe how the Distribution may be accessed and are classified under the applicable subclass of [`eucaim:SPEC1000021` — Dataset Access Condition](https://hyperontology.eucaim.cancerimage.eu/#SPEC1000021). Additional values MAY be selected from the [EUCAIM Data Use Conditions controlled vocabulary](https://eucaim.github.io/eucaim_dcat_ap/releases/controlled-vocabularies/data-use-conditions/) to describe permitted uses and reuse restrictions. EUCAIM Data Use Conditions are aligned with corresponding Data Use Ontology (DUO) concepts. Multiple values MAY be provided when more than one access or data-use condition applies. |
| Has Policy | — | `odrl:hasPolicy` | `odrl:Policy` | `0..1` | Optional | An ODRL policy expressing rights associated with the Distribution. | Use ODRL to express machine-readable permissions, prohibitions, and duties. When a Policy is supplied, at least one permission, prohibition, or obligation MUST be provided. |

## ODRL Policy

An `odrl:Policy` supplied through `odrl:hasPolicy` describes machine-readable permissions, prohibitions, and duties associated with the Distribution.

At least one of `odrl:permission`, `odrl:prohibition`, or `odrl:obligation` MUST be present in each Policy.

| Property | EUCAIM Modification | Property Path | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Permission | — | `odrl:hasPolicy / odrl:permission` | `odrl:Permission` | `0..n` | Conditional | An action permitted by the Policy. | At least one Permission, Prohibition, or Obligation MUST be supplied for each Policy. Each Permission MUST contain at least one `odrl:action`. |
| Prohibition | — | `odrl:hasPolicy / odrl:prohibition` | `odrl:Prohibition` | `0..n` | Conditional | An action prohibited by the Policy. | At least one Permission, Prohibition, or Obligation MUST be supplied for each Policy. Each Prohibition MUST contain at least one `odrl:action`. |
| Obligation | — | `odrl:hasPolicy / odrl:obligation` | `odrl:Duty` | `0..n` | Conditional | A duty that must be fulfilled under the Policy. | At least one Permission, Prohibition, or Obligation MUST be supplied for each Policy. Each Duty MUST contain at least one `odrl:action`. |
| Permission Action | — | `odrl:hasPolicy / odrl:permission / odrl:action` | `odrl:Action` | `1..n` | Conditional | An action permitted by the Policy. | MUST be provided for every Permission. Values MUST be selected from the [ODRL Common Actions vocabulary](https://www.w3.org/TR/odrl-vocab/#actionsCommon). |
| Prohibition Action | — | `odrl:hasPolicy / odrl:prohibition / odrl:action` | `odrl:Action` | `1..n` | Conditional | An action prohibited by the Policy. | MUST be provided for every Prohibition. Values MUST be selected from the [ODRL Common Actions vocabulary](https://www.w3.org/TR/odrl-vocab/#actionsCommon). |
| Obligation Action | — | `odrl:hasPolicy / odrl:obligation / odrl:action` | `odrl:Action` | `1..n` | Conditional | An action required by the Policy. | MUST be provided for every Duty. Values MUST be selected from the [ODRL Common Actions vocabulary](https://www.w3.org/TR/odrl-vocab/#actionsCommon). |

## Lifecycle

| Property | EUCAIM Modification | Property IRI | Range | Cardinality | Requirement | Description | Usage Notes |
|---|---|---|---|---|---|---|---|
| Status | — | `adms:status` | `skos:Concept` | `0..1` | Optional | The status of the Distribution in its maturity lifecycle. | The [EU Distribution Status authority table](http://publications.europa.eu/resource/authority/distribution-status) MUST be used where applicable. |
| Release Date | — | `dct:issued` | `rdfs:Literal` | `0..1` | Optional | Date of formal issuance or publication of the Distribution. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. The most precise datatype supported by the available information SHOULD be used. |
| Modification Date | — | `dct:modified` | `rdfs:Literal` | `0..1` | Optional | Most recent date on which the Distribution was changed. | The value MUST be a typed literal using `xsd:date`, `xsd:dateTime`, `xsd:gYear`, or `xsd:gYearMonth`. The most precise datatype supported by the available information SHOULD be used. |
