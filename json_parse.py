import json 


# [
#     {component details},
#     {component details},
#     {component details},
#     {component details},
#     {component details}
# ]



def scan_for_relevant_details(component : dict):
    '''Here we want to scan for the component name, and version'''
    name = component.get("name")
    curr_version = component.get("version")
    
    repository_metadata = component.get("repositoryMeta")
    
    latest_version = repository_metadata.get("latestVersion")
    
    print(f"Component: {name}, Current Version: {curr_version}, Latest Version: {latest_version}, Concatenated Name: {name}-v{curr_version}")
    
    
    
    

def parse_json_component_data(json_file : str):
    
    print("PRINTING COMPONENTS...")
    with open (json_file, "r") as f:
        
        data = json.load(f)
        
        for component in data:
            scan_for_relevant_details(component)
            print("-" * 50)
            
        
    