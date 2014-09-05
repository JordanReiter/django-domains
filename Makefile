project_name=domains

test:
	python setup.py develop
	python setup.py test
	python setup.py develop --uninstall


release:
	python setup.py sdist --format=zip,bztar,gztar register upload


flake8:
	flake8 --max-complexity 12 ${project_name}


coverage:
	make clean
	python setup.py develop
	coverage run --include=${project_name}/* setup.py test
	coverage html

clean:
	python setup.py develop --uninstall
	rm -rf *.egg-info *.egg
	rm -rf htmlcov
	rm -f .coverage
	find . -name "*.pyc" -exec rm -rf {} \;

coveralls:
	coveralls --config_file=coverage.rc
