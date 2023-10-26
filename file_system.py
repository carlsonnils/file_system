import settings



if __name__ == "__main__":
    
    # Launch procedure
    
    # Load settings
    stgs = settings.load_settings()
    
    # Check paths
    stgs = settings.check_base_paths_exist(
        settings=stgs
    )
    print(stgs)
    