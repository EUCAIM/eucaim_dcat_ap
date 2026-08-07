# EUCAIM DCAT Application Profile

The **EUCAIM DCAT Application Profile (EUCAIM DCAT-AP)** extends the **Data Catalog Vocabulary Application Profile (DCAT-AP)** and the **Health Data Catalog Application Profile (HealthDCAT-AP)** to support the description, publication, discovery, and interoperability of cancer imaging datasets within the **European Federation for Cancer Images (EUCAIM)** project.

The profile defines a harmonized metadata model for describing cancer imaging datasets and their distributions, enabling interoperability between data holders and the EUCAIM Catalogue while remaining aligned with the European Health Data Space (EHDS).

---

## Purpose

The EUCAIM DCAT Application Profile aims to:

- provide a common metadata model for cancer imaging datasets;
- facilitate dataset discovery across participating institutions;
- improve metadata interoperability between EUCAIM and external catalogues;
- extend HealthDCAT-AP with metadata elements specific to cancer imaging;
- promote FAIR data principles through standardized metadata.

---

## Repository Structure

Each released version of the application profile is maintained independently under the `releases/` directory.

```
eucaim-dcat-ap/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
└── releases/
    ├── v1.0/
    │   ├── README.md
    │   ├── Dataset.md
    │   ├── Distribution.md
    │   └── examples/
    │       ├── Dataset Examples.md
    │       └── Distribution Examples.md
    └── v2.0/
        ├── README.md
        ├── Dataset.md
        ├── Distribution.md
        └── examples/
            ├── Dataset Examples.md
            └── Distribution Examples.md
```

Each release contains the complete specification corresponding to a specific version of the EUCAIM DCAT Application Profile.

The root-level [`CHANGELOG.md`](CHANGELOG.md) describes changes between releases, including migration-relevant changes to properties, ranges, cardinalities, controlled vocabularies, and supporting resource structures.

---

## Current Releases

| Version | Based on | Status |
|----------|----------|--------|
| **v1.0** | HealthDCAT-AP Release 5 | Previous stable release |
| **v2.0** | HealthDCAT-AP Release 7 | Current release |

Version 2.0 updates the profile to HealthDCAT-AP Release 7 while retaining the cancer-imaging-specific metadata introduced by EUCAIM. It also provides more explicit implementation guidance for structured resources such as Agents, Contact Points, Checksums, Attributions, Relationships, and ODRL Policies.

---

## Specification

Each release contains the following documentation.

### Dataset

Defines the metadata properties describing a cancer imaging dataset, including:

- identification
- classification
- responsible parties
- access and rights
- population
- imaging characteristics
- annotations
- coverage
- standards and coding systems
- provenance
- quality
- relationships
- dates and versioning

Version 2.0 additionally documents structured-data and variable metadata, the Dataset Custodian, expanded contact-point information, and the supported properties of nested resources.

### Distribution

Defines the metadata properties describing a dataset distribution, including:

- access mechanisms
- technical characteristics
- standards
- rights and policies
- lifecycle information

Version 2.0 aligns Distribution usage guidance with HealthDCAT-AP Release 7, including the applicable controlled vocabularies for availability, file format, media type, packaging, and lifecycle status. It also explicitly documents the supported SPDX Checksum and ODRL Policy structures.

### Examples

Markdown documentation containing RDF/Turtle examples that illustrate how individual Dataset and Distribution properties can be represented using the EUCAIM DCAT Application Profile.

---

## Changes between releases

The [`CHANGELOG.md`](CHANGELOG.md) provides a consolidated description of the changes introduced in each release.

For the migration from v1.0 to v2.0, it identifies:

- properties added or removed;
- changes to property paths, ranges, cardinalities, and controlled vocabularies;
- changes inherited from HealthDCAT-AP Release 7;
- expanded processing requirements for nested RDF resources;
- implementation guidance for migrating catalogue harvesters and metadata records.

---

## Versioning

The repository follows **Semantic Versioning**.

Major versions correspond to significant revisions of the application profile, including alignment with a new HealthDCAT-AP release or changes that may require metadata providers and catalogue implementations to update their mappings.

| Version | Description |
|----------|-------------|
| Major | Breaking changes or alignment with a new HealthDCAT-AP release |
| Minor | Backwards-compatible additions or clarifications |
| Patch | Corrections that do not change the metadata model |

---

## Relationship with Other Specifications

The EUCAIM DCAT Application Profile builds upon and aligns with the following standards, application profiles, vocabularies, and metadata specifications:

- W3C DCAT 3
- DCAT Application Profile for data portals in Europe (DCAT-AP)
- HealthDCAT Application Profile (HealthDCAT-AP)
- BBMRI-ERIC Cataloguing Metadata Specification (MIABIS)
- Dublin Core Metadata Terms (DCT)
- Data Privacy Vocabulary (DPV)
- PROV Ontology (PROV-O)
- ODRL Information Model
- Data Quality Vocabulary (DQV)

---

## Contributing

Issues and suggestions for improving the specification are welcome.

Contributions should preserve compatibility with the underlying DCAT-AP and HealthDCAT-AP specifications.

---

## License

This repository is licensed under the **Apache License 2.0**.

See the `LICENSE` file for details.

---

## Acknowledgements

This work was developed within **Work Package 5 (WP5)** of the **EUCAIM** project.

The EUCAIM project has received funding from the European Union's **Digital Europe Programme (DEP)** under Grant Agreement **No. 101100633**.

The EUCAIM DCAT Application Profile extends the **HealthDCAT Application Profile (HealthDCAT-AP)** to support the description, publication, discovery, and interoperability of cancer imaging datasets.

### Authors

- **Valia Kalokyri** (Foundation for Research and Technology – Hellas, Institute of Computer Science, FORTH) – Lead author
- **Mirna El Ghosh** (Sorbonne Université, Inserm, Université Sorbonne Paris-Nord, LIMICS) – Major contributor

### Reviewers

The specification benefited from review and feedback from:

- **Irene Marin Radoszynski** (La Fe University and Polytechnic Hospital – La Fe Health Research Institute, HULAFE)
- **Eirini Kaldeli** (MAGGIOLI S.P.A. Research and Development Lab, MAG)
- **Alexander Harms** (STICHTING HEALTH-RI, Health-RI)

The authors also acknowledge the work of the **HealthDCAT-AP** and **DCAT-AP** communities, whose specifications constitute the foundation upon which the EUCAIM DCAT Application Profile is built.
