from jinja2 import Environment, FileSystemLoader


class SimpleTemplate:
    """
    Classe para envio de e-mails simples
    Templates inspirados nos emails do google
    """

    _env = Environment(loader=FileSystemLoader("templates/"))

    @staticmethod
    def message(**kwargs):
        """
        site_url: url of the site
        logo_url: url of the logo
        company_name: name of the company
        title: title of the message
        message: the message
        """
        template = SimpleTemplate._env.get_template("message.txt")
        return template.render(**kwargs)

    @staticmethod
    def confirm_email(**kwargs):
        """
        site_url: url of the site
        logo_url: url of the logo
        company_name: name of the company
        confirm_url: url to confirm the email
        """
        template = SimpleTemplate._env.get_template("email-confirm.txt")
        return template.render(**kwargs)

    @staticmethod
    def reset_password(**kwargs):
        """
        site_url: url of the site
        logo_url: url of the logo
        company_name: name of the company
        confirm_url: url to confirm the email
        """
        template = SimpleTemplate._env.get_template("password-reset.txt")
        return template.render(**kwargs)


if __name__ == "__main__":
    print(
        SimpleTemplate.message(
            site_url="http://www.example.com",
            logo_url="http://www.example.com/logo.png",
            company_name="Example",
            title="Hello World",
            message="Banana",
        )
    )
