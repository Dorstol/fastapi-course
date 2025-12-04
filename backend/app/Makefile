ALEMBIC = alembic

PHONY: mm m

mm: # make migrations
	${ALEMBIC} revision --autogenerate -m ${msg}

m: # migrate
	${ALEMBIC} upgrade head
