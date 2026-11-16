import json
import os
import zipfile

from sprite_cpp_generator import generate_sprite_cpp, generate_register_cpp

if __name__ == '__main__':
    sb3_file_path = input('Enter the path to the .sb3 file: ')

    # Unzip everything that isn't project.json in the sb3 file
    with zipfile.ZipFile(sb3_file_path, 'r') as zipf:
        for file in zipf.namelist():
            if file != 'project.json':
                os.makedirs('generated/assets/', exist_ok=True)
                zipf.extract(file, 'generated/assets/')

    # Load the project.json file
    with zipfile.ZipFile(sb3_file_path, 'r') as zipf:
        with zipf.open('project.json') as project_file:
            project_data = json.load(project_file)

    # Generate the code now
    target_index = 0
    os.makedirs('generated/sprites/', exist_ok=True)
    for target in project_data['targets']:
        with open(f'generated/sprites/Sprite{target_index}.cpp', 'w') as f:
            f.write(generate_sprite_cpp(target, target_index))
        target_index += 1
    generate_register_cpp(project_data['targets'])
    with open('generated/RegisterSprites.cpp', 'w') as f:
        sorted_targets = sorted(project_data['targets'], key=lambda t: t['layerOrder'])
        f.write(generate_register_cpp(sorted_targets))
