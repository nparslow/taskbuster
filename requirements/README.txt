
# note the -r in these files means to load the file mentioned there

# to get the right environment setup for development:
workon ~/marinamele_env
pip install -r requirements/development.txt

# to activate the test environment:
workon tb_test
pip install -r requirements/testing.txt

