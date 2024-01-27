#!/usr/bin/python
# -*- coding: utf-8 -*-

# Creative Commons Zero v1.0 Universal
# SPDX-License-Identifier: CC0-1.0

from ansible.module_utils.basic import AnsibleModule
from PIL import Image

DOCUMENTATION = '''
module: render_frame
short_description: Render a frame
description:
  - Renders a frame from an image file into a text grid
  - Requires the Pillow library
version_added: "1.0.0"
options:
  input_file:
    description:
      - Path to the input image file
    required: true
    type: str
  grid_width:
    description:
      - Width of the text grid
    required: false
    type: int
    default: 100
  grid_height:
    description:
      - Height of the text grid
    required: false
    type: int
    default: 30
'''

EXAMPLES = '''
- name: Render frame
    render_frame:
        input_file: /path/to/input/file.png
        grid_width: 100
        grid_height: 30
    register: output

- name: Print frame
    debug:
        msg: "{{ output.frame }}"

'''

RETURN = '''
frame:
    description: The rendered frame
    type: list
    elements: str
'''

def image_to_text_grid(input_image_path, grid_width, grid_height):
    # Load the image
    image = Image.open(input_image_path)

    # Resize the image to match the grid size
    image = image.resize((grid_width, grid_height))

    # Convert the image to grayscale
    image = image.convert('L')

    # Define ASCII characters for different brightness levels
    ascii_chars = " .:-=+*#%@"

    # Calculate the range of each brightness level
    step = 256 // len(ascii_chars)

    # Create the text grid
    text_grid = []
    for y in range(grid_height):
        line = ""
        for x in range(grid_width):
            brightness = image.getpixel((x, y))
            char_index = min(brightness // step, len(ascii_chars) - 1)
            line += ascii_chars[char_index]
        text_grid.append(line)

    print(text_grid)

    return text_grid

def run_module():
    module_args = dict(
        input_file=dict(type='str', required=True),
        grid_width=dict(type='int', required=False, default=100),
        grid_height=dict(type='int', required=False, default=30),
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    input_file = module.params['input_file']
    grid_width = module.params['grid_width']
    grid_height = module.params['grid_height']

    frame = image_to_text_grid(input_file, grid_width, grid_height)

    result['msg'] = "Frame rendered to module output"
    result['frame'] = frame
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
