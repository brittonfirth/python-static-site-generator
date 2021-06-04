import typer
from ssg.site import ssg.site

def main(source='content', dest='dist'):
    config = {"config" : source, "dest" : dest}

    site = Site(**config)
    site.build()

typer.run(main())
