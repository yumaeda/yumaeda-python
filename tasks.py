"""Pythonのタスクランナー"""

from invoke import task

@task
def clean(c, bytecode=False, extra=''):
    """クリーンアップ処理"""
    patterns = ['build']
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))

@task
def build(c):
    """ビルド＆Linting処理"""
    c.run('pylint ./selenium_unittest_common/**/*.py')
    c.run('python3 -m compileall ./selenium_unittest_common/**/*.py -b')
    c.run('mkdir build')
    c.run('mv ./selenium_unittest_common/common/*.pyc build')
    c.run('mv ./selenium_unittest_common/unittest/*.pyc build')
