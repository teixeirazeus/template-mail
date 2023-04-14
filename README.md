![banner](https://raw.githubusercontent.com/teixeirazeus/template-mail/main/readme_assets/banner.png)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/12348e15a77e4ada96fd4dfd23ca804d)](https://app.codacy.com/gh/teixeirazeus/template-mail/dashboard?utm_source=gh\&utm_medium=referral\&utm_content=\&utm_campaign=Badge_grade)
[![License](https://raw.githubusercontent.com/teixeirazeus/validator-pizza-python/main/readme_assets/mit.svg)](http://opensource.org/licenses/MIT)

Simple templates in html for email.

## Install

```bash
pip install git+https://github.com/teixeirazeus/template-mail
```

## Usage

```python
from template_mail import SimpleTemplate

print(
        SimpleTemplate.message(
            site_url="http://www.example.com",
            logo_url="https://t.ctcdn.com.br/essK16aBUDd_65hp5umT3aMn_i8=/400x400/smart/filters:format(webp)/i606944.png",
            company_name="Google",
            title="Title",
            message="Sample message",
        )
    )
```

## Developer

*   Thiago da Silva Teixeira

## License

Released under the [MIT License](http://opensource.org/licenses/MIT).
