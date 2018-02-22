# content of conftest.py
import pytest
import smtplib


# @pytest.fixture(scope="module")
# def smtp():
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


# @pytest.fixture(scope="module")
# def smtp(request):
#     server = getattr(request.module, "smtpserver", "smtp.gmail.com")
#     smtp = smtplib.SMTP(server, 587, timeout=5)
#     yield smtp
#     print("finalizing %s (%s)" % (smtp, server))
#     smtp.close()


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp
    print("finalizing %s" % smtp)
    smtp.close()
