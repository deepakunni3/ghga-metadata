
# Class: ontology class mixin


Mixin for entities that represent an class/term/concept from an ontology.

URI: [GHGA:OntologyClassMixin](https://w3id.org/GHGA/OntologyClassMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]uses%20-.->[OntologyClassMixin&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name:string%20%3F],[DataUsePermission]uses%20-.->[OntologyClassMixin],[DataUseModifier]uses%20-.->[OntologyClassMixin],[Ancestry]uses%20-.->[OntologyClassMixin],[AnatomicalEntity]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature],[DataUsePermission],[DataUseModifier],[Ancestry],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]uses%20-.->[OntologyClassMixin&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name:string%20%3F],[DataUsePermission]uses%20-.->[OntologyClassMixin],[DataUseModifier]uses%20-.->[OntologyClassMixin],[Ancestry]uses%20-.->[OntologyClassMixin],[AnatomicalEntity]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature],[DataUsePermission],[DataUseModifier],[Ancestry],[AnatomicalEntity])

## Mixin for

 * [AnatomicalEntity](AnatomicalEntity.md) (mixin)  - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
 * [Ancestry](Ancestry.md) (mixin)  - Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
 * [DataUseModifier](DataUseModifier.md) (mixin)  - Data use modifiers indicate additional conditions for use.
 * [DataUsePermission](DataUsePermission.md) (mixin)  - A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) (mixin)  - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: An identifier that uniquely represents an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)
 * [concept name](concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)
 * [ontology class mixin➞description](ontology_class_mixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [ontology name](ontology_name.md)  <sub>0..1</sub>
     * Description: The name of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)
 * [ontology version](ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)
 * [ontology class mixin➞name](ontology_class_mixin_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
