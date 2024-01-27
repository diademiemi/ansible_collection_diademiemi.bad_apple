
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.6.1

.. Anchors

.. _ansible_collections.diademiemi.bad_apple.render_frame_module:

.. Anchors: short name for ansible.builtin

.. Title

diademiemi.bad_apple.render_frame module -- Render a frame
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `diademiemi.bad_apple collection <https://galaxy.ansible.com/ui/repo/published/diademiemi/bad_apple/>`_ (version 1.0.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install diademiemi.bad\_apple`.

    To use it in a playbook, specify: :code:`diademiemi.bad_apple.render_frame`.

.. version_added

.. rst-class:: ansible-version-added

New in diademiemi.bad\_apple 1.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Renders a frame from an image file into a text grid
- Requires the Pillow library


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grid_height"></div>

      .. _ansible_collections.diademiemi.bad_apple.render_frame_module__parameter-grid_height:

      .. rst-class:: ansible-option-title

      **grid_height**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grid_height" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Height of the text grid


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`30`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grid_width"></div>

      .. _ansible_collections.diademiemi.bad_apple.render_frame_module__parameter-grid_width:

      .. rst-class:: ansible-option-title

      **grid_width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grid_width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Width of the text grid


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`100`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-input_file"></div>

      .. _ansible_collections.diademiemi.bad_apple.render_frame_module__parameter-input_file:

      .. rst-class:: ansible-option-title

      **input_file**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-input_file" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to the input image file


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Render frame
        render_frame:
            input_file: /path/to/input/file.png
            grid_width: 100
            grid_height: 30
        register: output

    - name: Print frame
        debug:
            msg: "{{ output.frame }}"





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-frame"></div>

      .. _ansible_collections.diademiemi.bad_apple.render_frame_module__return-frame:

      .. rst-class:: ansible-option-title

      **frame**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-frame" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The rendered frame


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/diademiemi/ansible_collection_diademiemi.bad_apple/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/diademiemi/ansible_collection_diademiemi.bad_apple"
    external: true


.. Parsing errors

