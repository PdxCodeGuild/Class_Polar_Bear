
threat_action = []
threat_family = {
    'personnel': {'threat_name': str(), 'threat_action': threat_action, 'threat_target': str(), 'control': { }},
    'physical': {'threat_name': str(), 'threat_action': threat_action, 'threat_target': str(), 'control': { }},
    'resource': {'threat_name': str(), 'threat_action': threat_action, 'threat_target': str(), 'control': { }},
    'technical': {'threat_name': str(), 'threat_action': threat_action, 'threat_target': str(), 'control': { }}
    }

control = {
    'control_name': str(),
    'control_description': str(),
    'control_stage': ['Preperation', 'Prevent', 'Detect', 'Respond', 'Recover'],
    'control_implementation': {'yes': bool(), 'no': ['Planned', 'Not Planned', 'Cannot Implement']},
    'control_implementation_type': {'people': bool(), 'process': bool(), 'technology': {'false' : False, 'manual': str(), 'automated': str()}},
    'control_efficacy': ['Strong', 'Sufficient', 'Improvement Recommended', 'Weak', 'Not Implemented']
}