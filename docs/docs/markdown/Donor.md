
# Class: donor


A Donor is an Individual that participates in a research Study by donating a Biospecimen. The use of the Biospecimen is restricted to the consent provided by the Donor.

URI: [GHGA:Donor](https://w3id.org/GHGA/Donor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature],[Individual],[File],[Individual]^-[Donor&#124;sex(i):biological_sex_enum;karyotype(i):string%20%3F;age(i):age_range_enum;vital_status(i):vital_status_enum;geographical_region(i):string%20%3F;alias(i):string;accession(i):string%20%3F;ega_accession(i):string%20%3F;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Disease],[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature],[Individual],[File],[Individual]^-[Donor&#124;sex(i):biological_sex_enum;karyotype(i):string%20%3F;age(i):age_range_enum;vital_status(i):vital_status_enum;geographical_region(i):string%20%3F;alias(i):string;accession(i):string%20%3F;ega_accession(i):string%20%3F;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Disease],[Ancestry])

## Parents

 *  is_a: [Individual](Individual.md) - An Individual is a Person who is participating in a Study.

## Attributes


### Inherited from individual:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)
 * [given name](given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [family name](family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [additional name](additional_name.md)  <sub>0..1</sub>
     * Description: Additional name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [individual➞sex](individual_sex.md)  <sub>1..1</sub>
     * Description: The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * Range: [biological sex enum](biological sex enum.md)
     * in subsets: (essential,restricted)
 * [karyotype](karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of an individual if defined.
     * Range: [String](types/String.md)
     * in subsets: (optional,restricted)
 * [individual➞age](individual_age.md)  <sub>1..1</sub>
     * Description: Age of an individual.
     * Range: [age range enum](age range enum.md)
     * in subsets: (essential,restricted)
 * [individual➞vital status](individual_vital_status.md)  <sub>1..1</sub>
     * Description: Last known Vital Status of an Individual.
     * Range: [vital status enum](vital status enum.md)
     * in subsets: (essential,restricted)
 * [geographical region](geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * Range: [String](types/String.md)
     * in subsets: (optional,restricted)
 * [has ancestry](has_ancestry.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * Range: [Ancestry](Ancestry.md)
     * in subsets: (optional,restricted)
 * [individual➞has parent](individual_has_parent.md)  <sub>0..\*</sub>
     * Description: One or more parent for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (optional,restricted)
 * [individual➞has children](individual_has_children.md)  <sub>0..\*</sub>
     * Description: One or more children for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (optional,restricted)
 * [individual➞has disease](individual_has_disease.md)  <sub>0..\*</sub>
     * Description: The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
     * Range: [Disease](Disease.md)
     * in subsets: (essential,public)
 * [individual➞has phenotypic feature](individual_has_phenotypic_feature.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.
     * Range: [PhenotypicFeature](PhenotypicFeature.md)
     * in subsets: (essential,restricted)
 * [individual➞has file](individual_has_file.md)  <sub>0..\*</sub>
     * Description: Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * Range: [File](File.md)
     * in subsets: (essential,restricted)
 * [individual➞alias](individual_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | participant |

