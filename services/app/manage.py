import os
from flask.cli import FlaskGroup


from project import app
from project.services.selenium.chrome.ChromeBrowser import ChromeBrowser


cli = FlaskGroup(app)


@cli.command("sys_info", help="Show all info")
def sys_info():
    cpu = os.cpu_count()
    print(f'CPU: {cpu=}')


@cli.command("test", help="Test selenium")
def test():
    browser = ChromeBrowser()
    browser.searchGoogle()


if __name__ == "__main__":
    cli()
