PYTHON ?= python3

.PHONY: build check strict previews artifact accent clean

## build: regenerate dist/ from tokens/near-ai.tokens.json and css/
build:
	$(PYTHON) scripts/build.py

## check: contrast floors, token references, component cards, stale dist/
check:
	$(PYTHON) scripts/check.py

## strict: as check, and product themes that miss a floor fail too
strict:
	$(PYTHON) scripts/check.py --strict

## previews: render every component card (light, dark) and contact sheets to build/render/
previews: build
	$(PYTHON) scripts/preview.py --all light,dark

## artifact: assemble build/artifact/ for publishing to the Design System page
artifact: build
	$(PYTHON) scripts/artifact.py

## accent SEED=#rrggbb: derive a product accent family from one seed color
accent:
	$(PYTHON) scripts/accent.py "$(SEED)"

clean:
	rm -rf build
