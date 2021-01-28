# Created on January, 2021
# @author: Fábio Araújo de Sá

def mail_merge(names, mail_template):

    all_emails = []

    with open(names, "r") as nomes:
        all_names = nomes.readlines()

    with open(mail_template, "r") as email:
        template = email.read()

    for name in all_names:
        new_email = template.replace("<name>", name[:-1])
        all_emails.append(new_email)

    return all_emails
