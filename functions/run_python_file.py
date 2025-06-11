import os 
import subprocess

def run_python_file(working_directory, file_path):
    
    abs_path_wd = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_path_wd, file_path))
    
    if not target_file.startswith(abs_path_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    file_extension = os.path.splitext(file_path)[1]
    if file_extension != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        
        file_info = subprocess.run(["python3",target_file], capture_output=True, timeout=30, text=True)
        final_string = []
        if file_info.stdout == "" and file_info.stderr == "":
            return "No output produced."
        final_string.append(f'STDOUT: {file_info.stdout}')
        final_string.append(f'STDERR: {file_info.stderr}')
        if file_info.returncode != 0:
            final_string.append(f'Process exited with code {file_info.returncode}')
        
        return "\n".join(final_string)
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    