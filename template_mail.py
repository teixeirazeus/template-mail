from jinja2 import Environment, FileSystemLoader


class SimpleMail:
    _env = Environment(loader=FileSystemLoader("templates/"))

    @staticmethod
    def confirm_email(**kwargs):
        """
        site_url: url of the site
        logo_url: url of the logo
        company_name: name of the company
        confirm_url: url to confirm the email
        """
        template = SimpleMail._env.get_template("message.txt")
        return template.render(**kwargs)
