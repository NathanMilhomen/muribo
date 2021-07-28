po:
	@find . -type f -name "*.py" ! -path "./venv/*" ! -path "./muribo/*" | xargs xgettext --from-code=UTF-8 --default-domain=base -o locales/base.po

mo:
	@msgfmt -o locales/pt-br/LC_MESSAGES/base.mo locales/pt-br/LC_MESSAGES/base.po

start:
	@make mo
	@python main.py

ping:
	@echo pong