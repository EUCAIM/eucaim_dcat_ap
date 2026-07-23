# Distribution Examples

This document provides illustrative RDF/Turtle snippets for the properties defined in the **EUCAIM DCAT Application Profile Distribution specification**.

The examples are based on the Distribution examples included in EUCAIM Deliverable D5.3. Additional simple examples are included for properties for which the deliverable did not provide a separate snippet.

## Prefixes

The snippets below assume the following prefixes:

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcatap: <http://data.europa.eu/r5r/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/eucaim/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eucaim: <https://cancerimage.eu/ontology/EUCAIM#> .
```

---

# Access

## Access URL

```turtle
    dcat:accessURL <https://negotiator.eucaim.cancerimage.eu/collection/a96b56cd-59d4-444a-8e59-32a7fb0d7dea> .
```

## Access Service

```turtle
    dcat:accessService ex:eucaim-access-service .

    ex:eucaim-access-service
        a dcat:DataService ;
        dct:title "EUCAIM Dataset Access Service"@en ;
        dcat:endpointURL
            <https://negotiator.eucaim.cancerimage.eu/> .
```

## Download URL

```turtle
    dcat:downloadURL <https://example.org/eucaim/distributions/prostate-mri.zip> .
```

Use `dcat:downloadURL` only when the data can be directly downloaded.

## Availability

```turtle
    dcatap:availability <http://publications.europa.eu/resource/authority/planned-availability/AVAILABLE> .
```

---

# Description

## Title

```turtle
    dct:title "DICOM imaging data distribution"@en .
```

## Description

```turtle
    dct:description "This is the DICOM imaging data distribution."@en .
```

## Documentation

```turtle
    foaf:page <https://example.org/eucaim/distributions/prostate-mri/documentation> .
```

---

# Technical Characteristics

## Format

```turtle
    dct:format <http://publications.europa.eu/resource/authority/file-type/DCM> .
```

Where no suitable EU file-type concept is available, a media type URI may be referenced:

```turtle
    dct:format <https://www.iana.org/assignments/media-types/application/dicom> .
```

## Media Type

```turtle
    dcat:mediaType <https://www.iana.org/assignments/media-types/application/dicom> .
```

## Compression Format

```turtle
    dcat:compressFormat <https://www.iana.org/assignments/media-types/application/zip> .
```

## Packaging Format

```turtle
    dcat:packageFormat <https://www.iana.org/assignments/media-types/application/zip> .
```

## Image Size

```turtle
    dcat:byteSize "348966092800"^^xsd:decimal .
```

`dcat:byteSize` is expressed in bytes. The value above corresponds to approximately 325 GB.

## Checksum

```turtle
    spdx:checksum [
        a spdx:Checksum ;
        spdx:algorithm spdx:checksumAlgorithm_sha256 ;
        spdx:checksumValue
            "4e07408562bedb8b60ce05c1decfe3ad16b7223095b6f7f1f4a87b9b6e6f9f74"
    ] .
```

## Checksum Algorithm

```turtle
    spdx:checksum [
        a spdx:Checksum ;
        spdx:algorithm spdx:checksumAlgorithm_sha256 ;
        spdx:checksumValue
            "4e07408562bedb8b60ce05c1decfe3ad16b7223095b6f7f1f4a87b9b6e6f9f74"
    ] .
```

## Spatial Resolution

```turtle
    dcat:spatialResolutionInMeters "0.001"^^xsd:decimal .
```

## Temporal Resolution

```turtle
    dcat:temporalResolution "PT1S"^^xsd:duration .
```

---

# Standards

## Linked Schemas

```turtle
    dct:conformsTo <https://www.dicomstandard.org/current> .
```

## Language

```turtle
    dct:language <http://publications.europa.eu/resource/authority/language/ENG> .
```

---

# Rights & Policies

## Applicable Legislation

```turtle
    dcatap:applicableLegislation <http://data.europa.eu/eli/reg/2022/868/oj> .
```

## License

```turtle
    dct:license <https://creativecommons.org/licenses/by/4.0/> .
```

For non-public health data, the applicable data-use agreement or licence should be referenced instead of an open-content licence where appropriate.

## Rights

```turtle
    dct:rights [
        a dct:RightsStatement ;
        rdfs:label
            "Authorization is required to access, view and process the dataset in situ."@en
    ] .
```

## Has Policy

```turtle
    odrl:hasPolicy [
        a odrl:Policy ;

        odrl:permission [
            a odrl:Permission ;
            odrl:action
                odrl:read ,
                odrl:derive
        ] ;

        odrl:prohibition [
            a odrl:Prohibition ;
            odrl:action
                <http://creativecommons.org/ns#CommercialUse>
        ] ;

        odrl:obligation [
            a odrl:Duty ;
            odrl:action
                <https://schema.org/RegisterAction>
        ]
    ] .
```

## Access Conditions

```turtle
    dct:rights [
        a dct:RightsStatement ;
        rdfs:label
            "Authorization is required to access, view and process the dataset in situ."@en
    ] .
```

## Access Rights

```turtle
    dct:accessRights <http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC> .
```

---

# Lifecycle

## Status

```turtle
    adms:status <http://publications.europa.eu/resource/authority/dataset-status/COMPLETED> .
```

## Release Date

```turtle
    dct:issued "2023-11-22"^^xsd:date .
```

## Modification Date

```turtle
    dct:modified "2024-02-15"^^xsd:date .
```
