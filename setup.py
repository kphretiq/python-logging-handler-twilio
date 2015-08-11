from distutils.core import setup
with open("requirements.txt") as f:
    required = f.read().splitlines()
setup(
        name="TwilioHandler",
        version="0.1",
        description="logging handler sends sms via twilio api",
        author="Doug Shawhan",
        author_email="kphretiq@gmail.com",
        url="https://github.com/kphretiq/python-logging-handler-twilio",
        platforms=["all"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Python Software Foundation License",
            "Programming Language :: Python",
            "Topic :: Communications :: SMS",
            "Topic :: Logging :: Handlers",
            "Topic :: Software Development :: Bug Tracking",
            ],
        install_requires=required,
        )
