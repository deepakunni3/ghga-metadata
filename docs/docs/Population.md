
# Class: population


A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.

URI: [GHGA:Population](https://w3id.org/GHGA/Population)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Population&#124;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[Family],[Population]^-[Cohort],[Population]^-[Ancestry],[MaterialEntity]^-[Population],[MaterialEntity],[Family],[Cohort],[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Population&#124;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[Family],[Population]^-[Cohort],[Population]^-[Ancestry],[MaterialEntity]^-[Population],[MaterialEntity],[Family],[Cohort],[Ancestry])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Children

 * [Ancestry](Ancestry.md) - Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
 * [Cohort](Cohort.md) - A cohort is a collection of individuals that share a common characteristic/observation and have been grouped together for a research study/investigation.
 * [Family](Family.md) - A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption.

## Referenced by Class


## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

### Inherited from material entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>0..1</sub>
     * Description: The alias (alternate identifier) for an entity.
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
