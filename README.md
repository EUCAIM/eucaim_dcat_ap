# EUCAIM DCAT Application Profile

The **EUCAIM DCAT Application Profile (EUCAIM DCAT-AP)** extends the **Data Catalog Vocabulary Application Profile (DCAT-AP)** and the **Health Data Catalog Application Profile (HealthDCAT-AP)** to support the description, publication, discovery, and interoperability of cancer imaging datasets within the **European Cancer Imaging Initiative (EUCAIM)**.

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
├── LICENSE
└── releases/
    ├── v1.0/
    │   ├── README.md
    │   ├── Dataset.md
    │   ├── Distribution.md
    │   └── examples/
    │       ├── Dataset.ttl
    │       └── Distribution.ttl
    └── v2.0/
        └── ...
```

Each release contains the complete specification corresponding to a specific version of the EUCAIM DCAT Application Profile.

---

## Current Releases

| Version | Based on | Status |
|----------|----------|--------|
| **v1.0** | HealthDCAT-AP Release 5 | Final |

Future releases will be added as the profile evolves alongside HealthDCAT-AP.

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

### Distribution

Defines the metadata properties describing a dataset distribution, including:

- access mechanisms
- technical characteristics
- standards
- rights and policies
- lifecycle information

### Examples

Machine-readable RDF/Turtle examples illustrating how Dataset and Distribution metadata can be represented using the EUCAIM DCAT Application Profile.

---

## Versioning

The repository follows **Semantic Versioning**.

Major versions correspond to significant revisions of the application profile, typically aligned with new releases of HealthDCAT-AP.

| Version | Description |
|----------|-------------|
| Major | Breaking changes or alignment with a new HealthDCAT-AP release |
| Minor | Backwards-compatible additions or clarifications |

---

## Relationship with Other Specifications

The EUCAIM DCAT Application Profile builds upon the following standards and specifications:

- W3C DCAT 3
- DCAT Application Profile for data portals in Europe (DCAT-AP)
- HealthDCAT Application Profile (HealthDCAT-AP)
- Dublin Core Metadata Terms (DCT)
- Data Privacy Vocabulary (DPV)
- PROV Ontology (PROV-O)
- ODRL Information Model
- Data Quality Vocabulary (DQV)

---

## Contributing

Issues and suggestions for improving the specification are welcome.

Contributions should preserve compatibility with the underlying DCAT-AP and HealthDCAT-AP specifications whenever possible.

---

## License

This repository is licensed under the **Apache License 2.0**.

See the `LICENSE` file for details.

---

## Acknowledgements

This work was developed within **Work Package 5 (WP5)** of the **European Cancer Imaging Initiative (EUCAIM)**.

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