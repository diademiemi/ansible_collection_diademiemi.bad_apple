from ansible.module_utils.basic import AnsibleModule
from PIL import Image

def image_to_text_grid(input_image_path, grid_width=100, grid_height=30):
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

    frame = image_to_text_grid(input_file)

    result['msg'] = "Frame rendered to module output"
    result['frame'] = frame
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
