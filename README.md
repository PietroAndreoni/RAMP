<img src="https://github.com/SESAM-Polimi/RAMP/blob/master/RAMP_logo_basic.png" width="300">

*An open-source bottom-up stochastic model for generating multi-energy load profiles.*

---

## Overview
RAMP is a bottom-up stochastic model for the generation of high-resolution multi-energy profiles, conceived for application in contexts where only rough information about users' behaviour are obtainable. Those may range from remote villages to whole countries.

<img src="https://github.com/SESAM-Polimi/RAMP/blob/master/Example%20output.png" width="300">

The source-code is currently released as v.0.2.1-pre. This should be regarded as a pre-release: it is not yeat accompained by a detailed documentation, but the Python code is fully commented in each line to allow a complete understanding of it. Further details about the conceptual and mathematical model formulation are provided in the related Journal publication (https://doi.org/10.1016/j.energy.2019.04.097). 

Please consider that a newer, fully commented and more user friendly version is under development and should be released soon.

The repository also hosts all the input files used to generate the profiles appearing in the abovementioned study, which may be also used as a reference example. To access the code version used for the Journal publication, select the tag "v.0.1-pre".

## Requirements
The model is developed in Python 3.6, and requires the following libraries:
* numpy
* matplotlib
* math
* random

## Quick start
To get started, download the repository and simply run the "RAMP_run.py" script. The console will ask how many profiles (i.e. independent days) need to be simulated, and will provide the results based on the default inputs defined in "input_file_1.py" and "input_file_2". To change the inputs, just modify the latter files. Some guidance about the meaning of each input parameter is available in the "core.py" file, where the *User* and *Appliance* Python classes are defined and fully commented. 

## Authors
The model has been developed by:

**Francesco Lombardi** <br/>
Politecnico di Milano, Italy <br/>
E-mail: francesco.lombardi@polimi.it <br/>

**Sergio Balderrama** <br/>
University of Liege, Belgium - Universidad Mayor de San Simon, Bolivia <br/>

**Sylvain Quoilin** <br/>
KU Leuven, Belgium <br/>

**Emanuela Colombo** <br/>
Politecnico di Milano, Italy <br/>

## Citing
Please cite the original Journal publication if you use RAMP in your research:
*F. Lombardi, S. Balderrama, S. Quoilin, E. Colombo, Generating high-resolution multi-energy load profiles for remote areas with an open-source stochastic model, Energy, 2019, https://doi.org/10.1016/j.energy.2019.04.097.*

## Contribute
This project is open-source. Interested users are therefore invited to test, comment or contribute to the tool. Submitting issues is the best way to get in touch with the development team, which will address your comment, question, or development request in the best possible way. We are also looking for contributors to the main code, willing to contibute to its capabilities, computational-efficiency, formulation, etc. 

## License
Copyright 2019 RAMP, contributors listed in **Authors**

Licensed under the European Union Public Licence (EUPL), Version 1.1; you may not use this file except in compliance with the License. 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License
