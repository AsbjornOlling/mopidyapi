
CODEGEN_DIR=./codegen

test:
	python -m pytest

build: test
	flit build

install: build
	flit install

reinstall: build
	pip uninstall mopidyapi
	flit install

gen-controller-code:
	# run from git repo root
	pipenv run \
	python $(CODEGEN_DIR)/codegen.py \
	--template $(CODEGEN_DIR)/controller.tpl \
	--outdir ./mopidy_api/controllers
