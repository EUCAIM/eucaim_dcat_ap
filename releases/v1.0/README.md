# EUCAIM DCAT Application Profile v1.0 

## Main classes

### Catalog

This document defines the properties used to describe a `dcat:Catalog` in version 1.0 of the EUCAIM DCAT Application Profile. The specification inherits the Catalogue specification from [HealthDCAT-AP Release 5](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/) without modification.

The Catalogue contains metadata records describing EUCAIM datasets and their associated distributions. EUCAIM-specific requirements for individual datasets and distributions are defined separately in the [Dataset](Dataset.md) and [Distribution](Distribution.md) specifications.

### Dataset

The **Dataset** is the core entity of the EUCAIM DCAT Application Profile. It represents a collection of cancer imaging data and associated metadata published through the EUCAIM Catalogue.

The EUCAIM DCAT-AP extends **DCAT-AP v3** and **HealthDCAT-AP Release 5** by introducing additional metadata elements required for the discovery, understanding and reuse of cancer imaging datasets in the context of cancer imaging research.

This specification corresponds to **EUCAIM DCAT-AP v1.0**.

### Distribution 

A **Distribution** represents a specific representation of a Dataset that can be accessed, shared or reused.

Within the EUCAIM DCAT Application Profile, a Distribution describes the technical characteristics, access mechanisms, formats, licensing conditions and availability of the Dataset.

This specification corresponds to **EUCAIM DCAT-AP v1.0**, aligned with **HealthDCAT-AP Release 5**.

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

---
# Implementation details

The property policy from dataset will be implemented later. Due to its complex structure some additional time is needed to figure out how to best
display this information in the EUCAIM catalogue user interface.

