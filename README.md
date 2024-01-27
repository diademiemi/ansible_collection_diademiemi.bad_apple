Ansible Collection - diademiemi.bad_apple
========================================

<img src="https://raw.githubusercontent.com/diademiemi/ansible_collection_diademiemi.bad_apple/main/thumbnail.png" width="50%">

[YouTube Video](https://www.youtube.com/watch?v=Wb9iwFk3atA)

This is an Ansible Collection which features:
- A module `render_frame` which converts a frame of the Bad Apple video into an ASCII art representation.
- A playbook `bad-apple.yml` which:
  - Installs necessary Pip packages.
  - Downloads the Bad Apple video.
  - Splits the video into PNG frames.
  - Renders each frame into an ASCII art representation.
  - Displays the ASCII art representation of each frame in the terminal.

To run the playbook, install the collection and run the playbook:
```bash
ansible-galaxy collection install diademiemi.bad_apple
```
OR locally
```bash
ansible-galaxy collection install .
```

Then run the playbook:
```bash
ansible-playbook playbooks/bad-apple.yml -K
```
OR to skip installing Pip packages (`yt-dlp` and `Pillow`)
```bash
ansible-playbook playbooks/bad-apple.yml --skip-tags prereq
```

Wait 20 minutes and enjoy Bad Apple in Ansible!