import jinja2

# Load the Jinja2 template
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)

def generate_sprite_cpp(target, index):
    if target['isStage']:
        # Set the values that aren't in the stage to their default values
        target['x'] = 0.0
        target['y'] = 0.0
        target['visible'] = True
        target['size'] = 100.0
        target['direction'] = 90.0
        target['draggable'] = False
        target['rotationStyle'] = 'all around'

    # Load the template
    template = template_env.get_template('sprite.cpp.jinja')
    return template.render(
        target=target,
        sprite_index=index
    )

def generate_register_cpp(targets):
    # Load the template
    template = template_env.get_template('register.cpp.jinja')
    return template.render(targets=targets)