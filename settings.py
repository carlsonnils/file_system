import json

from tkinter import Tk
from tkinter.filedialog import askdirectory



def load_settings() -> dict:
    """
    Load the settings file at .\settings.json
    
    Returns:
        dict
    """
    with open(file='settings.json', mode='r') as file:
        return json.load(file)
    
    
    
def save_settings(settings: dict) -> None | dict:
    """
    Save the settings dict to the settings.json file.
    Returns dict if selected.
    
    Return:
        dict
        None
    """
    
    with open(file='settings.json', mode='w') as file:
        json.dump(settings, file)



def check_base_paths_exist(
        settings: dict,
    ) -> dict:
    
    # Home Path
    home_path = settings['home_path']

    if home_path == '':
        home_path = askdirectory(title='Select Home Folder')
        
    settings['home_path'] = home_path
    
    
    # Client Paths
    client_paths = settings['client_paths']
    assert isinstance(client_paths, list)
    
    if len(client_paths) == 0 or client_paths[0] == '':
        if settings['register_clients']:
            user_path = askdirectory(title='Select Clients Folder')
        
            if user_path == "":
                response = input("Set client paths? (y/n): ")
                match response.lower():
                    case "y":
                        check_base_paths_exist(settings=settings)
                    case "n":
                        settings['register_clients'] = False
            else:
                settings['client_paths'] = client_paths.append(user_path)
    
    # Save the settings
    save_settings(settings=settings)
    
    return settings