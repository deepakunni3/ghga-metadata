
# Class: ega accession mixin


Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

URI: [GHGA:EgaAccessionMixin](https://w3id.org/GHGA/EgaAccessionMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[EgaAccessionMixin&#124;ega_accession:string%20%3F],[Sample]uses%20-.->[EgaAccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[DataAccessCommittee]uses%20-.->[EgaAccessionMixin],[Analysis]uses%20-.->[EgaAccessionMixin],[Study],[Sample],[Individual],[File],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[EgaAccessionMixin&#124;ega_accession:string%20%3F],[Sample]uses%20-.->[EgaAccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[DataAccessCommittee]uses%20-.->[EgaAccessionMixin],[Analysis]uses%20-.->[EgaAccessionMixin],[Study],[Sample],[Individual],[File],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Analysis])

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Experiment](Experiment.md) (mixin)  - An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [ega accession](ega_accession.md)  <sub>0..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)
