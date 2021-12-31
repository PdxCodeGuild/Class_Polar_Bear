## Project Overview

This application will serve as a "one stop shop" for travelers looking to get the most out of their travel adventures by creating their own itinerary to include flights, trains and buss routes that fits their budget.

- A key feature is the ability to get a more accurate and cost effective itinerary anywhere in the world
- Looking to cutdown the time and money it takes to craft a budget friendly travel itinerary
- Libraries and framework being used are React, Django, Javascript and HTML/CSS

## Functionality

- **Main Page:** A brief explanation of what the application is as well as the option to join/login to start getting notified of flight deals to destinations you'd want to visit.
- **User Profile**: Users will pick destination in which they want to be notified if a flight drops bellow a pre determined amount.
- **Recommendation:** Based on their travel plans, the application will suggest/offer a list of alternate flights routes/trains/busses that could be cheaper.

## Data Model

**User Model**:

- name (charfield)
- email (emailField)
- username (charfield)
- password (charfield)

**Destination:**

- Country (charfield)
- City (charfield)
- Currency (charfield)
- Airport code (charfield)

## Schedule

- [x] **Dec 23 -Jan 1**: Start building backend
- [] **Jan 10**: Refresh React.JS and start planning frontend
- []**Jan 15**: Start connecting APIs
- []**Jan 20 -End of proj**: Test and deploy
