#Threat Modeling Third Parties App

##Project Overview
The project will allow users to outline the use case for implementing the Third Party being modeled. The Third Party engagement will be categorized, a library of common threats and controls will be available to attach to the use case, a high level data flow diagram will be able to be attached to the use case. 

The application will allow for assessment of security threats posed to an organization by engaging with the Third Party. 

- Django framework
- Threat frameworks will come from OWASP and MITRE.
- Control frameworks will come from Cyber Security Framework.
- Data Flow Diagram functionality will come from embedding 'Diagrams.net' application, Graphviz or Diagram.
- Dash Open Source framework for support team analysis

##Functionality
There are three intended user groups of the application: 
    1. Requesting teams
    2. Support teams
    3. External teams

The user's perspective will be developed in the order listed above.

###Requesting Team perspective:
    Initial page:
        - description of what the application does and the expected outcome 
        - overall process for completing a security review prior to engaging with a 3P
        - key security terms that user should be aware of to improve the experience
    Create New Threat Model:
        - index along the side with steps linked and completion status
        - form for User to input data on 3P
        - data flow diagram tool for User to show conceptual integration (initial outline provided per 3P category)
            * there will need to be a repository for the diagrams (DropBox, Box, etc.)
        - return list of threats to consider at each major transition point (untrusted user, untrusted device, untrusted application, untrusted network, etc.) threats will be interactive (likelihood adjusted based on deployment)
        - each threat will have a list of controls to address the threat (the controls will be interactive (implemented, planned, not planned))
        - inherent risk rating for threat model created (prior to analysis from support teams)
        - way to upload additional supporting documents 
        - way to link additional supporting documents
    View Existing Threat Models:
        - index along the side with steps linked and completion status
        - status of the security review of the threat model
        - threat report to show threats, needed controls, likelihood, and impact calculations from the security support engineer
        - Users answers rendered on the page in an easy to read format
        - note section along side for comments or questions
        - remaining tasks needing to be complete summary page
        - history page of all actions taken by Requester and Support teams on the threat model
    Catalogue page:
        - index of all 3P Threat Models completed
        - index of all threats
        - index of all controls
###Support Team Perspective
    Dashboard page:
        - Threat Models queued for support
        - Threat Models completed
        - Threat Models WIP
        - sec risks identified
        - sec risks mitigated
        - sec risks accepted and in prod
    View Existing Threat Models:
        - same as above (support team comments, notes, and actions uniquely identifiable)
    Catalogue page:
        - same as above
        - ability to add threats
        - ability to add controls

##Data Model
class Team(models.Model):
    team_name = models.CharField(max_length=20, blank=True)
    team_leader_first_name = models.CharField(max_length=20, blank=True)
    team_leader_last_name = models.CharField(max_length=20, blank=True)
    team_leader_alias = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.team_name} {self.team_leader_alias}'

class Third_Party_Categories(models.Model):
    third_party_category = models.CharField(max_length=20, blank=True, choices=THIRD_PARTY_CATEGORY)
    third_party_subcategory = models.CharField(max_length=20, blank=True, choices=THIRD_PARTY_SUBCATEGORY)

class Control(models.Model):
    control_family = models.CharField(max_length=10,choices=CONTROL_FAMILY, blank=True)
    control_name = models.CharField(max_length=20, blank=True)
    control_description = models.CharField(max_length=200, blank=True)
    control_owner = models.CharField(max_length=20, blank=True)
    control_implementation = models.CharField(max_length=10, choices=CONTROL_IMPLEMENTATION, blank=True)
    def __str__(self):
        return f'Control Family: {self.control_family} {self.control_name}'

class Threat(models.Model):
    third_party_type = models.ForeignKey(Third_Party_Categories, on_delete=models.CASCADE, related_name='categories_of_third_parties_threat', blank=True)
    threat_family = models.CharField(max_length=10,choices=THREAT_FAMILY, blank=True)
    threat_event_name = models.CharField(max_length=20, blank=True)
    threat_description = models.CharField(max_length=200, blank=True)
    threat_tactic_technique_procedure = models.CharField(max_length=20, blank=True)
    threat_exploit = models.CharField(max_length=20, blank=True)
    threat_campaign = models.CharField(max_length=20, blank=True)
    threat_resources = models.CharField(max_length=20, blank=True)
    threat_id = models.CharField(max_length=20, blank=True)
    threat_control = models.ForeignKey(Control, on_delete=models.CASCADE)


    def __str__(self):
        return f'Threat Family: {self.threat_family} {self.threat_event_name}'

class Third_Party(models.Model):
    third_party_type = models.ForeignKey(Third_Party_Categories, on_delete=models.CASCADE, related_name='categories_of_third_parties', blank=True)
    third_party_typical_threats = models.ForeignKey(Threat, on_delete=models.CASCADE, related_name='categories_of_third_parties', blank=True)
    third_party_name = models.CharField(max_length=20, blank=True)
    third_party_product = models.CharField(max_length=20, blank=True)
    third_party_contact = models.CharField(max_length=20, blank=True)
    third_party_assessed = models.BooleanField(default=False)
    recent_assessment_date = models.DateTimeField(max_length=10)
    third_party_industry = models.CharField(max_length=20, blank=True)
    third_party_service = models.CharField(max_length=20, blank=True)
    third_party_inherent_risk = models.CharField(max_length=20, blank=True)
    third_party_assessment_score = models.CharField(max_length=20, blank=True)
    third_party_open_source_data = models.CharField(max_length=20, blank=True)
    third_party_url = models.CharField(max_length=20, blank=True)
    third_party_assets = models.CharField(max_length=20, blank=True)
    third_party_size = models.IntegerField(default=0, blank=True)
    third_party_IT_size = models.IntegerField(default=0, blank=True)
    third_party_SEC_size = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return f'Name: {self.third_party_name} Product: {self.third_party_product}'

class Threat_Modeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='requesting_team', blank=True)
    third_party = models.ForeignKey(Third_Party, on_delete=models.CASCADE, related_name='name_of_third_party', blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(max_length=20, blank=True)
    project_description = models.CharField(max_length=500, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)
    threat_model_number = models.CharField(max_length=20, blank=True)
    number_of_issues = models.IntegerField(default=0, blank=True)
    number_of_targets = models.IntegerField(default=0, blank=True)
    number_of_risks = models.IntegerField(default=0, blank=True) 
    number_of_controls = models.IntegerField(default=0, blank=True) 
    threat_model_risk = models.CharField(max_length=20, blank=True)
    security_certifier_list = models.CharField(max_length=20, blank=True)
    security_certifier_assignee = models.CharField(max_length=20, blank=True)
    security_certifier_singoff = models.BooleanField(default=False)
    security_review = models.BooleanField(default=False)
    security_leadership_notes = models.CharField(max_length=20, blank=True)
    security_leadership_decision = models.CharField(max_length=20, blank=True)
    leadership_decision = models.CharField(max_length=20, blank=True)
    leadership_notes = models.CharField(max_length=20, blank=True)
    team_notes = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"Team: {self.team} Project: {self.project_name[:21]} TM#: {self.threat_model_number} {self.updated_date.year}/{self.updated_date.month}/{self.updated_date.day} @ {self.updated_date.hour}:{self.updated_date.minute}"

class Target(models.Model):
    threat_modeling_id = models.ForeignKey(Threat_Modeling, on_delete=models.CASCADE, related_name='related_threat_models', blank=True)
    target_name = models.CharField(max_length=20, blank=True)
    target_environment = models.CharField(max_length=20, blank=True)
    target_container = models.CharField(max_length=20, blank=True)
    target_description = models.CharField(max_length=200, blank=True)
    target_owner = models.CharField(max_length=20, blank=True)
    target_function = models.CharField(max_length=200, blank=True)
    target_data_classification = models.CharField(max_length=10, choices=DATA_CLASS, blank=True)
    target_access = models.CharField(max_length=20, choices=ACCESS, blank=True)
    def __str__(self):
        return f'Target: {self.target_name} {self.target_container}'

##Schedule
    1 day - Setup environment 
    2 days - Create data models
    1 day - Create Login
    4 days - Create Requester pages
        Questionnaire (1 day)
        Data Flow Diagram (3 days)
    Milestone 1 Complete
    1 day - Create Threats
    1 day - Create Controls
    1 day - Create Catalogue
    Milestone 2 Complete
    3 days - Create Support page
    Milestone 3 Complete
    3 days - Snazzy UI
    2 days - Test features all together


