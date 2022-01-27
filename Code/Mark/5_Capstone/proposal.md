# Machine Intelligence Experiment Tracker

## Project Overview

- Description = Build an application to serve as a semi-automated journal of computational experiments in the field of biologically-inspired machine intelligence, with a focus on Numenta's algorithms.
- Major Features = Table of experiments with functionality supporting deep dives into simulation results.
- Problem to be Solved = Support experiment tracking of neuroscience-based simulations. In other words, create a lab notebook containing a record of every experiment that has been run.
- Libraries and Frameworks = The five key technologies will be employed (Python, Django, JavaScript, HTML, and CSS) and links will be built between the proposed application and [Numenta's applications](https://github.com/numenta). No current plans to use Axios, Bootstrap, or Vue.

## Functionality

- Main Page = categorized list of experiments that have been run
- Experiment Record Page = algorithm employed (including versioning and traceability); input parameters; results summary; simulation data (dates, runtime, hardware and software details)
- Experiment Results Page = qualitative and quantitative representations of experimental results; common statistical fields; exploratory data analysis tools
- Experiment Comparison Page
- Experiment Planning Section

## Data Model

`Experiment`
- `number` (IntegerField)
- `algorithm` (CharField)
- `version` (IntegerField)
- `name` (CharField)
- `notes` (CharField)

`SimulatedResults`
- `date` (DateField)
- `runtime` (IntegerField)
- `outputs` (?)

`DerivedResults`
- `statistics` (?)

## Schedule

- 03 Jan | Milestone 1 = Initial structure with a draft version of each software component.
- 10 Jan | Milestone 2 = Finalize mature version of data model and implement in software application.
- 17 Jan | Milestone 3 = Finalize frontend.
- 20 Jan | Milestone 4 = Finalize backend, including support for automation of experiment tracking following simluations.
- 21 Jan | Project Presentation
- Future Work | Milestone 5 = Improved version for exploratory data analysis of experimental results. Support for benchmarking algorithms. Support for rapid integration of new algorithms via an API.

