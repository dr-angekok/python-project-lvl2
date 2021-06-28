# makefile

install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

package-install-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff
