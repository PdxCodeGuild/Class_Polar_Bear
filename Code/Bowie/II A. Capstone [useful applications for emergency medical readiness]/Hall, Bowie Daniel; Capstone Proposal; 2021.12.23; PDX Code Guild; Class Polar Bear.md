Project Overview

Bottom line up front: 
-
- Applying technology to answer questions like these…
- How far away is an air rescue in my weekend warrior or experienced explorer destination?
- Might I get mauled by a polar bear?
- If an air rescue is far away and I might get mauled by a polar bear, what’s the best polar bear repellant to bring?
- AeroMed ready is a model website that uses geographic information to indicate how far away air ambulance helicopters might be in the event of emergencies—especially in wilderness areas, uses filtered word counting to suggest what types of emergencies might be the most likely in given areas that provide emergency information, and offers a simple gear review section to offer suggestions regarding what types of equipment might be useful to prevent and respond to emergencies.

My project addresses a gap in academic research and applied emergency medicine practice that currently exists in the United states due to a shift from a well-established database on air medical bases (the Atlas and Database of Air Medical Services, or ADAMS) to a nascent one that is currently under development with an apparent intent of incorporating crowd-sourced information (the Emergency Transport Healthcare Operations and Services, or ETHOS).

One can broadly consider air medical bases as being locations—often helipads near hospitals, airports, or land ambulance bases—from which air ambulances depart for rescue and medical transportation operations of various sorts. Air ambulances are typically rotary-wing aircraft (“helicopters”—though there is nascent work toward “quadcopter” and related asses) and can also be fixed-wing aircraft (“airplanes”). For the current work, only air medical bases housing the former—helicopters—will be considered because these constitute the majority of the bases and those which are generally most relevant for rescues.


Functionality

What are the major features of the web application? 
-
- 1) “Emergency Air Rescue Distance”: A graphical interface based on the Google Maps developer tools that allows users to click on a location and receive an output of the three closest air medical bases to there.
- 2) “Emergency Types”: A prioritized word-sort program, similar to that which we created using Python, but with modifications that provide users filtered key words to help them identify potential risks.
- 3) “Emergency Gear”: A simple blog-like gear review sections with links to external sites for purchase (a potential source of relatively passive revenue).

What problems is it attempting to solve? 
-
- Academic: There is a gap in the transition from the old ADAMS database to the new ETHOS database that makes it difficult to perform research on access to emergency medicine assets.
- The ETHOS website (https://ethos.aams.org/) currently carries the following caveat: “ETHOS is currently in its initial phase of data collection and should not yet be considered a comprehensive listing of air medical assets.
- Practical:
- “Emergency Air Rescue Distance”: It can be difficult to determine how far away air evacuation assets might be, especially in wilderness areas, creating a problem for accessing the outdoors safely
- “Emergency Types”: It can be difficult to determine what kinds of emergencies have occurred in specific areas
- “Emergency Gear”: It can be difficult to determine what types of gear to bring while balancing considerations on existing information such as what’s scientifically verifiable information versus marketing fluff as well as common outdoors-specific tradeoffs such as cost, weight(mass)/size, and various performance metrics. 
-
What libraries or frameworks will you use?
-
- “Emergency Air Rescue Distance”: 
- After consideration of options such as ArcPy and NumPy, a front end-based design using JavaScript, the information that is available from developer tools for Google Maps, and batch-processed conversion of addresses of air medical bases to coordinates seems preferable.
- I used an online service and manual processing of addresses of the roughly 260 air medical bases for which information currently exists on the ETHOS database. From this, software can perform simple distance-related calculations.
- “Emergency Types”: 
- Ajax and Python/Django—this would be like an updated and applied version of the Python word-count lab, which I found extraordinarily useful after I modified the code to remove “trivial words” such as articles and conjunctions. As an immediately useful example, running the roughly 600,000 words of an old version of Gray’s Anatomy through the program yielded an output “[('lower', 1610), ('upper', 1681), ('side', 1773), ('artery', 1849), ('fibers', 2030), ('nerve', 2072), ('lateral', 2242), ('posterior', 2301), ('surface', 2389), ('anterior', 2441)]”—which are indeed important terms for prioritizing anatomical study and arose recently regarding the divisions of the mediastinum for a surgery rotation. Running the program with a link to a nuclear, biological, and chemical emergency text also proved useful. For the present purposes, the software would rely on entry of information like that on a site titled “911 Emergency Calls-Exploratory Data Analysis” (https://www.kaggle.com/dktalaicha/911-emergency-calls-exploratory-data-analysis/data). This site includes latitude and longitude information with associated emergencies, which would be great to use in conjunction with the “Emergency Air Rescue Distance” section—but doing so is not currently realistic in the US because robust information is not immediately available for all areas.
- “Emergency Gear”: 
- Likely simple HTML and CSS, though eventually this would 



Walk through the application from the user’s perspective. What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back end?

- 1) “Emergency Air Rescue Distance” page:
- User-facing: Click a location on a US map à receive an output of the three closest air medical bases to that location
- 2) “Emergency Types” page:
- User-facing: Click on a link with à receive an output of prioritized key words that would be used to help focus on what types of emergencies one should consider 
- Note: having this link automatically to the “Emergency Air Rescue Distance” location entry would be ideal, but is not realistic in the US because for some areas an abundance of information is readily available and for other areas the opposite appears to be the case.
- Back-end: 
- JavaScript/Ajax to Django/Python to access word-sort code and produce output
- 3) “Emergency Gear”:
- User-facing: Simple gear review entries with links
- Back-end:
- There is no current intent to monetize this, but it could hypothetically be used to link to sites like Amazon.com or to sell directly using the appropriate back-end technologies.


Your proposal must cover all major topics we’ve covered:
-
- HTML/CSS
- overall site
- JavaScript
- Mostly for “Emergency Air Rescue Distance” section
- Python/Django
- Mostly for “Emergency Types” section
-
- Data Model
-
- What data will you need to store as part of your application?
- There is no intent to store user information
- I have already converted the address information that is available from the ETHOS database using a batch conversion from the air medical base address to latitude and longitude information, which I have converted to a comma-separated values (CSV) file and a basic Google Map.
- I intend to return information for the “Emergency Types” section using JSON.
-
-
- Schedule
-
- Week 1:
- Catch up on remaining labs
- Adapt some of the work from previous labs for aspects of the capstone
-
- Week 2: 
- Complete Milestone 1: Overall site layout and basic “Emergency Gear” section
- Work on functionality for the “Emergency Types” section
-
- Week 3: 
- Complete Milestone 2: Functional “Emergency Types” section
- Complete the basic map layout of the “Emergency Air Rescue Distance” section
-
- Week 4: 
- Complete Milestone 3: Functional “Emergency Air Rescue Distance” section
- Prepare to present 
-
- After capstone is finished:
- I need to focus on medical school for the rest of the academic year, but I plan to revisit the information for research purposes in the summer of 2022. I am specifically interested in how this could be applied to create a new generation of aeromedical evacuation equipment based on electric-powered flight. Developing an understanding of the geographic, emergency-type, and equipment-related considerations would be highly applicable for this purpose.
