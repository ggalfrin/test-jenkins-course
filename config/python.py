import config.project

package_name = config.project.project_name

dev_requires = [
    "pydmt",
]
config_requies = [
    "pyclassifiers",
]
test_requires = [
    "pytest",
]
make_requies = [
    "pymakehelper",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
