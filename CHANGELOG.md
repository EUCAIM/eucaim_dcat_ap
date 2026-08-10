# EUCAIM DCAT Application Profile — Changelog

This document describes the changes to the EUCAIM Dataset specification between version 1.0 and version 2.0.

| EUCAIM version | Base application profile |
|---|---|
| v1.0 | HealthDCAT-AP Release 5 |
| v2.0 | HealthDCAT-AP Release 7 |

The changelog distinguishes changes to Dataset properties from the expanded documentation of nested resources such as Agents, Contact Points, Attributions, and Relationships.

## Added Dataset properties

The following Dataset-level properties are introduced in v2.0.

| Property | Property IRI | Range | Cardinality | Requirement | Description |
|---|---|---|---|---|---|
| Structured Data | `healthdcatap:hasStructuredData` | `xsd:boolean` | `1..1` | Mandatory | Indicates whether the Dataset contains structured data for which a machine-readable description of its variables can be provided. |
| Variables | `healthdcatap:hasVariables` | `csvw:TableGroup` | `0..n` | Conditional | Links the Dataset to a CSVW Table Group. It is mandatory when `healthdcatap:hasStructuredData` is `true`. |
| Custodian | `geodcatap:custodian` | `foaf:Agent` | `0..1` | Recommended | Identifies the Agent accountable for the care and maintenance of the Dataset. |

## Removed properties

The following supporting property documented in v1.0 is no longer included in v2.0.

| Property | Property path | v1.0 | v2.0 |
|---|---|---|---|
| Publisher Trusted Data Holder | `dct:publisher / healthdcatap:trustedDataHolder` | `0..1` | Removed |

No other Dataset-level property has been removed. Some existing properties have been reorganised into different sections or renamed for clarity.

## Changed property paths and contact-point representation

HealthDCAT-AP Release 7 uses the Core Vocabularies Contact Point model for Publisher, Custodian, and Health Data Access Body contact information.

| Property | v1.0 path and range | v2.0 path and range |
|---|---|---|
| Publisher Contact Point | `dct:publisher / dcat:contactPoint`; `vcard:Kind` | `dct:publisher / cv:contactPoint`; `cv:ContactPoint` |
| Health Data Access Body Contact Point | `healthdcatap:hdab / dcat:contactPoint`; `vcard:Kind` | `healthdcatap:hdab / cv:contactPoint`; `cv:ContactPoint` |

The Dataset-level `dcat:contactPoint` continues to use `vcard:Kind`. Version 2.0 explicitly documents its supported contact page and email properties.

## Changed ranges and ontology references

| Property | v1.0 range | v2.0 range | Change |
|---|---|---|---|
| Segmentation Label | `eucaim:BodyStructure` | `rdfs:Resource` | Broadened to support anatomical structures, pathological findings, lesions, imaging findings, and other ontology-defined annotation labels. |
| Code Values | `skos:Concept` | `rdfs:Literal` | Code values are represented as literals rather than requiring SKOS concepts. |


## Expanded Dataset contact-point documentation

Version 1.0 documented only `dcat:contactPoint`. Version 2.0 explicitly documents the supported contact mechanisms.

| Property | Property path | Cardinality | Requirement |
|---|---|---|---|
| Dataset Contact Page | `dcat:contactPoint / vcard:hasURL` | `0..1` | Conditional |
| Dataset Contact Email | `dcat:contactPoint / vcard:hasEmail` | `0..1` | Conditional |

At least one contact page or email must be supplied for each Dataset contact point.

## Expanded Publisher documentation

Version 2.0 replaces the label **Publisher Note** with **Publisher Description**. The RDF path remains `dct:publisher / dct:description`.

Version 2.0 also explicitly defines the supported Publisher contact-point attributes:

- contact page;
- email;
- telephone;
- availability restrictions;
- description and recurrence of availability restrictions;
- opening hours;
- description and recurrence of opening hours.

These rows describe the accepted structure of the Publisher resource; they are not additional properties directly attached to the Dataset.

## New Custodian structure

Version 2.0 introduces a Custodian section supporting:

- name and Agent type;
- contact point;
- contact page, email, and telephone;
- availability restrictions and their recurrence;
- opening hours and their recurrence.

The Custodian is distinct from the Publisher and represents the Agent accountable for the care and maintenance of the Dataset.

## Expanded Health Data Access Body documentation

Version 1.0 documented the Health Data Access Body, its name, type, and contact point. Version 2.0 additionally defines:

- contact page;
- email;
- telephone;
- availability restrictions and their recurrence;
- opening hours and their recurrence.

The contact-point representation changes from `dcat:contactPoint` and `vcard:Kind` to `cv:contactPoint` and `cv:ContactPoint`.

## Expanded Creator documentation

Version 2.0 adds explicit support for:

| Property | Property path | Cardinality | Requirement |
|---|---|---|---|
| Creator Contact Page | `dct:creator / foaf:homepage` | `0..n` | Optional |
| Creator Email | `dct:creator / foaf:mbox` | `0..n` | Optional |

Creator Name is explicitly Conditional and must be supplied whenever a Creator is described.

## Expanded Qualified Attribution documentation

Version 2.0 adds explicit support for the following properties of an Agent referenced through `prov:qualifiedAttribution`:

- Agent description;
- Agent type;
- Agent email;
- Agent homepage.

The Agent, Agent Name, and Agent Role are explicitly Conditional whenever a Qualified Attribution is supplied.

## Expanded provenance documentation

Version 2.0 adds the Activity Type supporting property.

| Property | Property path | Range | Cardinality | Requirement |
|---|---|---|---|---|
| Activity Type | `prov:wasGeneratedBy / dct:type` | `skos:Concept` | `1..1` | Conditional |

When a `prov:Activity` is supplied, the Activity Type must be provided and should use the Health Activity controlled vocabulary where applicable.

## Controlled-vocabulary clarifications

Version 2.0 provides explicit controlled-vocabulary requirements and stable references for:

- EUCAIM interoperability levels;
- EUCAIM Dataset Types and the DPV Data taxonomy;
- Health Categories and Health Themes;
- DPV Legal Bases, Purposes, and Personal Data;
- EU Access Rights;
- HealthDCAT-AP Publisher Types;
- EU Languages and Frequencies;
- EU geographical authority lists and GeoNames;
- Health Activities;
- HealthDCAT-AP Standards;
- ISO 19115 Agent roles;
- EUCAIM cancer conditions, imaging modalities, equipment manufacturers, body structures, annotation labels, segmentation methods, and collection methods.

## Quality annotation clarification

Version 2.0 clarifies that:

- `dqv:hasQualityAnnotation` associates the Dataset with a `dqv:QualityCertificate`;
- `dqv:inDimension` identifies the assessed quality dimension;
- EUCAIM quality certificates and associated quality dimensions are not yet formally defined and remain work in progress.

## Documentation and conformance changes

Version 2.0 introduces:

- explicit definitions of Mandatory, Recommended, Conditional, and Optional;
- explicit Mandatory (`M`), Recommended (`R`), Conditional (`C`), and Optional (`O`) requirement indicators; in the Dataset specification these are presented together with cardinality in the **Occurrence** column;
- processing-conformance requirements for EUCAIM catalogue harvesters;
- separate definitions of accepting and processing metadata;
- rules for handling RDF properties not explicitly listed in the profile;
- explicit interpretation of cardinalities for structured resources;
- more normative Usage Notes using MUST, SHOULD, and MAY;
- a reorganised section structure.

## Controlled vocabularies

Version 2.0 introduces or publishes the following EUCAIM controlled-vocabulary resources:

- **Access Conditions** — describes whether access is provided through download, in-situ processing, or remote processing without direct data access.
- **Data Use Conditions** — provides EUCAIM data-use and reuse conditions aligned with the Data Use Ontology.
- **Segmentation Labels** — provides the EUCAIM concepts accepted as segmentation labels.

The controlled vocabularies are published under
[`releases/controlled-vocabularies`](https://github.com/EUCAIM/eucaim_dcat_ap/tree/main/releases/controlled-vocabularies).

## Migration guidance

Implementers migrating from v1.0 to v2.0 should:

1. add support for `healthdcatap:hasStructuredData` and conditionally for `healthdcatap:hasVariables`;
2. add support for the recommended `geodcatap:custodian` structure;
3. update Publisher and Health Data Access Body contact points to the `cv:ContactPoint` model;
4. stop producing `healthdcatap:trustedDataHolder` as part of the v2.0 Publisher structure;
5. update the listed EUCAIM ranges to their exact ontology identifiers;
6. accept `rdfs:Resource` values for Segmentation Label;
7. represent HealthDCAT-AP Code Values as literals;
8. treat Health Theme as Recommended with cardinality `0..n`;
9. implement the explicitly documented nested contact, Agent, Activity, Attribution, and Relationship properties;
10. apply the new Mandatory, Recommended, Conditional, and Optional requirement levels.

> [!NOTE]
> Most additional rows in v2.0 document attributes of existing structured resources. They do not all represent new predicates directly attached to `dcat:Dataset`. Implementations should distinguish new Dataset fields from expanded processing requirements for nested RDF resources.


### Distribution

Version 2.0 updates the Distribution specification to align it with
HealthDCAT-AP Release 7 and to provide more precise processing requirements
for EUCAIM catalogue harvesters.

#### Structural and range changes

| Property | Version 1.0 | Version 2.0 |
|---|---|---|
| Access Service | `1..1` | `0..n` |
| Byte Size | `dcat:byteSize`, range `xsd:decimal` | `dcat:byteSize`, range `xsd:nonNegativeInteger` |
| Checksum | Direct use of `spdx:checksumValue` | `spdx:checksum` linking to a structured `spdx:Checksum` resource |
| Checksum Algorithm | Direct `spdx:algorithm` value | `spdx:checksum / spdx:algorithm` |
| Temporal Resolution | `dct:temporal` | `dcat:temporalResolution` |
| Applicable Legislation | `rdfs:Resource` | `eli:LegalResource` |
| Release Date | `rdfs:TemporalLiteral` | `rdfs:Literal` with an XML Schema temporal datatype |
| Modification Date | `rdfs:TemporalLiteral` | `rdfs:Literal` with an XML Schema temporal datatype |

#### Rights and access conditions

Version 1.0 documented **Rights** and **Access Conditions** as separate rows
using the same `dct:rights` property. Version 2.0 consolidates them into one
repeatable `dct:rights` property with range `dct:RightsStatement`.

Values may be selected from:

- the [EUCAIM Access Conditions controlled vocabulary](https://eucaim.github.io/eucaim_dcat_ap/releases/controlled-vocabularies/access-conditions/), describing how the Distribution can be accessed;
- the [EUCAIM Data Use Conditions controlled vocabulary](https://eucaim.github.io/eucaim_dcat_ap/releases/controlled-vocabularies/data-use-conditions/), describing permitted uses and reuse restrictions and aligning them with corresponding Data Use Ontology concepts.

#### Checksum processing

Version 2.0 explicitly documents the internal structure of `spdx:Checksum`.
When a Checksum is provided, it must contain:

- exactly one `spdx:checksumValue`;
- exactly one `spdx:algorithm`.

#### ODRL policy processing

Version 2.0 defines the supported structure of an `odrl:Policy`, including:

- `odrl:uid`;
- `odrl:permission`;
- `odrl:prohibition`;
- `odrl:obligation`;
- the `odrl:action` values associated with each Rule.

Every Policy must contain at least one Permission, Prohibition, or Obligation.
Every Rule must contain at least one action from the ODRL Common Actions
vocabulary.

#### Controlled-vocabulary guidance

Version 2.0 also strengthens the controlled-vocabulary requirements:

- `dcatap:availability` uses the EU Planned Availability authority table;
- `dct:format` uses the EU File Type authority table;
- `dcat:compressFormat`, `dcat:mediaType`, and `dcat:packageFormat` use IANA Media Types where applicable;
- `adms:status` uses the EU Distribution Status authority table;
- `dct:language` uses the EU Languages authority table;
- `dcatap:applicableLegislation` may reference the EHDS Regulation using its ELI URI.