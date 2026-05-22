.PHONY: pin pin-dev

# Pin exact versions + generate hashes for supply chain security.
# Requires: pip install pip-tools
# Run after updating version constraints in requirements.txt / requirements-dev.txt.
pin:
	pip-compile --generate-hashes requirements.txt -o requirements.txt

pin-dev:
	pip-compile --generate-hashes requirements-dev.txt -o requirements-dev.txt
