from invoke import task

@task
def start(ctx):
    ctx.run("python main.py")

@task
def test(ctx):
    ctx.run("pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")
    ctx.run("coverage report -m")

@task
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint main")
