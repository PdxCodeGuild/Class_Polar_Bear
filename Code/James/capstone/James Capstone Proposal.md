# James Thornton's Capstone Proposal

## Project Overview

### Project Endstate: I will create a supply chain risk simulator that uses an SQL database. 
- This project will be a skeleton framework for data integrations to form a linear, digital thread across a system. This simple model will use a supply chain to connect data and track the movement of information across multiple nodes. The development will start small with three nodes (supplier, manufacturer, and customer) and then expand out to additionals events/nodes if time permits. 
- This application will be useful to businesses with supply chains that need to be connected or modeled. This model will be easily transferable to projects that require information sharing between SQL databases.
- Python will be the primary language for the model. I will use a minimal amount of Django, Javascript and HTML. Languages outside of Python and SQL are only needed for GUI functionality as they will not be easily supported in the target environment for this application. I will experiment with CSS in the final week to make the demo of the project look impressive.

## Functionality

- There will be just one page, like an application rather than a website. 
- The user will see a list of input fields and buttons to execute each input field.
- There will be a graphical user interface to show the outcome of the simulation. This could be numbers or colors on nodes on a line. This could be a live simulation on a map if time or a proper API is available. 

### Page Sketch

![Sketch](mockup.jpg)

## Data Model

![Data Model](datamodel.jpg)

## Schedule

#### 28-31 December
- Catch up on Django and Javascript labs. 
- Learn about supply chain models and simulators.
#### 3-7 January
- Build basic front end (inputs, buttons, and a GUI) with back end connections. 
- Include placeholder values in Python instead of full back end logic. 
- Start with three nodes and then expand. Complete all Javascript this week.
#### 10-14 January
- Build back end math
- Expand from basic math connecting nodes in the supply chain
- Start with node/event scores, metric averages, standard deviations, and a calculated expected values of perfect information. 
#### 17-21 January
- Add in CSS. 
- Continue to add to the number of inputs and back end logic.
#### February
- Import Python code to work laptop.
- Take skeleton supply chain logic and feed in live SQL data.