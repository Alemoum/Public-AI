import os 

def write_file(working_directory, file_path, content):
    
    abs_path_wd = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_path_wd, file_path))
    
    
    if not target_file.startswith(abs_path_wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
    
    dir_to_file = os.path.dirname(target_file)
    if not os.path.exists(dir_to_file):
        os.makedirs(dir_to_file)
    
    try:
        with open(target_file, "w") as f:
            new_file = f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"