# Dungeons and Dragons Compendium
## * * Capstone Proposal

## Project Overview
The primary focus of this project is to build a searchable compendium of Dungeons and Dragons 5e. After that the goal is to create a system to categorize/tag pieces of data in the compendium to make it easier to search. Finally gives the user the ability to add custom content to the compendium and personalize the compendiums categories to fit their needs. What this compendium will indever to solve is the ability for a user to group and search for spells/items/locations/characters based off their need. For example, group said items by their element or location for quick and easy world building. The other issue the compendium will try to solve is to give the user a creative space to store the world they build and possibly in the future to share that work and collaborate with other users.

## Functionality
The user will create a world in their compendium that starts with the basic D&D 5E rules. There will be an editable list of item/spells/characters/classes/races/locations for them to search and add to. Each item will have categories that describe it allowing the user for instance to search "close range spells" and find spells that are only useful at close range. The most useful feature will be the ability to add your own descriptive tags/catagories to items to make it easier for that user to find what they want or group the items how they need. Each item will be stored on a mysql database each type of item will have its own table and the catagories will create forieng keys between them. The user will work with a front end build in Django and Vue to make changes and to add inputs.

## Data Model
The data stored will include:
### Items
### Classes
### Races
### Locations
### Characters
### Spells
### Abilities
### Feats

Each one will need its own model with the ability to modify them.

## Schedule
### First Milestone
Setup Django/Github/Basic layout of the frontend 
### Second Milestone
Build Database with Basic D&D 5E
### Third Milestone
Create Models for each catagory
### Fourth Milestone
Make compendium searchable
### Fifth Milestone
Make models/database editable by the user