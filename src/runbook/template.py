TEMPLATE = """
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e368013b",
   "metadata": {},
   "source": [
    "# DATE_REGEX - TITLE - Purpose"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30d9dcb9",
   "metadata": {},
   "source": [
    "## Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19ef6903-2fcd-4bdf-935e-92ce2940b277",
   "metadata": {
    "editable": true,
    "jupyter": {
     "source_hidden": true
    },
    "slideshow": {
     "slide_type": ""
    },
    "tags": [
     "parameters"
    ]
   },
   "outputs": [],
   "source": [
    "# PARAMETERS DEFAULTS\n",
    "dry_run = True # controls sh behavior for safety"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1db85d5-89a4-4721-837c-2f17f55581eb",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# SHELL HELPERS\n",
    "from runbook.shell import shell, gather, Q, shell_builder, confirm, style\n",
    "\n",
    "sh = shell_builder(dry_run)\n",
    "\n",
    "from functools import partial\n",
    "sh = partial(sh, tags_default={'environment': 'testing'}, confirm_default=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b60b6e71-13da-40d3-9a74-016f75fbaf46",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Widgets\n",
    "\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "w = widgets.Dropdown(\n",
    "    options=[('Production', 1), ('Staging', 2), ('Development', 3)],\n",
    "    value=3,\n",
    "    description='Environment:',\n",
    ")\n",
    "\n",
    "v = widgets.Dropdown(\n",
    "    options=['Mysql', 'Redis', 'Memcached'],\n",
    "    value='Redis',\n",
    "    description='Database:',\n",
    ")\n",
    "display(w)\n",
    "display(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79b18076-340f-42d3-a021-96a661de7e3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f\"Value of widget: {w.value} {v.value}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7610298",
   "metadata": {},
   "source": [
    "## Operation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "adf2dc3c",
   "metadata": {},
   "source": [
    "### Step 1 - Get git info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ee12661-62b8-43b7-b557-2acc9a346d84",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "output = await sh(\"git --version && echo 333 >&2\", confirm=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82c90614",
   "metadata": {},
   "source": [
    "### Step 2 - Print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c94548f-2197-4de7-b72c-b1feb29bc18c",
   "metadata": {
    "editable": true,
    "jupyter": {
     "source_hidden": true
    },
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "print(output)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0e9eade",
   "metadata": {},
   "source": [
    "<span style='color: red;'><bold>DANGER</bold></span> <span style='color: red;'><bold>DANGER</bold></span> <span style='color: red;'><bold>DANGER</bold></span>\n",
    "\n",
    "The following code is going to be risky. Be prepared with rollback procedures."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0add2816-a9cb-410c-83f3-a4aad6aaff5f",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [],
   "source": [
    "confirm(style(\"Danger, ready to proceed?\", fg='red', bold=True), abort=True)\n",
    "cmds = [sh(\"sleep 1; echo 1\\n\\n\"), sh(\"sleep 2; echo 2\"), sh(\"sleep 3; echo 3\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef525b6d-2059-412e-a0cb-c1e908ca54c7",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [],
   "source": [
    "result = await gather(*cmds)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74d941f2",
   "metadata": {},
   "source": [
    "## Cleanup"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5b16dbe",
   "metadata": {},
   "source": [
    "## Rollback"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e6541b9",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "jpcodetoc-autonumbering": true,
  "jpcodetoc-showcode": true,
  "jpcodetoc-showmarkdowntxt": true,
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {
     "00d94a91289843ffa289f8711cf0281a": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "01341d57d5fc40a4bb87ded20ede1437": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "05b0cf51a08b43229025c7c9911fc9d9": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "0ead60e3a50a435b9fb9108fd94b3ef7": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "26ceedc50f214066a71dd231e26dca1d": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_8cb274d527ee4c54be3088a2732b20e9",
       "style": "IPY_MODEL_0ead60e3a50a435b9fb9108fd94b3ef7"
      }
     },
     "31e91bd783104ce9bd315f16e52454c3": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "3a7daaf1e8bd4d549e0151fc6596aa14": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "3e4cfd68ff254861ac8fd426e76c0580": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "427492d955e44f0d9afd084a21992ded": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "42a5190cc2cb4a6bbcba0c991ad5267e": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "51ba6b65921045ca800f808a412f3dfa": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_d14ce861c12a41a8bb79ac50dd4873c8",
       "style": "IPY_MODEL_d18b37b01ec5407f897e73c09bd65653"
      }
     },
     "592021c74b9b48d6bc07ae294942d7d6": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "5ec47e068e3348099337b1e47027a348": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "656be4c079b6403f83154df4406ece9c": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "678cd2805a084f849b54cd55729ae378": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_592021c74b9b48d6bc07ae294942d7d6",
       "style": "IPY_MODEL_718480fa720f4f7382b7dea519524aba"
      }
     },
     "6908ff02704f4c27813f1595a672e5ed": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Number:",
       "index": 2,
       "layout": "IPY_MODEL_777edccc15ae45868a93fcc7090d34e9",
       "style": "IPY_MODEL_ebc750825be045328000c93cc6ae2bf2"
      }
     },
     "69d03ef4722d422cb5d10d0404058dd5": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "7109b74a8e9e44b38084c41724828b56": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "One",
        "Two",
        "Three"
       ],
       "description": "Number:",
       "index": 1,
       "layout": "IPY_MODEL_7e40b958d31548c2970991e1abbd9faa",
       "style": "IPY_MODEL_9992e1a4b6e14bec9411207094813329"
      }
     },
     "718480fa720f4f7382b7dea519524aba": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "76132f74032b4016a1bacae0c28b4b26": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "777edccc15ae45868a93fcc7090d34e9": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "7e40b958d31548c2970991e1abbd9faa": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "8819944f058a4c1497543f3c5ed5a143": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "8cb274d527ee4c54be3088a2732b20e9": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "8cefc8b7b51444889eda30c599711e4d": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "8e23030d63184e3ba7f90ff33d835ff0": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "9992e1a4b6e14bec9411207094813329": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "a75d478efda64f25ba54974966d616a4": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 1,
       "layout": "IPY_MODEL_8819944f058a4c1497543f3c5ed5a143",
       "style": "IPY_MODEL_a7e49efe71ff47e0914fb37d1773ab09"
      }
     },
     "a7c26ec9b69b4d5c8c336721b788ca38": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_8cefc8b7b51444889eda30c599711e4d",
       "style": "IPY_MODEL_3e4cfd68ff254861ac8fd426e76c0580"
      }
     },
     "a7e49efe71ff47e0914fb37d1773ab09": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "ade157b2c24443588ca8c932ebedd88b": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_3a7daaf1e8bd4d549e0151fc6596aa14",
       "style": "IPY_MODEL_5ec47e068e3348099337b1e47027a348"
      }
     },
     "c10e8cba88014761844e20acd058c4bd": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Number:",
       "index": 2,
       "layout": "IPY_MODEL_01341d57d5fc40a4bb87ded20ede1437",
       "style": "IPY_MODEL_00d94a91289843ffa289f8711cf0281a"
      }
     },
     "c3d6f82b7fb84fd2b9cc6db68e61387a": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Environment:",
       "index": 2,
       "layout": "IPY_MODEL_76132f74032b4016a1bacae0c28b4b26",
       "style": "IPY_MODEL_427492d955e44f0d9afd084a21992ded"
      }
     },
     "c69d73d746044a1eae3917467a75310c": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Number:",
       "index": 2,
       "layout": "IPY_MODEL_42a5190cc2cb4a6bbcba0c991ad5267e",
       "style": "IPY_MODEL_69d03ef4722d422cb5d10d0404058dd5"
      }
     },
     "c980c1dd75cc407a875a66f2adffdfc0": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "cf0a1e6ca0084d30869c7dfa2e2caf4b": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "d14ce861c12a41a8bb79ac50dd4873c8": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "d18b37b01ec5407f897e73c09bd65653": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "d3371b87a1314998a9305412b87a8248": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Production",
        "Staging",
        "Development"
       ],
       "description": "Number:",
       "index": 2,
       "layout": "IPY_MODEL_05b0cf51a08b43229025c7c9911fc9d9",
       "style": "IPY_MODEL_8e23030d63184e3ba7f90ff33d835ff0"
      }
     },
     "d3b8599fb504440db91bf5e0cf1a49db": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Mysql",
        "Redis",
        "Memcached"
       ],
       "description": "Database:",
       "index": 2,
       "layout": "IPY_MODEL_31e91bd783104ce9bd315f16e52454c3",
       "style": "IPY_MODEL_cf0a1e6ca0084d30869c7dfa2e2caf4b"
      }
     },
     "e4264bbf458848cda3869372f69bb134": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DropdownModel",
      "state": {
       "_options_labels": [
        "Mysql",
        "Redis",
        "Memcached"
       ],
       "description": "Database:",
       "index": 1,
       "layout": "IPY_MODEL_c980c1dd75cc407a875a66f2adffdfc0",
       "style": "IPY_MODEL_656be4c079b6403f83154df4406ece9c"
      }
     },
     "ebc750825be045328000c93cc6ae2bf2": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     }
    },
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
"""
