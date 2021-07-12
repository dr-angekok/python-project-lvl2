# makefile

install:
	python3 -m poetry install

diff:
	python3 -m poetry run gendiff
	
build:
	python3 -m poetry build
	
publish:
	python3 -m poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

package-install-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	python3 -m poetry run flake8 gendiff

test:
	python3 -m poetry run pytest

extended-test:
	python3 -m poetry run pytest -vv
